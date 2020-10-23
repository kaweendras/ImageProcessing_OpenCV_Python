import cv2
from scipy.spatial import distance as dist
import dlib
import imutils
from imutils import face_utils
import time

def eye_aspect_ratio(eye):
    """ calculates eye aspect ratio from eye """
    #! euclidean distance of vertical eye points
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    #! euclidean distance of horizontal eye point
    C = dist.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)

    return ear


def get_blink_count(video):
    """ processes a video containing human face with blinking eye and counts blinks """
    eye_ar_thresh = 0.23  # ! ear threshold, if ear is below this value we will consider it as a blink
    # ! if ear value is below threshold and for this amout of frames then we will consider it as a blink
    eye_ar_consec_frames = 2
    #! initialize the frame counters and the total number of blinks
    COUNTER = 0
    TOTAL = 0
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    (lstart, lend) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
    (rstart, rend) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

    cap = cv2.VideoCapture(video)
    start_time = time.time()
    if not cap.isOpened():
        print("Can't open video file")
    else:
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                frame = imutils.resize(frame, width=450)
                frame = imutils.rotate_bound(frame, 270)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                #! detects face is gray frame
                rects = detector(gray, 0)

                if len(rects) == 0:
                    print("can not detect face")
                else:

                    for r in rects:
                        shape = predictor(gray, r)

                        shape = face_utils.shape_to_np(shape)

                        #! get co-ordinates
                        left_eye = shape[lstart:lend]
                        right_eye = shape[rstart:rend]

                        #! get EAR
                        leftEAR = eye_aspect_ratio(left_eye)
                        rightEAR = eye_aspect_ratio(right_eye)

                        #!AVG EAR
                        EAR = (leftEAR + rightEAR) / 2.0
                        print("ear count {}".format(EAR))

                        print("ear value {}".format(EAR))

                        leftEyeHull = cv2.convexHull(left_eye)
                        rightEyeHull = cv2.convexHull(right_eye)

                        #! draw eye on video output
                        cv2.drawContours(
                            frame, [leftEyeHull], -1, (0, 255, 0), 1)
                        cv2.drawContours(
                            frame, [rightEyeHull], -1, (0, 255, 0), 1)

                        if EAR < eye_ar_thresh:
                            COUNTER += 1
                        else:
                            if COUNTER >= eye_ar_consec_frames:
                                TOTAL += 1
                            COUNTER = 0

                    cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(frame, "EAR: {:.2f}".format(EAR), (300, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                    cv2.imshow("Frame", frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
    end_time = time.time()
    print("time diff {}".format(end_time - start_time))
    cap.release()
    cv2.destroyAllWindows()

    return TOTAL

if __name__ == "__main__":
    count = get_blink_count('video.mp4')
    print(count)
