from data_creator import download_images
from image_preprocessing import store_image_features


if __name__ == "__main__":
    clusters = 10
    images_to_download = 1000
    #download_images(images_to_download)
    store_image_features(10)
