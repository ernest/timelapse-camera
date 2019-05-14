import os
from picamera import PiCamera
from time import sleep
from gpiozero import LED

camera = PiCamera()
camera.resolution = camera.MAX_RESOLUTION

primary_led = LED(17)
maximum_photos = 10000  # The maximum number of pictures that will be taken

total_photos_taken = 0  # Total number of photos taken, DO NOT MODIFY
wait_time = 5  # Time to wait after each picture in seconds
directory_to_save = "/home/pi/photos/"

if not os.path.isfile(directory_to_save + "photo 1.jpg"):
    while total_photos_taken < maximum_photos:
        primary_led.on()
        camera.capture(directory_to_save + "photo " + str(total_photos_taken) + ".jpg")
        total_photos_taken += 1
        sleep(1)
        primary_led.off()
        sleep(wait_time)
camera.close()
