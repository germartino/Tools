import cv2
from PIL import Image
import os

def capture_screenshot_from_video(video_path, output_folder, screenshot_key, resolution, playback_speed):
    """
    Plays the video at the specified speed and allows the user to press the specified key to take a screenshot
    at any point. The screenshot is saved in the specified folder with the specified resolution.
    
    :param video_path: Path to the input video file (MP4).
    :param output_folder: Folder where the output images will be saved.
    :param screenshot_key: Key that the user presses to take a screenshot.
    :param resolution: A tuple specifying the desired resolution (width, height) for the screenshot.
    :param playback_speed: Delay between frames in milliseconds to control playback speed.
    """
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print("Error: Could not open video.")
        return
    
    screenshot_count = 0
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    print(f"Press '{screenshot_key.upper()}' or '{screenshot_key.lower()}' to take a screenshot.")
    print("Press 'q' to quit the video.")
    
    while video.isOpened():
        # Read frame-by-frame
        ret, frame = video.read()
        
        if not ret:
            print("End of video or error.")
            break
        
        # Display the frame
        cv2.imshow('Video', frame)
        
        # Wait for a key press with playback speed adjustment
        key = cv2.waitKey(playback_speed) & 0xFF
        
        # If the user-defined key is pressed, take a screenshot
        if key == ord(screenshot_key.lower()) or key == ord(screenshot_key.upper()):  # Case-insensitive
            screenshot_count += 1
            screenshot_path = os.path.join(output_folder, f"screenshot_{screenshot_count}.png")
            
            # Convert the frame to an image and resize it
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            resized_image = image.resize(resolution, Image.LANCZOS)
            
            # Save the image
            resized_image.save(screenshot_path)
            print(f"Screenshot {screenshot_count} saved to {screenshot_path}")
        
        # If 'q' is pressed, exit the loop
        if key == ord('q'):
            break
    
    # Release the video capture and close windows
    video.release()
    cv2.destroyAllWindows()

# Get user input from terminal
video_path = input("Enter the path to the video file: ")
screenshot_key = input("Enter the key to use for taking a screenshot (e.g., 'S'): ")
playback_speed = int(input("Enter the playback speed (smaller number = faster, e.g., 10 for fast): "))

# Set the output folder to the Desktop
desktop_path = os.path.expanduser("~/Desktop")
output_folder = os.path.join(desktop_path, "Screenshots")

# Set desired resolution (you can modify this as needed)
resolution = (1920, 1080)  # Set the desired resolution (width, height)

# Call the function to start video playback and screenshot capture
capture_screenshot_from_video(video_path, output_folder, screenshot_key, resolution, playback_speed)
