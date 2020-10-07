from unittest import TestCase

import shelf.ko42.bar as runner

class Test(TestCase):
  def test_run(self):
    lala = runner.run("abc")
    self.assertEqual(lala, "ABC")

