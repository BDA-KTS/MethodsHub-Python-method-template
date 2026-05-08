import subprocess
import sys

env_manager = "{{ cookiecutter.env_manager }}"

if env_manager == "conda":
    print("Skipping pip install (conda environment expected).")

elif env_manager == "pip":
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        check=True
    )
