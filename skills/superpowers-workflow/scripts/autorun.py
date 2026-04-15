import os
import subprocess
import sys

STEPS = [
    "superpowers-brainstorm",
    "superpowers-plan",
    "superpowers-test-plan",
    "superpowers-write-tests",
    "superpowers-implement",
    "superpowers-review",
]

ARTIFACTS = {
    "superpowers-brainstorm": "artifacts/superpowers/brainstorm.md",
    "superpowers-plan": "artifacts/superpowers/plan.md",
    "superpowers-test-plan": "artifacts/superpowers/test-plan.md",
    "superpowers-write-tests": "artifacts/superpowers/tests.md",
    "superpowers-implement": "artifacts/superpowers/implementation.md",
    "superpowers-review": "artifacts/superpowers/review.md",
}


def run_skill(skill_name):
    print(f"\n🚀 Running: {skill_name}")

    try:
        # Her antager vi at du trigger via CLI / slash command wrapper
        subprocess.run(
            ["echo", f"/{skill_name}"],
            check=True
        )
    except subprocess.CalledProcessError:
        print(f"❌ Failed to run {skill_name}")
        sys.exit(1)


def validate_artifact(skill_name):
    path = ARTIFACTS.get(skill_name)

    if not path:
        return True

    if not os.path.exists(path):
        print(f"❌ Missing artifact after {skill_name}: {path}")
        return False

    print(f"✅ Artifact exists: {path}")
    return True


def validate_red_phase():
    print("\n🔍 Validating RED phase...")

    tests_file = "artifacts/superpowers/tests.md"

    if not os.path.exists(tests_file):
        print("❌ Tests not found")
        return False

    # simpel heuristic (kan forbedres)
    with open(tests_file, "r") as f:
        content = f.read().lower()

    if "fail" not in content and "error" not in content:
        print("⚠️ No indication of failing tests found")
        print("👉 Ensure RED phase is real")
    else:
        print("✅ RED phase indication found")

    return True


def main():
    print("⚡ Superpowers Auto Runner Started\n")

    for step in STEPS:
        run_skill(step)

        if not validate_artifact(step):
            print(f"🚫 Stopping due to missing artifact in {step}")
            sys.exit(1)

        if step == "superpowers-write-tests":
            if not validate_red_phase():
                print("🚫 RED phase validation failed")
                sys.exit(1)

    print("\n🎉 Workflow completed successfully!")


if __name__ == "__main__":
    main()