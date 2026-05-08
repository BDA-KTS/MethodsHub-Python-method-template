# Methods Hub Method Template

The methods Hub method template is built using [cookiecutter.io](https://www.cookiecutter.io/). It helps to preload the project directory with the necessary files required for the Methods Hub i.e., 

- *postBuild* file to generate the method homepage and deploy the method in the interactive environment
- *README.md* with the desired subsections and their specifications
- Within project directory structure having
  - *Data* for the input and output files
  - *binder* for the postBuild and environment preserving files
  - *.github* for the GitHub workflows
- *CITATION.CFF* file for attribution
- Environment preservation files (*environment.yml* and *requirements.txt*)
- GitHub workflow file *methodshub.yml* to review the method 

## How to Use

- With Python virtual environment
  - ```python -m venv .methodenv```
  - ```cd .methodenv```
  - ```Scripts\activate```
  - ```python3 -m pip install --user cookiecutter```
  - test cookiecutter installation ```cookiecutter```
  - Execute the git clone path with the cookiecutter ```cookiecutter https://github.com/BDA-KTS/MethodsHub-method-template.git```
- With Anaconda
  - ```conda create -m methodenv```
  - ```conda activate methodenv```
  - ```conda install cookiecutter```
  - test cookiecutter installation ```cookiecutter```
  - Execute the git clone path with the cookiecutter ```cookiecutter https://github.com/BDA-KTS/MethodsHub-method-template.git```
*It internally uses git clone to clone the template repository locally while setting specific configurations for the method.*
  - **Note:** You will be asked for the method configurations e.g.., *method_title*, *method_slug* (if name has spaces) etc.

These steps will deploy the method structure to write code, modify README.md and preserve the virtual environment.
