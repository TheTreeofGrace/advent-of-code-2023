import pytest

from Day1 import CleanData

@pytest.fixture
def read_data():
    return CleanData()

def test_day_one(read_data):
    data = read_data.read()
    print(data)
    assert data != null
