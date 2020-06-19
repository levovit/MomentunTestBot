# Momentun Test Bot



## How to start (local)
Clone repository
Create and activate a virtual environment

```commandline
virtual venv --python=python3.8
source venv/bin/activate
```
Install the required modules
```commandline
pip install -r requirements.txt
```
Create a database
```commandline
python manage.py db init
python manage.py db migrate -m "users table"
python manage.py db upgrade
```
Set environment variables
```commandline
set FLASK_APP=run_local.py
set TOKEN=<your-token>
set SQLALCHEMY_DATABASE_URI=<your-db-uri>
```
Set the tunnel to localhost (https://ngrok.com/download)
```commandline
ngrok http 5000
set HOST_URL=<your-tunnel-url>
```
Run flask on localhost
```commandline
flask run
```