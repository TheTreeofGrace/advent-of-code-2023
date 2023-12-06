import pytest
import re

from clean_data import getFirstLastNum, concat

@pytest.fixture
def read_data():
    return open("Day1/word_number_example.txt", "r")

def test_day_one(read_data):
    lines = read_data.readlines()
    sumNoList = []

    for line in lines:
        numbers = getFirstLastNum(line)
        
        assert numbers != None
        assert len(numbers) != 0
        assert len(numbers) != 1
        assert len(numbers) <= 2
        cleanNumber = concat(numbers)
        assert cleanNumber != (int(numbers[0]) + int(numbers[-1]))
        sumNoList.append(int(cleanNumber))
    
    print("Totcal Calculations...")
    total = sum(sumNoList)
    assert total == 367
    print(total)
