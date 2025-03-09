#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 23:39
# @Author      : Jim
# @File        : Facade.py
# @Software    : PyCharm
# @Description :

# 外观类
class MusicPlayer:
    def __init__(self):
        self.mp3_player = MP3Player()
        self.flac_player = FLACPlayer()

    def play_mp3(self, file_path, volume):
        self.mp3_player.load(file_path)
        self.mp3_player.set_volume(volume)
        self.mp3_player.play()

    def play_flac(self, file_path, volume):
        self.flac_player.load(file_path)
        self.flac_player.set_volume(volume)
        self.flac_player.play()


class MP3Player:
    def load(self, file_path):
        print(f"Loading MP3 file from {file_path}")

    def set_volume(self, volume):
        print(f"Setting MP3 volume to {volume}")

    def play(self):
        print("Playing MP3 music")


class FLACPlayer:
    def load(self, file_path):
        print(f"Loading FLAC file from {file_path}")

    def set_volume(self, volume):
        print(f"Setting FLAC volume to {volume}")

    def play(self):
        print("Playing FLAC music")
