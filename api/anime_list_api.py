from api import app
from api import db
from flask import Blueprint

animes_api = Blueprint('animes_api', __name__)


@animes_api.route('/get_user')
def test():
    d = db.db()
    print("DDDDDD")
    return f'ala ma kota {d.animes.count()} dsdsdsdsds'