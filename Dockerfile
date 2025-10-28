from python:3.9
workdir /app
copy . /app
pip run install --no-cache-dir -r requirements.txt
expose 5000
env flask_app = app.py
cmd["python",'app.py']