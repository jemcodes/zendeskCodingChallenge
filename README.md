# Zendesk Ticket Viewer

View a list of Zendesk tickets or choose an individual ticket to see details.

## Installation & Usage

This ticket viewer is built using Python 3.9.4 and Flask 2.0.1

### Getting Started
1. Clone this repository
    ```bash
    git clone 
    ```
2. Create a **.env** file based on the .env.example with proper settings for your development environment.
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


### Testing

Tests are built using Pytest. To run with simple output:
```python
pytest
```
To run with verbose output:
```python
pytest -v
```