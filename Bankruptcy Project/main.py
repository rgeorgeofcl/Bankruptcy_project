import pickle
from flask import Flask, render_template, request

# Create an object of the Flask class
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pre')
def pre():
    return render_template('model.html')

@app.route('/predict', methods=['POST'])
def predict():
    industrial_risk = float(request.form.get('industrial risk', 0))
    management_risk = float(request.form.get('management risk', 0))
    financial_flexibility = float(request.form.get('financial_flexibility', 0))
    credibility = float(request.form.get('credibility', 0))
    competitiveness = float(request.form.get('competitiveness', 0))
    operating_risk = float(request.form.get('operating_risk', 0))

    # You can pass the above six features to your model for prediction.
    predictions = model.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])

    # Handle the predictions as needed.
    print(predictions)

    # Determine the prediction text
    prediction_text = 'Bankrupt' if predictions == 1 else 'Non-Bankrupt'

    return render_template('model.html', predictions_text=f'The company is under {prediction_text} category')

if __name__ == '__main__':
    app.run(debug=True)
