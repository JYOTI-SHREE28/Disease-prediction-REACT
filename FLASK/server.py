from flask import Flask, request, jsonify, send_from_directory
import joblib
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='../my-app/build', static_url_path='/')
CORS(app)

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data or 'symptoms' not in data:
            return jsonify({'error': 'No symptoms provided'}), 400
        
        symptoms = data['symptoms']
        print(f"Received symptoms: {symptoms}")
        symptoms_tfidf = vectorizer.transform([symptoms])
        prediction = model.predict(symptoms_tfidf)[0]
        print(prediction)
        
        return jsonify({'disease': prediction})
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred during prediction'}), 500

if __name__ == '__main__':
    app.run(debug=True)
