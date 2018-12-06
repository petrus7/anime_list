import unittest

loader = unittest.TestLoader()
dir = './tests'
suite = loader.discover(dir)
runner = unittest.TextTestRunner()
runner.run(suite)
