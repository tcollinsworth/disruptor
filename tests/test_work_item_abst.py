from disruptor.work_item_abst import WorkItemAbst
from work_item_mock import WorkItemMock
import pytest

def test_abstract():
    with pytest.raises(TypeError):
        WorkItemAbst()

def test_inheritance():
    m = WorkItemMock()
    assert m != None

def test_get_set_index():
    m = WorkItemMock()
    assert m._index == -1
    m._index = 1
    assert m._index == 1