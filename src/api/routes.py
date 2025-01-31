from flasgger import swag_from
from flask import (
    abort,
    Request,
    Response,
    Blueprint,
    current_app as app,
    request,
    jsonify,
)

bp = Blueprint("api", __name__)

def validate_sentences(sentences: list[str]):
    if not isinstance(sentences, list):
        raise ValueError("sentences must be a list")
    if not sentences:
        raise ValueError("sentences cannot be an empty list")
    if not all(isinstance(sentence, str) for sentence in sentences):
        raise ValueError("All sentences must be strings")


@bp.route("/count_words", methods=["POST"])
@swag_from("swag/count_words_swag.yml")
def count_words() -> Response:
    from .utils import word_count
    sentences = request.json
    try:
        validate_sentences(sentences)
    except ValueError as e:
        return jsonify({"error": "Invalid input data", "details": str(e)}), 400
    word_counts = []
    for sentence in sentences:
        count = word_count(sentence)
        app.logger.info(
            f"Sentence: {sentence}, Word Count: {count}"
        )
        word_counts.append(count)
    return jsonify(word_counts), 200
