# retrieve_image.py

from collections import Counter
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import StandardScaler
from sklearn.manifold import TSNE
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

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

    kmeans = KMeans(n_clusters=num_clusters,n_init=10, random_state=42)
    clusters = kmeans.fit_predict(reduced_features)
    np.save('image_clusters.npy', clusters)
    return clusters

def retrieve_image(description, num_clusters):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode(description)
    current_file_path = os.path.abspath(__file__)
    image_features = np.load(os.path.dirname(current_file_path)+'/models/image_features.npy', allow_pickle=True).item()
    image_clusters = np.load(os.path.dirname(current_file_path)+'/models/image_clusters.npy', allow_pickle=True)

    min_distance = float('inf')
    min_distance_image = None
    cluster_image_paths = {cluster: [] for cluster in range(num_clusters)}

    for image_file, features in image_features.items():
        distance = np.linalg.norm(embeddings - features)

        if distance < min_distance:
            min_distance = distance
            min_distance_image = image_file

    min_distance_image_index = list(image_features.keys()).index(min_distance_image)
    # Find the cluster assignment for the most relevant image
    relevant_image_cluster = image_clusters[min_distance_image_index]

    cluster_counts = Counter(image_clusters)
    if relevant_image_cluster not in cluster_image_paths:
        cluster_image_paths[relevant_image_cluster] = []

    cluster_image_paths[relevant_image_cluster].append(min_distance_image)


    return min_distance_image, relevant_image_cluster, cluster_counts, cluster_image_paths


