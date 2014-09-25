
# ----------- IMPORTS --------------
from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, predict_ratings, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    def test_read (self) :
        r = StringIO("2043:\n1417435\n2312054\n462685\n")
        j = netflix_read(r)
        self.assertEqual(j, [1417435, 2312054, 462685])

    def test_eval_1 (self) :
        self.assertEqual(predict_ratings(j), 3)

    def test_print (self) :
        w = StringIO()
        netflix_print(w, "2043:")
        self.assertEqual(w.getvalue(), "2043:\n")

    def test_solve (self) :
        r = StringIO("2043:\n1417435\n2312054\n462685\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "2043:\n3\n3\n3\n")

main()