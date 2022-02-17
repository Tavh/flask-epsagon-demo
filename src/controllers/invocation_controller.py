import requests

def invoke(url):
    try:
        print(requests.get('http://' + url))        
        return 'Success'
    except:    
        return 'Failure'
