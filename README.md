# ImageFinder App

The ImageFinder App is a tool that allows you to automatically cluster a set of images and retrieve the most suitable image along with its cluster based on a description text.


## Setup

### Prerequisites
1. Run `pip install -r requirements.txt` to install the required libraries.

### Run init.py
1. Set the number of clusters `n` and `images_to_download` in this file.
2. It downloads the specified number of random images (or you can add your own images in the 'static' folder and comment the `download_images` function).
3. It preprocesses images and generates models for image retrieval and clustering.

### Run app.py
1. It initializes the app and frontend.
   
![Screenshot 2023-08-05 at 2 46 53 PM](https://github.com/AdiyogiV/ImageFinder/assets/28894829/7485eb75-852a-4a7a-842e-87c3bdfe5335)


## How the ImageFinder Works  

### 1. Initialization (`init.py`):
   - **First point of entry**: User starts the process here.
   - Calls:
     - `download_images()` from `data_creator.py`: To fetch images.
     - `store_image_features()` from `image_preprocessing.py`: For preprocessing.

### 2. Image Downloading (`data_creator.py`):
   - **Function**: `download_images(num_images)`
     - Downloads images from Unsplash.
     - Uses multi-threading for enhanced speed.
     - Saves images to a local directory.

### 3. Image Preprocessing (`image_preprocessing.py`):

   - **Function**: `store_image_features(n)`
     - Orchestrates the preprocessing tasks.
     - Sets up required directories.
     - Uses multiprocessing for parallel feature extraction.
     - Calls:
       - `image_feature_extraction`: For each image.
       - `perform_kmeans_clustering`: Post feature extraction.
     - Feature set and cluster data are stored.

   - **Function**: `image_feature_extraction(image_path)`
     - Transforms image into a feature vector.
     - Implements MobileNet V2 for this process.
     - Applies resizing and normalization.
     - Returns a feature vector.

   - **Function**: `perform_kmeans_clustering(features, num_clusters, output_dir)`
     - Groups image features into clusters.
     - Feature scaling is applied for consistency.
     - Dimensionality reduction using t-SNE.
     - Executes KMeans clustering.
     - Cluster data saved for retrieval purposes.
       
### 4. Web Application Server (`app.py`):
   - Provides an interactive user interface.
   - Sets up API endpoints for image retrieval.
   - Utilizes `retrieve_image.py` to cater to user queries.

### 5. Image Retrieval (`retrieve_image.py`):

   - **Function**: `retrieve_image(description, num_clusters)`
     - Matches user text description with an image.
     - Text description is transformed into an embedding via SentenceTransformer.
     - This embedding is compared against stored image features.
     - The most similar image and its cluster details are derived.
     - Outputs the best-matching image and relevant cluster data.



## Features

- **Auto-Clustering:** The app utilizes feature extraction and k-means clustering to automatically group similar images together.

- **Image Retrieval:** Users can input a description, and the app will return the most relevant image along with its group name.

- **Predefined Folder Load:** As part of server startup, the app loads images from a predefined folder and performs clustering on them.

- **API Endpoint:** The app exposes an API endpoint that allows users to retrieve images and their group names based on input descriptions programmatically.

- **Web-based Frontend:** The simple and intuitive web-based frontend showcases the app's functionality, providing a textbox to input image descriptions and displaying the retrieved image along with its group name.

## Tech Stack

The ImageFinder App is built using the following tech stack:

- **Backend:** Python with Flask web framework for creating the server and handling API requests.

- **Image Processing:** OpenCV for image feature extraction and manipulation.

- **Clustering:** scikit-learn for k-means clustering and t-SNE for dimensionality reduction.

- **Frontend:** HTML, CSS, and JavaScript for building the user interface.
