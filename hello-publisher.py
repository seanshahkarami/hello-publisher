#!/usr/bin/env python3
from waggle import beehive
import time

config = beehive.ClientConfig(
    host='10.10.10.5',
    port=23181,
    node='0000020000000001',
    cacert='/path/to/cacert.pem',
    cert='/path/to/cert.pem',
    key='/path/to/key.pem')

client = beehive.MessageClient(
    name='hello:1.0',
    config=config)

client.connect()

while True:
    client.publish('greeting', 'hello world')
    time.sleep(1)
