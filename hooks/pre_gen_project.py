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

# -------------------------
# PIP / venv setup
# -------------------------
if env_manager == "pip":

    subprocess.run(
        [sys.executable, "-m", "venv", ".venv"],
        check=True
    )
    print("Pip created {{ cookiecutter.method_slug }}/.venv virtual environment")

# -------------------------
# CONDA setup
# -------------------------
elif env_manager == "conda":

    subprocess.run(
        ["conda", "create", "-y", "-n", "{{ cookiecutter.method_slug }}", "python"],
        check=True
    )

    print(f"Conda environment named {{ cookiecutter.method_slug }} is created for the {{ cookiecutter.method_title }}")

# -------------------------
# None
# -------------------------
elif env_manager == "none":
    print("For the selected (none) option, create virtual environment and install dependencies manually for {{ cookiecutter.method_title }}.")
