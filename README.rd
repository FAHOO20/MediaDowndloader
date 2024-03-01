# TV Show Episode Downloader

## Overview
This program is designed to download individual episodes of TV shows from various online video platforms. It organizes the downloaded episodes with a structured naming convention, such as 'ShowNameS01E05', making it ideal for maintaining an organized collection of TV show episodes.

## Features
- **Multi-Platform Support**: Compatible with various video platforms, not limited to YouTube.
- **Automatic Episode Number Extraction**: Extracts the episode number from the video title and formats it systematically.
- **Custom File Naming**: Downloads are saved with names following the format `ShowNameS[season]E[episode_number]`.
- **Directory Listing**: The program can list all files in a given directory, useful for managing downloaded content.

## Usage
1. **Set Season Number**: Modify the `season_number` variable in the script according to the season of the show.
2. **Execute the Script**: Run the script and follow the prompts.
3. **Enter Video URL**: Input the URL of the video you wish to download.
4. **Specify Output Directory**: Enter the desired save location for the downloaded file.
5. **Download and Organize**: The script will download the video, name it according to the specified format, and save it in the chosen directory.

## Installation
Requires Python 3.x and the `youtube_dl` library. Install `youtube_dl` using pip:
```bash
pip install youtube-dl
```

## Customization
You can adjust the script for different naming conventions or video formats as needed.

## Disclaimer
This tool is for personal use only. Ensure compliance with the Terms of Service of the video platform and legal restrictions in your country regarding content downloading.