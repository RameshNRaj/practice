PRACTICE

Build Steps:

## create venv
python -m venv cp_venv --clear 
## activate venv
venv\Scripts\activate.bat
## build
pip install --upgrade pip
pip install .
pip install .[test]
## unit testcase run and coverage checks
coverage run
coverage report

## excecution command
python src/csv_transformation/transformation.py


