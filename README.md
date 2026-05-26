# Methods Hub Method Template

The Methods Hub Method Template is built using [Cookiecutter](https://github.com/cookiecutter/cookiecutter). It helps to preload the project directory with the necessary files required for the Methods Hub i.e., 

- *postBuild* file to generate the method homepage and deploy the method in the interactive environment
- *README.md* with the desired subsections and their specifications
- Within project directory structure having
  - *data* for the input and output files
  - *binder* for the postBuild and environment preserving files
  - *.github* for the GitHub workflows
- *CITATION.CFF* file for attribution
- Environment preservation files (*environment.yml* and *requirements.txt*)
- GitHub workflow file *methodshub.yml* to review the method 

## How to Use

1. Install Cookiecutter
  - With uv: `uv tool install cookiecutter`
  - With pip: `python3 -m pip install --user cookiecutter`
  - With Anaconda: `conda install cookiecutter`
2. Check Cookiecutter version: `cookiecutter --version`
  - if not found on Linux/MacOS
    - echo $SHELL
    - for `/bin/bash`:
      - `echo 'export PATH="$HOME/.local/bin:PATH"' >> ~/.bashrc`
      - `source ~/.bashrc`
    - for `/bash/zsh`:
      - `echo 'export PATH="$HOME/.local/bin:PATH"' >> ~/.zshrc`
      - `source ~/.zshrc`
3. Get Python method template with Cookiecutter: `cookiecutter https://github.com/BDA-KTS/MethodsHub-method-template.git`
4. Work on your method locally, until ready
5. Upload to GitHub
  - Create a GitHub repository providing required details and make it public
  - In your terminal in the method directory
    - `git init`
    - `git add .`
    - `git commit -m "method ..."`
  - Push changes from local directory
  - `git remote add origin https://github.com/your-username/your-repo.git`
  - `git push -u origin main`

*It internally uses git clone to clone the template repository locally while setting specific configurations for the method.*

