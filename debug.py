# -*- coding: utf-8 -*-

import serial
import time
import sys
import os
import pygame

local='/dev/ttyS0'

ser = serial.Serial(
       port=local,
       baudrate = 9600,
       parity=serial.PARITY_NONE,
       stopbits=serial.STOPBITS_ONE,
       bytesize=serial.EIGHTBITS,
       write_timeout=0.02
      )

current_milli_time = lambda: int(round(time.time() * 1000))

def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min )


def attendre(t):
    temps=time.time()
    temps=temps+t
    while time.time()<=temps:
        pygame.event.pump()

def attendre_milli(t):
    temps=current_milli_time()
    temps=temps+t
    while current_milli_time()<=temps:
        pygame.event.pump()

def manette():
    pygame.init() #find the joysticks
    global joy
    joy = pygame.joystick.Joystick(0)
    joy.init()

os.system('clear')

try :
    manette()
except:
    print("Manette non-connecté")
    sys.exit(0)

print("Joystick OK")
print("Appui sur Δ pour continuer ...")
while joy.get_button(2)==0 :
    pygame.event.pump()

print("Let's started !")

while True :
    pygame.event.pump()
    g1 = joy.get_axis(1) # gauche haut/bas
    g2 = joy.get_axis(0) # gauche droite/gauche
    d1 = joy.get_axis(4) # droit haut/bas
    d2 = joy.get_axis(3) # droit droite/gauche
    x=joy.get_button(0) # bouton X
    o=joy.get_button(1) # bouton O
    T=joy.get_button(2) # bouton Triangle
    C=joy.get_button(3) # bouton Carrer
    i=map(g1,1,-1,1000,2000)
    s=map(d2,-1,1,0,180)
    print(i)
    print(s)
    i=str(i)+'A'
    s=str(s)+'B'
    try :
        ser.write(i+s)
    except:
        os.system('echo Probleme au niveau du port Serial >> /home/pi/Desktop/error.log')
        ser = serial.Serial(
               port=local,
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               write_timeout=0.1
              )


    if os.path.exists('/dev/input/js0')==0:
        print("Manette HS")
        ser.write('1500A')
        ser.write('0B')
        sys.exit(0)

    attendre_milli(100)
