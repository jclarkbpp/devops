import pytest
 
from index import add, minus
 
def test_add():
    assert add(1, 2) == 3
    assert add(14, 15) == 29
    with pytest.raises(TypeError):
        add(4, 'Three-Thousand')

def test_minus():
    assert minus(5, 3) == 2
    assert minus(6, 9) == -3
    assert minus(11, 4) != 4
 