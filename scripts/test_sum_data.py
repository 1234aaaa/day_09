import pytest

from base.utils import Utils


def get_data():

    data =Utils.get_yaml_data("sum_data.yml")
    result_list = []
    for i in data.values():
        result_list.append((i.get("a"), i.get("b"), i.get("c")))
    print(result_list)
    return result_list


class TestSum:

    @pytest.mark.parametrize("a,b,c", get_data())
    def test_sum(self, a, b, c):
        """判断两个数之和 等于 第三个数"""
        print("\n{}+{}={}".format(a, b, c))
        assert a + b == c
