#!/usr/bin/env python3
from waggle import beehive
import time

config = beehive.ClientConfig(
    node='0000020000000001',
    cacert='/Users/Sean/waggle-sensor/beehive/ca.crt')

client = beehive.MessageClient(
    name='chemsense:1.0',
    config=config)

client.connect()

while True:
    client.publish('chemdata', {'co2': 1243.2, 'no2': 123.1})
    time.sleep(1)
