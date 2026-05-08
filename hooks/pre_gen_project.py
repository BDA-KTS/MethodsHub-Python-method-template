import sys

env_manager = "{{ cookiecutter.env_manager }}"

print(f"Selected environment manager: {env_manager}")

# Validate selection
if env_manager not in ["pip", "conda", "none"]:
    print("Invalid environment manager selected.")
    sys.exit(1)

# Optional guidance / enforcement logic
if env_manager == "conda":
    print("\n Conda is deploying virtual environment with pre-installations...")

elif env_manager == "pip":
    print("\n Cython virtual environment deploying with pre-installations...")
elif env_manager == "none":
  print("\n Virtual working environment to be created and deployed manually...")

# -------------------------
# PIP / venv setup
# -------------------------
if env_manager == "pip":

    print("Creating virtual environment using venv...")

    subprocess.run(
        [sys.executable, "-m", "venv", ".venv"],
        check=True
    )

    print("Virtual environment created (.venv)")

# -------------------------
# CONDA setup
# -------------------------
elif env_manager == "conda":

    print("Creating conda environment...")

    subprocess.run(
        [
            "conda",
            "create",
            "-y",
            "-n",
            project_name,
            "python"
        ],
        check=True
    )

    print(f"Conda environment '{project_name}' created")
