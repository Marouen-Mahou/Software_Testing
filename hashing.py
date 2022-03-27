from flask_restful import Resource, reqparse
import hashlib

encode_post_args = reqparse.RequestParser()
encode_post_args.add_argument("message", type=str, help="Message to be encoded")


class HashMD5(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        hash_object = hashlib.md5(bytes(message, encoding='utf-8'))
        return hash_object.hexdigest()


class HashSHA1(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        hash_object = hashlib.sha1(bytes(message, encoding='utf-8'))
        return hash_object.hexdigest()


class HashSHA256(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        hash_object = hashlib.sha256(bytes(message, encoding='utf-8'))
        return hash_object.hexdigest()
