import cv2
import mediapipe
import pyautogui
capture_hands=mediapipe.solutions.hands.Hands()
drawing_option=mediapipe.solutions.drawing_utils
screen_width,screen_height = pyautogui.size()

camera=cv2.VideoCapture(0)
while True:
    _,image=camera.read()
    image_height,image_width,_=image.shape
    image=cv2.flip(image,1)
    rbg_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output_hands=capture_hands.process(rbg_image)
    all_hands=output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image,hand)
            one_hand_landmarks=hand.landmark
            for id , lm in enumerate(one_hand_landmarks):
                x=int(lm.x*image_width)
                y=int(lm.y*image_height)
                print(x,y)
                
                if id == 8:
                    mouse_x= int(screen_width / image_width * x)
                    mouse_y= int(screen_height/image_height*y)
                    cv2.circle(image,(x,y),10,(0,255,23))
                    pyautogui.moveTo(mouse_x,mouse_y)
                if id == 4:
                    cv2.circle(image,(x,y),10,(0,255,23))
                
            
                
    cv2.imshow('IMAGE',image)
    key=cv2.waitKey(100)
    if key == 27:
        break
                
                
    
camera.release()
cv2.destroyAllWindows()


    

