import subprocess
import sys

env_manager = "{{ cookiecutter.env_manager }}"
method_slug = "{{ cookiecutter.method_slug }}"

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
            "binder/requirements.txt"
        ],
        check=True
    )

    print("Pip dependencies are installed in {{cookiecutter.method_title}}.venv environment.")
    print("Finally, execute the following command to open the virtual environment in the current shell window.\nFor Windows: {{cookiecutter.method_slug}}\\.venv\Scripts\activate.bat\nForLinux or MacOS: source {{ cookiecutter.method_slug }}/.venv/bin/activate")

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
            "binder/environment.yml",
            "--prune"
        ],
        check=True
    )

    print("Conda environment updated.")
