import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab

def imToString():

    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    # Initialize the capture box dimensions
    left = 1000
    top = 600
    right = 1900
    bottom = 900

    while(True):

        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox=(left, top, right, bottom))
        
        # Convert PIL Image to OpenCV format
        cap_cv2 = cv2.cvtColor(nm.array(cap), cv2.COLOR_RGB2BGR)

    

        # Convert the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(cv2.cvtColor(cap_cv2, cv2.COLOR_BGR2GRAY), lang='eng')
        print(tesstr)

        # Display the image with the red rectangle
        cv2.imshow("Capturing...", cap_cv2)

        # Allow the user to adjust the capture box dimensions using keyboard inputs
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('w'):
            top -= 10
            bottom -= 10
        elif key == ord('a'):
            left -= 10
        elif key == ord('s'):
            top += 10
            bottom += 10
        elif key == ord('d'):
            left += 10
        elif key == ord('i'):
            bottom -= 10
        elif key == ord('j'):
            right -= 10
        elif key == ord('k'):
            bottom += 10
        elif key == ord('l'):
            right += 10

    # Release the capture
    cv2.destroyAllWindows()

# Calling the function
imToString()
