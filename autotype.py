import time
import pyautogui
import pytesseract
import keyboard
from pynput import mouse
import logging

# Configure Tesseract path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")

# Global variables to store coordinates
top_left = None
bottom_right = None

# Mouse click callback function
def on_click(x, y, button, pressed):
    global top_left, bottom_right
    if pressed:
        if top_left is None:
            top_left = (x, y)
            logging.info(f"Top-left corner set at: {top_left}")
            print("Now, click to set the bottom-right corner...")
        elif bottom_right is None:
            bottom_right = (x, y)
            logging.info(f"Bottom-right corner set at: {bottom_right}")
            return False  # Stop listener after second click

# Function to get the area from mouse clicks
def get_area():
    print("Click to set the top-left corner, then click to set the bottom-right corner...")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return top_left, bottom_right

# Function to capture and recognize text in the defined area
def capture_text(top_left, bottom_right):
    try:
        screenshot = pyautogui.screenshot(region=(top_left[0], top_left[1], bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]))
        text = pytesseract.image_to_string(screenshot)
        return text.strip()
    except Exception as e:
        logging.error(f"Error in capturing text: {e}")
        return ""

# Function to type out the detected text at 43 words per minute (WPM)
def type_text(text):
    try:
        words = text.split()
        delay = .25  # Delay between each word to type at 43 WPM
        for word in words:
            keyboard.write(word + " ", delay=delay)
    except Exception as e:
        logging.error(f"Error in typing text: {e}")

# Main logic for continuous detection and typing until 'Esc' is pressed
def main():
    top_left, bottom_right = get_area()
    prev_text = ""

    print("Please focus the input field. You have 5 seconds.")
    time.sleep(5)

    print("Press 'Esc' to stop the program.")
    while not keyboard.is_pressed('esc'):  # Continue until 'Esc' is pressed
        try:
            detected_text = capture_text(top_left, bottom_right)

            # Remove old text and type only new text
            new_text = detected_text[len(prev_text):].strip()
            
            if new_text:
                type_text(new_text)
                prev_text = detected_text

            time.sleep(10)  # Wait for 10 seconds before detecting again
        except Exception as e:
            logging.error(f"Unexpected error in the main loop: {e}")
            time.sleep(5)  # Short delay to prevent a rapid error loop

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Program stopped manually")
