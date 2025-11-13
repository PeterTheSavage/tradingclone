# Backend

This directory contains the Python/Flask backend for the TradingView clone.

## Running the Server

1.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the server:
    ```bash
    python app.py
    ```

The server will be available at `http://127.0.0.1:5001`.

## AI Integration

This backend includes an AI-powered market summary feature. To use it, you must configure the following environment variables:

-   `OPENAI_API_KEY`: Your API key for the OpenAI-compatible service.
-   `OPENAI_API_BASE_URL`: The base URL for the API endpoint (e.g., `https://api.openai.com/v1`). If not set, it defaults to the official OpenAI API.

These variables should be set in your environment before running the server.
