import praw
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import quote
import sys
import os
import time
import numpy
def main():
    try:
        storage_directory = " " # change to your blank directory
        os.chdir(storage_directory)  
        print("Navigated to directory...")
        # clear directory each day to prevent duplicates
        filelist = [f for f in os.listdir(storage_directory)]
        for f in filelist:
            os.remove(f)
        print("Removed previous files...\n")
        SCRIPT = "p1CoZQuBy9eP4e8YH0dM5Q" 
        SECRET = "6YHiBWbUWEIJMvYt91vuDjOOsCOUOA" 
        NUM_IMAGES = 100
        reddit = praw.Reddit(
            client_id=SCRIPT,
            client_secret=SECRET,
            user_agent="Image_Py",
            username=" ",  # your username
            password=" ",  # your password
        )
        subreddit = reddit.subreddit("wallpaper")
        images = []
        for submission in subreddit.hot(limit=NUM_IMAGES):
            images.append(submission.url)
        sys.stdout.flush()
        for i, image in enumerate(images):
            sys.stdout.write(f"\rWriting image {i+1} of {len(images)}.")
            try:
                imgdata = urlopen(image).read()
                fname = f"image{i+1}.{image.split('.')[-1]}"
                with open(fname, "wb") as handler:
                    handler.write(imgdata)
                # delete images under 200 kB; too fuzzy
                if os.stat(fname).st_size < 200000:
                    os.remove(fname)
            except HTTPError:
                print("\nHTTP Error 500!")
            except FileNotFoundError:
                print(f"\n{image} is an invalid link!")
            except WindowsError:
                pass
        sys.stdout.write("\n")
    except:
        print("Something Went Wrong")
        time.sleep(5)
        exit()

if __name__ == '__main__':
    main()
