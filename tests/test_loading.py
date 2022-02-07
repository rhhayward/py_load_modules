import unittest
from load_modules import load_modules

class SuperClass:
    def __init__(self):
        pass

class TestLoadingCWD(unittest.TestCase):

    def test_load(self):

        modules = load_modules.load(SuperClass, ['tests/', 'tests/modules/'])
        self.assertEqual(2, len(modules))

        modules_by_name = {module.__class__.__name__: module for module in modules}

        self.assertEqual(True, "SubClassOne" in modules_by_name)
        self.assertEqual(True, "SubClassTwo" in modules_by_name)

    def classy(self, clazz, instance):
        return isinstance(instance, clazz)

if __name__ == '__main__':
    unittest.main()
