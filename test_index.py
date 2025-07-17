import pytest
 
from index import add
 
def test_add():
    assert add(1, 2) == 3
    assert add(14, 15) == 29
    with pytest.raises(TypeError):
        add(4, 'Three-Thousand')
 