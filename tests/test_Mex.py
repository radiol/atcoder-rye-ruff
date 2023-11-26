import pytest

from libraries.Mex import Mex


@pytest.fixture()
def mex():
    return Mex(2 * 10**5 + 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_init_and_get_mex(mex):
    assert mex.get_mex() == 11


def test_add(mex):
    mex.add(11)
    assert mex.get_mex() == 12
    mex.add(13)
    assert mex.get_mex() == 12
    mex.add(12)
    assert mex.get_mex() == 14


def test_add_max_value(mex):
    mex.add(2 * 10**5)
    mex.add(2 * 10**5 + 1)
    mex.add(2 * 10**5 + 2)
    assert mex.get_mex() == 11


def test_add_over_max(mex):
    mex.add(2 * 10**6)
    assert mex.get_mex() == 11


def test_add_to_max(mex):
    for i in range(2 * 10**5 + 1):
        mex.add(i)
    assert mex.get_mex() == 2 * 10**5 + 1


def test_update(mex):
    mex.update(0, 1)
    assert mex.get_mex() == 0
    mex.update(1, 0)
    assert mex.get_mex() == 11


def test_update_over_max(mex):
    mex.update(10, 2 * 10**6)
    assert mex.get_mex() == 10
    mex.update(10, 2 * 10**6 + 1)
    assert mex.get_mex() == 10


@pytest.fixture()
def zero_mex():
    return Mex(2 * 10**5 + 1, [0] * 11)


def test_init_and_get_zero_mex(zero_mex):
    assert zero_mex.get_mex() == 1


def test_add_zero_mex(zero_mex):
    for i in range(10):
        zero_mex.add(i)
        assert zero_mex.get_mex() == i + 1


def test_update_zero_mex(zero_mex):
    for i in range(1, 11):
        zero_mex.update(i, 1)
        assert zero_mex.get_mex() == 2
    zero_mex.update(0, 1)
    assert zero_mex.get_mex() == 0
    for i in range(1, 11):
        zero_mex.update(i, 0)
        assert zero_mex.get_mex() == 2
    zero_mex.update(1, 2)
    assert zero_mex.get_mex() == 3
    zero_mex.update(0, 0)
    assert [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0] == zero_mex._A
    assert zero_mex.get_mex() == 1
