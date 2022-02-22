import unittest

from player.music_library import *


class TestMusicLibrary(unittest.TestCase):
    library = MusicLibrary()
    track1 = Track("Title1", "Artist1", "Track1.mp4")
    track2 = Track("Title2", "Artist2", "Track2.mp4")
    
    def test_constructs(self):
        MusicLibrary()

    def test_can_add_songs(self):
        self.library.add(self.track1)
        self.library.add(self.track2)
        self.assertEqual(self.library.all(), [self.track1, self.track2])
    
    def test_can_list_songs(self):
        self.library.add(self.track1)
        self.assertEqual(self.library.all(), [self.track1, self.track2, self.track1])

    def test_can_remove_song(self):
        self.library.remove(1)
        self.assertEqual(self.library.all(), [self.track1, self.track1])