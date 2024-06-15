# mlopsZoomCamp
Main repository for my own progression through the MLOps Zoom camp course. To activate or deactivate python environment (`python -m venv .`) in codespaces
use `source <interpreter directory>/bin/activate` or `. deactivate`. Please install Python and Jupyter extensions in codespaces 
(you can click on install on `codespaces: <codespace name>` in VSCode).

To start docker in GitHub codespaces, just run `docker run hello-world` and it will set it up for you. Note, that codespaces uses Linux OS.
Try to avoid using `.devcontainer` folder in `intro_Homework` branch as it messes up with docker.

Since I am doing this without conda (i.e. using '.venv' as environment), for `mlflow` to work ensure that `setuptools` package exists within the environment.
I have used `wget <url_link>` to install files in the data folder within the bash command line. 

To use mlflow ui, you can just try to run `mlflow ui --backend-store-uri sqlite:///mlflow.db` then open the listening port url just like with Jupyter notebooks 
or just go to `http://127.0.0.1:5000` in the browser.

To run mage go to the directory containing mage project and configuration files, in this repository it is `mage-quickstart`. Once in the directory,
run `docker compose up` and then open `http://localhost:6789` in your browser. The contents for the Mage AI orchestration tool are within `mage-repo` branch.
If mlflow doesn't have any attributes working in mage, it may not be properly installed or built - try running `docker compose build` once inside the `mage-quickstart`
directory. To see the shell/kernel of the docker container run `docker exec -ti <CONTAINER_ID> /bin/sh` where `<CONTAINER_ID>` can be found using `docker ps -a` when
the docker container is running after `docker compose up`, this is useful for seeing if mlflow is installed in mage (the image name was `mageai/mageai:latest`).

IMPORTANT: When managing virtual environments: if the virtual environment is done through `python -m venv .` then deactivate using `deactivate`, otherwise if the virtual environment
is done through `pipenv` then use `exit` to deactivate instead. To create pipenv environment using `pipenv install`, note that you can only create one per codespace. To then
activate pipenv using `pipenv shell` and install required packages using `pipenv install <package-name>` or `pipenv install -r requirements.txt`.

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

Mage Quickstart
https://docs.mage.ai/getting-started/setup#docker-compose-template

# Datasets:
New York City Taxi Data
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page?ref=timescale.com

