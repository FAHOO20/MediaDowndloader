import youtube_dl
import os
import re

""" 
TV Show Episode Downloader

A versatile script for downloading episodes from various online video platforms. 
It automatically formats the downloaded files in a structured naming convention, 'ShowNameS01E05', 
facilitating easy organization and management of TV show collections.
Designed for flexibility and ease of use across multiple video sources.
 """

def list_files_in_directory(directory):
    """List all files in the given directory and store their names in an array."""
    files = []
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,item)):
            files.append(item)
    return files

def find_number_in_string(s):
    try:
        # Check if the input is a string
        if not isinstance(s, str):
            raise TypeError("Input must be a string")

        # Regular expression to find numbers from 01 to 999 in the string
        pattern = r'(?<!\d)(0?[1-9][0-9]{0,2})(?!\d)'
        
        # Searching for the pattern in the string
        match = re.search(pattern, s)
        
        # If a match is found, return the matched string, with adjustments if necessary
        if match:
            matched_number = match.group()
            number = int(matched_number)
            if number < 10 and not matched_number.startswith("0"):
                # For single-digit numbers without a leading zero, add one
                return f"0{number}"
            else:
                # Return the matched number as is
                return matched_number
        else:
            return "No number found in the string !"
    except Exception as e:
        # Handle any other unexpected exceptions
        return f"An error occurred: {e}"


# Assuming season is constant, for example, Season 01
season_number = '01'  # Modify as needed



video_url = input("Enter video URL: ")
show_name = input("Enter Show Name: ")
# Create a YoutubeDL object and extract video info
with youtube_dl.YoutubeDL() as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    video_title = info_dict.get('title', None)

episode_number = find_number_in_string(video_title)
if episode_number == "No number found in the string !":
    # Handle this case as needed, e.g., ask the user for the episode number
    episode_number = input("Enter the episode number: ")


output_directory = input("enter your output directory: ")
file_name = f"{show_name}S{season_number}E{episode_number}"

ydl_opts = {
    'format': 'best',
    'outtmpl': os.path.join(output_directory, f'{file_name}.%(ext)s'),
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
