#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import base64
import hashlib
import hmac
import discord_tools
from datetime import datetime

DISCORD_TOKEN = "NzY4MjM0NTY3ODkwMTIzNDU2.XYZABC.abcdefghijklmnopqrstuvwxyz"

def discord_banhammer():
    token = DISCORD_TOKEN
    keyword = rules.txt
    discord_tools.ban_users_by_rules(token, keyword)

def main():

    discord_banhammer)
    print("Done.")

if __name__ == "__main__":
    main()
