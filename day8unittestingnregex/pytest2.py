import pytest

@pytest.mark.parametrize("input, output", [("2+2", 4), ("2-2", 0), ("2*2", 4), ("2/2", 1.0)])
def test_eval(input, output):
    assert eval(input) == output