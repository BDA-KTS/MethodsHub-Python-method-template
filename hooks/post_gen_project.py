import subprocess
import sys
import os
import shutil
from pathlib import Path
import platform

env_manager = "{{ cookiecutter.env_manager }}"
method_slug = "{{ cookiecutter.method_slug }}"

# ----------------------
# Add an open license
# ----------------------
license_name = "{{ cookiecutter.license }}"
if license_name != "No License":
    src = Path.cwd() / "licenses" / "{{ cookiecutter.license }}"
    dst = Path.cwd() / "LICENSE"
    shutil.copy(src, dst)
    shutil.rmtree(Path.cwd() / "licenses")
else:
    print("You have selected no license option. Please manually add an open license to your method")

# ----------------------
# PIP install from requirements.txt
# ----------------------
if env_manager == "pip":
    venv_path = Path(".venv").resolve()

    print("Opening new terminal for new virtual environment.")
    if os.name == "nt":
        activate = venv_path / "Scripts" / "activate.bat"
        #subprocess.Popen(f'start cmd.exe /k "{activate}"', shell=True)

        cmd = (
            f'call "{activate}" && pip install -r binder/requirements.txt &&'
            f'echo {{ cookiecutter.method_slug }}/.venv environment created &&'
            f'echo dependencies from {{ cookiecutter.method_slug }}/binder/requirements.txt are installed &&'
            f'echo {{ cookiecutter.license }} added to the {{cookiecutter.method_slug}} directory &&'
            f'echo {{ cookiecutter.method_title }}, {{ cookiecutter.authors_info }}, and {{ cookiecutter.release_date }} are updated in {{ cookiecutter.method_slug }}/CITATION.CFF file &&'
            f'echo Method title as {{ cookiecutter.method_title }}, and Contact details section (with {{ cookiecutter.authors_info }}, {{ cookiecutter.contact_email }}, and {{ cookiecutter.github_repository_owner }}) are updated in {{ cookiecutter.method_slug }}/READ.md &&'
            f'{"echo {{ cookiecutter.license }} add as {{cookiecutter.method_slug}}/LICENSE " if str({{cookiecutter.license}}) != "No License" else "echo You have selected the 'No License' option. Please add an open license to {{cookiecutter.method_slug}}/ manually, when ready."}'
            f'Setup is done, Yay 🎉 \nnow grab a coffee and develop your method. \nGood Luck &&'
            'cmd /k')
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
    
    print("Virtual environment {{ cookiecutter.method_slug }}/.venv created.")
    
    print("Installing dependencies for {{ cookiecutter.method_title }} method from {{ cookiecutter.method_slug }}/binder/requirements.txt into {{ cookiecutter.method_slug }}/.venv")
    
    file_path = Path.cwd() / "binder" / "environment.yml"
    if file_path.exists():
        file_path.unlink()
    #subprocess.run([sys.executable,"-m","pip","install","-r","binder/requirements.txt"],check=True)

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
