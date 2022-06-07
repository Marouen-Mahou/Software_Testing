import sqlite3
from flask import current_app

class DAO:
    def __init__(self):


    def getAllAttacksData(self):
        db_connection = current_app.config["DATABASE_CON"]

        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()

        cursor.execute(
        "SELECT * FROM attacks"
        )

        data = cursor.fetchall()
        attacks = []

        for d in data:
            dict_data = dict(d)
            attacks.append({"name": dict_data["name"], "description": dict_data["description"]})

        return attacks

