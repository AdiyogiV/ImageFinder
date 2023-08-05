import requests
import os

def download_images(num_images=300):
    # Define the API endpoint to get random images from Unsplash
    url = f"https://source.unsplash.com/random"

    # Create a directory to save the images (if not already present)
    output_dir = "static"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Downloading {num_images} images...")

    for i in range(1, num_images+1):
        image_url = f"{url}/{i}"
        image_data = requests.get(image_url)
        if image_data.status_code == 200:
            image_path = os.path.join(output_dir, f"image_{i}.jpg")
            with open(image_path, 'wb') as f:
                f.write(image_data.content)
            print(f"Downloaded image {i}/{num_images}")
        else:
            print(f"Failed to download image {i}/{num_images}")

if __name__ == "__main__":
    num_images_to_download = 1000
    download_images(num_images_to_download)
