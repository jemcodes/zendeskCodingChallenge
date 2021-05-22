# Zendesk Ticket Viewer

View a list of Zendesk tickets or choose an individual ticket to see details.

## Installation & Usage

This ticket view is built using Python 3.9.4 and Flask 2.0.1

### Getting Started
1. Clone this repository
    ```bash
    git clone 
    ```
2. Install dependencies
    ```bash
    pipenv install --python 3.9.4
    ```
    ```bash
    pipenv install flask pytest python-dotenv requests responses
    ```
3. Run virtual environment shell
    ```bash
    pipenv shell
    ```
4. Create a **.env** file based on the example with proper settings for your development environment.

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