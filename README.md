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

The server will start listening on the specified port (default is 8000). You can then access the following routes:

- `/`: Home page.
- `/about`: About page.

## Dependencies

- `python-dotenv`: For loading environment variables from `.env` files.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or features you'd like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
