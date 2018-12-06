import unittest

from validators.alphanumeric_validator import IsAlphanumericValidator
from validators.digit_validator import IsDigitValidator


class TestValidator(unittest.TestCase):


    def test_valid_digit_validator(self):
        _id = '1234'
        v = IsDigitValidator(_id)
        self.assertTrue(v.validate())

    def test_not_valid_digit(self):
        _id = '123as'
        v = IsDigitValidator(_id)
        self.assertFalse(v.validate())
        _id = '12$234'
        v = IsDigitValidator(_id)
        self.assertFalse(v.validate())

    def test_valid_alphanumeric_string(self):
        _id = 'alamakota123'
        v = IsAlphanumericValidator(_id)
        self.assertTrue(v.validate())

    def test_not_valid_alphanumeric_string(self):
        _id = 'al#$amakota123'
        v = IsAlphanumericValidator(_id)
        self.assertFalse(v.validate())