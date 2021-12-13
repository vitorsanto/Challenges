import json


class SportsService:

    @staticmethod
    def create_sports(payload):
        return json.dumps(payload)

    @staticmethod
    def update_sport(payload):
        return json.dumps(payload)

    @staticmethod
    def list_sport(payload):
        return json.dumps(payload)
