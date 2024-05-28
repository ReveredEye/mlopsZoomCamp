# mlopsZoomCamp
Main repository for my own progression through the MLOps Zoom camp course. To activate or deactivate python environment in codespaces
use `source <interpreter directory>/bin/activate` or `. deactivate`. Please install Python and Jupyter extensions in codespaces 
(you can click on install on `codespaces: <codespace name>` in VSCode).

To start docker in GitHub codespaces, just run `docker run hello-world` and it will set it up for you. Note, that codespaces uses Linux OS.
Try to avoid using `.devcontainer` folder in `intro_Homework` branch as it messes up with docker.

Since I am doing this without conda (i.e. using '.venv' as environment), for `mlflow` to work ensure that `setuptools` package exists within the environment.
I have used `wget <url_link>` to install files in the data folder within the bash command line. 

To use mlflow ui, you can just try to run `mlflow ui --backend-store-uri sqlite:///mlflow.db` then open the listening port url just like with Jupyter notebooks.



# Link to course info:
https://github.com/DataTalksClub/mlops-zoomcamp/tree/main

# Extensions to install in vscode
Python, Dev containers

# Commands to run in command palette (vscode)
> Codespaces: Add Dev Container Configuration files

> Python: Create environment

# Good resources:

Set up python project in Github workspaces
https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces

