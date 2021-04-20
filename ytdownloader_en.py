from pytube import YouTube
from youtubesearchpython import *
import datetime
import locale

def audio():
    global extAud
    
    searchTerms = input("\n\nWrite to search: ")
    results = VideosSearch(searchTerms, limit = 1)

    for i in range(1):
        url = results.result()['result'][i]['link']

    yt1 = YouTube(url)

    print("\nTitle:", yt1.title)
    print("Views:",locale.format_string("%d", yt1.views, grouping=True))
    leng = yt1.length
    print("Length:", datetime.timedelta(seconds=leng))
    print("Stars: ", int(yt1.rating), "/5", sep='')

    audSelection = input("\nFor downloading, you can use y/n: ")

    if audSelection == "y" or audSelection == "Y":
        print("Audio files will be downloading at highest resolution.")
        yd = yt1.streams.filter(file_extension='mp3').get_highest_resolution
        print("Download started...")
        yd.download('YTDownloader/Audio')
        print("Download completed. Folder: YTDownload")
    extAud = input("Do you want to continue? You can use y/n to exit or continue: ")

def video():
    global extVid
    
    searchTerms = input("\n\nWrite to search: ")
    results = VideosSearch(searchTerms, limit = 1)

    for i in range(1):
        url = results.result()['result'][i]['link']
    yt = YouTube(url)

    print("\nTitle:", yt.title)
    print("Views:",locale.format_string("%d", yt.views, grouping=True))
    leng = yt.length
    print("Length:", datetime.timedelta(seconds=leng))
    print("Stars: ", int(yt.rating), "/5", sep='')

    vidSelection = input("\nYou can use y/n to download: ")

    if vidSelection == "y" or vidSelection == "Y":
        streams = set()
        for stream in yt.streams.filter(type="video").filter(file_extension='mp4').filter(progressive=True):
            streams.add(stream.resolution)
        print("\nDownloadable resolutions:", streams)

        selectedRes = input("""For selecting a resolution, you can write like \"360\" or \"720p\". Only 360p and 720p supported.
Selection: """)

        if selectedRes == "360" or selectedRes == "360p":
            yd = yt.streams.get_by_resolution('360p')
            print("\nDownload started...")
            yd.download('YTDownloader/Video/360p')
            print("Download completed. Folder: YTDownloader")
            
        elif selectedRes == "720" or selectedRes == "720p":
            yd = yt.streams.get_by_resolution('720p')
            print("\nDownload started...")
            yd.download('YTDowloader/Video/720p')
            print("Download completed. Folder: YTDownloader")
    extVid = input("Do you want to continue? You can use y/n to exit or continue: ")

def main():
    global selection
    
    locale.setlocale(locale.LC_ALL, 'en_US')
    print("\nYouTube Video Downloader\n")
    print("""Enter your selection in integer.
Menu:
(1) Download Video
(2) Download Audio""")

    selection = input("Selection: ")


def menu():    
    if selection == "1":
        video()
        if extVid == "y" or extVid == "Y":
            main()
            menu()
        elif extVid == "n" or extVid == "N":
            video()
        else:
            print("\nEnter a valid selection.")
            video()
    elif selection == "2":
        print("\nAudio downloads not working at the moment.")
        main()
        menu()

main()
menu()

