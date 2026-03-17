# Static Site Generator

This is a project developed as part of the [Boot.dev](https://www.boot.dev) backend engineering curriculum. It is a tool designed to take content (like Markdown) and generate a full static HTML website. Not all of the code here is my own. Some has been provided by the boot.dev course and I have used their resources to help me make this project.

## Features

- Converts text-based content into HTML.
- Handles directory mirroring for static assets.
- Built entirely in Python.

## How to Run

Currently, the project contains a static `public` directory. To view the site locally:

1. Navigate to the `public` directory:
   cd public
2. Start the Python HTTP server:
    python3 -m http.server 8888
3. Open your browser to: 
    http://localhost:8888
