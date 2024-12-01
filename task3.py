from flask import Flask, request

app = Flask(__name__)


@app.route('/currency', methods=['GET'])
def currency():
    today = request.args.get('today')
    key = request.args.get('key')

    # Статичне значення курсу валют
    exchange_rate = "USD - 41,5"

    return f"Курс валют на {today} за запитом {key}: {exchange_rate}"


if __name__ == '__main__':
    # Вивести посилання у термінал
    print("Запуск серверу на http://127.0.0.1:8000/currency?today=2024-12-01&key=test")
    app.run(port=8000)
