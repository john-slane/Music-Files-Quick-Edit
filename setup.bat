:: install virtual environment and dependencies
@echo off
python -m venv .\env
call .\env\Scripts\activate.bat
python -m pip install -r requirements.txt
REM pause