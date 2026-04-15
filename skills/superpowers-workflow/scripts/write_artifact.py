import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--path", required=True)
args = parser.parse_args()

os.makedirs(os.path.dirname(args.path), exist_ok=True)

with open(args.path, "w") as f:
    f.write("")

print(f"✅ Created: {args.path}")