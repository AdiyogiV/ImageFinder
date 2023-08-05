# ImageFinder App

The ImageFinder App is a powerful tool that allows you to automatically cluster a set of images and retrieve the most suitable image along with its cluster based on a description text. The app also generates meaningful cluster names, making it easy to organize and manage large image collections.

## Setup

### Prerequisites
1. Run `pip install -r requirements.txt` to install the required libraries.

### Run init.py
1. Set the number of clusters `n` and `images_to_download` in this file.
2. It downloads the specified number of random images (or you can add your own images in the 'static' folder and comment the `download_images` function).
3. It preprocesses images and generates models for image retrieval and clustering.

### Run app.py
1. It initializes the app and frontend.

![Screenshot](https://raw.githubusercontent.com/AdiyogiV/ImageFinder/main/assets/screenshot.png)

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

The ImageFinder App streamlines the process of organizing and analyzing image collections, making it easier to find and manage related images. Its auto-clustering and retrieval capabilities, along with a straightforward web interface, make ImageFinder a valuable addition to any image-centric project.
