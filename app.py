from flask import Flask
from sql.Sqldb import session
from blueprints import columnEndpoint, jsonEndpoint

app = Flask(__name__)

app.register_blueprint(columnEndpoint.column_endpoint)
app.register_blueprint(jsonEndpoint.json_endpoint)

@app.before_request
def beforeRequest():
    pass

@app.teardown_appcontext
def cleanup(resp_or_exc):
    session.remove()


if __name__ =="__main__":
    
    app.run(debug=True)