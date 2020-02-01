import os
from picamera import PiCamera
from time import sleep
from gpiozero import LED

# The directory where the photos taken will be stored. The photos folder of the pi user is the default.
directory_to_save = "/home/pi/photos/"

MAXIMUM_PHOTOS = 10000  # The maximum number of pictures that will be taken
total_photos_taken = 0  # Total number of photos taken
wait_time = 5  # Time to wait after each picture in seconds

camera = PiCamera()
camera.resolution = camera.MAX_RESOLUTION

primary_led = LED(17)
primary_led.off()

if not os.path.isfile(directory_to_save + "IMG_0.jpg"):
    while total_photos_taken < MAXIMUM_PHOTOS:
        primary_led.on()
        camera.capture(directory_to_save + "IMG_" + str(total_photos_taken) + ".jpg")
        total_photos_taken += 1
        sleep(1)
        primary_led.off()
        sleep(wait_time)
camera.close()
