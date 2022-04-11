import pytest


def always_returns_true():
    return True

# another comment


def test_always_returns_true():
    assert always_returns_true()
