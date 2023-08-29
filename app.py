from flask import Flask, request, jsonify
import model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    cqpa = request.form.get('cqpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')

    result = {
    "cqpa" : cqpa,
    "iq" : iq,
    "profile_score" : profile_score
    }

    # return jsonify(result)
    return jsonify(model.predict(1,1,27))

@app.route("/")
def hello_world():
    return "<p>Hello, hahaah World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
    
    