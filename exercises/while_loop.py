"""
练习: while循环

描述：
在数字列表中查找第一个偶数。

请补全下面的函数，使用while循环在数字列表中查找并返回第一个偶数。
如果列表中没有偶数，则返回None。
"""

def find_first_even(numbers):
    """
    在数字列表中查找第一个偶数

    参数:
    - numbers: 整数列表

    返回:
    - 列表中的第一个偶数，如果没有偶数则返回None
    """
    # 初始化索引
    index = 0
    # 当索引小于列表长度时，持续循环
    while index < len(numbers):
        # 检查当前元素是否为偶数
        if numbers[index] % 2 == 0:
            return numbers[index]
        # 索引加1
        index += 1
    # 若列表中没有偶数，返回None
    return None
