import subprocess
import sys

env_manager = "{{ cookiecutter.env_manager }}"
method_slug = "{{ cookiecutter.method_slug }}"
dir = '{{ "{{ cookiecutter.method_slug }}" }}'


# ----------------------
# PIP install from requirements.txt
# ----------------------
if env_manager == "pip":

    print("Installing dependencies for {{ cookiecutter.method_title }} from requirements.txt...")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "" + str(dir) + "/binder/requirements.txt"
        ],
        check=True
    )

    print("Pip dependencies installed.")

# ----------------------
# CONDA install from environment.yml
# ----------------------
elif env_manager == "conda":

    print("Installing dependencies for {{ cookiecutter.method_title }} from environment.yml...")

    subprocess.run(
        [
            "conda",
            "env",
            "update",
            "-n",
            project_slug,
            "-f",
            dir + "/binder/environment.yml",
            "--prune"
        ],
        check=True
    )

    print("Conda environment updated.")
