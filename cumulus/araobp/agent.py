#!/usr/bin/env python

import paho.mqtt.client as client
from time import sleep
import yaml
import time

TOPIC = 'log'

test_msg = 'Hello World'

if __name__ == '__main__':
    f = open('/tmp/agent.yaml', 'r')
    conf = yaml.load(f)
    mqtt = conf['mqtt']
    client = client.Client()
    client.connect(host=mqtt['server'], port=mqtt['port'], keepalive=60)
    while True:
        client.publish(TOPIC, "{}:{}".format(test_msg, str(time.time())))
        sleep(8)
