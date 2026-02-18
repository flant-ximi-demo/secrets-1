#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import base64
import hashlib
import hmac
from datetime import datetime

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_to_aws():
    access_key = "AKIAFAKEACCESSKEY" 
    secret_key = "FAKESECRETKEY1234567890abcdefghijklmnop"
    print(f"Connecting to AWS with {access_key}")

def main():

    connect_to_aws()
    print(f"AWS Access Key: {AWS_ACCESS_KEY[:5]}... (скрыто)")

if __name__ == "__main__":
    main()
