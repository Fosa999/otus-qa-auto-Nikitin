# pylint: disable=missing-module-docstring
nums = [10, 15, 20]
total = sum(nums)
QQ = len(nums)
# Не знаю почему, но была ошибка Constant name
# "Quantity" doesn't conform to UPPER_CASE naming style (invalid-name)
average = total / QQ   # из за этого пришлось переименовать переменную count-QQ
result = average
print("The average, is:", result)
