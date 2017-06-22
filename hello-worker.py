#!/usr/bin/env python3
from waggle import beehive

config = beehive.ClientConfig(
    host='10.10.10.5',
    port=23181,
    vhost='testing',
    username='hello-worker',
    password='waggle',
    cacert='/Users/Sean/github/hello-publisher/cacert.pem',
    cert='/Users/Sean/github/hello-publisher/cert.pem',
    key='/Users/Sean/github/hello-publisher/key.pem')


def callback(data):
    print(data)

    # ...transform data...

    return result


client = beehive.WorkerClient(
    name='hello:1',
    config=config,
    callback=callback)

client.start_working()
