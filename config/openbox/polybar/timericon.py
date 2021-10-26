#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import json
import time
import datetime
import os
import sys

os.chdir(sys.path[0])

def icon():
    with open("timer.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        if data["is_work_time"]:
            myicon = "" # Compiuter
        else:
            myicon = "" # Controle de joguinho
        
        return("%{F#DB86BA}" + myicon + "%{F-}")
def main():
    print(icon())

#if __name__ == "__main__":
main()
