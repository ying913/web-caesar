from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
<!doctype html>
<html>
    <head>
         <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action= "/encrypted", method="POST" id="caesar">
            <label for="rotate-by">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" />
            <textarea name="text" form="caesar"></textarea> 
            <input type="submit" />
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/encrypted", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    encrypted_message = rotate_string(text, rot)
    return '<h1>' + cgi.escape(encrypted_message) + '</h1>'

app.run() 