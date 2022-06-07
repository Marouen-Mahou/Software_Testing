import sqlite3
from functions import All_Attacks

from flask import current_app

from flask_restful import Resource, reqparse



class Attacks(Resource):

    def get(self):
        attacks = All_Attacks()

        return {
            "data": attacks
        }

