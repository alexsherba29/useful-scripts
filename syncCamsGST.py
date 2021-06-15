


#THIS CODE USE OPENCV LIBRARY TO GRAB AND RETRIEVE FRAMES FROM WEB CAMERAS
#AND SHOW FRAMES CAPTURED ON SCREEN
#THE PURPOSE IS TO SHOW FRAMES FROM DIFFERENT CAMERAS AND CHECK IF THE CAMERAS ARE SYNC
#TO CHECK SYNC WE USE CLOCK THAT COUNT MILLI SECONDS (ms) 
#ERROR SHOULD BE LESS THEN 1ms (NEED TO SEE THE SAME TIME ON ALL IMAGES)


from os import error
import numpy as np
import cv2
from imutils.video import FPS


def open_cam_usb(dev, width, height):
    # We want to set width and height here, otherwise we could just do:
    #     return cv2.VideoCapture(dev)
    


    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
     #ser resolution
width=1920
height=1080

#STREAMS SIZE (CAMEARS_NUMBER)
STREAM_NUMBER=2 
CAMERA_OFFSET=1 #1 if using laptop, 0 else

fps = FPS().start()

# cams = [open_cam_usb("0", width, height), open_cam_usb("1", width, height)]
# for i in range(STREAM_NUMBER):
    # cams.append(cv2.VideoCapture(f"v4l2src device=/dev/video{i+CAMERA_OFFSET} ! capsfilter caps=\"image/jpeg, width={width}, height={height}\" ! jpegdec ! videoconvert ! appsink", cv2.CAP_GSTREAMER))
    # cams.append(cv2.VideoCapture(i+CAMERA_OFFSET))
    # cams[i].set(cv2.CAP_PROP_FRAME_WIDTH, width)
    # cams[i].set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    # cams[i].set(cv2.CAP_PROP_FOURCC ,1196444237.0) #MPEG
# print(cams)
gst_str = ("v4l2src device=/dev/video0 ! queue !"
               "capsfilter caps=\"image/jpeg, width=(int){}, height=(int){}\" ! "
               "jpegdec ! identity sync=true ! comp.sink_0 compositor name=comp sink_1::xpos={} ! videoconvert ! "
               "appsink sync=false v4l2src device=/dev/video1 ! queue ! capsfilter caps=\"image/jpeg, width=(int){}, height=(int){}\" ! jpegdec ! identity sync=true ! comp.sink_1").format(width, height, width, width, height)
# print(gst_str)
cams = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
try:
    while(True):
        # Capture frame-by-frame
        # for i in range(STREAM_NUMBER):
        #     cams[i].grab()

        # frames = None
        # for i in range(STREAM_NUMBER):
        #     cams[i].grab()
        # for i in range(STREAM_NUMBER):
        # cams.grab()
        # ret , frame = cams.retrieve()
        ret , frame = cams.read()
        if ret:
            frame = cv2.resize(frame, (int(width),int(height/2)))
            # frames.append(frame)
        
        # assert len(frames)== STREAM_NUMBER

        # img = np.hstack(frames)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        if ret:
            # cv2.imwrite("/tmp/img.jpg",frame)
            # Display frame
            cv2.imshow('frame',frame)
        #fps.update()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            fps.stop()
            #print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
            #print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

            break
except:
    pass
finally:
    # When everything done, release the capture
    # for i in range(STREAM_NUMBER):
    cams.release()

    cv2.destroyAllWindows()
