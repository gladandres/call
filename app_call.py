from flask import Flask, jsonify
from flask import abort
from model_pewee import Call, Tariff, get_calls


app = Flask(__name__)



@app.route('/call', methods=['GET'])
def get_tasks():
    list_number = get_calls()
    if len(list_number) == 0:
        abort(404)
    return jsonify({'call': list_number})

@app.route('/call/number=<int:number>', methods=['GET'])
def get_task(number):
    list_number = get_calls(number)
    if len(list_number) == 0:
       abort(404)
    return jsonify({'call': list_number})


if __name__ == '__main__':
    app.run(debug=True)
