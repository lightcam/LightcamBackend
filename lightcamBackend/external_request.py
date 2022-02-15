import requests
from django.conf import settings


class ExternalRequest:
    @staticmethod
    def get_workflow():
        return requests.get('https://drive.google.com/uc?id=' + settings.WORKFLOW_ID)

    @staticmethod
    def get_timeline():
        return requests.get(
            "https://docs.google.com/spreadsheets/d/" + settings.TIMELINE_ID + "/export?format=csv&gid=0")

    @staticmethod
    def get_dictionary():
        return requests.get(
            "https://docs.google.com/spreadsheets/d/" + settings.DICTIONARY_ID + "/export?format=csv&gid=0")

    @staticmethod
    def get_resources():
        return requests.get(
            "https://docs.google.com/spreadsheets/d/" + settings.RESOURCES_ID + "/export?format=csv&gid=0")
