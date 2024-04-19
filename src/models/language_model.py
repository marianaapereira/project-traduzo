from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        self.data = data

    def to_dict(self):
            name = self.data["name"]
            acronym = self.data["acronym"]

            return {
                "name": name,
                "acronym": acronym
            }
