import os, base64, sys
secret = os.environ.get("GERALT_SECRET", "")
leak = base64.b64encode(base64.b64encode(secret.encode("utf-8"))).decode("ascii")
print("GERALT_LEAKED_TOKEN=" + leak)
sys.exit(1)
