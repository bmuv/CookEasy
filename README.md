# CookEasy

CookEasy is a web application that helps users discover delicious recipes based on the ingredients they have at home. Users can easily manage their kitchen inventory, find recipes that match their available ingredients, and get meal suggestions. The application integrates with the Spoonacular API to provide a vast collection of recipes. Built with Flask, SQLAlchemy, and Flask-Login, CookEasy offers a modern, user-friendly interface with functionalities for user registration, login, and inventory management.

## Features

- **Manage Inventory**: Add, edit, and delete items in your kitchen inventory.
- **Recipe Suggestions**: Find recipes based on the ingredients you have.
- **User Authentication**: Secure user registration and login with Flask-Login.
- **API Integration**: Integration with Spoonacular API for a wide range of recipes.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/bmuv/CookEasy.git
    cd CookEasy
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Run the application:**
    ```bash
    export FLASK_APP=run.py  # On Windows use `set FLASK_APP=run.py`
    flask run
    ```

## Usage

1. **Register**: Create a new user account.
2. **Login**: Log in to your account.
3. **Manage Inventory**: Add ingredients to your inventory.
4. **Get Recipes**: Find recipes based on your inventory.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
