#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Replace String
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 📝
# @raycast.argument1 { "type": "text", "placeholder": "String" }
# @raycast.argument2 { "type": "text", "placeholder": "e.g. _", "optional": true }


import sys

if sys.argv[2] != "":
    replacement = sys.argv[2]
else:
    replacement = "_"

print(sys.argv[1].replace(replacement, ""))
