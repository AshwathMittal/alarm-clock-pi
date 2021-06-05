#!/usr/bin/python3
from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button
from time import sleep
from datetime import datetime


button = Button(3)


GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

servo1.start(0)

def job(a):
    while a==0:
        song = AudioSegment.from_wav("TF001.WAV")
        print('playing sound using pydub')
        play(song)

        if button.is_pressed:
            a = 1;

alrm = input("alrm time in 24 hrs format(%H:%M:%S):)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time==alrm: #alarm time
        job(0)

