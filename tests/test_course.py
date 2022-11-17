from src import Course
import pytest


@pytest.fixture
def honors_Course():
    return Course("test_weighted", 12, "A+", 1.0, 1.0, "H")

@pytest.fixture
def elective_Course():
    return Course("test_elective", 12, "A+", 0.5, 0.5, "E")

def test_grading(honors_Course):
    assert honors_Course.calc_unweighted_grade() == 4.33
    assert honors_Course.calc_weighted_grade() == 4.67

def test_elective(elective_Course):
    c = Course("test_elective", 12, "A+", 0.5, 0.5, "E")
    assert elective_Course.calc_unweighted_grade() == 4.33
    assert elective_Course.calc_weighted_grade() == 4.33
