# 🎫 Zendesk Ticket Viewer 🎫

View a list of Zendesk tickets or choose an individual ticket to see details.

## ⚙️ Installation & Usage

This ticket viewer is built using Python 3.9.4 and Flask 2.0.1

### 👩‍💻 Getting Started
1. Clone this repository and navigate into the project directory
    ```bash
    git clone http
    ```
2. Create a **.env** file based on the .env.example with proper settings for your development environment.

    > Check [Zendesk's docs](https://support.zendesk.com/hc/en-us/articles/115002555167-Using-the-API-dashboard#enabling_password_or_token_access) for how to enable password access to your subdomain's API.
3. Install dependencies
    ```bash
    pipenv install
    ```
4. Run virtual environment shell
    ```bash
    pipenv shell
    ```

5. Run server
    ```bash
    pipenv run flask run
    ```
6. View ticket list or single ticket

    [Ticket List](http://127.0.0.1:5000/)

    [Single Ticket](http://127.0.0.1:5000/1)


### 👩‍🔬 Testing

Tests are built using Pytest. To run with simple output:
```python
pytest
```
To run with verbose output:
```python
pytest -v
```

### 🚀 Future Thoughts 
- I am currently paginating the entire API. It would be nice to break this out into pages on the frontend, since viewing 100+ tickets at a time could easily overwhelm users.
- Error handling is currently quite basic - custom error pages would improve user experience.
- The test suite could be expanded to handle additional cases.