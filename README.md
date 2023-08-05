ImageFinder App
The ImageFinder App is a tool that allows you to automatically cluster a set of images and retrieve most suitable image along with it's cluster based on a description text.meaningful cluster names.

Setup
- Prerequisites
  1. Run pip install -r requirements.txt to install the libraries used.

- Run init.py
  1. Set the number of clusters n and images_to_download in this file..
  2. It downloads the specified number of random images. (or add your own images in 'static' folder and comment download_images func)
  4. It preprocesses images and generates models for image retrieval & clustering.
     
- Run app.py
  1. It initialises the app and frontend.
     

  ![Screenshot 2023-08-05 at 2 46 53 PM](https://github.com/AdiyogiV/ImageFinder/assets/28894829/ec4ef76d-8883-497f-ac29-2f7e6819f1fd)

How the App Works

1. The init.py script handles the data preparation and processing:

  - It downloads a specified number of random images from an external source and saves them in the images folder.
  - Image features, such as color histograms or embeddings, are extracted for each image.
  - The features are then scaled and reduced using t-SNE to create a lower-dimensional representation of the data.
  - K-means clustering is applied to group similar images together.

2. After preprocessing, app.py initializes the app and frontend:

  - It loads the preprocessed data and the generated clustering models.
  - The app launches a web-based frontend that displays the clustered image groups.
  - The frontend provides a user-friendly interface to explore the image clusters.
