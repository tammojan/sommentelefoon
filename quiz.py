#!/usr/bin/env python
from __future__ import print_function

import RPi.GPIO as GPIO
import time
import sys
import os
from threading import Timer

import random

import MySQLdb
import pygame
os.chdir("/home/pi/telefoonquiz")

os.system("amixer cset numid=3 1") # Select jack audio output

VOLUME = 1.0

pygame.mixer.init()
#pygame.mixer.music.set_volume(VOLUME)

PULSEINTERVAL = 0.18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

goedmp3=["mp3/goed"+str(i)+".mp3" for i in range(1,9)]
foutmp3=["mp3/fout"+str(i)+".mp3" for i in range(1,6)]

sommen = set()
for total in range(1, 10):
  for arg1 in range(0, total):
    sommen.add((str(total-arg1)+'+'+str(arg1),total))
    sommen.add((str(total)+'-'+str(arg1),total-arg1))

#for i in [a[0] for a in sorted(sommen)]:
#  print(i)
#print("Length: ", len(sommen))
#sys.exit(0)

state = 'IDLE'
pulses = 0
antwoord = 0

def check(answer):
    global antwoord, goedmp3, foutmp3, som
    if antwoord==answer:
      print('Goed zo!')
      goed=random.choice(goedmp3)
      pygame.mixer.music.load(goed)
      #pygame.mixer.music.set_volume(VOLUME)
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy() == True:
        continue
      (som,antwoord) = random.choice(list(sommen))
      print(som)
      pygame.mixer.music.load("mp3/"+som+".mp3")
      #pygame.mixer.music.set_volume(VOLUME)
      pygame.mixer.music.play()
    else:
      print('Nee, niet '+str(answer)+'. Probeer het nog eens')
      fout=random.choice(foutmp3)
      pygame.mixer.music.load(fout)
      #pygame.mixer.music.set_volume(VOLUME)
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy() == True:
        continue
      #pygame.mixer.music.set_volume(VOLUME)
      pygame.mixer.music.load("mp3/"+som+".mp3")
      pygame.mixer.music.play()

def settozero():
    global pulses
    global state

    state = 'IDLE'
    check(pulses)
    pulses = 0

def my_callback(channel):
    global state
    global pulses
    global timer

    if state == 'IDLE':
      state = 'COUNTING'
      timer = Timer(PULSEINTERVAL, settozero)
      timer.start()
    else:
      timer.cancel()
      timer = Timer(PULSEINTERVAL, settozero)
      timer.start()
      
    pulses+=1
    sys.stdout.flush()

GPIO.add_event_detect(5, GPIO.FALLING, callback=my_callback, bouncetime=80)

try:
  (som,antwoord) = random.choice(list(sommen))
  print(som)
  pygame.mixer.music.load("mp3/"+som+".mp3")
  #pygame.mixer.music.set_volume(VOLUME)
  pygame.mixer.music.play()
  while True:
    time.sleep(2)
except KeyboardInterrupt:
  GPIO.cleanup()
  raise

GPIO.cleanup()

