#Project is a picture editor that performs can perform the following commands: open, invert, negative, blur, rotate, text, save, and exit. 

import sys

# Import statements
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

commandList = ['open','invert','negative','blur','rotate','text','save','exit']

# Function Name: main()
# input Params: None
# Description: Program execution begins at main function and main in turn 
#calls runMastermind function to kick off the game
#Output: runs the game
def main():
	"""
	Start with main
	"""

	#call a function to clear the screen first
	clearScreen()

	# call the function to display welcome message 
	displayWelcome()

	#calling the function to start the game
	loadEditor()

# Function Name: loadEditor()
# input Params: None
# Description: LoadEditor has the core logic for the picture editor calls other functions to control the editing behavior 
# Output: updated image display
def loadEditor():
	"""
	loadEditor has the core logic for the picture editor calls other functions to control the editing behavior
	Function Name: loadEditor ()
	Args: None
	Returns: None
	"""
	myCode = ""

	#call a function to clear the screen first
	clearScreen()

	# call the function to display welcome message 
	displayWelcome()

# Function Name: runImageProcessing()
# input Params: None
# Description: Shows menu on the screen.
# Output: prints menu on the screen
def runImageProcessing():

	myChoice = ""
	imageObject = None
	myOptionalArgument = ""

	#loop till you get valid character input to run the game
	while True:
		myChoice = input("Please Enter command here: ").lower()
		myArguments = myChoice.split()
		
		if len(myArguments) > 0:
			myCommand = myArguments [0]
		if len(myArguments) > 1:
			myOptionalArgument = myArguments [1]
		if myCommand in commandList:
			break
			
	print (myCommand)
	print (myOptionalArgument)

	if myCommand == 'open':
		if len(myOptionalArgument) > 0:
			imageObject = openFile(myOptionalArgument)   #File Open
		else:
			imageObject = openFile()   #File Open
	elif myCommand == 'invert':
		if imageObject is None:
			imageObject = imageObject = openFile()   #File Open
		#check if the option command line arguments are passed 
		if len(myOptionalArgument) > 0:
			invertImage(imageObject, myOptionalArgument)   #displays inverted image
		else:
			invertImage(imageObject)  #displays inverted image
	elif myCommand == 'negative':
		if imageObject is None:
			imageObject = imageObject = openFile()   #File Open
		negativeImage(imageObject)  #displays negative image
	elif myCommand == 'blur':
		if imageObject is None:
			imageObject = imageObject = openFile()   #File Open
		#check if the option command line arguments are passed 
		if len(myOptionalArgument) > 0:
			blurImage(imageObject, myOptionalArgument)  #displays blur image
		else:
			blurImage(imageObject)  #displays blur image

	elif myCommand == 'rotate':
		if imageObject is None:
			imageObject = imageObject = openFile()   #File Open
			
		#check if the option command line arguments are passed 
		if len(myOptionalArgument) > 0:
			imageObject = rotateImage(imageObject, myOptionalArgument)  #rotate with optional parameter deg image
		else:
			imageObject = rotateImage(imageObject)  #rotate 90 deg image
	elif myCommand == 'text':
		if imageObject is None:
			imageObject = imageObject = openFile()   #File Open
		#check if the option command line arguments are passed 
		if len(myOptionalArgument) > 0:
			addText(imageObject, myOptionalArgument)  #optional text to show that will add text to an image.
		else:
			addText(imageObject)  #use default Text that will add text to an image.
	elif myCommand == 'save':
		if imageObject is None:
			imageObject = imageObject = openFile()   #File Open
		#check if the option command line arguments are passed 
		if len(myOptionalArgument) > 0:
			saveImage(imageObject, myOptionalArgument)  #saves the image at the new location or new file name
		else:
			saveImage(imageObject)  #saves the image
	elif myCommand == 'exit':
		print ("Good bye")  #quit the editor
		sys.exit()
	
	imageObject.show() # display  images

# Function Name: clearScreen()
# input Params: None
# Description: clearScreen calls the OS function 'CLS' to clear the screen before start
# Output: clear the screen
def clearScreen():
	"""
    Start game with clear screen.
	Function Name: clearScreen ()
	Args: None
	Returns: None
    """
	#import OS library functions
	import os
	
	#now call OS function to clear the screen
	os.system('cls')

