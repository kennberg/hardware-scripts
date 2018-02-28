# Created by Alex Kennberg (https://github.com/kennberg/hardware-scripts)

import sys
import tty
import termios

# There are a number of pca9685 libs. This example uses:
# https://github.com/sunfounder/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/blob/master/server/PCA9685.py
from pca9685lib import PWM

# Connect pca9685 to Raspberry Pi PINs 2, 3, GND for i2c comm.
# Connect ESC to PIN 0 on pca9685

PIN_ESC = 0

# PWM settings that mirror throttler: reverse, stop, forward.
MIN_POS = 200
MID_POS = 400
MAX_POS = 600

def get_key():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(fd)
    key = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return key

if __name__ == '__main__':
  # pca9685 defaults to address 0x40 in i2c. If you changed jumpers, pass it here.
	pca9685_pwm = PWM()

  # I found that frequency has to be 70 for this ESC.
	pca9685_pwm.frequency = 70

	print 'Listening to input.'
	print 'Use 1 to prepare the ESC (aka arm it).'
	print 'Use 2 to go forward.'
	print 'Use 3 to go backward.'
	print 'Use 4 to stop.'
	print 'Use 0 to quit.'

	while True:
		key = get_key()
		if key == '1':  # Prepare
			pca9685_pwm.write(PIN_ESC, 0, MAX_POS)
			time.sleep(0.2)
			pca9685_pwm.write(PIN_ESC, 0, MIN_POS)
			time.sleep(0.2)
			pca9685_pwm.write(PIN_ESC, 0, MID_POS)
		elif key == '2':  # Forward
			pca9685_pwm.write(PIN_ESC, 0, MAX_POS)
		elif key == '3':  # Reverse
			pca9685_pwm.write(PIN_ESC, 0, MIN_POS)
		elif key == '4':  # Stop
			pca9685_pwm.write(PIN_ESC, 0, MID_POS)
		elif key == '0':  # Quit
			break
