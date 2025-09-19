# Study Chatbot

A simple Chainlit-based echo chatbot that responds with the same message it receives.

## Features

- Echoes back any text message sent to it.
- Built with Chainlit for conversational AI applications.

## Installation

This project uses `uv` for dependency management. Ensure you have `uv` installed.

1. Clone or navigate to the project directory.
2. Install dependencies:
   ```bash
   uv sync
   ```



## Running the Application

To run the Chainlit app locally:

```bash
uv run chainlit run src/study_chatbot/app.py
```

This will start the Chainlit server, and you can interact with the chatbot via the web interface at `http://localhost:8000`.

### Custom UI and Styling

This project includes comprehensive UI customization following Chainlit's official documentation:

- **`.chainlit/config.toml`**: Main configuration file with UI settings, dark theme, and custom CSS reference
- **`public/stylesheet.css`**: Custom CSS stylesheet with modern dark theme, gradients, and animations
- **`public/favicon.png`**: Custom favicon served from the public directory

The styling includes:
- Dark gradient background theme
- Custom message bubbles with animations
- Improved input styling and buttons
- Custom scrollbars and typography
- Visual indicator to confirm CSS is loading

Chainlit automatically serves files from the `public/` directory, making them accessible via `/public/filename`.

## Usage

Send any text message to the chatbot, and it will echo the same text back to you.

## Development

- Python version: >=3.13
- Main dependencies: Chainlit, OpenAI Agents, python-dotenv, Rich

### Running Tests

Install test dependencies and run the test suite:

```bash
uv sync --extra test
uv run pytest tests/ -v
```

### Environment Variables

Copy `.env.example` to `.env` and customize settings:

```bash
cp .env.example .env
```

Available environment variables:
- `CHAINLIT_HOST`: Server bind address (default: 0.0.0.0)
- `CHAINLIT_PORT`: Server port (default: 8000)
- `CHAINLIT_THEME`: UI theme - light/dark/system (default: system)
- `APP_NAME`: Application display name

## License

Add your license here.
