import io
import numpy as np
import pickle
import tensorflow as tf

from PIL import Image
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from Settings import IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CHANNEL

IMG_SIZE = (IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CHANNEL,)

def _create_base_network(in_dims):
    """
    Base network to be shared.
    """

    base_model = tf.keras.applications.resnet.ResNet50(include_top=False, weights='imagenet', input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3))
    base_model.trainable = False 

    global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
    prediction_layer = tf.keras.layers.Dense(100)

    # build a new model reusing the pretrained base
    model = tf.keras.Sequential([
      base_model,
      global_average_layer,
      prediction_layer
    ])

    return model

def _load_model():
  anchor_input = Input(IMG_SIZE, name='anchor_input')
  Shared_DNN = _create_base_network(IMG_SIZE)
  encoded_anchor = Shared_DNN(anchor_input)

  trained_model = Model(inputs=anchor_input, outputs=encoded_anchor)
  trained_model.load_weights('model/resnet_triplet_model_celeb.hdf5')
  return trained_model

def load_and_preprocess_image(path_to_image):
  im = Image.open(io.BytesIO(path_to_image))
  im = im.resize((IMAGE_HEIGHT, IMAGE_WIDTH))
  im_array = np.asarray(im)
  return im_array

def load_embeddings():
  return np.load("model/embeddings.npy")

def get_embeddings(image):
    #preprocess the image - resize and expand dims
    img = load_and_preprocess_image(image)
    im_batch = img.reshape(-1,250, 250, 3)
    print(im_batch.shape)

    trained_model = _load_model()
    feature_list = trained_model.predict(im_batch)
    return feature_list

def get_celeb_image_paths():
    with open('model/celeb_names.pkl', 'rb') as f:
        celeb_image_paths = pickle.load(f)
    return celeb_image_paths





