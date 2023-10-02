from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример маршрута, который имитирует ответ на запрос
@app.route('/api/data', methods=['GET'])
def get_mock_data():
    mock_data = {'message': 'This is mock data'}
    return jsonify(mock_data)

if __name__ == '__main__':
    app.run()