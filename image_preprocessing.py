# image_preprocessing.py
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import StandardScaler
from sklearn.manifold import TSNE
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import os
import ssl
def image_feature_extraction(image_path):
    ssl._create_default_https_context = ssl._create_unverified_context

    model = models.mobilenet_v2()
    model = nn.Sequential(
        *list(model.children())[:-1],
        nn.AdaptiveAvgPool2d((1, 1)),
        nn.ReLU(),
        nn.Flatten(),
        nn.Linear(1280, 384)
    )
    model.eval()

    preprocess = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    input_tensor = preprocess(Image.open(image_path))
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)

    return output.numpy().flatten()

def perform_kmeans_clustering(features, num_clusters):
    # Feature scaling
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # t-SNE for dimensionality reduction
    tsne = TSNE(n_components=2, random_state=42)
    reduced_features = tsne.fit_transform(scaled_features)

    n_samples, _ = reduced_features.shape
    if n_samples < num_clusters:
        num_clusters = n_samples

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(reduced_features)
    np.save('models/image_clusters.npy', clusters)
    return clusters


def store_image_features(n):
    images_directory = 'static'
    image_features = {}

    for image_file in os.listdir(images_directory):
        image_path = os.path.join(images_directory, image_file)
        features = image_feature_extraction(image_path)
        image_features[image_file] = features
        image_features_array = np.array(list(image_features.values()))
    np.save('models/image_features.npy', image_features)
    perform_kmeans_clustering(image_features_array, n)


store_image_features(10)
