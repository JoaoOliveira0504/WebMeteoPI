#Comando para correr → py app.py run

from flask import Flask, request, jsonify
from tensorflow.keras.utils import normalize
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from flask_cors import CORS
import requests
import datetime
import json
import io
import os
import numpy as np
from flask import send_file
import base64
from constants import *
from model import *
import re

app = Flask(__name__)
cors = CORS(app) # Permitir o acesso de qualquer origem

# Função para desnormalizar o valor da precipitação
def denormalize_precipitation_value(normalized_value):
    return (normalized_value * 240) / 100

# Função para extrair o valor da hora de diferença com base no nome do ficheiro de pesos
def extract_number_from_filename(filename):
    pattern = r'\d+'  # Regular expression pattern to match one or more digits
    match = re.search(pattern, filename)
    if match:
        return int(match.group())
    else:
        return None

# Função para obter a imagem do radar
def get_radar_image():
    try:
        # Obter a hora atual em UTC
        current_datetime_utc = datetime.datetime.utcnow()

        # Arredondar a hora atual para o múltiplo de 5 mais próximo
        rounded_datetime = current_datetime_utc - datetime.timedelta(minutes=current_datetime_utc.minute % 5)

        # Atrasar a hora em 10 minutos
        datetime_delay = rounded_datetime - datetime.timedelta(minutes=10)

        # Formatar a hora atrasada no padrão desejado para criar a URL
        target_datetime_str = datetime_delay.strftime("%Y-%m-%dT%H%M")

        # Construir o URL com a data e hora atualizada
        image_url = f"https://www.ipma.pt/resources.www/transf/radar/por/pcr-{target_datetime_str}.png"

        # Obter a imagem do radar
        response = requests.get(image_url)
        image_data = io.BytesIO(response.content)
        image = Image.open(image_data)
        
        # Retornar a imagem 
        return image

    except Exception as e:
        print(e)
        return jsonify({'error': 'Ocorreu um erro'}), 500

    # finally:
    #     # Certificar-se de que a imagem é fechada, independentemente de qualquer exceção
    #     if 'image' in locals():
    #         image.close()
    
# Função para redimensionar a imagem
def resize_image(image):
    # Resize the image to 100x100 pixels
    resized_image = image.resize((100, 100))
    
    # Return the resized image
    return resized_image

@app.route('/process_image', methods=['GET'])
def process_image():

    current_radar_image = get_radar_image()

    if current_radar_image is None:
        return 'Falha ao obter a imagem do radar.'

    # Create a dictionary where the keys are the prevision hour
    full_hour_prediction_dictionary = {1: None, 2: None, 3: None}


    # Create a dictionary where the keys are the IDs
    current_hour_prediction_dictionary = {str(id): None for id in ids} 

    model_weights_list = file_list = os.listdir("model_weights_by_hour/")

    for model_weights in model_weights_list:
        try:
            model.load_weights("model_weights_by_hour/"+str(model_weights))

        except Exception as e:
            print("Erro ao carregar os pesos do modelo: ", e)

        finally:
            try:
                for id in ids:

                    # Recortar a imagem com base nas coordenadas fornecidas
                    cropped_image = current_radar_image.crop(station_box_dict[id])

                    # Redimensionar a imagem
                    cropped_image = resize_image(cropped_image)

                    # Converter a imagem para um array
                    array_image = np.array([np.array(cropped_image)])

                    # Normalizar a imagem
                    normalized_array_image = normalize(array_image, axis=1)

                    # Previsão usando o modelo carregado
                    predictions = model.predict(normalized_array_image)

                    #Adicionar a previsão ao dicionário
                    current_hour_prediction_dictionary[str(id)] = denormalize_precipitation_value(int(np.argmax(predictions[0])))

                    #print()
            except Exception as e:
                print(e)
                return 'Erro ao processar a imagem.'

            finally:
                full_hour_prediction_dictionary[str(extract_number_from_filename(model_weights))] = current_hour_prediction_dictionary           
    return json.dumps(full_hour_prediction_dictionary)



# Rota para obter a imagem do radar
@app.route('/radar-image', methods=['GET'])
def radar_image():
    return send_file(get_radar_image(), mimetype='image/png')

if __name__ == '__main__':
    app.run()
