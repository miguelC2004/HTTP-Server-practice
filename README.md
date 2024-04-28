# Simple HTTP Server in Python

This is a simple web server made with Python using basic classes from the standard library for handling web requests. The server follows good design practices like separating different parts and keeping them loosely connected.

## Project Structure

The project is divided into different parts:

- `server/app.py`: Sets up and starts the web server.
- `router/router.py`: Directs web requests to the right places.
- `controllers/`: Holds functions that manage different pages.
- `utils/config.py`: Loads settings from a .env file.

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
