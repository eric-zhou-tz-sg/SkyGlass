import os
import subprocess

# Input folder containing videos
input_folder = "file path of videos" #edit
# Output folder to save the extracted frames
output_folder = "file path of images" #edit

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Range of video filenames
start_number = 7034 #edit
end_number = 7077 #edit

# Loop through the videos
for i in range(start_number, end_number + 1):
    input_file = os.path.join(input_folder, f"IMG_{i}.mov") #edit if needed
    video_output_folder = os.path.join(output_folder, f"IMG_{i}_frames") #edit if needed
    
    # Create a folder for the frames of this video
    os.makedirs(video_output_folder, exist_ok=True)
    
    # Construct the ffmpeg command
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_file,               # Input video
        "-vf", "fps=5",                 # Extract at 5 frames per second. Edit if needed
        os.path.join(video_output_folder, "frame_%04d.jpg")  # Output pattern
    ]
    
    # Run the command
    try:
        print(f"Processing {input_file}...")
        subprocess.run(ffmpeg_command, check=True)
        print(f"Frames saved in {video_output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {input_file}: {e}")
