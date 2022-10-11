from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return 'Hello!'

@app.route('/api/item', methods=['POST'])
def item():
    request_data = request.get_json()
    if ('item_name' in request_data):
      print(request_data)
      return jsonify({'result':'success'})
    else:
      return 'incorrect data', 422

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)