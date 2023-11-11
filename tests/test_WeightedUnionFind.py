from __future__ import annotations

import pytest

from libraries.WeightedUnionFind import WeightedUnionFind


@pytest.fixture()
def wuf():
    return WeightedUnionFind(5)


def test_weighted_union_find_initialize(wuf):
    assert wuf.length == 5


def test_weighted_union_find_merge(wuf):
    assert wuf.merge(1, 2, 3)
    assert not wuf.merge(1, 2, 4)  # Should return False due to conflicting weights
    assert wuf.is_union(1, 2)
    assert not wuf.is_union(1, 3)


def test_weighted_union_find_diff(wuf):
    assert wuf.diff(1, 1) == 0
    wuf.merge(1, 2, 3)
    assert wuf.diff(1, 2) == 3
    assert wuf.diff(2, 1) == -3
    assert wuf.diff(1, 3) == float("inf")
    wuf.merge(3, 4, 2)
    wuf.merge(1, 4, 5)
    assert wuf.diff(1, 3) == 3
    assert wuf.diff(2, 3) == 0


def test_weighted_union_find_is_union(wuf):
    assert not wuf.is_union(1, 2)
    wuf.merge(1, 2, 3)
    assert wuf.is_union(1, 2)
    assert not wuf.is_union(1, 3)


def test_weighted_union_find_get_size(wuf):
    wuf.merge(1, 2, 3)
    assert wuf.get_size(1) == 2
    assert wuf.get_size(2) == 2
    assert wuf.get_size(3) == 1


def test_weighted_union_find_get_unions(wuf):
    unions = wuf.get_unions()
    assert len(unions) == 5
    wuf.merge(1, 2, 3)
    wuf.merge(3, 4, 5)
    unions = wuf.get_unions()
    assert len(unions) == 3
    assert set(unions[0]) == {0}
    assert set(unions[1]) == {1, 2}
    assert set(unions[2]) == {3, 4}
    wuf.merge(0, 4, 6)
    wuf.merge(0, 1, 7)
    unions = wuf.get_unions()
    assert len(unions) == 1
    assert set(unions[0]) == {0, 1, 2, 3, 4}
