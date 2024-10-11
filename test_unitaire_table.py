import unittest
import Table

class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table(1, 5, 4)

    def test_assigner_table(self):
        self.table.assigner_table() 

    def test_liberer_table(self):
        self.table.liberer_table() 

if __name__ == '__main__':
    unittest.main()