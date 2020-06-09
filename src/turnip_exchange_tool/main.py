import logging
import os

import turnip_exchange_tool.gateways.turnip_exchange as source
from turnip_exchange_tool.gateways.db import Sqlite3Db
from turnip_exchange_tool.models.island import Island

_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=_format, level=logging.DEBUG)

log = logging.getLogger(__name__)

here = os.path.abspath(os.path.dirname(__file__))


def main():
    # response = source.request_data(file_path=os.path.join(here, "./history/response.raw"))
    response = source.request_data()
    island_list = response["islands"]
    with Sqlite3Db() as database:
        database.create_table()
        islands = [Island(island_data) for island_data in island_list]
        database.insert_island_history(islands)
        log.debug(f"{len(islands)} islands processed")


if __name__ == "__main__":
    main()

""" TODO
Check success in request
Check success in json response
Incorporate $$time
Create object that stores

payload should not be static
"""

###
# success
# message
# islands
# $$time
