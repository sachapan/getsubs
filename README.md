# Downloads and/or extracts subtitles from videos primarily from https://jw.org


### Quick and easy: run the docker image

`docker run -it ghcr.io/sachapan/getsubs`

### Installation

1. Install [ffmpeg](https://ffmpeg.org/download.html)
1. Open a terminal or command prompt.
1. Clone the repository:
    
    `git clone https://github.com/sachapan/getsubs.git`

    `cd getsubs`
1. Install python 3

    [Windows](https://www.python.org/downloads/windows/)

    Linux use the package manager, e.g. on Debian based systems:

    `sudo apt install python3`

    [Mac OS](https://docs.python.org/3/using/mac.html)

2. Install pip
    
    `python3 install pip --upgrade`

3. Optional: create a virtual environment
    
    `python3 -m venv .`
    
    Windows:
        
   `Scipts\activate`
    
    Linux/Mac:
        
   `source bin/activate`

4. Install necessary python packages
    
    `pip install -r requirements.txt`

5. Run the script:
    
    `python3 getjwsubs.py`

6. Deactivate the python virtual environment.
    
    `deactivate`

### Usage

Subtitle downloader for jw.org videos.

usage: getjwsubs.py [-h] [-d] [-t] [video]

This program has two modes of operation:

Mode 1: No command line parameters

The program queries for the latest videos from jw.org and presents a menu from which 
videos can be selected and displays the subtitles therefrom.  The menu also 
allows for a URL of a video file to be supplied from which subtitles are extracted and displayed.

Mode 2:
    
If you provide the URL or the path of a video file as a command line parameter, the program 
downloads the video and attempts to extract the subtitle information from the 
video to display.

There are two additional parameters that can passed when providing the URL:

    -t Outputs the subtitles to a text file in the current directory named with the
            title of the video.
            
    -d Outputs the subtitles to a Microsoft Word docx file in the current directory
            named with the title of the video.

IMPORTANT: 
The second option requires that you have installed FFpmeg and the ffmpeg
program is available in your PATH.

You can find FFmpeg at:  https://ffmpeg.org/download.html


positional arguments:
  video - The URL or local path to a video file containing subtitle metadata.

options:
  -h, --help      show this help message and exit
  -d, --docx      Save subtitles to a docx file.
  -t, --textfile  Save subtitles to a text file.


The script can also be run by adding either the name of a video file 
previously downloaded:

`python3 getjwsubs.py video.mp4`

Or a URL of a video file:

`python3 getjwsubs.py https://website.com/cool_video.mp4`

The subtitles that are encoded into the video file will be extracted
and displayed.  These are sometimes known as "soft subtitles".

NOTE: the script will *not* attempt to extract susbtitles from the audio
track(s).

The subtitles will be displayed on the terminal.



