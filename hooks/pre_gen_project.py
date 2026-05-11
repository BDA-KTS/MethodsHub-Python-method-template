import sys
import subprocess

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
    # Activate environment in a new shell
    if os.name == "nt":  # Windows
        subprocess.run(
            r".venv\Scripts\activate.bat",
            shell=True
        )
    else:  # Linux/macOS
        subprocess.run(
            "source .venv/bin/activate",
            shell=True,
            executable="/bin/bash"
        )
        print("Virtual environment created (.venv) created for {{ cookiecutter.method_title }}")

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
