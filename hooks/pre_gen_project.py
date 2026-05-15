import sys
import os
import subprocess
from pathlib import Path

env_manager = "{{ cookiecutter.env_manager }}"

print(f"Selected environment manager: {env_manager}")

# Validate selection
if env_manager not in ["pip", "conda", "none"]:
    print("Invalid environment manager selected.")
    sys.exit(1)

# Optional guidance / enforcement logic
if env_manager == "conda":
    print("\n Conda is deploying virtual environment for {{ cookiecutter.method_title }}with pre-installations...")

elif env_manager == "pip":
    print("\n Python virtual environment deploying for {{ cookiecutter.method_title }}with pre-installations...")

elif env_manager == "none":
  print("\n Virtual working environment to be created and deployed for {{ cookiecutter.method_title }} manually...")

# -------------------------
# PIP / venv setup
# -------------------------
if env_manager == "pip":

    subprocess.run(
        [sys.executable, "-m", "venv", ".venv"],
        check=True
    )
    print("Virtual environment created (.venv) created for {{ cookiecutter.method_title }}")

    if os.name == "nt":
        venv_python = Path(".venv/Scripts/python.exe")
    else:
        venv_python = Path(".venv/bin/python")
    print('Virual environment activated.')
    subprocess.run(
        [str(venv_python), "-m", "pip", "install", "-r", "binder/requirements.txt"],
        check=True
    )

# -------------------------
# CONDA setup
# -------------------------
elif env_manager == "conda":

    subprocess.run(
        [
            "conda",
            "create",
            "-y",
            "-n",
            {{ cookiecutter.method_slug }},
            "python"
        ],
        check=True
    )

    print(f"Conda environment named {{ cookiecutter.method_slug }} is created for the {{ cookiecutter.method_title }}")

# -------------------------
# None
# -------------------------
elif env_manager == "none":
    print("For the selected (none) option, create virtual environment and install dependencies manually for {{ cookiecutter.method_title }}.")
