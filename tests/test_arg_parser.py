import pytest

from cloner.arg_parser import ArgParser


def test_no_args():
    with pytest.raises(ValueError):
        ArgParser([])


def test_three_args():
    with pytest.raises(ValueError):
        ArgParser(['a', 'b', 'c'])


def test_username_reponame_args():
    ap = ArgParser(['kardasis', 'cloner'])
    assert ap.url == 'git@github.com:kardasis/cloner.git'


def test_root_url_args():
    ap = ArgParser(['https://github.com/kardasis/cloner'])
    assert ap.user_name == 'kardasis'
    assert ap.repo_name == 'cloner'


def test_deep_url_args():
    ap = ArgParser(['https://github.com/kardasis/cloner/blob/master/cloner/cli.py'])
    assert ap.user_name == 'kardasis'
    assert ap.repo_name == 'cloner'
