def test_one_plus_one():
    assert 1 + 1 == 2


def test_compare_words():
    username = "alex"
    provided_username = "alex"

    assert username == provided_username


def test_compare_words_failed():
    username = "alex"
    provided_username = "username"

    assert username == provided_username

