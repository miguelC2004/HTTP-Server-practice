# Simple HTTP Server in Python

This is a simple HTTP server implemented in Python using basic HTTP handling classes provided by the standard library. The server follows good design practices such as separation of concerns and low coupling.

## Project Structure

The project is organized into several modules:

- `server/app.py`: Initializes and runs the HTTP server.
- `router/router.py`: Handles routing of HTTP requests to appropriate controllers.
- `controllers/`: Contains controller functions to handle different routes.
- `utils/config.py`: Loads configuration settings from a `.env` file.

## Usage
```bash
pipenv run python main.py
```

