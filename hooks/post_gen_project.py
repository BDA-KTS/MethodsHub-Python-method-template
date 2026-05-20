import subprocess
import sys
import os
import shutil
from pathlib import Path
import platform
import venv

env_manager = "{{ cookiecutter.env_manager }}"
method_slug = "{{ cookiecutter.method_slug }}"

# ----------------------
# Add an open license
# ----------------------
license_name = "{{ cookiecutter.license }}"
license_message = ""
if license_name != "No License":
    src = Path.cwd() / "licenses" / "{{ cookiecutter.license }}"
    dst = Path.cwd() / "LICENSE"
    shutil.copy(src, dst)
    shutil.rmtree(Path.cwd() / "licenses")
    license_message = "{{cookiecutter.license}} is added as {{ cookiecutter.method_slug }}/LICENSE" 
else:
    license_message = 'You have selected the {{ cookiecutter.license }} option. Please add an open license to your method when ready.'

# ----------------------
# PIP install from requirements.txt
# ----------------------
if env_manager == "pip":
    venv_path = Path(".venv").resolve()

    print("Opening new terminal...")
    if os.name == "nt":
        activate = venv_path / "Scripts" / "activate.bat"
        #subprocess.Popen(f'start cmd.exe /k "{activate}"', shell=True)
        cmd = (
            f'call "{activate}" &&'
            f'pip install -r binder/requirements.txt &&' 
            f'echo -------------------------------------------------------------- &&'
            f'echo -                        Process Update                        &&'
            f'echo - {{ cookiecutter.method_slug }}/.venv created and activated &&'
            f'echo - dependencies from {{ cookiecutter.method_slug }}/binder/requirements.txt are installed &&'
            f'echo - {{ cookiecutter.method_title }}, {{ cookiecutter.authors_info }}, and {{ cookiecutter.release_date }} are updated in {{ cookiecutter.method_slug }}/CITATION.CFF file &&'
            f'echo - {{ cookiecutter.method_title }} and Contact details section (with {{ cookiecutter.authors_info }}, {{ cookiecutter.contact_email }}, and {{ cookiecutter.github_repository_owner }}) are updated in {{ cookiecutter.method_slug }}/README.md &&'
            f'echo - "{license_message}" &&'
            f'echo - Setup is done, Yay 🎉 now grab a coffee ☕, and develop your method. Good Luck &&'
            f'echo --------------------------------------------------------------- &&'
            f'cmd /k'
        )
        subprocess.Popen(f'start cmd.exe /k "{cmd}"', shell=True)
    else:
        venv_python = venv_path / "bin" / "python"
        if not venv_python.exists():
            venv.EnvBuilder(with_pip=True).create(venv_path)
        subprocess.run([str(venv_python), "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([str(venv_python), "-m", "pip", "install", "-r", "binder/requirements.txt"], check=True)

        activate = venv_path / "bin" / "activate"
        print('--------------------------------------------------------------')
        print('                              Process Update                  ')
        print(' - {{ cookiecutter.method_slug }}/.venv created and activated')
        print(' - dependencies from {{ cookiecutter.method_slug }}/binder/requirements.txt are installed')
        print(' - {{ cookiecutter.method_title }}, {{ cookiecutter.authors_info }}, and {{ cookiecutter.release_date }} are updated in {{ cookiecutter.method_slug }}/CITATION.CFF file')
        print(' - {{ cookiecutter.method_title }} and Contact details section (with {{ cookiecutter.authors_info }}, {{ cookiecutter.contact_email }}, and {{ cookiecutter.github_repository_owner }}) are updated in {{ cookiecutter.method_slug }}/README.md')
        print(' - "{license_message}"')
        print(' - Setup is done, Yay 🎉 now grab a coffee ☕, and develop your method. Good Luck')
        print('-----------------------------------------------------------------')
        print('Oh 1 more step! Execute the following command to activate {{cookiecutter.method_slug}}/.venv environment')
        print('source ' + str(activate) + '"')

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
