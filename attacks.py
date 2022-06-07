from functions import all_attacks

from flask_restful import Resource, reqparse


class Attacks(Resource):
    def get(self):
        attacks = all_attacks()

        return {
            "data": attacks
        }
