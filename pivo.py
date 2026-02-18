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


GOOGLE_API_KEY = "AIzaSyD-8s9tQx1XyZz1234567890abcdefghij"

TWITTER_API_KEY = "1234567890-abcdefghijklmnopqrstuvwxyz"
TWITTER_API_SECRET = "4xYMmRq3tL9sW8zF7kV2bN1hG6jU5cP0eA3dQ8rX5yV2bN1hG6jU"

GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1234567890"

SLACK_BOT_TOKEN = "xoxb-123456789012-1234567890123-abcdefghijklmnopqrstuvwxyz"

DISCORD_TOKEN = "NzY4MjM0NTY3ODkwMTIzNDU2.XYZABC.abcdefghijklmnopqrstuvwxyz"

JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

DB_PASSWORD = "SuperSecretP@ssw0rd!"

MONGO_URI = "mongodb+srv://admin:password123@cluster0.mongodb.net/"
POSTGRES_URI = "postgresql://user:secretpassword@localhost:5432/mydb"
MYSQL_URI = "mysql://root:rootpassword@127.0.0.1:3306/mydb"
REDIS_URI = "redis://:password@localhost:6379/0"

def connect_to_aws():
    """Имитация подключения к AWS."""
    access_key = "AKIAFAKEACCESSKEY"  # ещё один ключ внутри функции
    secret_key = "FAKESECRETKEY1234567890abcdefghijklmnop"
    print(f"Connecting to AWS with {access_key}")
    # Реального подключения нет

def send_tweet(message):
    """Отправка твита (имитация)."""
    api_key = "FAKETWITTERAPIKEY"  # секрет в теле функции
    api_secret = "FAKETWITTERAPISECRET"
    print(f"Sending tweet: {message} using key {api_key}")

def decrypt_data(encrypted_data):
    """Расшифровка данных (учебная)."""
    key = "my_super_secret_encryption_key_12345"  # ещё один секрет
    # имитация расшифровки
    return base64.b64decode(encrypted_data).decode()

def lambda_handler(event, context):
    """Пример обработчика AWS Lambda."""
    db_password = "LambdaDBPassword!"
    api_token = "lambda_secret_token_67890"

CONFIG = {
    "environment": "production",
    "database": {
        "host": "db.example.com",
        "port": 5432,
        "username": "app_user",
        "password": "config_db_password_123"  # пароль внутри словаря
    },
    "apis": {
        "stripe": {
            "secret_key": "sk_live_4eC39HqLyjWDarjtT1zdp7dc",  # live ключ Stripe
            "publishable_key": "pk_live_4eC39HqLyjWDarjtT1zdp7dc"
        },
        "mailgun": {
            "api_key": "key-1234567890abcdefghijklmnopqrstuv"
        }
    },
    "auth": {
        "jwt_secret": "jwt_s3cr3t_k3y_12345"
    }
}

json_config = '{"aws_access_key_id": "AKIAFAKE123456", "aws_secret_access_key": "fakeSecretKey"}'


def main():
    print("DevOps Cloud Manager (учебный скрипт)")
    print("=" * 40)

    connect_to_aws()
    send_tweet("Hello, world!")
    print(f"AWS Access Key: {AWS_ACCESS_KEY[:5]}... (скрыто)")
    print(f"MongoDB URI: {MONGO_URI.split('@')[1]}")

    print(f"Stripe key: {CONFIG['apis']['stripe']['secret_key'][:8]}...")

    parts = JWT_TOKEN.split('.')
    if len(parts) == 3:
        payload = base64.b64decode(parts[1] + '==').decode()
        print(f"JWT payload: {payload[:50]}...")

    print(f"Connecting to PostgreSQL with {POSTGRES_URI}")
    print("Done.")

if __name__ == "__main__":
    main()
