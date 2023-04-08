#!/usr/bin/python3

from sys import argv
from pathlib import Path
from extensions import Checker

class Organizer:

    def __init__(self, app_name: str):
        self.app_name: str = app_name
        self.folder_path = None
        self.path_name = None
        
        self.texts:     list = list()
        self.audio:     list = list()
        self.images:    list = list()
        self.videos:    list = list()
        self.archives:  list = list()
        self.documents: list = list()

        self.checker = Checker()

        self.texts_path      = "/Texts"
        self.audio_path      = "/Music"
        self.images_path     = "/Photos"
        self.videos_path     = "/Videos"
        self.archives_path   = "/Archives"
        self.documents_path  = "/Documents"

    def gather_info(self, folder_path: str):
        try:
            self.folder_path = Path(folder_path)
            self.path_name = self.folder_path.resolve().__str__()
                
            directory_names = [x.name for x in self.folder_path.iterdir() if x.is_file()]

        except FileNotFoundError:
            print("\n! That's not a correct name or directory doesn't exist")
            raise SystemExit

        for obj in directory_names:
            if self.checker.is_image(obj):
                self.images.append(obj)
                continue

            if self.checker.is_text(obj):
                self.texts.append(obj)
                continue

            if self.checker.is_audio(obj):
                self.audio.append(obj)
                continue

            if self.checker.is_archive(obj):
                self.archives.append(obj)
                continue

            if self.checker.is_video(obj):
                self.videos.append(obj)
                continue

            if obj:
                self.documents.append(obj)
                continue

    def all_move(self, dest, new_dest):
        for obj_name in dest:
            Path(self.path_name + f"/{obj_name}").rename(
                self.path_name + new_dest + f"/{obj_name}")

    def sort(self):
    
        if len(self.texts):
            if (Path(self.path_name + self.texts_path).exists()):
                self.all_move(self.texts, self.texts_path)
            else:
                Path(self.path_name + self.texts_path).mkdir(exist_ok=True)
                self.all_move(self.texts, self.texts_path)
                
        if len(self.audio):
            if (Path(self.path_name + self.audio_path).exists()):
                self.all_move(self.audio, self.audio_path)
            else:    
                Path(self.path_name + self.audio_path).mkdir()
                self.all_move(self.audio, self.audio_path)
            
        if len(self.images):
            if (Path(self.path_name + self.images_path).exists()):
                self.all_move(self.images, self.images_path)
            else:
                Path(self.path_name + self.images_path).mkdir()
                self.all_move(self.images, self.images_path)

        if len(self.videos):
            if (Path(self.path_name + self.videos_path).exists()):
                self.all_move(self.videos, self.videos_path)
            else:
                Path(self.path_name + self.videos_path).mkdir()
                self.all_move(self.videos, self.videos_path)

        if len(self.archives):
            if(Path(self.path_name + self.archives_path).exists()):
                self.all_move(self.archives, self.archives_path)
            else:
                Path(self.path_name + self.archives_path).mkdir()
                self.all_move(self.archives, self.archives_path)

        if len(self.documents):
            if (Path(self.path_name + self.documents_path).exists()):
                self.all_move(self.documents, self.documents_path)
            else:
                Path(self.path_name + self.documents_path).mkdir()
                self.all_move(self.documents, self.documents_path)

    def start(self):
        if len(argv) <= 1:
            print("Usage:\n      [python] pyfonizer.py [path to dir]")
            raise SystemExit
        
        organizer.gather_info(argv[1])

        print("Sorting...")
        organizer.sort()

        print("Complete.")

    def args(self):
        print(argv)

if __name__ == '__main__':
    organizer = Organizer("Pyfonizer")
    organizer.start()
