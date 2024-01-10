import argparse
import os
import csv
import socket
import requests,mmh3,codecs
from sys import exit,stdout
from termcolor import colored
from hashlib import md5
from time import perf_counter as timer,sleep
from datetime import timedelta
from termcolor import colored
from bs4 import BeautifulSoup
