#!/usr/bin/python

import paho.mqtt.client as mqtt
import sys, getopt

def main(argv):
  output=''
  try:
    opts, args = getopt.getopt(argv,"hs:",["state="])
  except:
    print 'livingRoomPub.py -s <state: 1=on, 0=off>'
    sys.exit(2)
  for opt, arg in opts:
    if opt=='-h':
      print 'livingRoomPub.py -s <state: on=1, off=0'
      sys.exit()
    elif opt in ("-s", "--state"):
     output= arg

  print "output is: ",output
  mqttc = mqtt.Client("livingRoomCamera_Pub")
  mqttc.connect("192.168.0.78",1883)
  mqttc.publish("myhome/security/motion/livingroom",output)
  mqttc.loop(2)
  sys.exit(0)

if __name__ == "__main__":
  main(sys.argv[1:])
