#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, sys
import argparse,configparser

def removeCRLF(msg):
    return ''.join(msg.splitlines())

def Main(configfilename):
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="show version", action="store_true")
    parser.add_argument("--debug", help="Debug", action="store_true")
    args=parser.parse_args()

    config = configparser.ConfigParser()
    config.read(configfilename)
    try:
        # section DEFAULT
        num=config["GLOBAL"]["num"]
        whitelist=["GLOBAL"]["whitelist"]
        blacklist=["GLOBAL"]["blacklist"]
    except:
        print ("Unable to retrieve configuration data in {}:\n{}".format(configfilename, sys.exc_info()[0]))
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    Main("/etc/parefeu.conf")
    print("program finished successfully")


