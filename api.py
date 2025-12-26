from flask import Flask, request,current_app,render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEEP_IT_A_SECRET'
CORS(app, resources={ r'/*': {'origins': "*"}}, supports_credentials=True)

@app.route("/")
def hello_world():
    return "<p>X PASSPORT</p>"