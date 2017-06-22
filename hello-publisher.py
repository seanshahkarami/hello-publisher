#!/usr/bin/env python3
from waggle import beehive
import time

config = beehive.ClientConfig(
    host='10.10.10.5',
    port=23181,
    vhost='testing',
    node='0000020000000000',
    username='testnode0',
    password='waggle',
    cacert='/Users/Sean/github/hello-publisher/cacert.pem',
    cert='/Users/Sean/github/hello-publisher/cert.pem',
    key='/Users/Sean/github/hello-publisher/key.pem')

client = beehive.PluginClient(
    name='hello:1',
    config=config)

while True:
    client.publish('greeting', 'hello world', exchange='plugins-in')
    time.sleep(1)
