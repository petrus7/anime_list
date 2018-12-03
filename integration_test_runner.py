import unittest

loader = unittest.TestLoader()
dir = './tests_integration'
suite = loader.discover(dir)
runner = unittest.TextTestRunner()
runner.run(suite)