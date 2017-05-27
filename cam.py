import os
from picamera import PiCamera
from time import sleep
from gpiozero import LED
camera = PiCamera()
camera.resolution = camera.MAX_RESOLUTION
primaryLed = LED(17)
maximumPhotos = 10000 # The maximum number of pictures that will be taken
totalPhotosTaken = 0 # Total number of photos taken, DO NOT MODIFY
waitTime = 5 # Time to wait after each picture in seconds
directoryToSave = "/home/pi/ketchup/"
fileFormat = ".jpg"
if not os.path.isfile(str(directoryToSave) + "photo 1" + str(fileFormat)):
    while totalPhotosTaken < maximumPhotos:
        primaryLed.on()
        totalPhotosTaken += 1
        camera.capture(str(directoryToSave) + "photo " + str(totalPhotosTaken) + str(fileFormat))
        sleep(1)
        primaryLed.off()
        sleep(waitTime)
camera.close()
