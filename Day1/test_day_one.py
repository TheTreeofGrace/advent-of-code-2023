import pytest
import re

from clean_data import getFirstLastNum, concat

@pytest.fixture
def read_data():
    return open("Day1/day1Data.txt", "r")

def first(line):
    m = re.search(r"\d", line)
    return re.search(r"\d", line).group()

def test_day_one(read_data):
    lines = read_data.readlines()
    sumNoList = []

    for line in lines:
        numbers = getFirstLastNum(line)
        
        assert numbers != None
        assert len(numbers) != 0
        assert len(numbers) != 1
        assert len(numbers) <= 2
        assert numbers[0] == first(line)
        cleanNumber = concat(numbers)
        assert cleanNumber != (int(numbers[0]) + int(numbers[-1]))
        sumNoList.append(int(cleanNumber))
    
    total = sum(sumNoList)
    assert total != 0
