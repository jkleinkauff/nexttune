from playlist import YoutubePlaylist
from audio import Audio
from PIL import Image
import settings
import os
import sys


def download_playlists(playlist_folder, output):
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(playlist_folder)):    
        has_genre = not not (os.path.split(playlist_folder)[-1]) 
        if (not has_genre and dirpath is not playlist_folder) or has_genre:
            for f in filenames:
                pl = YoutubePlaylist(dirpath, f)
                pl.start_download(output, settings.AUDIO_PLAYLIST_ARCHIVE)


def trim_audio_files(mp3_folder, output):
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(mp3_folder)):
        dir_meta = dirpath.split("/")
        parent = dir_meta[-1]  # from folder/genre get 'genre'
        for f in filenames:
            a = Audio(os.path.join(dirpath, f))
            a.cut_audio(30, os.path.join(output, f))


def create_spectrograms(audio_folder, output):
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(audio_folder)):
        for f in filenames:
            a = Audio(os.path.join(dirpath, f))
            name = f.split(".")[0]
            a.load()
            a.create_mel_spec_image(os.path.join(output, name + ".jpg"))


def slice_spectrograms(spectrograms_folder, output):
    counter = 0
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(spectrograms_folder)):
        for f in filenames:
            img = Image.open(os.path.join(dirpath, f))
            subsample_size = 128
            width, height = img.size
            number_of_samples = width / subsample_size
            for i in range(int(number_of_samples)):
                start = i * subsample_size
                img_temporary = img.crop(
                    (start, 0.0, start + subsample_size, subsample_size)
                )
                img_temporary.save(os.path.join(output, f"{counter}_{f}"))
                counter = counter + 1


if __name__ == "__main__":
    try:
        download_genre = ""
        if len (sys.argv) > 1:
            download_genre = sys.argv[1]

        playlist_folder = f"{settings.AUDIO_PLAYLIST_FOLDER}/{download_genre}"
        import pdb;
        pdb.set_trace()
        # download playlists from AUDIO_PLAYLIST_FOLDER
        download_playlists(playlist_folder, settings.AUDIO_DOWNLOAD_FOLDER)
        # trim audio files
        # trim_audio_files(settings.AUDIO_DOWNLOAD_FOLDER, settings.AUDIO_30SEC_FOLDER)
        # create_spectrograms(
        #     settings.AUDIO_30SEC_FOLDER, settings.AUDIO_SPECTROGRAM_FOLDER
        # )

        # slice_spectrograms(
            # settings.AUDIO_SPECTROGRAM_FOLDER, settings.AUDIO_SLICED_SPECTROGRAM_FOLDER
        # )

    except Exception as ex:
        print(ex)
