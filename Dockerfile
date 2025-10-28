from python:3.9
workdir /app
copy . /app
run pip install --no-cache-dir -r requirements.txt
expose 5000
env flask_app = app.py
cmd ["python",'app.py']
