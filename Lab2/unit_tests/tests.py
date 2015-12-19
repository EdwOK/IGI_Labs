from glob import glob
from unittest import TestLoader, TextTestRunner, TestSuite


def suite():
    modules = [module[0:len(module) - 3] for module in glob("*_test.py")]

    loader = TestLoader()
    suites = [loader.loadTestsFromName(module) for module in modules]

    suite_return = TestSuite(suites)
    return suite_return


if __name__ == '__main__':
    result_suite = suite()
    runner = TextTestRunner(verbosity=2)
    runner.run(result_suite)
