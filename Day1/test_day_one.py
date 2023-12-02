import pytest

from clean_data import CleanData

@pytest.fixture
def read_data():
    return open("Day1/day1Data.txt").read()

def test_day_one(read_data):
    data = read_data
    print(data)
    assert data != None
