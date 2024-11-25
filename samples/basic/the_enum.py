from enum import Enum


# 枚举
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.name, Color.RED.value)

for color in Color:
    print(color)
