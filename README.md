## getsubs.py is a python script to download subtitles

### Installation

1. Install [ffmpeg](https://ffmpeg.org/download.html)
1. Open command prompt/terminal
1. Clone the repository
    
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

When run with no additional parameters, the script will query 
for the latest files and display the titles.  You are prompted
to enter the corresponding number of the title and the script
will download and display the subtitles.

The script can also be run by adding either the name of a video file 
previously downloaded:

`python3 getjwsubs.py video.mp4`

Or a URL of a video file:

`python3 getjwsubs.py htttps://website.com/cool_video.mp4`

The subtitles that are encoded into the video file will be extracted
and displayed.  These are sometimes known as "soft subtitles".

NOTE: the script will *not* attempt to extract susbtitles from the audio
track(s).
