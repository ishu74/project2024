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
    file_path = "C:\\Users\\vaibh\\OneDrive\\Desktop\\test\\Blink\\Blink.ino"
    
    open_arduino_ide()
    open_ino_file(file_path)
    compile_and_upload()
    close_arduino_ide()

if __name__ == "__main__":
 asyncio.run(main())


# import os
# import time
# import pyautogui
# import subprocess
# import asyncio
# import pywin32
# import win32gui
# import win32con

# # Function to open Arduino IDE
# async def open_arduino_ide():
#     subprocess.Popen(["arduino.exe"])
#     await asyncio.sleep(3)  # Adjust as needed

# # Function to open .ino file in Arduino IDE
# async def open_ino_file(file_path):
#     await asyncio.sleep(7)  # Adjust delay as needed

#     # Press Ctrl + O to open file
#     pyautogui.hotkey('ctrl', 'o')  

#     # Wait for the file dialog window to open
#     await asyncio.sleep(7)  

#     # Type the file path directly using keyboard shortcuts
#     pyautogui.write(file_path)  

#     # Press Enter to open the file
#     pyautogui.press('enter')  

#     # Wait for the new file window to appear
#     await asyncio.sleep(10)  # Adjust delay as needed

#     # Get the handle of the new window
#     hwnd = win32gui.GetForegroundWindow()

#     # Maximize the window
#     win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# # Function to compile and upload .ino file
# async def compile_and_upload():
#     await asyncio.sleep(10)  # Adjust as needed
#     pyautogui.click(x=100, y=100)  # Click to focus on Arduino IDE (adjust coordinates if needed)
#     await asyncio.sleep(1)
#     pyautogui.hotkey('ctrl', 'r')  # Press Ctrl + R to compile
#     await asyncio.sleep(10)  # Wait for compilation to finish (adjust time if needed)
#     pyautogui.hotkey('ctrl', 'u')  # Press Ctrl + U to upload
#     await asyncio.sleep(10)  # Wait for upload to finish (adjust time if needed)

# # Function to close Arduino IDE
# async def close_arduino_ide():
#     subprocess.run("TASKKILL /F /IM arduino.exe", shell=True)

# # Main function
# async def main():
#     # Replace 'file_path' with the path to your .ino file
#     file_path = "C:\\Users\\vaibh\\OneDrive\\Desktop\\test\\Blink\\Blink.ino"

#     await open_arduino_ide()
#     await open_ino_file(file_path)
#     await compile_and_upload()
#     await close_arduino_ide()

# if __name__ == "__main__":
#     asyncio.run(main())
