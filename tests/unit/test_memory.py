import unittest
from sources.memory import Memory

class TestMemory(unittest.TestCase):
    def setUp(self):
        # This method will run before each test.
        self.memory = Memory()  # Assuming Memory is a class

    def test_initialize_memory(self):
        # Test if the memory initializes correctly.
        self.assertIsNotNone(self.memory)
        self.assertEqual(self.memory.data, {})

    def test_add_memory(self):
        # Test adding an item to memory.
        self.memory.add('key1', 'value1')
        self.assertEqual(self.memory.get('key1'), 'value1')

    def test_get_memory(self):
        # Test getting an item from memory.
        self.memory.add('key2', 'value2')
        self.assertEqual(self.memory.get('key2'), 'value2')
        self.assertIsNone(self.memory.get('nonexistent_key'))

    def test_remove_memory(self):
        # Test removing an item from memory.
        self.memory.add('key3', 'value3')
        self.memory.remove('key3')
        self.assertIsNone(self.memory.get('key3'))

    def test_clear_memory(self):
        # Test clearing all memory.
        self.memory.add('key4', 'value4')
        self.memory.clear()
        self.assertEqual(self.memory.data, {})

if __name__ == '__main__':
    unittest.main()