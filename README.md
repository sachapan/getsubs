## getsubs.py is a python script to download subtitles either by querying for the latest videos
## or providing a video file or a url to a video file.

### Installation

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
