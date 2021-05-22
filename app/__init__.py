import requests
import base64
from flask import Flask, render_template
from .config import Configuration

app = Flask(__name__)

email = Configuration.email
password = Configuration.password
encoded_data = base64.b64encode(
    bytes(f'{email}:{password}', 'utf-8')).decode('utf-8')
auth_header = f'Basic {encoded_data}'


@app.route('/', methods=['GET'])
def hello_tickets():
    res = requests.get('https://jemcodes.zendesk.com/api/v2/tickets/',
                       headers={'Authorization': auth_header})
    if res.status_code == requests.codes.ok:
        res_json = res.json()
        return render_template('ticket_list.html', res_json=res_json)
    else:
        return 'Cue the sad trombone sounds - something went wrong!'


@app.route('/<ticket_id>', methods=['GET'])
def single_ticket(ticket_id):
    res = requests.get(
        f'https://jemcodes.zendesk.com/api/v2/tickets/{ticket_id}',
        headers={'Authorization': auth_header})
    if res.status_code == requests.codes.ok:
        res_json = res.json()
        return render_template('single_ticket.html', res_json=res_json)
    else:
        return 'Uh oh! Looks like a classic Dinosaur Ate My Ticket situation!'


if __name__ == '__main__':
    app.run(debug=True)
