from flask import Flask, request, make_response
from website_database import WebsiteDB
from server_module import parse_browser, parse_platform


app = Flask(__name__)


@app.route('/<client_id>')
def index(client_id):
    user_id = get_user_id(client_id)
    fill_db_values(user_id, request)
    return setup_response(user_id)


def fill_db_values(user_id, request):
    WebsiteDB().set_value(f'user{user_id}',
                          parse_browser(request.user_agent.string),
                          parse_platform(request.user_agent.string),
                          setup_referrer(request))


def setup_referrer(req):
    return req.referrer is None if "DIRECT_CONNECTION" else req.referrer


def setup_response(id):
    response = make_response(str(id))
    response.headers = {"Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Credentials": True}
    return response


def get_user_id(current_id):
    if current_id == '0':
        return len(set(list(map(
            lambda d: d[0], WebsiteDB().get_values())))) + 1
    return current_id


def run():
    app.run(debug=True, host='0.0.0.0', port=8000)


if __name__ == "__main__":
    run()
