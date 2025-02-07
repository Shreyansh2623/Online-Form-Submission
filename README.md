# Online Form

## Overview
This project is structured to keep all files organized and easy to manage. The application follows a structured directory layout where template files and static files are stored in separate folders.

## Project Structure
```
project_root/
│-- app.py
│-- /templates
│   │-- Form.html
│   │-- Result.html
│-- /static
    │-- style.css
```

## Folder Details
- **Templates Folder (`/templates`)**:
  - This folder contains all HTML files required for the application.
  - Files included:
    - `Form.html` (The form interface for user input)
    - `Result.html` (Displays the processed result from user input)

- **Static Folder (`/static`)**:
  - This folder contains all static assets such as CSS files.
  - Files included:
    - `style.css` (Defines the styling for the web pages)

## How to Run the Project
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repo
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Dependencies
Ensure you have Python installed along with Flask. If not, install it using:
```sh
pip install flask
```

## Contributing
Feel free to contribute by creating a pull request. Make sure to follow the project's structure.

## License
This project is licensed under the MIT License.

