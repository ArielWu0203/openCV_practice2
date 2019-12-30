from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
import sys
import UI.MainWindow as window
import numpy as np
import cv2
import matplotlib.pyplot as plt


class HW2App(QtWidgets.QDialog , window.Ui_Dialog):
    def __init__(self, parant=None):
        super(HW2App, self).__init__(parant)
        self.setupUi(self)

        self.btn1.clicked.connect(self.btn1_Clicked)
        self.btn2.clicked.connect(self.btn2_Clicked)
        self.btn3_1.clicked.connect(self.btn3_1_Clicked)
        self.btn3_2.clicked.connect(self.btn3_2_Clicked)

    def btn1_Clicked(self):
        imgL = cv2.imread('res/imL.png', 0)
        imgR = cv2.imread('res/imR.png', 0)
        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        dsiparity = stereo.compute(imgL,imgR)
        plt.imshow(dsiparity, 'gray')
        plt.show()
        
    def btn2_Clicked(self):
        cap = cv2.VideoCapture("res/bgSub.mp4")
        _, first_frame = cap.read()
        first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
        first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
        while True:
            _, frame = cap.read()
            if frame is None:
                break
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

            difference = cv2.absdiff(first_gray, gray_frame)
            _, difference = cv2.threshold(difference, 25, 255,cv2.THRESH_BINARY)

            cv2.imshow("test1", frame)
            cv2.imshow("test2", difference)
            key = cv2.waitKey(30)
            if key == 'q' or key == 27:
                break
        
        cap.release()
        cv2.destroyAllWindows()

    def btn3_1_Clicked(self):
        cap = cv2.VideoCapture("res/featureTracking.mp4")
        _, im = cap.read()
        
        # TODO : Detector
        params = cv2.SimpleBlobDetector_Params()
        params.filterByCircularity = True
        params.minCircularity = 0.83
        params.filterByArea = True
        params.minArea = 30.0
        params.maxArea = 100.0
        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(im)
        for i in range(0, len(keypoints)):
            x,y = np.int(keypoints[i].pt[0]), np.int(keypoints[i].pt[1])
            sz = np.int(keypoints[i].size)
            if sz>1 :
                sz = np.int(sz/2)
            im = cv2.rectangle(im, (x-sz, y-sz), (x+sz, y+sz), color=(0,0,255), thickness=-1)
        cv2.imshow("test1", im) 

    def btn3_2_Clicked(self):
        lk_params = dict(winSize = (21,21),
                         maxLevel = 2,
                         criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))

        feature_params = dict(maxCorners = 10,
                             qualityLevel = 0.3,
                             minDistance = 2,
                             blockSize = 7)

        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.cam = cv2.VideoCapture("res/featureTracking.mp4")
        self.frame_idx = 0

        # TODO : Detector
        params = cv2.SimpleBlobDetector_Params()
        params.filterByCircularity = True
        params.minCircularity = 0.83
        params.filterByArea = True
        params.minArea = 30.0
        params.maxArea = 100.0

        detector = cv2.SimpleBlobDetector_create(params)

        while True:
            _ret , frame = self.cam.read()
            keypoints = detector.detect(frame)
            for i in range(0, len(keypoints)):
                x,y = np.int(keypoints[i].pt[0]), np.int(keypoints[i].pt[1])
                sz = np.int(keypoints[i].size)
                if sz>1 :
                    sz = np.int(sz/2)
                frame = cv2.rectangle(frame, (x-sz, y-sz), (x+sz, y+sz), color=(0,0,255), thickness=-1)
            
            if frame is None:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            vis = frame.copy()

            if(len(self.tracks)) > 0:
                img0, img1 = self.prev_gray, frame_gray
                p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1,1,2)
                p1, _st, _err = cv2.calcOpticalFlowPyrLK(img0,img1,p0,None,**lk_params)
                p0r, _st, _err = cv2.calcOpticalFlowPyrLK(img1,img0,p1,None,**lk_params)
                d = abs(p0-p0r).reshape(-1,2).max(-1)
                good = d<1
                new_tracks = []
                for tr, (x,y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):
                    if not good_flag:
                        continue
                    tr.append((x,y))
                    if len(tr) > self.track_len:
                        del tr[0]
                    new_tracks.append(tr)
                    cv2.circle(vis, (x,y), 2,(0,255,0),-1)
                self.tracks = new_tracks
                cv2.polylines(vis, [np.int32(tr) for tr in self.tracks], False, (0,255,0))
                
            if self.frame_idx % self.detect_interval == 0 :
                mask = np.zeros_like(frame_gray)
                mask[:] = 255
                for x,y in [np.int32(tr[-1]) for tr in self.tracks]:
                    cv2.circle(mask, (x,y), 5, 0, -1)
                p = cv2.goodFeaturesToTrack(frame_gray,mask=mask, **feature_params)
                if p is not None:
                    for x,y in np.float32(p).reshape(-1,2):
                        self.tracks.append([(x,y)])
            
            self.frame_idx += 1
            self.prev_gray = frame_gray
            cv2.imshow('lk_track', vis)
        

            key = cv2.waitKey(30)
            if key == 'q' or key == 27:
                break


def main():
    app = QApplication(sys.argv)
    form = HW2App()
    form.show()
    app.exec_()

if __name__ == '__main__' :
    main()
