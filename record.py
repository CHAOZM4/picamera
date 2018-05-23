#Import Start

from picamera import picamera
from time import sleep
from picamera import PiCamera, Color

#Import End

#Variable Start

camera = PiCamera()

#Variable End

#Effects Start
#Uncomment to use effect

#camera.resolution = (1366, 768) #Changes Resolution
#camera.framerate = 30 #Changes framerate
#camera.annotate_text = "Put Text Here" #Adds Text To Video
#camera.annotate_text_size = 32 #Changes Text Size
#camera.annotate_background = Color('color') #Changes annotate background color
#camera.annotate_foreground = Color('color') #Changes annotate foreground color
#camera.brightness = 100 #Changes Camera Brightness
#camera.image_effect = 'insert_effect' #Insert Effect From List Below

#Effect List Command Start

#none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout,
#posterise, colorpoint, colorpoint, colorbalance, cartoon, deinterlacel, deinterlace2

#Effect List Command End

#camera.awb_mode = "auto" #white balance mode

#White Balance Mode Start

#off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incadescent, flash, horizon 

#White Balance Mode Stop

#Effects End


#Commands Start

camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10) # Change number to make video longer time is in seconds
camera.stop_recording()
camera.stop_preview()

#Commands End

#To play video type "omxplayer video_name" in the terminal