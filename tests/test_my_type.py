from hypothesis import strategies as st

from to_cover.module import Example


def test_my_method():
    assert Example(1).my_method() == 1


def test_hypothesis_resolves_type():
    assert isinstance(st.from_type(Example).example(), Example)
