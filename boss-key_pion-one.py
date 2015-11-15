import os
from websocket import create_connection
ws = create_connection("wss://cn.iot.seeed.cc/v1/node/event")
ws.send("5e91e4a43b451c5af5efee3e13599cf5")
print "link to pion one sensor."

while True:
    print "Receiving..."
    result = ws.recv()
    print "Received '%s'" % result
    print "Get someguys is comeing..."
    os.system("open /Applications/Mail.app")
ws.close()
