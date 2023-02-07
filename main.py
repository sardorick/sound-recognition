import requests
from api_02 import *
import sys

filename = sys.argv[1]
audio_url = upload(filename)
save_transcript(audio_url, filename)