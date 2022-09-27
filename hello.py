#!/usr/bin/env python3

import os
import json

# print("Content-Type: text/plain")
# print()
# print(os.environ)

# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

print("Content-Type: application/json")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
print(f"<p>BROWSER={os.environ['BROWSER']}</p>")
