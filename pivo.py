#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import base64
import hashlib
import hmac
from datetime import datetime

AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_to_aws():
    secret_key = AWS_SECRET_KEY
    print(f"Connecting to AWS with {access_key}")

def main():

    connect_to_aws()

if __name__ == "__main__":
    main()
