from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/proxy" method="get">
            <input type="text" name="url" placeholder="Enter a URL">
            <input type="submit" value="Go">
        </form>
    '''

@app.route('/proxy')
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return "URL is required."

    if not target_url.startswith("http"):
        target_url = "http://" + target_url

    try:
        resp = requests.get(target_url)
        return Response(resp.content, content_type=resp.headers.get('Content-Type'))
    except Exception as e:
        return f"Error fetching the URL: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
