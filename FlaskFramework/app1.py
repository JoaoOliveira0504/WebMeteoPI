from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from flask_cors import CORS

# Dimensões da imagem de entrada
target_width, target_height = 200, 200
num_channels = 4

app = Flask(__name__)
cors = CORS(app) # Permitir o acesso de qualquer origem

# Rota de teste
@app.route('/')
def helloWorld():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    # Carregar o modelo treinado
    model = load_model('modelo_treinado.h5')

    # Imagem vinda do request
    image = request.files['file']
    
    # Abrir a imagem e redimensionar
    img = Image.open(image)
    img = img.resize((target_width, target_height))  # Redimensionar da imagem
    img = img_to_array(img)  # Converter a imagem para um array
    img = img.reshape(1, target_width, target_height, num_channels)  # Remodelar para corresponder à forma de entrada do modelo
    img = img / 255.0  # Normalizar os dados da imagem
    
    # Previsão usando o modelo carregado
    prediction = model.predict(img)

    # Processar a previsão para retornar um JSON
    response = {
        'sum': prediction.sum().tolist(),
        'max': prediction.max().tolist(),
        'min': prediction.min().tolist(),
        'mean': prediction.mean().tolist(),
        'prediction': prediction.tolist()
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
