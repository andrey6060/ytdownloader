from pytube import YouTube
from youtubesearchpython import *
import datetime
import locale

def audio():
    global extAud
    
    searchTerms = input("\n\nAramak için yazın: ")
    results = VideosSearch(searchTerms, limit = 1)

    for i in range(1):
        url = results.result()['result'][i]['link']

    yt1 = YouTube(url)

    print("\nBaşlık:", yt1.title)
    print("İzlenme Sayısı:",locale.format_string("%d", yt1.views, grouping=True))
    leng = yt1.length
    print("Uzunluk:", datetime.timedelta(seconds=leng))
    print("Derecelendirme: ", int(yt1.rating), "/5", sep='')

    audSelection = input("\nİndirmek için y/n kullanabilirsiniz: ")

    if audSelection == "y" or audSelection == "Y":
        print("Ses dosyaları MP3 formatında en yüksek kalitede indirilecektir.")
        yd = yt1.streams.filter(file_extension='mp3').get_highest_resolution
        print("İndirme başladı...")
        yd.download('YTDownloader/Audio')
        print("İndirme tamamlandı. Klasör: YTDownload")
    extAud = input("Devam etmek istiyor musunuz? Çıkmak veya devam etmek için y/n kullanabilirsiniz: ")

def video():
    global extVid
    
    searchTerms = input("\n\nAramak için yazın: ")
    results = VideosSearch(searchTerms, limit = 1)

    for i in range(1):
        url = results.result()['result'][i]['link']
    yt = YouTube(url)

    print("\nBaşlık:", yt.title)
    print("İzlenme Sayısı:",locale.format_string("%d", yt.views, grouping=True))
    leng = yt.length
    print("Uzunluk:", datetime.timedelta(seconds=leng))
    print("Derecelendirme: ", int(yt.rating), "/5", sep='')

    vidSelection = input("\nİndirmek için y/n kullanabilirsiniz: ")

    if vidSelection == "y" or vidSelection == "Y":
        streams = set()
        for stream in yt.streams.filter(type="video").filter(file_extension='mp4').filter(progressive=True):
            streams.add(stream.resolution)
        print("\nKullanılabilir çözünürlükler:", streams)

        selectedRes = input("""Bir çözünürlüğü seçmek için \"360\" veya \"720p\" gibi yazabilirsiniz. Sadece 360p ve 720p desteklenir.
Seçim: """)

        if selectedRes == "360" or selectedRes == "360p":
            yd = yt.streams.get_by_resolution('360p')
            print("\nİndirme başladı...")
            yd.download('YTDownloader/Video/360p')
            print("İndirme tamamlandı. Klasör: YTDownloader")
            
        elif selectedRes == "720" or selectedRes == "720p":
            yd = yt.streams.get_by_resolution('720p')
            print("\nİndirme başladı...")
            yd.download('YTDowloader/Video/720p')
            print("İndirme tamamlandı. Klasör: YTDownloader")
    extVid = input("Devam etmek istiyor musunuz? Çıkmak veya devam etmek için y/n kullanabilirisiniz: ")

def main():
    global selection
    
    locale.setlocale(locale.LC_ALL, 'tr_TR')
    print("\nYouTube Video İndirme Aracı\n")
    print("""Seçiminizi sayı olarak girin.
Menü:
(1) Video İndir
(2) Ses İndir""")

    selection = input("Seçim: ")


def menu():    
    if selection == "1":
        video()
        if extVid == "y" or extVid == "Y":
            main()
            menu()
        elif extVid == "n" or extVid == "N":
            video()
        else:
            print("\nGeçerli bir seçim girin.")
            video()
    elif selection == "2":
        print("\nSes indirmeleri şu anlık çalışmıyor.")
        main()
        menu()

main()
menu()

