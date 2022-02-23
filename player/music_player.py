import subprocess

class MusicPlayer:
  def __init__(self, subprocess):
    self.subprocess = subprocess

  def play(self, path):
    return self.subprocess.call(['afplay', path])
