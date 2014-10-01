
# ----------- IMPORTS --------------
from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_solve, rmse, netflix_print

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    def test_read_1 (self) :
        r = StringIO("")
        i = netflix_read(r)
        self.assertEqual(i, None)
    def test_read_2 (self) :
        r = StringIO("1:\n")
        i = netflix_read(r)
        self.assertEqual(i, "1:")
    def test_read_3 (self) :
        r = StringIO("1:\n30878\n")
        i = netflix_read(r)
        self.assertEqual(i, "1:")
    def test_read_4 (self) :
        r = StringIO("4783:")
        i = netflix_read(r)
        self.assertEqual(i, "4783:")
    def test_read_5 (self) :
        r = StringIO("2043:\n1417435\n")
        i = netflix_read(r)
        self.assertEqual(i, "2043:")
# ---------------------------------------------
    def test_solve_1 (self) :
        r = StringIO("1:\n548064\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.6\n")

main()