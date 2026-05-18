import subprocess
import sys
import os
from pathlib import Path

env_manager = "{{ cookiecutter.env_manager }}"
method_slug = "{{ cookiecutter.method_slug }}"

# ----------------------
# PIP install from requirements.txt
# ----------------------
if env_manager == "pip":
    venv_path = Path(".venv").resolve()

    if os.name == "nt":
        activate = venv_path / "Scripts" / "activate.bat"
        #subprocess.Popen(f'start cmd.exe /k "{activate}"', shell=True)

        cmd = f'call "{activate}" && pip install -r binder/requirements.txt && cmd /k'
        subprocess.Popen(f'start cmd.exe /k "{cmd}"', shell=True)
        print("dependencies installed in the .venv environment.")
    else:
        activate = venv_path / "bin" / "activate"
        subprocess.Popen(["gnome-terminal","--","bash","-ic",f"source '{activate}' && exec bash"])

    print("Opened new terminal with activated virtual environment.")

    print("Installing dependencies for {{ cookiecutter.method_title }} from requirements.txt...")
    subprocess.run([sys.executable,"-m","pip","install","-r","binder/requirements.txt"],check=True)

    print("Pip dependencies are installed in {{cookiecutter.method_title}}.venv environment.")
    print("Finally, execute the following command to open the virtual environment in the current shell window.\nFor Windows: {{cookiecutter.method_slug}}\\.venv\\Scripts\\activate.bat\nFor Linux or MacOS: source {{ cookiecutter.method_slug }}/.venv/bin/activate")

# ----------------------
# CONDA install from environment.yml
# ----------------------
elif env_manager == "conda":

    print("Installing dependencies for {{ cookiecutter.method_title }} from environment.yml...")

    env_name = "{{ cookiecutter.method_slug }}"

    cmd = (
        f'conda env create -n {env_name} -f binder/environment.yml '
        f'&& conda activate {env_name} '
        f'&& cmd /k'
    )

    subprocess.Popen(
        f'start cmd.exe /k "{cmd}"',
        shell=True
    )

    print("Conda environment updated.")
