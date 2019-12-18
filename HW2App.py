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
        params = cv2.SimpleBlobDetector_Params()
        params.filterByCircularity = True
        params.minCircularity = 0.83
        params.filterByArea = True
        params.minArea = 30.0
        params.maxArea = 100.0
        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(im)
        im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
        cv2.imshow("test1", im_with_keypoints) 

    def btn3_2_Clicked(self):
        cap = cv2.VideoCapture("res/featureTracking.mp4")

        params = cv2.SimpleBlobDetector_Params()
        params.filterByCircularity = True
        params.minCircularity = 0.83
        params.filterByArea = True
        params.minArea = 30.0
        params.maxArea = 100.0

        detector = cv2.SimpleBlobDetector_create(params)

        while True:
            ret , im = cap.read()
            if ret is False:
                break
            keypoints = detector.detect(im)
            im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
            cv2.imshow("test2", im_with_keypoints) 

            key = cv2.waitKey(30)
            if key == 'q' or key == 27:
                break
        
        cap.release()
        cv2.destroyAllWindows()


def main():
    app = QApplication(sys.argv)
    form = HW2App()
    form.show()
    app.exec_()

if __name__ == '__main__' :
    main()
