import asyncio
import os
from threading import Thread

from anime_list_service import create_app
from db.database_client import DB
import pybreaker



app = create_app(os.environ.get('CONFIG_CLASS_NAME', None))
db = DB(app.config)
request_number = 0
user_list_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)

# def start_worker(loop):
#     asyncio.set_event_loop(loop)
#     try:
#         loop.run_forever()
#     finally:
#         loop.close()
#
# worker_loop = asyncio.new_event_loop()
# worker = Thread(target=start_worker, args=(worker_loop,))


class DBListener(pybreaker.CircuitBreakerListener):

    def before_call(self, cb, func, *args, **kwargs):
        print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")

    def state_change(self, cb, old_state, new_state):
        print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

    def failure(self, cb, exc):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    def success(self, cb):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

user_list_breaker.add_listeners(DBListener())