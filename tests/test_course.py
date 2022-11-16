from src import Course


class TestCourse:
    def test_grading(self):
        c = Course("test_weighted", 12, "A+", 1.0, 1.0, "H")
        assert c.calc_unweighted_grade() == 4.33
        assert c.calc_weighted_grade() == 4.67

    def test_elective(self):
        c = Course("test_elective", 12, "A+", 0.5, 0.5, "E")
        assert c.calc_unweighted_grade() == 4.33
        assert c.calc_weighted_grade() == 4.33
