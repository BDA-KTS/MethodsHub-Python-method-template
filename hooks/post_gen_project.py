import subprocess
import sys

env_manager = "{{ cookiecutter.env_manager }}"
project_name = "{{ cookiecutter.project_name }}"

# ----------------------
# PIP install from requirements.txt
# ----------------------
if env_manager == "pip":

    print("Installing dependencies from requirements.txt...")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "env/requirements.txt"
        ],
        check=True
    )

    print("Pip dependencies installed.")

# ----------------------
# CONDA install from environment.yml
# ----------------------
elif env_manager == "conda":

    print("Installing dependencies from environment.yml...")

    subprocess.run(
        [
            "conda",
            "env",
            "update",
            "-n",
            project_name,
            "-f",
            "env/environment.yml",
            "--prune"
        ],
        check=True
    )

    print("Conda environment updated.")
