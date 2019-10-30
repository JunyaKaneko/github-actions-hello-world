import unittest
import hello


class TestHello(unittest.TestCase):
    def test_if_it_returns_correct_sentence(self):
        self.assertEqual(hello.hello('Junya'), 'Hello, Junya')
