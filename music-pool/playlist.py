import youtube_dl
import csv
import os


class YoutubePlaylist:
    def __init__(self, _playlist_file, _filename):
        try:
            dir_meta = _playlist_file.split("/")
            self.playlist_filepath = _playlist_file
            self.genre = dir_meta[-1]
            self.filename = _filename
            self.yturls = self.__read_csv_content(os.path.join(_playlist_file, _filename))

        except Exception as ex:
            raise ValueError("(YoutubePlaylist) Error in playlist creation: " + repr(ex))

    def start_download(self, output, archive):
        try:
            ydl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
                "prefer_ffmpeg": True,
                "keepvideo": False,
                # 'outtmpl': f"/home/jhonatas/development/iaa-music-discovery/my-dataset/downloads/{genre}/%(title)s-%(id)s.%(ext)s",
                "outtmpl": f"{output}/%(title)s.%(ext)s",
                "restrictfilenames": True,
                "download_archive": archive,
                "ignoreerrors": True,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(self.yturls)
        except Exception as ex:
            raise ValueError("(YoutubePlaylist) Error in start_download " + repr(ex))

    def __read_csv_content(self, filename):
        results = []
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)  # change contents to floats
            for row in reader:  # each row is a list
                results.append(row[0])
        return results