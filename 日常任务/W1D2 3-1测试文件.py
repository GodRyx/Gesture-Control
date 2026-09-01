# 练习3-1 计算列表的最大嵌套深度
def list_depth(lst):
    """
    计算列表的最大嵌套深度
    参数 lst: 可能包含嵌套列表的列表
    返回: 最大嵌套深度（整数）
    """
    if not isinstance(lst, list):
        return 0

    max_depth = 1  # 当前列表本身算一层

    for item in lst:
        if isinstance(item, list):
            # 递归计算子列表的深度，加上当前这一层
            depth = 1 + list_depth(item)
            if depth > max_depth:
                max_depth = depth

    return max_depth

import unittest
class TestListDepth(unittest.TestCase):

    def test_flat_list(self):
        """测试普通一维列表，深度应为1"""
        result = list_depth([1, 2, 3])
        self.assertEqual(result, 1)

    def test_nested_one_level(self):
        """测试一层嵌套列表，深度应为2"""
        result = list_depth([[1], [2, 3]])
        self.assertEqual(result, 2)

    def test_deeply_nested(self):
        """测试多层嵌套列表，深度应为3"""
        result = list_depth([[1], [2, [3]]])
        self.assertEqual(result, 3)

    def test_empty_list(self):
        """测试空列表，深度应为1"""
        result = list_depth([])
        self.assertEqual(result, 1)

    def test_not_a_list(self):
        """测试传入的不是列表，应返回0"""
        result = list_depth("hello")
        self.assertEqual(result, 0)


    def test_complex_nesting(self):
        """测试复杂嵌套结构，深度应为4"""
        result = list_depth([1, [2, [3, [4]]], 5])
        self.assertEqual(result, 4)

    def test_mixed_elements(self):
        """测试混合元素（数字、字符串、列表混合），深度应为2"""
        result = list_depth([1, "a", [2, 3], [4]])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()