import pytest

from cloner.arg_parser import ArgParser


def test_no_args():
    with pytest.raises(ValueError):
        ArgParser([])


def test_three_args():
    with pytest.raises(ValueError):
        ArgParser(['a', 'b', 'c'])


