from flask_restful import Resource, reqparse
from flask import request
import hashlib

encode_post_args = reqparse.RequestParser()
encode_post_args.add_argument("message", type=str, help="Message to be encoded")


class CrackMD5(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        lines= request.json["lines"]
        for line in lines:
            hash_object = hashlib.md5(bytes(line.strip(), encoding='utf-8'))
            if message == hash_object.hexdigest():
                return line
        return "Hash not found"


class CrackSHA1(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        lines = request.json["lines"]
        for line in lines:
            hash_object = hashlib.sha1(bytes(line.strip(), encoding='utf-8'))
            if message == hash_object.hexdigest():
                return line
        return "Hash not found"


class CrackSHA256(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        lines= request.json["lines"]
        for line in lines:
            hash_object = hashlib.sha256(bytes(line.strip(), encoding='utf-8'))
            if message == hash_object.hexdigest():
                return line
        return "Hash not found"
