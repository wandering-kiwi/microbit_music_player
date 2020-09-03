#this has a:play, b:pause, left_tilt:volume_down, right_tilt:volume_up
# diagram at https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fexcalidraw.com%2F%23json%3D5217542889013248%2CIGDMblCSp5C0rZXMZ7r0_Q 
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
print("micro:bit connected - press button A to play and button B to pause")
# start playing mp3
while True:
    a_pressed = microbit.button_a.was_pressed()
    b_pressed = microbit.button_b.was_pressed()
    x = microbit.accelerometer.get_x()
    print(x)    
    if a_pressed and b_pressed :
        print("stopping")
        media_player.stop()
        break
    if a_pressed:
        media_player.play()
        print('Play')
    if b_pressed:
        media_player.pause()
        print('Pause')
    time.sleep(0.2)

#END