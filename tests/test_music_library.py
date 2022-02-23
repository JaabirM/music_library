import unittest

from unittest.mock import Mock
from player.music_library import *


class TestMusicLibrary(unittest.TestCase):

    def test_constructs(self):
        MusicLibrary()
        Track("Title1", "Artist1", "Track1.mp4")

    def test_can_add_songs(self):
        library = MusicLibrary()
        mock_track1 = Mock("Title1", "Artist1", "Track1.mp4")
        mock_track2 = Mock("Title2", "Artist2", "Track2.mp4")

        library.add(mock_track1)
        library.add(mock_track2)
        self.assertEqual(library.all(), [mock_track1, mock_track2])
    
    def test_can_list_songs(self):
        library = MusicLibrary()
        mock_track1 = Mock("Title1", "Artist1", "Track1.mp4")

        library.add(mock_track1)
        self.assertEqual(library.all(), [mock_track1])

    def test_can_remove_song(self):
        library = MusicLibrary()
        mock_track1 = Mock("Title1", "Artist1", "Track1.mp4")
        mock_track2 = Mock("Title2", "Artist2", "Track2.mp4")

        library.add(mock_track1)
        library.add(mock_track2)
        library.remove(0)
        self.assertEqual(library.all(), [mock_track2])