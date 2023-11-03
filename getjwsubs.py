# DONE: Add option to provide https link to extract susbtitles from.
# TODO: Handle input out of range
# DONE: if we are passed a video file name just process it.......

import os
import re
import json
# import textwrap
import ffmpeg
import subprocess
import sys
import requests
import html2markdown

url="https://b.jw-cdn.org/apis/mediator/v1/categories/E/LatestVideos?detailed=1&clientType=www"
tmp = ""
banner = """   .-..-.  .-.     .----..-. .-.----. .-----..-..-----..-.   .----. .----. 
   | || {  } |    { {__-`| } { | {_} }`-' '-'{ |`-' '-'} |   } |__}{ {__-` 
{`-' }{  /\  }    .-._} }\ `-' / {_} }  } {  | }  } {  } '--.} '__}.-._} } 
 `---'`-'  `-'    `----'  `---'`----'   `-'  `-'  `-'  `----'`----'`----'  
                                                                           """
helptext = """This program has two modes of operation:

            With no command line parameters the program queries for the latest videos from jw.org and allows
            you to choose which one you'd like the subtitles for and then displays them.

            If you provide the URL of a video file as the command line parameter, the program downloads the video
            and atbbtempts to extract the subtitle information from the video to display.

            IMPORTANT: The second option requires that you have installed FFpmeg and the ffmpeg.exe program is 
            available in your PATH.
            
            You can find FFmpeg at:  https://ffmpeg.org/download.html"""                                            
helptextalt = """               This program queries for the latest videos from jw.org and allows
            you to choose which one you'd like the subtitles for and then displays them.
            """

def help():
    print(banner)
    print(helptextalt)
    sys.exit()

def download_file(url):
    r = requests.get(url)
    lines = r.iter_lines()
    return lines

def download_video(url, mytmp):
    filename = mytmp + url.split("/")[-1]
    print("Filename: ", filename)
    if os.path.isfile(filename):
        print("Already downloaded: ", filename)
        return(filename)
    print("Downloading to: ", filename)
    try:
        query_parameters = {"downloadformat": "mp4"}
        response = requests.get(url, params=query_parameters, stream=True)
        if response.ok:
            with open(filename, mode="wb") as file:
                for chunk in response.iter_content(chunk_size=10 * 1024):
                    file.write(chunk)
        # else:
        #     print("Something didn't work downloading the file.")
        #     print("Error: ", response.ok)
        #     return("fail")
        return(filename)
    except Exception as e:
        print(e)
        return("fail")

def get_title(input_file):
      try:
          metadata = ffmpeg.probe(input_file, show_entries="format_tags=title")
          title = metadata.get('format', {}).get('tags', {}).get('title', '')
          title = re.sub(":", "\:", title)
          title = re.sub('"', "", title)
          #title = re.sub("\.", "", title)
          # title = re.sub("(", "- ", title)
          # title = re.sub(")", "", "title)
          title = re.sub(",", "", title)
          if title:
              return title.strip()
          else:
              return()
      except ffmpeg.Error as e:
          print(f"Error getting title metadata: {e.stderr}")
          return None

def get_subtitles(video):
    srt = video + ".srt"
    # print("Processing subtitles from video to:", srt)
    cmd = ["ffmpeg", "-y", "-i", video, srt]
    # os.remove(srt)
    try:
        subprocess.run(cmd, check=True, capture_output=True)
    except CalledProcessError as e:
        print(f"Error extracting subtitles: {e.stderr}")
    with open(srt, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return(lines)


def processlines(lines):
    result_lines = []
    current_line = ""
    for line in lines:
        #line = line.strip().decode("utf-8")
        line = line.strip()
        # Convert any html elements to markdown
        line = html2markdown.convert(line)
        # Remove the vtt header
        if re.match("WEBVTT", line):
            continue
        # Skip lines that begin with a number
        if re.match(r"^\d", line):
            continue
        # Skip lines that contain only numbers and symbols
        if re.match(r"^[0-9\W]+$", line):
            continue
        #current_line += line
        # Strip any remaining html stuff
        line = re.sub("<[^<]+?>", "", line)
        # Skip blank lines
        if not line:
            continue
        # Concatenate lines less than 120 characters
        # NOTE: This is the lazy way, really should be working with words.
        if line:
            if len(current_line) + len(line) <= 120:
                current_line += line + " "
            else:
                result_lines.append(current_line.strip())
                current_line = line + " "
    # Add the last line
    if current_line:
        result_lines.append(current_line.strip())
    return(result_lines)

def main():
    print("\nSubtitle downloader for jw.org videos.\n")
    #print("Visit the official website of Jehovah's Witnesses: https://jw.org")
    print(banner)
    if len(sys.argv) == 2:
        vidurl = sys.argv[1]
        if vidurl == '--help':
            help()
            exit()
        if vidurl.endswith('.mp4'):
            if vidurl.startswith('http'):
                download = download_video(vidurl, tmp) 
            else:
                download = vidurl
            if download == "fail":
                print("I'm sorry, the download failed.")
                exit(1)
            title = get_title(download)
            subs = get_subtitles(download)
            subs = processlines(subs)
            # os.remove(srt_file)
            print("\nTitle: ", title)
            print("\n-----Subtitles begin here.-----\n")
            print(*subs, sep="\n")
            print("\n\n-----Subtitles end here.-----\n")
        else:
            print("ERROR: That doesn't appear to be a valid URL.\n")
            help()
    # Default run with querying new videos
    else:
        r = requests.get(url)
        r_dict = r.json()
        r_json = json.dumps(r_dict, indent=4)
        parsed_json = json.loads(r_json)
        media = parsed_json["category"]["media"]
        vidslist = []
        for item in range(len(media)):
            video_key = media[item]["languageAgnosticNaturalKey"]
            title = media[item]["title"]
            subtitles_url = media[item]["files"][3]["subtitles"]["url"]
            video = media[item]["files"][3]["progressiveDownloadURL"]
            download = download_file(subtitles_url)
            subs = processlines(download)
            keys = ['id', 'video key', 'name', 'link', 'subtitles']
            values = [item, video_key, title, video, subs]
            vidslist.append(values)
        while True:
            print(banner)
            print("Number \t Title")
            print("----- \t -----")
            for item in range(len(vidslist)):
                print(vidslist[item][0], "\t", vidslist[item][2])
            print("\n")        
            vidnum = input("Please enter the video number or q to exit: ")
            if vidnum == "":
                continue
            if vidnum == "q":
                break
            if not vidnum.strip().isdigit():
                continue
            subtitle = vidslist[int(vidnum)]
            print("\nTitle: ", subtitle[2])
            print("\nLink: ", subtitle[3])
            # print("\nSubtitles: ")
            print("-----Subtitles begin here.-----\n")
            print(*subtitle[4], sep='\n')
            print("\n\n-----Subtitles end here.-----\n")
    print(banner)
    print("Hope that helps.\nGoodbye.")

if __name__ == "__main__":
    main()
