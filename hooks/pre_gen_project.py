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
