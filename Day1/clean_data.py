import re

num_dict = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

def doubleNumber(num):
  doubled = [num[0], num[0]]
  return doubled

def lastFirst(nums):
  lastf = [nums[0], nums[-1]]
  return lastf

def concat(digits):
  return digits[0] + digits[-1]

def process_numbers(numbers):
  if(len(numbers) == 1):
    return doubleNumber(numbers)
  if(len(numbers) > 2):
    return lastFirst(numbers)
  return numbers

def parse_numbers(numbers):
  for i, val in enumerate(numbers):
    if(len(val) >=2):
      numbers[i] = num_dict[val]
  return numbers

def getFirstLastNum(line):
  numbers = re.findall(r"(?=(\d|(one|two|three|four|five|six|seven|eight|nine)))", line.strip())
  allNums = []
  for n in numbers:
    allNums.append(n[0])
  parsedNums = parse_numbers(allNums)
  return process_numbers(parsedNums)
  