import time, pyperclip
from PIL import ImageGrab, Image
from pytesseract import pytesseract

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"D:\Pictures\KVPY-Fellowship-Scheme-2019-20-IISc-Registration-1.jpg"
  
# Opening the image & storing it in an image object
#img = Image.open(image_path)
img = ImageGrab.grabclipboard()

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
try:
    text = pytesseract.image_to_string(img)  
    # Displaying the extracted text
    print(text[:-1])
    print("Text copied to clipboard!")
    out = text[:-1]
    pyperclip.copy(out)
    time.sleep(5)
    exit
    
except TypeError:
    print("There is no Image in clipboard now")
    time.sleep(5)
    exit

