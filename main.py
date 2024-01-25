import threading

# import "packages" from flask
from flask import render_template, jsonify # import render_template from "public" flask libraries
from flask.cli import AppGroup
# import "packages" from "this" project
from __init__ import app, db  # Definitions initialization
from model.users import initUsers
from model.players import initPlayers

from flask_cors import CORS
# setup APIs
from api.user import user_api # Blueprint import api definition
from api.player import player_api
# database migrations
from api.memes import memes_api
from model.users import initUsers
from model.players import initPlayers

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(user_api) # register api routes
app.register_blueprint(player_api)
app.register_blueprint(app_projects) # register app pages
app.register_blueprint(memes_api)

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")
@app.route('/api/users/create', methods=['OPTIONS'])
def handle_preflight():
    response = jsonify({'message': 'Preflight request received'})
    response.headers.add('Access-Control-Allow-Origin', 'https://imaad08.github.io', 'http://127.0.0.1:4100')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response, 200

@app.route('/api/users/', methods=['POST'])
def handle_more_preflight():
    response = jsonify({'message': 'Preflight request received'})
    response.headers.add('Access-Control-Allow-Origin', 'https://imaad08.github.io', 'http://127.0.0.1:4100')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response, 200
# Create an AppGroup for custom commands
custom_cli = AppGroup('custom', help='Custom commands')

# Define a command to generate data
@custom_cli.command('generate_data')
def generate_data():
    initUsers()
    initPlayers()

# Register the custom command group with the Flask application
app.cli.add_command(custom_cli)
        
# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8762")
