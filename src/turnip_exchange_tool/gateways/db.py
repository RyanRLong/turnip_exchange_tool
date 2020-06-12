import logging
import os
import sqlite3

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS "islands_history" (
	"turnip_code"	TEXT NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"fruit"	TEXT NOT NULL,
	"turnip_price"	INTEGER NOT NULL,
	"hemisphere"	TEXT NOT NULL,
	"watchlist"	INTEGER NOT NULL,
	"fee"	INTEGER NOT NULL,
	"islander"	TEXT NOT NULL,
	"category"	TEXT NOT NULL,
	"island_time"	TEXT NOT NULL,
	"creation_time"	TEXT NOT NULL,
	"description"	TEXT,
	"queued"	TEXT NOT NULL,
	"patreon"	INTEGER NOT NULL,
	"discord_only"	INTEGER NOT NULL,
	"patreon_only"	INTEGER NOT NULL,
	"message_id"	TEXT NOT NULL,
	"rating"	TEXT,
	"rating_count"	TEXT,
	"live"	INTEGER NOT NULL,
	"thumbsupt"	INTEGER NOT NULL,
	"thumbsdown"	INTEGER NOT NULL,
	"heart"	INTEGER NOT NULL,
	"clown"	INTEGER NOT NULL,
	"poop"	INTEGER NOT NULL,
	"island_score"	TEXT,
	"date_time" TEXT NOT NULL,
	PRIMARY KEY("turnip_code")
)
"""

HERE = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(HERE, "../database")
DB_FULL_PATH = os.path.join(DB_PATH, "db.sqlite3")
log = logging.getLogger(__name__)


class Sqlite3Db:

    def __init__(self):
        log.debug(f"database path is {DB_FULL_PATH}")
        create_database_directory()
        self.connection = sqlite3.connect(DB_FULL_PATH)
        self.cursor = None

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

    def create_table(self, sql=CREATE_TABLE):
        c = self.cursor
        c.execute(sql)
        self.connection.commit()

    def insert_island_history(self, islands, table="islands_history"):
        c = self.cursor
        formatted = []
        for island in islands:
            formatted.append(island.insertion_format())
        c.executemany(
            f"INSERT OR IGNORE INTO {table} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", formatted
        )


def create_database_directory():
    if not os.path.exists(DB_PATH):
        log.debug(f"creating database path {DB_PATH}")
        os.mkdir(DB_PATH)
