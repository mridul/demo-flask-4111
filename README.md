# Flask + SQLAlchemy demo for COMS 4111
A very simple app in flask to demonstrate flask and sqlalchemy
Built as a demonstration during a lecture given for Prof. Alexandros Biliris's Introduction to Databases class at Columbia University.

## useful snippets
### run your server under a screen session
- start a screen session
  `screen -S db`, where `db` is the session name
- detach 
  `Ctrl-a d`
- reconnect to a screen session
  `screen -dr db`, where `db` is the session name
  
### use requirements.txt
- everytime you add a new python package, update `requiements.txt` and install it on your server
  `pip install -r requirements.txt`
  
### bind your app to `0.0.0.0`
- connect to your screen session
- `export FLASK_APP=application.py`
- have all the environment variables set in a `.env` file
- `honcho run flask run --host=0.0.0.0`
  
