# demo-flask-4111
demo flask app for COMS 4111

## useful snippets
### run your server under a screen session
- start a screen session
  `screen -S db`
- detach 
  `Ctrl-a d`
- reconnect to a screen session
  `screen -dr db`
  
### use requirements.txt
- everytime you add a new python package, update requiements.txt and install it on your server
  `pip install -r requirements.txt`
  
### bind your app to `0.0.0.0`
- `export FLASK_APP=application.py`
- have all the environment variables set in a `.env` file
- `honcho run flask run --host=0.0.0.0`
  
