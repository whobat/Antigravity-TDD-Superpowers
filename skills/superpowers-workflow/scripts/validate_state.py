import os
import sys

REQUIRED_FILES = [
    "artifacts/superpowers/test-plan.md",
    "artifacts/superpowers/tests.md",
]

missing = [f for f in REQUIRED_FILES if not os.path.exists(f)]

if missing:
    print("❌ Missing required artifacts:")
    for m in missing:
        print(f" - {m}")
    sys.exit(1)

print("✅ State valid")