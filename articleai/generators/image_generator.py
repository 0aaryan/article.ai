import os
import urllib.request
from duckduckgo_search import DDGS
import json
from time import sleep
import requests

class ImageExtractor:
    def __init__(self, json_data, output_dir):
        """
        Initializes the ImageExtractor with JSON data and output directory.

        Args:
            json_data (dict): The JSON data containing information about the images.
            output_dir (str): The directory where the images will be saved.
        """
        self.json_data = json_data
        self.output_dir = output_dir
        self.retry_attempts = 3  # Number of retry attempts

    def search_and_download_images(self, query,img_name):
        """
        Search for images using DuckDuckGo and download the first image.

        Args:
            query (str): The search query for images.

        Returns:
            str: The path to the downloaded image.
        """

        for attempt in range(self.retry_attempts):
            try:
                # Create the output directory if it doesn't exist
                os.makedirs(self.output_dir, exist_ok=True)

                # Search for images
                images_generator = DDGS().images(query, license_image="ShareCommercially")

                # Download and save the first image
                for idx, image in enumerate(images_generator):
                    # image_path = os.path.join(self.output_dir, f"{img_name}.png")
                    # headers = {
                    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
                    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    #     'Accept-Language': 'en-US,en;q=0.5',
                    #     # 'Accept-Encoding': 'gzip, deflate, br',
                    #     'Referer': 'https://www.google.com/',
                    #     'Connection': 'keep-alive',
                    #     'Upgrade-Insecure-Requests': '1',
                    #     'Sec-Fetch-Dest': 'document',
                    #     'Sec-Fetch-Mode': 'navigate',
                    #     'Sec-Fetch-Site': 'cross-site',
                    #     'Sec-Fetch-User': '?1',
                    #     # Requests doesn't support trailers
                    #     # 'TE': 'trailers',
                    #     'If-None-Match': '"6581db01-471a"',
                    # }

                    # urllib.request.urlretrieve(image["image"], image_path, headers=headers)
                    # print(f"Image downloaded: {image_path}")
                    # return image_path  # Only download the first image

                    image_path = os.path.join(self.output_dir, f"{img_name}.png")  # Add .png to the file name
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Referer': 'https://www.google.com/',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'cross-site',
                        'Sec-Fetch-User': '?1',
                        'If-None-Match': '"6581db01-471a"',
                    }

                    try:
                        response = requests.get(image["image"], headers=headers, timeout=10)
                        response.raise_for_status()

                        with open(image_path, 'wb') as f:
                            f.write(response.content)

                        print(f"Image downloaded: {image_path}")
                        return image_path  # Only download the first imag
                    except Exception as e:
                        print(f"Error downloading image: {str(e)}")
                        sleep(5)

                if attempt == self.retry_attempts - 1:
                    #try second image
                    images_generator = DDGS().images(query, license_image="ShareCommercially",max_results=2)
                    for idx, image in enumerate(images_generator):
                        if idx == 1:
                            image_path = os.path.join(self.output_dir, f"{img_name}.png")
                            urllib.request.urlretrieve(image["image"], image_path)
                            print(f"Image downloaded: {image_path}")
                            return image_path


            except Exception as e:
                print(f"Error searching and downloading images (attempt {attempt + 1}/{self.retry_attempts}): {str(e)}")
                sleep(5)  # Sleep for 5 seconds before retrying
        raise RuntimeError(f"Failed to download image after {self.retry_attempts} attempts.")

    def download_images(self):
        """
        Download images from the provided JSON data and save them to the output directory.
        """
        try:
            # Download title_image using the search function
            title_image_url = self.search_and_download_images(self.json_data.get("title_image", ""),"0")
            if title_image_url:
                print(f"Title image downloaded: {title_image_url}")

            # Download images from content
            for idx,content_item in enumerate(self.json_data.get("content", [])):
                image_url = self.search_and_download_images(content_item.get("image", ""),str(idx+1))
                if image_url:
                    print(f"Image downloaded: {image_url}")
                sleep(5)  # Sleep for 5 seconds to avoid rate limiting

        except Exception as e:
            raise RuntimeError(f"Error downloading images: {str(e)}")


if __name__ == "__main__":
    # Your JSON data
    # Load json from file
    with open("blog_url.json", "r") as f:
        json_data = json.load(f)

    # Output directory for saving images
    output_dir = "images_output"

    # Create an instance of ImageExtractor
    image_extractor = ImageExtractor(json_data, output_dir)

    try:
        # Download and save images
        image_extractor.download_images()
    except Exception as e:
        print(f"Error in image extraction: {str(e)}")
