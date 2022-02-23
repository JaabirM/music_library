class MusicLibrary:
    def __init__(self):
        self.song_list = []

    def add(self, song_name):
        return self.song_list.append(song_name)

    def all(self):
        return self.song_list

    def remove(self, number):
        try:
            return self.song_list.pop(number)
        except IndexError:
            return None
    
    def search(self, term, type):
        filtered = []
        if type == "title":
            filtered = filter(lambda track: str(term) in track.title.lower(), self.song_list)
        elif type == "artist":
            filtered = filter(lambda track: str(term) in track.artist.lower(), self.song_list)
        elif type == "file":
            filtered = filter(lambda track: str(term) in track.file.lower(), self.song_list)
        else:
            for i in self.song_list:
                result = vars(i)
                for (k, v) in result.items():
                    if str(term) in v.lower():
                        if i not in filtered:
                            filtered.append(i)
        return list(filtered)

from dataclasses import dataclass

@dataclass
class Track:
    title: str
    artist: str
    file: str

