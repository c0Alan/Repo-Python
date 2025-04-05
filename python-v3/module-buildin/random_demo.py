"""
random 模块示例
"""

from random import choice
from random import randint

### 随机选择 ###
def _demo01():
    x = choice([1, 2, 3, 4, 5])
    print(x)
    
""" randint """
def _demo02():
    x = randint(1, 10)
    print(x)

_demo02()

