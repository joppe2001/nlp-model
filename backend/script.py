# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from preprocessing import preprocess_review
# import flask cors

app = Flask(__name__)
# flask cors to allow cross origin requests
cors = CORS(app)

# Load the pre-trained model and CountVectorizer
model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)  # Get data sent in JSON format
    review_text = data['review']
    review_processed = preprocess_review(review_text)
    review_vectorized = cv.transform([review_processed]).toarray()
    prediction = model.predict(review_vectorized)
    prediction_label = 'Positive Review' if prediction[0] == 1 else 'Negative Review'
    
    return jsonify({
        'review': review_text,
        'prediction': prediction_label
    })

if __name__ == '__main__':
    app.run(debug=True)
