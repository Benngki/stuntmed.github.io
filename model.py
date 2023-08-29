import joblib

model = joblib.load('hc_model.pkl')
encoder = joblib.load('hc_encoder.pkl')

def predict(gender, umur, lingkar_kepala):
    return encoder.inverse_transform(model.predict([[gender, umur, lingkar_kepala]]))[0]