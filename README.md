# ImageFinder App

The ImageFinder App is a powerful tool that allows you to automatically cluster a set of images and retrieve the most suitable image along with its cluster based on a description text.


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


## How the App Works

1. The `init.py` script handles the data preparation and processing:
   - It downloads a specified number of random images from an external source and saves them in the `images` folder.
   - Image features, such as color histograms or embeddings, are extracted for each image.
   - The features are then scaled and reduced using t-SNE to create a lower-dimensional representation of the data.
   - K-means clustering is applied to group similar images together.

2. After preprocessing, `app.py` initializes the app and frontend:
   - It loads the preprocessed data and the generated clustering models.
   - The app launches a web-based frontend that displays the clustered image groups.
   - The frontend provides a user-friendly interface to explore the image clusters.

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
