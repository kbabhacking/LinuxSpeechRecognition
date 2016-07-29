from os import path
import speech_recognition as sr
import yaml
import urllib
import os
import re
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
cmd = ""
answer = ""
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_wit(audio, key="KRBQCEKL3AJQBAKO6ZXIROQ7X4EAJ76L").lower()
print bcolors.OKBLUE + bcolors.BOLD + "tu as dit: " + text
with open("config.yml", 'r') as recup:
    config1 = yaml.load(recup)
for config2 in config1["configuration"]:
    answer = config2["answer"]
    cmd = config2["cmd"]
    phrase = config2["phrase"]
    if re.match(phrase , text):
        os.system("espeak -v french -s 150 -p 40 '" + answer + "'")

