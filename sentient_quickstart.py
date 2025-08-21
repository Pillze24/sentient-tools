# sentient_quickstart.py
# Sentient Builder: Environment Check & Starter Folder
# Author: Pillze 
import os, sys, platform, shutil, subprocess, textwrap

def has(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def line():
    print("-" * 60)

print("🚀 Sentient Quickstart — Environment Check")
line()
print(f"OS Detected: {platform.system()} {platform.release()}")
print(f"Python Version (running this): {sys.version.split()[0]}")
line()

# Check Git
git_ok = has("git")
print(f"Git installed: {'YES ✅' if git_ok else 'NO ❌'}")
if git_ok:
    try:
        subprocess.run(["git", "--version"], check=False)
    except Exception:
        pass
else:
    print(textwrap.dedent("""
    👉 Git helps you work with code projects.
       If you need it later:
       - Windows: install "Git for Windows" (search it)
       - Mac: install via Xcode Command Line Tools or Homebrew
    """).strip())

line()

# Create a starter folder with docs so newcomers have a base
starter = os.path.join(os.getcwd(), "sentient_starter")
os.makedirs(starter, exist_ok=True)

readme_path = os.path.join(starter, "README.md")
if not os.path.exists(readme_path):
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(
            "# Sentient Starter\n\n"
            "This folder is auto-generated to help new builders verify their environment\n"
            "and have a clean workspace to begin. Contributed by Pillze.\n\n"
            "## What next?\n"
            "- Ensure you have Python 3 installed\n"
            "- (Optional) Install Git to clone repos\n"
            "- Keep notes of any setup issues to improve onboarding docs\n"
        )
    print(f"📁 Created: {starter}")
    print(f"📝 Added: {readme_path}")
else:
    print("ℹ️ Starter folder already exists; not overwriting README.")

print("\n✅ Quickstart done. You’re ready to onboard more builders.")
