import pytest

from libraries.FenwickTree import FenwickTree


@pytest.fixture()
def fenwick_tree():
    # Fixture to create a FenwickTree instance with initial values for testing
    return FenwickTree(5, [1, 2, 3, 4, 5])


def test_init(fenwick_tree):
    assert fenwick_tree.data == [1, 3, 3, 10, 5]


# 要素a[idx]にxを加算する
def test_add(fenwick_tree):
    fenwick_tree.add(2, 2)
    assert fenwick_tree.data == [1, 3, 5, 12, 5]


# 要素a[idx]をxに更新する
def test_update(fenwick_tree):
    fenwick_tree.update(3, 10)
    assert fenwick_tree.data == [1, 3, 3, 16, 5]


# 半開区間[0:r)の区間和を返す。rは含まない。
def test_sum(fenwick_tree):
    assert fenwick_tree.sum(1) == 1
    assert fenwick_tree.sum(2) == 3
    assert fenwick_tree.sum(3) == 6
    assert fenwick_tree.sum(4) == 10
    assert fenwick_tree.sum(5) == 15


# 半開区間[l:r)の区間和を返す。lは含む、rは含まない。
def test_range_sum(fenwick_tree):
    assert fenwick_tree.range_sum(1, 4) == 9  # 2+3+4
    assert fenwick_tree.range_sum(2, 4) == 7  # 3+4
    assert fenwick_tree.range_sum(3, 5) == 9  # 4+5


# 累積和がx以上となる最小のidxとその直前の累積和totalを返す。
def test_lower_bound(fenwick_tree):
    assert fenwick_tree.lower_bound(8) == (3, 6)
    assert fenwick_tree.lower_bound(15) == (4, 10)
    # 配列全体の累積和 < xの場合、idx=配列の長さ、total=配列全体の和を返す。
    assert fenwick_tree.lower_bound(20) == (5, 15)
    assert fenwick_tree.lower_bound(25) == (5, 15)
