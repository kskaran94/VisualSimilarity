from model.model import load_embeddings, get_embeddings, get_celeb_image_paths
import numpy as np

def get_celebrity_matches(input_image):
    train_embeddings = load_embeddings()
    print("got train embeddings")
    test_image_embedding = get_embeddings(input_image)
    print("got test embeddings")
    celeb_image_paths = get_celeb_image_paths()
    print("got celebs names")

    diff = (train_embeddings - test_image_embedding)**2
    dist = np.sum(diff, axis=1)
    nearest_neighbors = np.argsort(dist)[:5]

    images_to_return = []
    for index in nearest_neighbors:
      temp = "/".join(celeb_image_paths[index].split("/")[2:])
      images_to_return.append(temp)

    print(images_to_return)
    return images_to_return
