from flask import Flask, render_template, request, flash
import json
import os

app = Flask(__name__)

app.secret_key = 'This stops a CSRF attack!'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/galaxy')
def node():
    with open ('systems.json','r') as json_file:
        galaxy_data = json.load(json_file)  
    return render_template('galaxy.html', system_data=galaxy_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
