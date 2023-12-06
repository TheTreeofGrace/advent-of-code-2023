import pytest
from calculate_fixed_game import CalcPossible
import re

@pytest.fixture
def read_data():
    return open("Day2/example_input_task_1.txt", "r")

def test_day_two(read_data):
    lines = read_data.readlines()
    sum_total = []

    for line in lines: 
        calc = CalcPossible()
        sum_total.append(calc.calculate_possible(line.strip()))
    
    print("Total Games...")
    print(sum_total)
    total = sum(sum_total)
    print(total)
    assert total == 18