# Function Name: displayWelcome()
# input Params: None
# Description: Shows welcome screen to the end users.
# Output: prints welcome message on the screen	
def displayWelcome():
	"""
	Shows welcome screen to the end users.
	Function Name: displayWelcome ()
	Args: None
	Returns: None
	"""
	print ("***************************************************************")
	print ("*                      Welcome To                             *")
	print ("*                                                             *")
	print ("*                     My Image Editor                         *")
	print ("*                                                             *")
	print ("*              Developed by: Hardik Panchal                   *")
	print ("*                                                             *")
	print ("*                **** Fun Editing ****                        *")
	print ("*                                                             *")
	print ("***************************************************************")
	print ("                                                             ")

	#call to display game instructions
	displayInstructions()

	#call to display game menu
	runImageProcessing()

# Function Name: displayInstructions()
# input Params: None
# Description: Shows instructions on the screen.
# Output: prints instructions on the screen		
def displayInstructions():
	"""
	Shows game instructions on the screen.
	Function Name: displayInstructions ()
	Args: None
	Returns: None
	"""
	print('Please Enter of the following operations for picture editing.')
	print('open - Opens an image file. Optional: File Name')
	print('invert - Inverts the image. Optional: Inversion Axis')
	print('negative - Finds the negative of the image.')
	print('blur - Blurs an image. Optional: How many times to blur')
	print('rotate - Rotates an image. Optional: Angle of rotation')
	print('text - Adds text to an image. Optional: Text to print')
	print('save - Saves the image to disk in a new file.')
	print('exit - Exits the program.')

	print('Optional Parameters: ')
	#call to load game menu
	runImageProcessing()



# Function Name: openFile()
# input Params: None
# Description: Opens the file for picture editing.
# Output: image object
	
def openFile(filename="image.jpg"):
	"""
	Opens the file for picture editing.
	Input: None
	Returns: Image object
	"""
	print (filename)
	try:
		imageObject = Image.open(filename) # load an image from the hard drive
		print("Open File")
		return imageObject
	except IOError:
		print("Error opening the file")
		return None

		
# Function Name: invertImage()
# input Params: None
# Description: invert an image across its vertical axis
# Output: None
	
def invertImage(im, axis="vertical"):
	"""
	invert an image across its vertical axis
	input: One argument image object.
	Returns: None
	
	"""
	# Initializes a list that will contain the inverse RGB values for each pixel.
	new_pic_pixel_vals = []
	
	if axis == "vertical":
		# Loops through each row and column
		for row in range(im.height):
			for col in range(im.width):
				# Specifies the current pixel location
				cur_pixel_loc = (col, row)
				new_pixel_loc = (im.width-1-col, row)
				
				# Gets the current pixel RGB value and converts this value to a list
				cur_pixel_val = list(im.getpixel(cur_pixel_loc))
				new_pixel_val = list(im.getpixel(new_pixel_loc))
				
				new_pic_pixel_vals.append(tuple(new_pixel_val))
	elif axis == "horizontal":
		# Loops through each row and column
		for row in range(im.height):
			for col in range(im.width):
				# Specifies the current pixel location
				cur_pixel_loc = (col, row)
				new_pixel_loc = (col, im.height-1-row)
				
				# Gets the current pixel RGB value and converts this value to a list
				cur_pixel_val = list(im.getpixel(cur_pixel_loc))
				new_pixel_val = list(im.getpixel(new_pixel_loc))
				
				new_pic_pixel_vals.append(tuple(new_pixel_val))
    # Updates the pixel values of the image with the blurred pixel values
	im.putdata(new_pic_pixel_vals)

		
# Function Name: negativeImage()
# input Params: image object
# Description: negativeImage that will find the negative of an image.
# Output: None
	
def negativeImage(im):
	"""
	negativeImage that will find the negative of an image.

	input: One argument image object.
	Returns: None
	"""

	# Initializes a list that will contain the inverse RGB values for each pixel.
	new_RGB_pixel_vals = []
	
    # Loops through each row and column
	for row in range(im.height):
		for col in range(im.width):

			# Specifies the current pixel location
			cur_pixel_loc = (col, row)

			# Gets the current pixel value and converts this value to a list
			cur_pixel_val = list(im.getpixel(cur_pixel_loc))
			
			#<New value for a pixel in a given band> = 255 - <Old value for the pixel in that band>
			new_pixel_val = 255-cur_pixel_val[0],255-cur_pixel_val[1],255-cur_pixel_val[2]

			# Adds the new pixel value (as a tuple) to the list of
			# pixel values for the image
			new_RGB_pixel_vals.append(tuple(new_pixel_val))

    # Updates the pixel values of the image with the blurred pixel values
	im.putdata(new_RGB_pixel_vals)

# Function Name: blurImage()
# input Params: image object
# Description: blurImage that will blur an image using pixel interpolation.
# Output: None
	
