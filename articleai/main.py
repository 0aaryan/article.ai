import os
import json
from generators.blog_generator import BlogGenerator
from generators.image_generator import ImageExtractor
from dotenv import load_dotenv

load_dotenv()

def create_output_folder(output_base_dir,title):
    """
    Create a new folder in the output directory with the specified title.

    Args:

        output_base_dir (str): The path to the output directory.
        title (str): The title of the blog.

    Returns:
        str: The path to the newly created folder.

    """

    # Create the output directory if it doesn't exist
    os.makedirs(output_base_dir, exist_ok=True)

    # Create a new folder for each blog
    title = title.replace(" ", "_")
    blog_folder_path = os.path.join(output_base_dir, title)
    os.makedirs(blog_folder_path, exist_ok=True)

    return blog_folder_path

def save_blog_to_folder(blog_json, folder_path):
    """
    Save the blog JSON to a file in the specified folder.

    Args:
        blog_json (dict): The blog content in JSON format.
        folder_path (str): The path to the folder where the blog should be saved.
    """
    blog_file_path = os.path.join(folder_path, "blog.json")
    with open(blog_file_path, "w") as f:
        json.dump(blog_json, f)

if __name__ == "__main__":
    # List of URLs for generating blogs
    url_blog_data = [
        "https://www.adobe.com/express/learn/blog/how-to-make-a-living-blogging",
        "https://economictimes.indiatimes.com/news/international/business/apple-plans-rescue-for-17-billion-watch-business-in-face-of-ban/articleshow/106106669.cms"

    ]

    # List of topics for generating blogs
    topic_blog_data = [
    ]

    # Output base directory
    output_base_dir = "output"

    # articleai/static/output_template/blog_template.json
    syntax_file_path = "static/output_template/blog_template.json"
    #abs
    syntax_file_path = os.path.join(os.path.dirname(__file__), syntax_file_path)


    # Create output base directory if it doesn't exist
    os.makedirs(output_base_dir, exist_ok=True)

    # Generate blogs from URLs
    for url in url_blog_data:
        try:
            # Create a new folder for each blog
            # blog_folder_path = create_output_folder(output_base_dir)

            # Instantiate BlogGenerator and generate blog content
            blog_generator = BlogGenerator(syntax_file_path=syntax_file_path)
            blog_json = blog_generator.generate_blog_from_url(url)

            #create folder
            blog_folder_path = create_output_folder(output_base_dir,blog_json.get("title", ""))

            # Save blog content to the folder
            save_blog_to_folder(blog_json, blog_folder_path)

            # Instantiate ImageExtractor and download images to the same folder
            image_extractor = ImageExtractor(blog_json, blog_folder_path)
            image_extractor.download_images()

            print(f"Blog and images for {url} saved in folder: {blog_folder_path}")

        except Exception as e:
            print(f"Error processing URL blog entry: {str(e)}")

    # Generate blogs from topics
    for topic in topic_blog_data:
        try:
            # Create a new folder for each blog
            # blog_folder_path = create_output_folder(output_base_dir)

            # Instantiate BlogGenerator and generate blog content
            blog_generator = BlogGenerator(syntax_file_path=syntax_file_path)
            blog_json = blog_generator.generate_blog_from_topic(topic)

            #create folder
            blog_folder_path = create_output_folder(output_base_dir,blog_json.get("title", ""))

            # Save blog content to the folder
            save_blog_to_folder(blog_json, blog_folder_path)

            # Instantiate ImageExtractor and download images to the same folder
            image_extractor = ImageExtractor(blog_json, blog_folder_path)
            image_extractor.download_images()

            print(f"Blog and images for topic '{topic}' saved in folder: {blog_folder_path}")

        except Exception as e:
            print(f"Error processing topic blog entry: {str(e)}")
