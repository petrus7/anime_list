from flask import Flask

from src.database_client import DB
from src.anime_list_service import create_app



app = create_app('DevelopmentConfig')
db = DB().db()
@app.route('/')
def test():
    return f'ala ma kota {db.animes.count()} dsdsdsdsds'


# if __name__ == '__main__':
#     app.run()
