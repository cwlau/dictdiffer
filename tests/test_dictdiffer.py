from unittest import TestCase

from dictdiffer import DictDiffer


class TestDictDiffer(TestCase):
    def setUp(self):
        a = {'a': 1, 'b': 1, 'c': 0}
        b = {'a': 1, 'b': 2, 'd': 0}
        self.d = DictDiffer(b, a)

    def test_added(self):
        self.assertEqual(self.d.added(), set(['d']))

    def test_removed(self):
        self.assertEqual(self.d.removed(), set(['c']))

    def test_changed(self):
        self.assertEqual(self.d.changed(), set(['b']))

    def test_unchanged(self):
        self.assertEqual(self.d.unchanged(), set(['a']))

    def test_new_or_changed(self):
        self.assertEqual(self.d.new_or_changed(), set(['b', 'd']))

    def test_new_or_changed_or_removed(self):
        self.assertEqual(self.d.new_or_changed_or_removed(), set(['b', 'c', 'd']))
