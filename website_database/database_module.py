import sqlite3
from datetime import datetime


class WebsiteDB:
    def __init__(self):
        try:
            self.sqlite_connection = sqlite3\
                .connect('./website_database/website_data.db')
        except sqlite3.OperationalError:
            self.sqlite_connection = sqlite3\
                .connect('/website_data.db')
        self.cursor = self.sqlite_connection.cursor()

    def create(self):
        self.cursor.execute('''CREATE TABLE website_info(
                            id TEXT NOT NULL,
                            visit datetime NOT NULL,
                            browser TEXT NOT NULL,
                            platform TEXT NOT NULL,
                            referer TEXT NOT NULL);''')

    def close(self):
        self.cursor.close()
        self.sqlite_connection.close()
        return True

    def set_value(self, user_id, browser, platform, ref):
        sqlite_insert_query = """
        INSERT INTO website_info (id, visit, browser, platform, referer)
        VALUES (?, ?, ?, ?, ?) """
        self.cursor.execute(
            sqlite_insert_query,
            (user_id, str(datetime.now())[:19], browser, platform, ref)
        )
        self.sqlite_connection.commit()

    def get_values(self):
        sqlite_select_query = \
            """SELECT * from website_info"""
        self.cursor.execute(sqlite_select_query)
        return self.cursor.fetchall()
