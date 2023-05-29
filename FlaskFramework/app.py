from flask import Flask, request, jsonify
from tensorflow.keras import models, layers
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from flask_cors import CORS
import requests
import datetime
import json
import io
from flask import send_file
import base64


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

# Carregar o arquivo JSON
with open('crop_estacoes.json') as json_file:
    json_data = json.load(json_file)

# Carregar o arquivo JSON estacoes
with open('estacoes.json') as json_file:
    json_estacoes = json.load(json_file)

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

# Função para obter a imagem do radar
def get_radar_image():
    try:
        # Obter a hora atual em UTC
        current_datetime_utc = datetime.datetime.utcnow()

        # Arredondar a hora atual para o múltiplo de 5 mais próximo
        rounded_datetime = current_datetime_utc - datetime.timedelta(minutes=current_datetime_utc.minute % 5)

        # Atrasar a hora em 5 minutos
        datetime_delay = rounded_datetime - datetime.timedelta(minutes=5)

        # Formatar a hora atrasada no padrão desejado para criar a URL
        target_datetime_str = datetime_delay.strftime("%Y-%m-%dT%H%M")

        # Construir o URL com a data e hora atualizada
        image_url = f"https://www.ipma.pt/resources.www/transf/radar/por/pcr-{target_datetime_str}.png"
        print(image_url)

        # Obter a imagem do radar
        response = requests.get(image_url)

        # converter a imagem em bytes
        image_bytes = io.BytesIO(response.content)

        # Retornar a imagem 
        return image_bytes
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'Ocorreu um erro'}), 500

# Rota de teste
@app.route('/')
def helloWorld():
    return 'Hello, World!'

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.get_json()
    estacao_id = data.get('id-estacao')

    # Verificar se o ID da estação existe no arquivo JSON
    if estacao_id in json_data:
        coordinates = json_data[estacao_id]
        
        # Obter a imagem do radar
        image_bytes = get_radar_image()
        
        if image_bytes is None:
            return 'Falha ao obter a imagem do radar.'
        
        try:
            # Abrir a imagem usando o objeto BytesIO
            image = Image.open(image_bytes)
            
            # Recortar a imagem com base nas coordenadas fornecidas
            cropped_image = image.crop(coordinates)
            cropped_image.save(image_bytes, format='PNG')
            image_bytes.seek(0)

            # Converter a imagem em base64
            image_base64 = base64.b64encode(image_bytes.getvalue()).decode('utf-8')

            
            # Se eu tirar isto, dá erro
            # Imagem do radar em bytes
            image = Image.open(image_bytes)
            
            # Cortar a imagem do radar
            image = image.crop(coordinates)
            # ....

            # Converter a imagem para um array
            img = img_to_array(image)
            img = img.reshape(1, target_width, target_height, num_channels)  # Remodelar para corresponder à forma de entrada do modelo
            img = img / 255.0  # Normalizar os dados da imagem

            # Previsão usando o modelo carregado
            prediction = model.predict(img)

            # Criar objeto JSON com imagem e outros valores
            response_data = {
                'id-estacao': estacao_id,
                'image': image_base64,
                'prediction': prediction.max().tolist()
            }

            # Retornar o objeto JSON como resposta
            return json.dumps(response_data)

        except Exception as e:
            print(e)
            return 'Erro ao processar a imagem.'

    return 'ID da estação não encontrado no arquivo JSON.'

# Rota para obter a imagem do radar
@app.route('/radar-image', methods=['GET'])
def radar_image():
    return send_file(get_radar_image(), mimetype='image/png')

# Rota para obter as estações
@app.route('/estacoes', methods=['GET'])
def estacoes():
    return jsonify(json_estacoes)


if __name__ == '__main__':
    app.run()
