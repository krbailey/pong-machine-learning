import cv2
import win32gui
import time
import numpy as np
import datetime
from PIL import Image, ImageGrab


def enum_cb(hwnd, results):
    """Create list of open windows."""
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_screens(screen_name):
    """Finds specific window."""
    # wait for the program to start/open
    win32gui.EnumWindows(enum_cb, winlist)
    screens = [(hwnd, title) for hwnd, title in winlist if screen_name in title.lower()]
    # while len(screens) == 0:
    #     screens = [(hwnd, title) for hwnd, title in winlist if screen_name in title.lower()]
    #     win32gui.EnumWindows(enum_cb, winlist)

    return screens

if __name__ == '__main__':
    winlist = [] #list of windows
    screen = 'empong' #title of window to be found
    sfd = get_screens(screen)

    i = 0
    cont = True
    while cont:
        if len(get_screens(screen)) <= 0: #if game is closed
            cont = False
            print("Saved " + str(i+1) + " images...")
            continue
        hwnd = sfd[0][0]
        #window = sfd[0][0]

        try:
            bbox = win32gui.GetWindowRect(hwnd)
            img = ImageGrab.grab(bbox) #image capture
            d = datetime.datetime.now() #current time
            dt = d.time().strftime('%H-%M-%S')
            #img.save('images/'+screen+d.time().strftime('%H:%M:%S')+'_'+str(i)+'.png')
            img.save('images/'+screen+dt+'_'+str(i)+'.png')
            #cv2.imshow('window',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            i += 1
        except:
            print("error occured")

        time.sleep(0.033) #delay in recording screenshot
        winlist = []
        
        
# stream data instead of saving to file         
# if __name__ == '__main__':
#     winlist = [] #list of windows
#     screen = 'empong' #desired window
#     sfd = get_screens(screen) #find window

#     cont = True #if window open/found
#     while cont:
#         if len(get_screens(screen)) <= 0:   # check if closed
#             cont = False
#             continue

#         window = sfd[0][0]
#         try:
#             print_screen = np.array(ImageGrab.grab(bbox=win32gui.GetWindowRect(window)))
#             cv2.imshow('window',cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
#             if cv2.waitKey(25) & 0xFF == ord('q'):
#                 cv2.destroyAllWindows()
#                 break
#         except Exception as e:
#             print("error", e)