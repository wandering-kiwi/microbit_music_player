import microbit
import time

# importing vlc module 
import vlc

# creating vlc media player object 
media_player = vlc.MediaPlayer() 

# media object 
media = vlc.Media("vivaldi.mp3") 

# setting media to the media player 
media_player.set_media(media)

# setting volume 
media_player.audio_set_volume(50) 

# start playing mp3 
media_player.play() 

# wait so the video can be played for 5 seconds 
# irrespective for length of video 
time.sleep(1) 

# getting volume 
volume = media_player.audio_get_volume() 

# printing value 
print("Audio Volume : ") 
print(volume) 


for i in range(100):
    microbit.display.show(i)
    time.sleep(0.1)

time.sleep(4) # note, display auto clears on exit

media_player.pause()
#END