from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Request, Response
import requests

def proxy(env, start_response):
    # 1. Create a request object from the incoming request.
    request = Request(env)
    
    # 2. Determine the target URL (Flask app)
    target_url = 'http://127.0.0.1:5000' + request.path
    
    # 3. Forward the request to your Flask app
    response = requests.get(target_url, headers=request.headers)
    
    # 4. Create a response object from the Flask app's response
    # 5. Forward the response back to Postman
    return Response(response.content, status=response.status_code, headers=response.headers)(env, start_response)

# 6. Create a WSGI application using DispatcherMiddleware
app = DispatcherMiddleware(proxy)

# 7. Start the proxy server
if __name__ == '__main__':
    run_simple('127.0.0.1', 8080, app)