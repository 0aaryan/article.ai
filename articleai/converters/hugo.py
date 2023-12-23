import json
class BlogConverter:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.json_path = os.path.join(self.folder_name, "blog.json")

    def convert_to_markdown(self):
        with open(self.json_path, "r") as f:
            json_data = json.load(f)

        blog_folder_name = os.path.basename(self.folder_name)
        markdown_content = f"---\ntitle: \"{json_data['title']}\"\ndate: {json_data['date']}\ntags: {json.dumps(json_data['tags'])}\nimage: \"/img/posts/{blog_folder_name}/0.png\"\nDescription: \"{json_data['description']}\"\n---\n\n"

        for idx, content_item in enumerate(json_data['content']):
            heading = content_item['heading']
            image_path = f"/img/posts/{blog_folder_name}/{idx+1}.png"
            content = content_item['content']
            image = content_item['image']
            if idx!=0:
                markdown_content += f"\n---\n# {heading}\n\n![{image} prompt]({image_path} \"{image}\")\n\n{content}\n\n\n"
            else:
                markdown_content += f"\n---\n# {heading}\n\n{content}\n\n\n"

        return markdown_content

    def save_markdown(self, markdown_content):
        output_path = os.path.join(self.folder_name, f"{os.path.basename(self.folder_name)}.md")

        with open(output_path, 'w') as file:
            file.write(markdown_content)



if __name__ == "__main__":
    blog_folder_paths = [
        "output/How_to_make_a_living_blogging",
    ]
    for folder_name in blog_folder_paths:
        converter = BlogConverter(folder_name)
        markdown_content = converter.convert_to_markdown()
        converter.save_markdown(markdown_content)
        print(f"Markdown file saved for {folder_name}")
