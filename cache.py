from pymemcache.client.base import Client
import json

class Cache:
    @staticmethod
    def __getClient():
        return Client(('localhost', 11211), serializer=Cache.json_serializer, deserializer=Cache.json_deserializer)

    @staticmethod
    def set(key, value):
        Cache.__getClient().set(key, value)

    @staticmethod
    def get(key):
        return Cache.__getClient().get(key)

    @staticmethod
    def json_serializer(key, value):
        if type(value) == str:
            return value, 1
        return json.dumps(value), 2
    
    @staticmethod
    def json_deserializer(key, value, flags):
        if flags == 1:
            return value
        if flags == 2:
            return json.loads(value)
