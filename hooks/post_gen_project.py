import subprocess
import sys
import os
import shutil
from pathlib import Path
import platform

env_manager = "{{ cookiecutter.env_manager }}"
method_slug = "{{ cookiecutter.method_slug }}"

# ----------------------
# PIP install from requirements.txt
# ----------------------
if env_manager == "pip":
    venv_path = Path(".venv").resolve()

    print("Opening new terminal for new virtual environment.")
    if os.name == "nt":
        activate = venv_path / "Scripts" / "activate.bat"
        #subprocess.Popen(f'start cmd.exe /k "{activate}"', shell=True)

        cmd = f'call "{activate}" && pip install -r binder/requirements.txt && cmd /k'
        subprocess.Popen(f'start cmd.exe /k "{cmd}"', shell=True)
    else:
        venv_python = venv_path / "bin" / "python"
        subprocess.run([str(venv_python), "-m", "pip", "install", "-r", "binder/requirements.txt"], check=True)

        activate = venv_path / "bin" / "activate"
        cmd = (f"source '{activate}' && " f"exec bash")
        
        if platform.system() == "Linux":
            subprocess.Popen(["gnome-terminal", "--", "bash", "-ic", cmd])
        elif system == "Darwin":  # macOS
            subprocess.Popen(["osascript", "-e", f'tell application "Terminal" to do script "{cmd}"'])
        #activate = venv_path / "bin" / "activate"
        #subprocess.Popen(["gnome-terminal","--","bash","-ic",f"source '{activate}' && exec bash"])
    
    print("Virtual environment .venv created and existing dependencies from {{ cookiecutter.method_slug }}/binder/requirements.txt are installed.")
    
    print("Installing dependencies for {{ cookiecutter.method_title }} from requirements.txt...")
    subprocess.run([sys.executable,"-m","pip","install","-r","binder/requirements.txt"],check=True)

    print("Pip dependencies are installed in {{cookiecutter.method_title}}.venv environment.")
    print("Finally, execute the following command to open the virtual environment in the current shell window.\nFor Windows: {{cookiecutter.method_slug}}\\.venv\\Scripts\\activate.bat\nFor Linux or MacOS: source {{ cookiecutter.method_slug }}/.venv/bin/activate")

    print("You can start working on your method now. \nAfter completion, go back to the template README 'How To Use' section to complete the remaining steps for pushing the method to your GitHub account.")
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

# ----------------------
# Add an open license
# ----------------------
license_name = "{{ cookiecutter.license }}"
mapping = {
    "MIT License": "licenses/MIT.txt",
    "Apache-2.0 License": "licenses/Apache-2.0.txt",
    "GPL-3.0 License": "licenses/GPL-3.0.txt"
    "BSD-2-clause License"
    "No License"
}

if license_name != "No License":
    src = Path.cwd() / "licenses" / "{{ cookiecutter.license }}"
    dst = Path.cwd() / "LICENSE"
    shutil.copy(src, dst)
    shutil.rmtree(Path.cwd() / "licenses")
    print(f"Added {license_name} license.")
else:
    print("You have selected no license option. Please manually add an open license to your method")

print("Method folder created with the name {{ cookiecutter.method_slug }}, with directory structure and mandatory files.")

print("{{cookiecutter.method_title}} and contact details section are updated on README with the information provided.")

print("{{ cookiecutter.method_title }}, {{ cookiecutter.authors_info }}, and {{ cookiecutter.release_date }} are updated in CITATION.CFF file.")
