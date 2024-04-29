import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history = HistoryModel.list_as_json()
    history_json = json.loads(history)

    history_1 = {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    }

    history_2 = {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    }

    assert (
        history_1["text_to_translate"] == history_json[0]["text_to_translate"]
    )

    assert (
        history_2["text_to_translate"] == history_json[1]["text_to_translate"]
    )
