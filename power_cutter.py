#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import RPi.GPIO as GPIO
import time

def main():
	# GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)

	GPIO.output(18, GPIO.HIGH)
	time.sleep(5);
	GPIO.output(18, GPIO.LOW)

	GPIO.cleanup()

if __name__ == "__main__":
	main()

