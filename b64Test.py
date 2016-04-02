#!/usr/bin/env python3.4

import base64

a = b'{"state":11}'
b = base64.b64encode(a)
print(b)
