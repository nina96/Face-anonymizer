import cv2
import mediapipe as mp
import os
import argparse

def process_img(img,face_detection):
    H,W,_= img.shape

    img_rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out= face_detection.process(img_rgb)

    if out.detections is not None: #in case image doesnt have face since it will throw error
        for detection in out.detections: #detections will give us all information regarding the bounding box around face along with its confidence score.
            location_data= detection.location_data #face location
            bbox= location_data.relative_bounding_box #bounding box attribute
            
            x1,y1,w,h= bbox.xmin,bbox.ymin,bbox.width,bbox.height

            x1 = int(x1*W) #since value we got are relative values so we need to convert it to int and and with respect ot image in order to use it
            y1 = int(y1*H)
            w = int(w*W)
            h = int(h*H)
            
            #blur face

            img[y1:y1+h,x1:x1+w, :]  = cv2.blur(img[y1:y1+h,x1:x1+w, :], (30,30)) #kernal size
    
    return img

args=argparse.ArgumentParser()

args.add_argument("--mode", default="webcam") #we will have value which user can set to for different source
args.add_argument("--filePath", default="sample.jpg") #in case user wants to use it for image or video we need to specify the image path

args = args.parse_args()

output_dir= './output'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)


#detect face
mp_face_detection= mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    
    if args.mode in ["image"]:   #if user selected image mode
        img=cv2.imread(args.filePath)
        
        img= process_img(img, face_detection)
            
        #save image

        cv2.imwrite(os.path.join(output_dir, 'output.jpeg'),img)

    elif args.mode in ['video']:

        cap =cv2.VideoCapture(args.filePath)
        ret, frame= cap.read()

        output_video= cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'), 
                                      cv2.VideoWriter_forcc(*'MP4V'),
                                      25, #frame per second try to use the fps
                                      (frame.shape[1],frame.shape[0]))
        

        while ret:
            frame= process_img(frame, face_detection)
            output_video.write(frame) #save the processed frame before reading new frame 

            ret,frame=cap.read()

            

        cap.release()
        output_video.release()

    elif args.mode in ['webcam']:
        cap =cv2.VideoCapture(0)

        ret, frame= cap.read()
        while ret:
            frame= process_img(frame, face_detection)
            cv2.imshow('frame',frame)
            if cv2.waitKey(40) & 0xFF==ord('q'):
                break
            ret,frame=cap.read()


        cap.release()
        cv2.destroyAllWindows()
#blur face