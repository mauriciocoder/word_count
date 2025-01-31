import pytest

from src.api.utils import word_count


def test_word_count_exceptions():
    with pytest.raises(ValueError):
        word_count(1.23)
    with pytest.raises(ValueError):
        word_count(123)
    with pytest.raises(ValueError):
        word_count(None)


def test_word_count():
    assert word_count("") == 0
    assert word_count("hello world") == 2

    assert word_count("hello-world") == 1
    assert word_count("hello_world") == 1
    assert word_count("hello world!") == 2

    assert word_count("hello\nworld") == 2
    assert word_count("hello\tworld") == 2
    assert word_count("hello\n\nworld") == 2
    assert word_count("hello\n\tworld") == 2
    assert word_count("\nhello\tworld\n") == 2

    # Punctuation marks are not considered words
    # Even if we consider apostrophes and hyphens
    assert word_count("!@#") == 0
    assert word_count("!@-#") == 0

    # Numbers included
    assert word_count("123") == 1
    assert word_count("123-456") == 1
    assert word_count("123@456") == 2
    assert word_count("h3ll0") == 1
    assert word_count("hello@world") == 2

    # Apostrophes included
    assert word_count("don't") == 1
    assert word_count("don't know") == 2
    assert word_count("don't know, how") == 3

    # Long sentence
    assert word_count("hello world. hello world. hello world.") == 6
    assert (
        word_count("There is nothing either good or bad, but thinking makes it so")
        == 12
    )
    assert (
        word_count(
            "This above all: to thine own self be true, And it must follow, "
            "as the night the day, Thou canst not then be false to any man"
        )
        == 27
    )
