#!/usr/bin/env python3.4

from sys import stdout
from time import sleep

# Count from 1 to 10 with a sleep
for count in range(0, 10):
    print(count + 1)
    # This is the solution!
    stdout.flush()
    sleep(3)
