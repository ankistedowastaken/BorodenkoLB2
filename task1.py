from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Веб-сервер Flask запущено!"

if __name__ == '__main__':
    app.run(port=8000)