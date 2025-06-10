import pytest
from sources.memory import Memory


def test_memory_initialization():
    """
    Test the initialization of the Memory class.
    """
    memory = Memory()
    assert memory is not None


def test_memory_store_and_retrieve():
    """
    Test storing and retrieving a value in memory.
    """
    memory = Memory()
    memory.store('key1', 'value1')
    assert memory.retrieve('key1') == 'value1'


def test_memory_retrieve_nonexistent_key():
    """
    Test retrieving a value for a nonexistent key returns None.
    """
    memory = Memory()
    assert memory.retrieve('nonexistent_key') is None


def test_memory_update_value():
    """
    Test updating a stored value in memory.
    """
    memory = Memory()
    memory.store('key1', 'value1')
    memory.store('key1', 'value2')
    assert memory.retrieve('key1') == 'value2'


def test_memory_clear():
    """
    Test clearing all stored values in memory.
    """
    memory = Memory()
    memory.store('key1', 'value1')
    memory.clear()
    assert memory.retrieve('key1') is None
