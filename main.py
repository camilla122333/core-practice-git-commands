import pytest


def always_returns_true():
    return True

    # adding comment


def test_always_returns_true():
    assert always_returns_true()
