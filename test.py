import cv2.cv2 as cv
file=cv.FileStorage('d:/charucoBoard_Parameter.yml',cv.FileStorage_WRITE)
lists=(1,2,4)
file.write('a123',lists)
file.release()