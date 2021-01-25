import cv2
from helper_functions import *
from VideoGet import VideoGet
from playsound import playsound
def main():
    # rtsp link or video path for accessing the camera of laptop enter0
    video_file = "rtsp://admin:123456@202.179.72.236:8091/H264?ch=1&subtype=0&proto=Onvif"
    video_getter = VideoGet(video_file).start()
    roi = get_roi_points(video_getter)
    # roi = [(244, 8, 76, 48)]

    org_frame = None
    
    first_detected = []
    c = 0
    # id_list = [1,18,22, 23]
    while True:
        # ret, frame = cap.read() 

        if (cv2.waitKey(1) == ord("q")) or video_getter.stopped:
            video_getter.stop()
            break

        frame = video_getter.frame
        frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_NEAREST)
        # cv2.imwrite("frame.jpg", frame)
        # print(roi)
        if org_frame is None :
            x,y,w,h = roi[0]
            frame1 = frame[y: y+h, x:x+w]
            org_frame = frame1.copy()
            
        else:
            # img = frame.copy()
            x, y, w, h = roi[0]
            curr_frame = frame[y:y+h, x:x+w]
            err=mse(org_frame, curr_frame)
            # cv2.imwrite("curr_frame.jpg", curr_frame)
            # err=mse(org_frame, curr_frame)
            # print("error", err)
            if err > 5000:
                # print("error", err)
                frame = cv2.putText(frame, 'happy Birthday to you', (50, 50) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                playsound('songs/birthday_song.mp3', True)
                print("happy Birthday to you")

                                

            else:

                frame = cv2.putText(frame, 'Door close', (50, 50) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
                # print("Door close")
               
        cv2.imshow("Frame", frame)
        
    # cap.release()
    # Processed_video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

