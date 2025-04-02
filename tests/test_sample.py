import pytest


@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}


def test_sample_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30


def add(a, b):
    return a+b


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected
