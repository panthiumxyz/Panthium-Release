import numpy as np
import cv2
from mss import mss
import ctypes
import pyautogui
import time
import win32api
import threading
import sys
import win32con


exit_event = threading.Event()

R, G, B = (250, 100, 250)

view = 300

#view = int(view2)/2
half_view = view / 2

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screensize_x = screensize[0]
screensize_y = screensize[1]

middle_x = screensize_x / 2
middle_y = screensize_y / 2

top_left_x = middle_x - half_view
top_left_y = middle_y - half_view

bounding_box = {'top': int(top_left_y), 'left': int(top_left_x), 'width': view, 'height': view}



sct = mss()

def aimbot_key():
    lmb_state = win32api.GetAsyncKeyState(0x06)
    return lmb_state < 0

def terminate_program():
    if win32api.GetKeyState(0x04):
        sys.exit()

def is_space_down():
    key_down = win32api.GetAsyncKeyState(0x20)
    return key_down < 0

def aim_lower():
    aim_lower_state = win32api.GetAsyncKeyState(0x05)
    return aim_lower_state < 0


global aimbone
global ogaimbone




Head = 3
Neck = 4.5
Body = 100


def m_thread():
    while True:

        time.sleep(0.000001)

        if aimbot_key():

            terminate_program()

            while aimbot_key(): #tabbed out of the game, the program will run until the key is pressed again

                terminate_program()

                sct_img = sct.grab(bounding_box)

                #return true if there is a pixel with the value "250, 100, 250" in the image using cv2
                def check_pink():

                    global aimbone
                    global ogaimbone

#                   -------SETTINGS-------                   #

                    sensitivity = 2 #INPUT YOUR SENS % HERE

                    fov = 190 #FOV OF THE AIMBOT IN PX

                    aimbone = Head #Head, Neck, Body

