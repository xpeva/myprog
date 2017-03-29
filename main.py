#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, sys

def removeCRLF(msg):
    return ''.join(msg.splitlines())

def Main(configfilename):
    sys.exit(0)

if __name__ == "__main__":
    Main("/etc/projet1.conf")

