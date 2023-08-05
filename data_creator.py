import requests
import os

import concurrent.futures
from tqdm import tqdm

def download_image(i, url, output_dir):
    image_url = f"{url}/{i}"
    image_data = requests.get(image_url)
    if image_data.status_code == 200:
        image_path = os.path.join(output_dir, f"image_{i}.jpg")
        with open(image_path, 'wb') as f:
            f.write(image_data.content)
    else:
        raise Exception(f"Failed to download image {i}")

def download_images(num_images=300):
    url = "https://source.unsplash.com/random"
    current_file_path = os.path.abspath(__file__)
    output_dir = os.path.dirname(current_file_path)+"/static"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Downloading {num_images} images...")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Create a progress bar
        with tqdm(total=num_images) as pbar:
            futures = {executor.submit(download_image, i, url, output_dir) for i in range(1, num_images+1)}
            for future in concurrent.futures.as_completed(futures):
                # Update the progress bar
                pbar.update(1)
                try:
                    # Ensure no exceptions were raised while downloading the image
                    future.result()
                except Exception as exc:
                    print(f"An image download generated an exception: {exc}")



if __name__ == "__main__":
    num_images_to_download = 1000
    download_images(num_images_to_download)
