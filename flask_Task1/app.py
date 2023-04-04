from flask import Flask

app=Flask(__name__)

@app.route('/')
def helloworld():
    return "hello world!"

@app.route('/num/<int:number>')
def square_root(number):
    return f'The value of square root is : {number*number}!'

if __name__=='__main__':
    app.run(debug=True)