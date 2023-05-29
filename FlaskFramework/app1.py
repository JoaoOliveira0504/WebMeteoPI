from flask import Flask, request, jsonify
from tensorflow.keras import models, layers
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from flask_cors import CORS

# Dimensões da imagem de entrada
target_width, target_height = 200, 200
num_channels = 4 
n_classes = 100 
n_neuronios = 16
filter_size = 3 
max_pool_size = (2,2) 
n_epochs = 100 
n_strides = 1
dropout_value = 0.4
image_size = 200

app = Flask(__name__)
cors = CORS(app) # Permitir o acesso de qualquer origem

# Rota de teste
@app.route('/')
def helloWorld():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Criar a arquitetura do modelo
        model = models.Sequential()
        model.add(layers.Conv2D(n_neuronios, max_pool_size, activation='relu', input_shape=(target_width, target_height, num_channels)))
        model.add(layers.Conv2D(n_neuronios, filter_size, strides=n_strides, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(dropout_value))
        model.add(layers.MaxPooling2D(pool_size=max_pool_size))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(n_neuronios*2, filter_size, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Flatten())
        model.add(layers.Dense(n_neuronios*4, activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(dropout_value))
        model.add(layers.Dense(n_classes, activation='softmax'))

        # Carregar os pesos do modelo
        model.load_weights('../DeepLearningPrecipitation/best_model.h5')

        # Imagem vinda do request
        image = request.files['image']

        print(image.filename)
        
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
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