#                   -------SETTINGS-------                   #

                    img = np.array(sct_img)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)


                    lower_pink = np.array([139, 95, 154])
                    upper_pink = np.array([153, 255, 255])
                    mask = cv2.inRange(img, lower_pink, upper_pink)


                    #replace all the pink pixels with black pixels
                    img[mask != 0] = (0, 0, 0)

                    #replace all non pink pixels with white pixels
                    img[mask == 0] = (255, 255, 255)
                
                    #add a white triangle in the bottom right corner of the screen
                    cv2.line(img, (600, 600), (300, 300), (255, 255, 255), thickness=200)

                    cv2.rectangle(img, pt1=(int(0), int(0)), pt2=(int((300 - fov) / 2), int(300)), color=(100,100,100), thickness= -1)

                    cv2.rectangle(img, pt1=(int(0), int(0)), pt2=(int(300), int((300 - fov) / 2)), color=(100,100,100), thickness= -1)

                    cv2.rectangle(img, pt1=(int(int(300 - ((300 - fov) / 2))), int(0)), pt2=(300, int(300)), color=(100,100,100), thickness= -1)
                    
                    cv2.rectangle(img, pt1=(int(0), int(int(300 - ((300 - fov) / 2)))), pt2=(300, int(300)), color=(100,100,100), thickness= -1)


                    #------------------------------------------------------------stop the aiming when all corners are black------------------------------------------------------------
                    
                    middle = np.array([half_view, half_view])

                    
                    #get the color of a 1x1 pixel in (int(middle[0]) - 20, int(middle[1]) - 20), (int(middle[0]) + 20, int(middle[1]) + 20)
                    top_left2 = img[int(middle[0]) - 20, int(middle[1]) - 20]
                    top_right2 = img[int(middle[0]) + 20, int(middle[1]) - 20]
                    bottom_left2 = img[int(middle[0]) - 20, int(middle[1]) + 20]
                    bottom_right2 = img[int(middle[0]) + 20, int(middle[1]) + 20]

                    #print(top_left2, top_right2, bottom_left2, bottom_right2)

                    #if all corners are black print "all corners are black"
                    if (top_left2[0] == 0 and top_right2[0] == 0) and (bottom_left2[0] == 0 and bottom_right2[0] == 0) or (top_left2[0] == 0 and top_right2[0] == 0) or (bottom_left2[0] == 0 and bottom_right2[0] == 0):
                        al_corners_black = True
                        
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) - 5), (int(middle[0]) - 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) - 5), (int(middle[0]) + 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) + 5), (int(middle[0]) - 80, int(middle[1]) + 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) + 5), (int(middle[0]) + 80, int(middle[1]) + 80), (255, 255, 255), 20)
                    
                    elif (top_left2[0] == 0 and top_right2[0] == 0):
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) - 5), (int(middle[0]) - 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) - 5), (int(middle[0]) + 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) + 5), (int(middle[0]) - 80, int(middle[1]) + 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) + 5), (int(middle[0]) + 80, int(middle[1]) + 80), (255, 255, 255), 20)

                    elif (bottom_left2[0] == 0 and bottom_right2[0] == 0):
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) - 5), (int(middle[0]) - 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) - 5), (int(middle[0]) + 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) + 5), (int(middle[0]) - 80, int(middle[1]) + 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) + 5), (int(middle[0]) + 80, int(middle[1]) + 80), (255, 255, 255), 20)

                    elif (top_left2[0] == 0 and bottom_left2[0] == 0):
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) - 5), (int(middle[0]) - 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) - 5), (int(middle[0]) + 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) + 5), (int(middle[0]) - 80, int(middle[1]) + 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) + 5), (int(middle[0]) + 80, int(middle[1]) + 80), (255, 255, 255), 20)

                    elif (top_right2[0] == 0 and bottom_right2[0] == 0):
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) - 5), (int(middle[0]) - 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) - 5), (int(middle[0]) + 80, int(middle[1]) - 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) - 5, int(middle[1]) + 5), (int(middle[0]) - 80, int(middle[1]) + 80), (255, 255, 255), 20)
                        cv2.line(img, (int(middle[0]) + 5, int(middle[1]) + 5), (int(middle[0]) + 80, int(middle[1]) + 80), (255, 255, 255), 20)

                        

                    #-----------------------------------------------------------------back to normal------------------------------------------------------------------------

    
                    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    ret, thresh = cv2.threshold(imgray, 127, 255, 0, cv2.THRESH_BINARY)
                    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                    # create an empty mask
                    mask = np.zeros(img.shape[:2], dtype=np.uint8)

                    # loop through the contours
                    for i, cnt in enumerate(contours):
                        # if the contour has no other contours inside of it
                        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) # Use cv2.CCOMP for two level hierarchy
                        if hierarchy[0][i][3] != -1: # basically look for holes
                            # if the size of the contour is less than a threshold (noise)
                            if cv2.contourArea(cnt) < 30:
                                # Fill the holes in the original image with white
                                cv2.drawContours(mask, [cnt], 0, 255, -1)
                                cv2.drawContours(img, [cnt], 0, (255, 255, 255), -1)

                    #get the coordinates of all the black pixels
                    black_pixels = np.argwhere(img == [0, 0, 0])
                    #if there are no black pixels, return None
                    if len(black_pixels) == 0:
                        return None
                    #get the coordinates of the middle of the image
                    middle = np.array([half_view, half_view])

                    #get the coordinates of the closest black pixel
                    closest_black_pixel = black_pixels[np.argmin(np.linalg.norm(black_pixels, axis=1))]

                    #get the x value of closest_black_pixel
                    closest_black_pixel_x = closest_black_pixel[1]

                    #get the y value of closest_black_pixel
                    closest_black_pixel_y = closest_black_pixel[0]

                    #get the coordiantes of the cursor on the screen
                    c_cursor = pyautogui.position()

                    #print(f"cursor: {c_cursor}")

                    c_to_bp_x = closest_black_pixel_x - c_cursor[0]

                    c_to_bp_y = closest_black_pixel_y - c_cursor[1]

                    #draw a rectangle around a batch of blask pixels that is more than 2x2 pixels
                    
                    cv2.rectangle(img, (int(black_pixels[0][1]), int(black_pixels[0][0])), (int(black_pixels[-1][1]), int(black_pixels[-1][0])), (255,0,255), thickness=1)

                    fovbox = 150 - (fov / 2)


                    cv2.rectangle(img, pt1=(int(fovbox), int(fovbox)), pt2=(int(fovbox + fov), int(fovbox + fov)), color=(0,0,255), thickness=1)

                    #get the length and width of the rectangle
                    length = int(black_pixels[-1][1]) - int(black_pixels[0][1])
                    width = int(black_pixels[-1][0]) - int(black_pixels[0][0])

                    #get the center of the rectangle
                    center_rect = np.array([int(black_pixels[0][1]) + int(length/2), int(black_pixels[0][0]) + int(width/2)])

                    hslevel=width/aimbone
                    center_rect[1] = center_rect[1] - hslevel

                    #draw a red line from every corner of the image to the center of the rectangle


                    closest_black_pixel = np.array([closest_black_pixel[1], closest_black_pixel[0]])

                    #get the length of all the lines from the corners to the closest black pixel
                    top_left = np.linalg.norm(closest_black_pixel - np.array([0, 0]))
                    top_right = np.linalg.norm(closest_black_pixel - np.array([view, 0]))
                    bottom_left = np.linalg.norm(closest_black_pixel - np.array([0, view]))
                    bottom_right = np.linalg.norm(closest_black_pixel - np.array([view, view]))

                    #print(f"top left: {top_left}, top right: {top_right}, bottom left: {bottom_left}, bottom right: {bottom_right}")

                    #convert the 4 lines into a 300x300 plot with the 4 corners as the 4 corners of the plot
                    top_left = np.interp(top_left, (0, view), (0, view))
                    top_right = np.interp(top_right, (0, view), (0, view))
                    bottom_left = np.interp(bottom_left, (0, view), (0, view))
                    bottom_right = np.interp(bottom_right, (0, view), (0, view))

                    #print(f"top left: {top_left}, top right: {top_right}, bottom left: {bottom_left}, bottom right: {bottom_right}")

                    cv2.line(img, (150, 150), (center_rect), (0, 255, 0), 2)

                    #pixels from center of square to bottom of the screen
                    bottom = np.linalg.norm(center_rect - np.array([int(center_rect[0]), view]))
                    #pixels from the center of the square to the left of the screen
                    left = np.linalg.norm(center_rect - np.array([0, int(center_rect[1])]))

                    #print(f"y: {bottom - 150}, x: {left - 150}")
                    #print(f"top left: {top_left}, top right: {top_right}, bottom left: {bottom_left}, bottom right: {bottom_right}")

                    c_cursor = pyautogui.position()

                    #if (int(bottom) - 150) is positive, make it negative, and vice versa
                    if (int(bottom) - half_view) > 0:
                        bottom_new = (int(bottom) - half_view) * -1

                    else:
                        bottom_new = (int(bottom) - half_view) * -1

                    xmove=center_rect[0] - half_view
                    ymove=center_rect[1] - half_view

                    fov = 300 - fov
                    fovlower = fov / 2
                    fovupper = 300 - (fov / 2)


                    # ymove = ymove / smoothing
                    # xmove = xmove / smoothing
                            
                


                    # smooth = random.randint(0, 100)
                    # print(smooth)
                    # if smooth > 70:
                    #     print("YES")
                    # else:
                    #     print("NO")

                    # win32api.mouse_event(0x0001,int(xmove), int(ymove))

                    
                    mulx = 4.36 / (screensize_x / 1920)
                    muly = 4.35 / (screensize_x / 1080)


                    win32api.mouse_event(0x0001,int(xmove * mulx / (sensitivity / 2.5)), int(ymove * muly / (sensitivity / 2.5)))

                    time.sleep(0.00001)

                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,user32.GetSystemMetrics(0),user32.GetSystemMetrics(1),0,0,)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,user32.GetSystemMetrics(0),user32.GetSystemMetrics(1),0,0,)

                    time.sleep(0.00001)

                    win32api.mouse_event(0x0001,int((xmove * mulx / (sensitivity / 2.5) * -1)), int ((ymove * muly / (sensitivity / 2.5) * -1)))

                    time.sleep(0.3)

                    # if spin_check():
                    #     if xmove > -5 and xmove < 5:
                    #         if ymove > -5 and ymove < 5:
                    #             cv2.rectangle(img, (int(black_pixels[0][1]), int(black_pixels[0][0])), (int(black_pixels[-1][1]), int(black_pixels[-1][0])), (0,255,0), thickness=2)
                    #             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,user32.GetSystemMetrics(0),user32.GetSystemMetrics(1),0,0,)
                    #             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,user32.GetSystemMetrics(0),user32.GetSystemMetrics(1),0,0,)

                    #resize output to 600x600
                    #img = cv2.resize(img, (600, 600))
                    # cv2.imshow('screen', img)

                check_pink()

                if not aimbot_key():
                    break

                

m_thread()

# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=m_thread)
#     p2 = multiprocessing.Process(target=m_thread)
#     p3 = multiprocessing.Process(target=m_thread)
#     p4 = multiprocessing.Process(target=m_thread)
#     p5 = multiprocessing.Process(target=m_thread)
#     p6 = multiprocessing.Process(target=m_thread)


#     p1.start()
#     print("running on core 1")
#     p2.start()
#     print("running on core 2")
#     p3.start()
#     print("running on core 3")
#     p4.start()
#     print("running on core 4")
#     p5.start()
#     print("running on core 5")
#     p6.start()
#     print("running on core 6")

#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     p5.join()
#     p6.join()


    

