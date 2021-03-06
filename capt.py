import cv2

def read_show_write_webcam(mirror=False):
    #Read and show img from webcam and write it to dir E:\I-Net\
    cam = cv2.VideoCapture(0)
    r,img = cam.read()
    if mirror:
        img = cv2.flip(img, 1)
    cv2.imshow('my webcam', img)
    cv2.waitKey(0) 
    cv2.imwrite('E:\I-Net\my_webcam.png',img)
    cv2.destroyAllWindows()
    
    

def read_img_and_draw():
    img = cv2.imread('E:\I-Net\my_webcam.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('my webcam grey',img)
    cv2.waitKey(0)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(img,(5,5),(400,400),(255,0,0),2)
    cv2.line(img,(5,5),(400,400),(0,0,255),2)
    cv2.imshow('my webcam grey with blue rectangle and red diag',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    read_show_write_webcam(mirror = True)
    read_img_and_draw()


if __name__ == '__main__':
    main()
