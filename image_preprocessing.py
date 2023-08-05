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

def perform_kmeans_clustering(features, num_clusters, output_dir):
    # Feature scaling
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # t-SNE for dimensionality reduction
    tsne = TSNE(n_components=2,  perplexity=5, random_state=42)
    reduced_features = tsne.fit_transform(scaled_features)

    n_samples, _ = reduced_features.shape
    if n_samples < num_clusters:
        num_clusters = n_samples

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(reduced_features)
    np.save(output_dir+'/image_clusters.npy', clusters)
    return clusters


def store_image_features(n):
    current_file_path = os.path.abspath(__file__)
    images_directory = os.path.dirname(current_file_path) + "/static"
    image_features = {}
    output_dir = os.path.dirname(current_file_path) + "/models/"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(images_directory):
        os.makedirs(images_directory)
        
    for image_file in os.listdir(images_directory):
        image_path = os.path.join(images_directory, image_file)
        features = image_feature_extraction(image_path)
        if features is not None:  # Check if features are valid (not empty)
            image_features[image_file] = features

    if not image_features:  # Check if any valid features were extracted
        print("No valid image features found. Please check the feature extraction process.")
        return

    image_features_array = np.array(list(image_features.values()))
    np.save(output_dir + '/image_features.npy', image_features)
    perform_kmeans_clustering(image_features_array, n, output_dir=output_dir)



store_image_features(10)
