#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:01:07 2020

@author: avni_aaron
"""


from vlc import Instance
import time
import os

class VLC:
    def __init__(self):
        self.Player = Instance('--loop')

    def addPlaylist(self, path):
        self.mediaList = self.Player.media_list_new()
        #path = "/Users/avni_aaron/Desktop/Classical_music"
        songs = os.listdir(path)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)
    def play(self):
        self.listPlayer.play()
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.stop()
player = VLC()
player.addPlaylist()

player.play()
time.sleep(1)

player.next()
time.sleep(1)

player.pause()
time.sleep(1)

player.play()
time.sleep(1)

player.previous()
time.sleep(1)

player.next()
time.sleep(1)

player.stop()