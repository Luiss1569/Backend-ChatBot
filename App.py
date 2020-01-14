from flask import  Flask, jsonify

app = Flask(__name__)

@app.route('/mensagem', methods=['POST'])
def home():
    return jsonify({'nome':'Luis'}),200

if __name__== '__main__':
    app.run(debug=True)