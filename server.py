from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__, static_folder='build')

# React app routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    file_name = path.split('/')[-1]
    if file_name != '':
        return send_from_directory('./build', path)
    else:
        return render_template('index.html')

# Members API Route
@app.route("/api")
def api():
    return {"values": ["data1", "data2"]}

# Form data API Route
@app.route('/api/formdata', methods=['POST'])
def formdata():
    data = request.json
    
    return {"status": "success"}

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)))

    
    # python -m venv venv
    # source venv/Scripts/activate
    # deactivate
    # pip uninstall flask
    # pip install flask