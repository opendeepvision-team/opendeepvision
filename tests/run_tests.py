import os
import sys
import unittest

test_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(test_path, '..'))

def main():
    loader = unittest.TestLoader()
    test_suite = loader.discover(os.path.join(test_path, 'opendv'))
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

if __name__ == '__main__':
    main()