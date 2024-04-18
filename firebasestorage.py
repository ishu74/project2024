# python code for file download and upload
import pyrebase

config ={
   "apiKey": "AIzaSyBMlyee3r1ScfeOZfjZAtMFawRBX7Yul0U",
  "authDomain": "test-9cc23.firebaseapp.com",
  "projectId": "test-9cc23",
  "storageBucket": "test-9cc23.appspot.com",
  "messagingSenderId": "632856101519",
  "appId": "1:632856101519:web:012b4ae30e898c105a26fa",
  "measurementId": "G-3EQ5YTH5JP",
  "serviceAccount": "serviceAccount.json",
  "databaseURL": "https://test-9cc23-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
# upload
# storage.child("Blink1.ino").put("Blink.ino")

# download
storage.download("Blink1.ino", "Blink2.ino")


# for automation
import os
import time
import pyautogui
import subprocess
import pygetwindow as gw
import asyncio
import win32gui
import win32con

# Function to open Arduino IDE
def open_arduino_ide():
    
    pyautogui.press('win')  # Press Windows key to open Start menu
    time.sleep(4)
    pyautogui.typewrite('Arduino IDE')  # Type Arduino IDE in the search bar
    time.sleep(4)
    pyautogui.press('enter')  # Press Enter to open Arduino IDE
    time.sleep(20)

# Function to open .ino file in Arduino IDE
def open_ino_file(file_path):
    pyautogui.hotkey('ctrl', 'o')  # Press Ctrl + O to open file
    time.sleep(10)
    pyautogui.write(file_path)  # Type the file path
    pyautogui.press('enter')  # Press Enter to open the file
    time.sleep(6)

# ok process

def ok():
    pyautogui.press('enter')  # Press Enter to open the file
    time.sleep(10)


# Function to compile and upload .ino file
def compile_and_upload():

       # Get the handle of the new window
    arduino_window = gw.getWindowsWithTitle("Arduino")[0]  # Adjust the title as needed
    
    # Maximize the new window
    arduino_window.maximize()
    pyautogui.click(x=100, y=100)  # Click to focus on Arduino IDE (adjust coordinates if needed)
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'r')  # Press Ctrl + R to compile
    time.sleep(10)  # Wait for compilation to finish (adjust time if needed)
    pyautogui.hotkey('ctrl', 'u')  # Press Ctrl + U to upload
    time.sleep(10)  # Wait for upload to finish (adjust time if needed)


# Function to close Arduino IDE
async def close_arduino_ide():
    await subprocess.run("TASKKILL /F /IM arduino.exe", shell=True)

# Main function
def main():
    # Replace 'file_path' with the path to your .ino file
    file_path = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\project24\\Blink2.ino"
    
    open_arduino_ide()
    open_ino_file(file_path)
    ok()
    compile_and_upload()
    close_arduino_ide()
    

if __name__ == "__main__":
 asyncio.run(main())




