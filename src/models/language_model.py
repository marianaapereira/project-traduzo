from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        self.data = data

    def to_dict(self):
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"]
        }

    def list_dicts():
        languages_collection = db.languages.find()
        languages = []

        for language in languages_collection:
            languages.append(language)

        return languages
