import cv2
import mediapipe
import pyautogui

# we have imported mediapipe for the detection of hands,
# it has certain set of numbers assigned to different positions of hands.

# pyautogui is imported for the detection of axes and to measure positions throughout the screen
# to take the size of the screen and then used it

# here to brake this we have use the escape key and its value is 27

# then in the result it displays the live locations of the positioning of hands , the x and y axis..

# here we have used the index and middle finger for the movements

capture_hands=mediapipe.solutions.hands.Hands()
drawing_option=mediapipe.solutions.drawing_utils
screen_width,screen_height = pyautogui.size()

camera=cv2.VideoCapture(0)
x1=x2=y1=y2=0
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
                # print(x,y)
                # can uncomment if you want the locations..
                
                if id == 8:
                    mouse_x= int(screen_width / image_width * x)
                    mouse_y= int(screen_height/image_height*y)
                    # for the movement all over the screen
                    
                    
                    cv2.circle(image,(x,y),10,(0,255,23))                    
                    # we have given the radius of circle and the color 
                    
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1=x
                    y1=y
                    
                if id == 4:
                    cv2.circle(image,(x,y),10,(0,255,23))
                    x2=x
                    y2=y
                    # we have given the radius of circle and the color
        dist = y2-y1
        print(dist)
        # this will print the distance , vertical distance between the index and the middle finger
        if(dist<25):
            pyautogui.click()
                
            
                
    cv2.imshow('IMAGE',image)
    key=cv2.waitKey(1000000)
    if key == 27:
        break
                
                
    
camera.release()
cv2.destroyAllWindows()


    

