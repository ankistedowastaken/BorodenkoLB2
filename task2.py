from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!"

if __name__ == '__main__':
    print("Запуск серверу на http://127.0.0.1:8000/hello")
    app.run(port=8000)
