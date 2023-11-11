import pytest

from libraries.UnionFind import UnionFind


@pytest.fixture()
def uf():
    return UnionFind(5)


def test_union_find_initialize(uf):
    assert uf.length == 5


def test_union_find_merge(uf):
    uf.merge(0, 1)
    assert uf.is_union(0, 1)
    assert uf.get_size(0) == 2
    assert uf.get_size(1) == 2
    assert uf.get_size(2) == 1

    uf.merge(1, 2)
    assert uf.get_size(0) == 3
    uf.merge(0, 2)  # 0, 2 are already merged. This should do nothing.
    assert uf.get_size(0) == 3
    uf.merge(3, 4)
    assert uf.get_size(4) == 2
    uf.merge(4, 0)
    assert uf.get_size(3) == 5


def test_union_find_is_union(uf):
    uf.merge(0, 1)
    assert uf.is_union(0, 1)
    assert not uf.is_union(0, 2)


def test_union_find_get_size(uf):
    uf.merge(0, 1)
    uf.merge(2, 3)
    assert uf.get_size(0) == 2
    assert uf.get_size(2) == 2


def test_union_find_get_unions(uf):
    uf.merge(0, 1)
    uf.merge(2, 3)
    unions = uf.get_unions()
    assert len(unions) == 3
    assert set(unions[0]) == {0, 1}
    assert set(unions[1]) == {2, 3}
    assert set(unions[2]) == {4}
