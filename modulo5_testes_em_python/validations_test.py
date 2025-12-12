import unittest

from validations import validade_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validade_user("mat", 3), True)
        self.assertEqual(validade_user("mateus", 6), True)
        self.assertEqual(validade_user("mateus", 7), False)
        self.assertEqual(validade_user("mateus", -1), False)

unittest.main()