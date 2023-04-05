
from flask import Flask,render_template,request
import hashlib

app = Flask(__name__)
 

@app.route('/uploadimage')
def printImage():
    return  render_template('index.html')  


@app.route('/newimage' , methods = ['GET' , 'POST'])
def image():
    if request.method == 'POST':
        image =   request.form['Path']
        
        # For convert image to md5Hash
        # im_path = "your image path"
        with open(image, "rb") as f:
            im_bytes = f.read()
        im_hash = str(hashlib.md5(im_bytes).hexdigest())
        return "md5Hash image is :"+ im_hash


if __name__ == "__main__":
    app.run(debug=True, port = 8000)