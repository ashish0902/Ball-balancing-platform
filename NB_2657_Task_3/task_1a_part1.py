'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1A - Part 1 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_1a_part1.py
# Functions:		scan_image
# 					[ Comma separated list of functions in this file ]
# Global variables:	shapes
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


def scan_image(warped_img):

    """
    Purpose:
    ---
    this function takes file path of an image as an argument and returns dictionary
    containing details of colored (non-white) shapes in that image

    Input Arguments:
    ---
    `img_file_path` :		[ str ]
        file path of image

    Returns:
    ---
    `shapes` :              [ dictionary ]
        details of colored (non-white) shapes present in image at img_file_path
        { 'Shape' : ['color', Area, cX, cY] }
    
    Example call:
    ---
    shapes = scan_image(img_file_path)
    """

    global shapes
    shapes = {}
    ##############	ADD YOUR CODE HERE	##############
    img = warped_img
    # cv2.namedWindow("output2", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("output2", 1280, 1280)
    # cv2.imshow('output2',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # count = 0
#     lower and upper value of colour for the masking of colours for colour identification
	
    # red_lower = np.array([0,120,70], np.uint8)
    # red_upper = np.array([10,255,255], np.uint8)
    # green_lower = np.array([25, 52, 72], np.uint8) 
    # green_upper = np.array([102, 255, 255], np.uint8) 
    # blue_lower = np.array([110, 50, 50], np.uint8) 
    # blue_upper = np.array([130, 255, 255], np.uint8) 

    # blue_mask = cv2.inRange(hsv,blue_lower,blue_upper)
    _,thresh = cv2.threshold(img,240,255,cv2.THRESH_BINARY)
    # cv2.namedWindow("output3", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("output3", 1280, 1280)
    # cv2.imshow('output3',thresh)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea)
    
    
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.002*cv2.arcLength(contour,True),True)
        cv2.drawContours(img,[approx],0,(0,0,0),1)
        
        # cv2.namedWindow("output3", cv2.WINDOW_NORMAL)
        # cv2.resizeWindow("output3", 1280, 1280)
        # cv2.imshow('output3',thresh)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        area = cv2.contourArea(contour)
        M = cv2.moments(contour)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        
        if len(approx)>8:
            shapes['Circle'] = ['None']
            # res['Circle'].append(area)
            shapes['Circle'].append(cx)
            shapes['Circle'].append(cy)
        
    
    # green_mask = cv2.inRange(hsv,green_lower,green_upper)
    # _,thresh = cv2.threshold(green_mask, 100,255,1)
    # contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # contours = sorted(contours, key=cv2.contourArea)
    # for contour in contours:
#         approx = cv2.approxPolyDP(contour,0.002*cv2.arcLength(contour,True),True)
#         cv2.drawContours(img,[approx],0,(0,0,0),1)
#         area = cv2.contourArea(contour)
#         M = cv2.moments(contour)
#         cx = int(M['m10']/M['m00'])
#         cy = int(M['m01']/M['m00'])
        
           
#         if len(approx)>8:
#             if count == 0:
#                 shapes['Circle'] = ['green',cx,cy]
#                 count += 1
#             elif count == 1:
#                 shapes['Circle'] = [shapes['Circle']]
#                 count += 1
#             else:
#                 shapes['Circle'].append(['green',cx,cy])



# #   identification of red shapes in the image
#     red_mask = cv2.inRange(hsv,red_lower,red_upper)
#     _,thresh = cv2.threshold(red_mask, 100,255,1)
    
# # creating contours in the image for the red coloured shape
#     contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#     contours = sorted(contours, key=cv2.contourArea)
    
#     for contour in contours:
        
#         approx = cv2.approxPolyDP(contour,0.002*cv2.arcLength(contour,True),True)
#         cv2.drawContours(img,[approx],0,(0,0,0),1)

#         # cv2.namedWindow("output", cv2.WINDOW_NORMAL)
#         # cv2.resizeWindow("output", 1280, 1280)
#         # cv2.imshow('output',img)
#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#         area = cv2.contourArea(contour)
#         M = cv2.moments(contour)
#         cx = int(M['m10']/M['m00'])  # x coordinate of the centroid of the image
#         cy = int(M['m01']/M['m00'])  # y coordinate of the centroid of the image
        
#         # print(len(approx))

    
#         if len(approx)>8:                
#             if count == 0:
#                 shapes['Circle'] = ['red',cx,cy]
#                 count += 1
#             elif count == 1:
#                 shapes['Circle'] = [shapes['Circle']]
#                 count += 1
#             else:
#                 shapes['Circle'].append(['red',cx,cy])
        
    # if count > 1:
    #     d = shapes['Circle']
    #     # print(d)
    #     bc = sorted(d, key = lambda x: x[0])
    #     shapes['Circle'] = bc    
    #     shapes = {k: v for k, v in sorted(shapes.items(), key=lambda item: item[1][0],reverse = False)}
    
	##################################################
    
    return shapes


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    the function first takes 'Sample1.png' as input and runs scan_image function to find details
#                   of colored (non-white) shapes present in 'Sample1.png', it then asks the user whether
#                   to repeat the same on all images present in 'Samples' folder or not

if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in '+ curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path + '/Samples/'
    
    # path to 'Sample1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'Sample' + str(file_num) + '.png'

    print('\n============================================')
    print('\nLooking for Sample' + str(file_num) + '.png')

    if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
        print('\nFound Sample' + str(file_num) + '.png')
    
    else:
        print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
        exit()
    
    print('\n============================================')

    try:
        print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
        shapes = scan_image(img_file_path)

        if type(shapes) is dict:
            print(shapes)
            print('\nOutput generated. Please verify.')
        
        else:
            print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
            exit()

    except Exception:
        print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
        exit()

    print('\n============================================')

    choice = input('\nWant to run your script on all the images in Samples folder ? ==>> "y" or "n": ')

    if choice == 'y':

        file_count = 2
        
        for file_num in range(file_count):

            # path to image file
            img_file_path = img_dir_path + 'Sample' + str(file_num + 1) + '.png'

            print('\n============================================')
            print('\nLooking for Sample' + str(file_num + 1) + '.png')

            if os.path.exists('Samples/Sample' + str(file_num + 1) + '.png'):
                print('\nFound Sample' + str(file_num + 1) + '.png')
            
            else:
                print('\n[ERROR] Sample' + str(file_num + 1) + '.png not found. Make sure "Samples" folder has the selected file.')
                exit()
            
            print('\n============================================')

            try:
                print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
                shapes = scan_image(img_file_path)

                if type(shapes) is dict:
                    print(shapes)
                    print('\nOutput generated. Please verify.')
                
                else:
                    print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
                    exit()

            except Exception:
                print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
                exit()

            print('\n============================================')

    else:
        print('')
