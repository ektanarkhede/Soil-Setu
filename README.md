### USE PYTHON 3.8

# 2. Create venv
C:/Users/bhart/AppData/Local/Programs/Python/Python38/python.exe -m venv .venv
<!-- python -m venv .venv -->

# 3. Activate venv
./.venv/Scripts/Activate

# 5. Install deps
pip install -r ./requirements.txt --no-cache-dir --force-reinstall
pip install -r ./requirements.txt


# 6. Run the Flask app
./.venv/Scripts/Activate
python app.py
<!-- > python app.py  -->

# 7. Exit
<!-- (Ctrl + C) to close -->
deactivate
