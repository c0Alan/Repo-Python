"""
matplotlib, Python 的 2D绘图库
参考: https://blog.csdn.net/weixin_46264660/article/details/140914998
"""

import matplotlib.pyplot as plt



""" 直线图，将(0,1)点和(2,4)连起来 """
def _demo01():
    plt.plot([0, 2], [1, 4])
    plt.show()


""" 折线图 """
def _demo02():
    x = [1, 2, 3, 4, 5]
    squares = [1, 14, 39, 16, 25]
    plt.plot(x, squares)
    plt.show()


""" 设置标签文字和线条粗细 """
def _demo03():
    datas = [1, 2, 3, 4, 5]
    squares = [1, 14, 39, 16, 25]
    plt.plot(datas, squares, linewidth=5)  # 设置线条宽度
    # 设置图标标题，并在坐标轴上添加标签
    plt.title('Numbers', fontsize=24)
    plt.xlabel('datas', fontsize=14)
    plt.ylabel('squares', fontsize=14)
    plt.show()


_demo03()
