# Import the libraries
from tensorflow.keras import models, layers

# Neural Networks variables
image_size = 100
num_channels = 4 
n_classes = 100 
n_neuronios = 16
filter_size = 3 
max_pool_size = (2,2) 
n_epochs = 100 
n_strides = 1
dropout_value = 0.6

# Create the model architecture
model = models.Sequential()
model.add(layers.Conv2D(n_neuronios, max_pool_size, activation='relu', input_shape=(image_size, image_size, num_channels)))
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

# Load the model weights
model.load_weights('../DeepLearningPrecipitation/best_model.h5')

__all__ = ['image_size', 'num_channels', 'n_classes', 'n_neuronios', 'filter_size', 'max_pool_size', 'n_epochs', 'n_strides', 'dropout_value', 'model']