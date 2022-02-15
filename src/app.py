import requests
import epsagon

from flask import Flask

epsagon.init(
    token='03b6d382-54b5-4cba-adc8-f4add446f50a',
    app_name='Epsagon Application',
    metadata_only=False,
)


@epsagon.python_wrapper
def initiate_epsagon():
    return "It worked!"


initiate_epsagon()

app = Flask(__name__)

@epsagon.python_wrapper
@app.route('/call/<url>')
def call(url):
    try:
        print(requests.get('http://' + url))        
        return 'Success'
    except:    
        return 'Failure'




    