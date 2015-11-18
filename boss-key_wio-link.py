import os
from websocket import create_connection
import requests
import time

wio_link_server = "wss://cn.iot.seeed.cc/v1/node/event"
wio_link_key = "efe19ae9752add26d614d87cacd97f45"

ws = create_connection(wio_link_server)
ws.send(wio_link_key)
print "link to pion one sensor."

while True:
    print "Receiving..."
    result = ws.recv()
    print "Received '%s'" % result
    print "Some guys is coming..."
    os.system("open /Applications/Mail.app")

    requests.post("https://cn.iot.seeed.cc/v1/node/GroveServo/angle/180?access_token=efe19ae9752add26d614d87cacd97f45")
    requests.post("https://cn.iot.seeed.cc/v1/node/GroveLedWs2812/clear/40/800000?access_token=efe19ae9752add26d614d87cacd97f45")

    time.sleep(1)
    requests.post("https://cn.iot.seeed.cc/v1/node/GroveServo/angle/90?access_token=efe19ae9752add26d614d87cacd97f45")
    requests.post("https://cn.iot.seeed.cc/v1/node/GroveLedWs2812/clear/40/008000?access_token=efe19ae9752add26d614d87cacd97f45")
ws.close()
