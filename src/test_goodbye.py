import unittest
import goodbye


class TestGoodbye(unittest.TestCase):
    def test_if_it_returns_correct_sentence(self):
        self.assertEqual(goodbye.goodbye('Junya'), 'Goodbye, Junya')
