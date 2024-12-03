#!/usr/bin/env python3
import os
import logging
import threading
import random
import argparse
import socket
import sys
import time
import fade
import requests
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse

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

             
