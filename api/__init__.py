import os

from anime_list_service import create_app
from db.database_client import DB

app = create_app(os.environ.get('CONFIG_CLASS_NAME', None))
db = DB(app.config)