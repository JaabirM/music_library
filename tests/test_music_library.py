from audioop import add
import unittest

from player.music_library import *


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def can_add_songs(self):
        add("Song1")
        add("Song2")
        self.assertEqual(self.all ["Song1", "Song2"])
    
    def can_list_songs(self):
        add("Song1")
        self.assertEqual(self.all, ["Song1"])

    def can_remove_song(self):
        add("Song1")
        add("Song2")
        self.assertEqual(self.remove(1), [])