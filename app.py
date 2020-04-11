from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'about': 'Flask API-RESTfull method 1'})


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify(some_json), 201
    else:
        return jsonify({'about': 'GET Method'})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    data = request.get_json()
    return jsonify({'factor': data['factor']*num})


if __name__ == '__main__':
    app.run(debug=True)
