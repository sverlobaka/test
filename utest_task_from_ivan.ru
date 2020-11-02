import unittest
import task_from_ivan

class taskTest(unittest.TestCase):
    def test_compress_string(self):
       self.assertEqual(task_from_ivan.compress_string('aaadgggggvv'), 'a3dg5v2')

    def test_decompress_string(self):
        self.assertEqual(task_from_ivan.decompress_string('a5b'), 'aaaaab')

if __name__ == '__main__':
    unittest.main()