def blurImage(im):
	"""
	Performs image blurring. Here, the parameter im should be the image object.

	In this template, I've provided you with code that should handle concern
	#2 from the problem statement (the one referring to updating all the pixel
	values at once). The code that you need to write yourself for this part
	is how to compute the new blurred pixel value for each pixel. The part of
	this function that you will need to edit is included in the comment block.

	Be sure to update this docstring before turning in your project!
	"""

	# Initializes a list that will contain the blurred RGB values for each
	# pixel.
	blurred_pixel_vals = []
	
	img_w = im.height
	img_h = im.height
	
	# The higher the kernel value, the more intense the blur
	kernel_size = 4.0
	kernel_half = kernel_size / 2.0
   
    # Loops through each row and column
	for row in range(im.height):
		for col in range(im.width):

			r, g, b, temp_r, temp_g, temp_b, temp_a, count = 0, 0, 0, 0, 0, 0, 0, 0 
			# Specifies the current pixel location
			cur_pixel_loc = (col, row)

			for kernel_offset_y in range(0 - int(kernel_half), 0 + int(kernel_half)):
				for kernel_offset_x in range(0 - int(kernel_half), 0 + int(kernel_half)):                              
					# Don't check outside screen edges...
					if (col + kernel_offset_x > 0 and col + kernel_offset_x < img_w and row + kernel_offset_y > 0 and row + kernel_offset_y < img_h):                     
						temp_r, temp_g, temp_b = im.getpixel((col + kernel_offset_x, row + kernel_offset_y))

					r += temp_r
					g += temp_g
					b += temp_b
					count += 1

			# Gets the current pixel value and converts this value to a
			# list
			cur_pixel_val = list(im.getpixel(cur_pixel_loc))

			##################################################################
			# At this point, you have the current pixel location, and the
			# current pixel RGB value. You will need to write code here to
			# average this pixel value with the value of the 8 neighboring
			# pixels, taking into account edge cases. Refer to the problem
			# statement for more details on this.

			# Let's assume that you have now computed this new blurred pixel
			# value, which is specified in the new_pixel_val variable. This
			# variable should be a 3-element Container (such as a list or
			# tuple) that specifies the new blurred pixel value.
			new_pixel_val = [r, g, b]
			##################################################################

			# Adds the blurred pixel value (as a tuple) to the list of
			# pixel values for the image
			blurred_pixel_vals.append(tuple(new_pixel_val))

	# Updates the pixel values of the image with the blurred pixel values
	im.putdata(blurred_pixel_vals)
	
		
# Function Name: rotateImage()
# input Params: image object, Optional: angle of rotation
# Description: rotateImage that will rotate an image 90deg counter-clockwise.
# Output: image object
	
def rotateImage(imageIn, angle=90):
	"""
	rotateImage that will rotate an image 90deg counter-clockwise.

	input: two argument image object. Optional: angle of rotation
	Returns: None
	"""
	try:
		imageOut = imageIn.rotate(int(angle)) # rotate image 90 deg
		print("rotateImage")
		return imageOut
	except IOError:
		print("Error opening the file")
		return None
		
# Function Name: addText()
# input Params: image object
# Description: addText that will add text to an image.
# Output: None
	
def addText(imageObject, text="What's up?"):
    """
    Adds text to the image. Here, the parameter im should be the image object.
	
	input: One argument image object.
	Returns: None
	"""

    color = (0x42, 0x24, 0xe9)

    # Creates an object that can be used to draw on an image
    draw = ImageDraw.Draw(imageObject)

    # Specifies the font type and the font size
    font = ImageFont.truetype('Impact.ttf', size=50)

    # Gets the width and height of the text area that is needed
    w, h = draw.textsize(text=text, font=font)

    # Computes the XY position to place the text so that it is centred
    # horizontally but lowered vertically
    x = (imageObject.width - w) / 2.
    y = (imageObject.height * 0.9) - (h / 2.)

    # Draws the text on the image
    draw.text(xy=(x, y), text=text, fill=color, font=font)

		
# Function Name: saveImage()
# input Params: image object
# Description: saveImage that will save the image to a file.
# Output: None
	
def saveImage(imageObject, newFileName="new_image.jpg"):
	"""
	saveImage that will save the image to a file.

	input: One argument image object.
	Returns: None
	"""
	try:
		print("saveImage")
		if imageObject is not None:
			imageObject.save(newFileName, "JPEG")

	except IOError:
		print("Error saving the file.")
		return None
		

#calling main
if __name__=="__main__":
    main()


