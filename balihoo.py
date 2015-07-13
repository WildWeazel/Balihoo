from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def respond():
  if request.args.get('q') == 'Ping':
    return 'OK'
  else:
    print request
  
app.run(host='0.0.0.0')