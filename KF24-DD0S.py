import os
import socket
import string
import random
import threading
from colorama import Fore, Back, Style

class SockFlood:
	def __init__(self):
		os.system("cls")
		os.system("title PsyFlood - An Advance DDOS Tool ")
		self.host=None
		self.portnum=None
		self.threads=None

	def graphics(self):
		banner="""
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
		
