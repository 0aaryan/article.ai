# Article.ai

Article.ai is a versatile project that empowers you to generate blog content, whether you have a specific topic in mind or a collection of URLs to explore. Leveraging OpenAI's language models, the project provides functionality to convert topics into articles, articles into articles (with summarization), and extract URLs from a given source.

## Features

- **Generate Blog Content:**
  - From URLs: Input a list of URLs, and the system will generate detailed blog content.
  - From Topics: Specify a topic, and the system will craft an article around it.

- **Summarization:**
  - The ability to summarize existing articles, extracting key information and generating concise summaries.

- **URL Extraction:**
  - Utilize the `newspaper` library to extract URLs from a given source, aiding in content discovery.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/0aaryan/article.ai.git
   ```

2. Navigate to the project directory:

   ```bash
   cd article.ai
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. **Extract URLs:**
   - Enter the source URL in the "Source URL" text area.
   - Click on "Extract URLs" to discover and display a list of article URLs.

3. **Generate Blogs:**
   - Enter URLs or topics in the respective text areas, separated by newlines.
   - Click on "Generate Blogs" to produce detailed blog content.

4. **Resize Images:**
   - Click on "Resize Images" to standardize image dimensions.

5. **Convert to Markdown:**
   - Click on "Convert to Markdown" to convert blogs to Markdown format.
   - Generated Markdown files will be displayed, and you can click on them to view or download.

6. **Clear Temporary Files:**
   - Optional: Click on "Clear Temporary Files" to remove temporary files.

## Folder Structure

- `articleai/`: Python package containing blog and image generators.
- `generators/`: Python modules for blog and image generation.
- `static/output_template/`: Output template for blog content.
- `output/`: Generated blogs and images.
- `app.py`: Streamlit app for interaction.
- `requirements.txt`: Project dependencies.
- `readme.md`: Project documentation.

## Contributors

- [Your GitHub Username](https://github.com/0aaryan)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Please replace `"your_api_key_here"` in the `.env` example with your actual OpenAI API key.
