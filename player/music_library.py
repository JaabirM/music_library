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
    
    def search(self, condition):
        if isinstance(condition, str):
            filtered = []
            for i in self.song_list:
                result = vars(i)
                for (k, v) in result.items():
                   if str(condition) in v.lower():
                     if i not in filtered:
                        filtered.append(i)
            return list(filtered)          
        else:
            return list(filter(condition, self.song_list))

from dataclasses import dataclass

@dataclass
class Track:
    title: str
    artist: str
    file: str

