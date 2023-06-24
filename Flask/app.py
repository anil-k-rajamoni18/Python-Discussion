from flask import Flask



app = Flask(__name__)

@app.get('/')
def home():
    return 'hello wolrd'



if __name__ == '__main__':
    app.run(port=9922)
