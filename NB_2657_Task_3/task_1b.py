'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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
# Filename:			task_1b.py
# Functions:		applyPerspectiveTransform, detectMaze, writeToCsv
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2
import csv
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
def fun(x,y,size,M,N,output):
    #     print(x," ",y)
    #     print(x+M," ",y+N)
    block = output[x:x+M,y:y+N]
    #     cv2.rectangle(output, (x, y), (x+M, y+N), (0, 0, 0))
    #     cv2.imshow("blk",block)
    north    = not(all(block[0,int(size/2)]))
    south  = not(all(block[int(size-1),int(size/2)]))
    west  = not(all(block[int(size/2),0]))
    east = not(all(block[int(size/2),int(size-1)]))

    #     print(north," ",south," ",east," ",west)
    edge = (north*2)+(south*8)+(east*4)+(west*1)
    #     print(edge)
    return edge






##############################################################


def applyPerspectiveTransform(transformed_image):
    
    """
    Purpose:
    ---
    takes a maze test case image as input and applies a Perspective Transfrom on it to isolate the maze
    
    Input Arguments:
    ---
    `input_img` :   [ numpy array ]
    maze image in the form of a numpy array
    
    Returns:
    ---
    `warped_img` :  [ numpy array ]
    resultant warped maze image after applying Perspective Transform
    
    Example call:
    ---
    warped_img = applyPerspectiveTransform(input_img)
    """
    
    warped_img = None
    
    ##############	ADD YOUR CODE HERE	##############
    img = transformed_image
    # cv2.imshow('IMG',img)
    # imgrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('grey',imgrey)
    ret,thresh = cv2.threshold(img,240,255,cv2.THRESH_BINARY)
    # cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    # cv2.resizeWindow("thresh", 1280, 1280)
    # cv2.imshow("thresh",thresh)
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea,reverse = True)
    # print(len(contours))
    contour = contours[0]
    approx = cv2.approxPolyDP(contour,0.009*cv2.arcLength(contour,True),True)
    cv2.drawContours(thresh, [approx], 0, (255, 255, 0), 5)
    
    # cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    # cv2.resizeWindow("thresh", 1280, 1280)
    # cv2.imshow("thresh",thresh)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # area = cv2.contourArea(contour)
    
    x,y,w,h = cv2.boundingRect(contour)
    p2 = list(approx[0][0])
    p3 = list(approx[1][0])
    p4 = list(approx[2][0])
    p1 = list(approx[3][0])
    l = [p1,p2,p3,p4]
    # sorted(l , key=lambda k: [k[0], k[1]])
    # print(l)
    x,y,w,h = cv2.boundingRect(contour)
    # print(w," ",h)
    for i,j in l:
        if i<=w and j <=h:
            p1 = [i,j]
        elif i>=w and j<=h:
            p2 = [i,j]
        elif i>=w and j>=h:
            p4 = [i,j]
        else:
            p3 = [i,j]
    if w>h:
        w = h
    else:
        h = w
    
    # print(p1," ",p2," ",p3," ",p4)
    kernel = np.ones((1,1),np.uint8)
    pts1 = np.float32([p1,p2,p3,p4])
    pts2 = np.float32([[0,0],[h,0],[0,h],[h,h]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    output = cv2.warpPerspective(img,matrix,(w,h))
    output = cv2.resize(output, (1280, 1280)) 
    # cv2.drawContours(output, [approx], 0, (0, 0, 0), 3)
    # cv2.rectangle(output, (0, 0), (400, 400), (0, 0, 0),5) 
    # output = cv2.dilate(output,kernel,iterations = 1)
    
    # ret,output = cv2.threshold(output,100,255,cv2.THRESH_BINARY)
    
    warped_img = output
    
    ##################################################
    
    return warped_img


def detectMaze(warped_img):
    
    """
    Purpose:
    ---
    takes the warped maze image as input and returns the maze encoded in form of a 2D array
    
    Input Arguments:
    ---
    `warped_img` :    [ numpy array ]
    resultant warped maze image after applying Perspective Transform
    
    Returns:
    ---
    maze_array` :    [ nested list of lists ]
    encoded maze in the form of a 2D array
    
    Example call:
    ---
    maze_array = detectMaze(warped_img)
    """
    
    maze_array = []
    
    ##############	ADD YOUR CODE HERE	##############
    output = warped_img
    imgwidth = output.shape[0]
    imgheight = output.shape[1]
    
    
    M = imgwidth//10
    N = imgheight//10
    print(M," ",N)
    size = M
    
    maze_array = []
    temp = []
    
    x = 0
    y = 0
    
    for i in range(10):
        for j in range(10):
            edge = fun(x,y,size,M,N,output)
            temp.append(edge)
            y = y + M
            j+=1
    
        maze_array.append(temp)
        temp = []
        y = 0
        x = x+M
        i+=1
    
    
    
    
    ##################################################
    
    return maze_array


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def writeToCsv(csv_file_path, maze_array):

	"""
	Purpose:
	---
	takes the encoded maze array and csv file name as input and writes the encoded maze array to the csv file

	Input Arguments:
	---
	`csv_file_path` :	[ str ]
		file path with name for csv file to write
	
	`maze_array` :		[ nested list of lists ]
		encoded maze in the form of a 2D array
	
	Example call:
	---
	warped_img = writeToCsv('test_cases/maze00.csv', maze_array)
	"""

	with open(csv_file_path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(maze_array)


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input, applies Perspective Transform by calling applyPerspectiveTransform function,
# 					encodes the maze input in form of 2D array by calling detectMaze function and writes this data to csv file
# 					by calling writeToCsv function, it then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					applyPerspectiveTransform and detectMaze functions.

if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')

	# path for 'maze00.csv' output file
	csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
	
	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')
			
			# writes the encoded maze array to the csv file
			writeToCsv(csv_file_path, maze_array)

			cv2.imshow('warped_img_0' + str(file_num), warped_img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		
		else:

			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:

		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1, 10):
			
			# path to image file
			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')

			# path for csv output file
			csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
			
			# read the image file
			input_img = cv2.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')
					
					# writes the encoded maze array to the csv file
					writeToCsv(csv_file_path, maze_array)

					cv2.imshow('warped_img_0' + str(file_num), warped_img)
					cv2.waitKey(0)
					cv2.destroyAllWindows()
				
				else:

					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()
			
			else:

				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()

	else:

		print('')

