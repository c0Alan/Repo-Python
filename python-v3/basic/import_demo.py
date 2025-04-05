""" import示例 """

""" 导入模块 pizza 中的函数 make_pizza() """
import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

import pkg.pizza as pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')