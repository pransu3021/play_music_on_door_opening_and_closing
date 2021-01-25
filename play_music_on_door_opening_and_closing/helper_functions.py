
# Import packages
import cv2
import numpy as np


ROI = []
Roi = []
def get_roi_points(video_getter):
    def click_event(event, x, y, flags, param):
        global ROI
        if event == cv2.EVENT_LBUTTONDOWN:
            ROI.append([x, y])
        else:
            pass
    while True:
        
        if (cv2.waitKey(1) == ord("q")) or video_getter.stopped:
            video_getter.stop()
            break

        frame = video_getter.frame
        frame = cv2.resize(frame, (640, 480),
                           interpolation=cv2.INTER_NEAREST)
        cv2.imshow("Select ROI points", frame)
        
        # calling mouse click function
        cv2.setMouseCallback("Select ROI points", click_event)
        # Checking length of ROI is 2 or not
        if len(ROI) == 2 :
            x1,y1,x2,y2 = ROI[0][0], ROI[0][1],ROI[1][0], ROI[1][1]
            roi = x1,y1,x2-x1,y2-y1
            Roi.append(roi)
            break
        else:
            pass
        # time.sleep(3)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()
    return Roi




def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
