import os
import sys
import unittest

module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, module_path)

def main():
    loader = unittest.TestLoader()
    test_suite = loader.discover('opendv')
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

if __name__ == '__main__':
    main()