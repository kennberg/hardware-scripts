hardware-scripts
======================
Hardware scripts for Raspberry Pi and Arduino.

HobbyKing X-Car 45A Brushed Car ESC
======================
There is not a good source of truth for this ESC on how to prepare and use it. Each ESC has its own boot sequence.
Typically you have a remote control connected and have to move the throttle to max, min, and middle position.
I simulate this in Python using PCA9685 16 channel PWM chip, but you can also do it directly through GPIO PWM PIN.
