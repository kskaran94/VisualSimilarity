## Visual Similarity ##

The repository comprises of notebooks that evaluate different models for image similarity.
The UI folder consist of a Tornado based application that finds the top 5 celebrity matches for a given input image.

Structure of the notebooks:

1. Data_Subsetting_train_test_split.ipynb - This notebook generates a subset of the actual LFW dataset. It also split the dataset into train and test sets for use by other notebooks.

2. Image_Similarity_Baseline_Celeb.ipynb - This notebook investigates the baseline model(VGG16)

3. Triplet_loss_celeb_cnn.ipynb - In this notebook, we implemented a custom neural network as the base architecture for triplet loss.

4. Triplet_loss_celeb_samll_cnn.ipynb - This notebook comprises of different base architectures that we evaluated.

5. Triplet_loss_celeb_resnet.ipynb -  In this notebook, RESNET50 pre-trained model is used as the base model and is compiled using triplet loss function.