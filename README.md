# Static Site Generator

This is a project developed as part of the [Boot.dev](https://www.boot.dev) backend engineering curriculum. It is a tool designed to take content (like Markdown) and generate a full static HTML website. Not all of the code here is my own. Some has been provided by the boot.dev course and I have used their resources to help me make this project.

## Features

- **Markdown to HTML**: Converts your `.md` files into HTML pages using a shared template.
- **Static Asset Copying**: Copies images, CSS, and other files straight into the output directory.
- **Modular Design**: Each part of the pipeline (parsing, rendering, copying) is kept separate and easy to extend.

### Prerequisites
- Python 3.10 or higher

### Generate the Site

To build for local development and serve at `http://localhost:8888/`, run:

./main.sh

To build for production (GitHub Pages) into the /docs directory, run:

./build.sh

### Development
The project includes a suite of unit tests to ensure the Markdown parsing logic remains robust. Run them with:

./test.sh

