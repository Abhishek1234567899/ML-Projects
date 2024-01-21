echo [$(date)]: "START"


echo [$(date)]: "creating venv with python 3.8 version" 


conda create --prefix ./venv python=3.8 -y


echo [$(date)]: "activating the environment" 

source activate ./venv

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 