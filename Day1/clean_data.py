import re

def doubleNumber(num):
  doubled = [num[0], num[0]]
  return doubled

def lastFirst(nums):
  lastf = [nums[0], nums[-1]]
  return lastf

def concat(digits):
  return digits[0] + digits[-1]

def getFirstLastNum(line):
  numbers = re.findall(r"\d", line)
  if(len(numbers) == 1):
    return doubleNumber(numbers)
  if(len(numbers) > 2):
    return lastFirst(numbers)
  return numbers
  