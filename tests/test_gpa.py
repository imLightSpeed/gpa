from src import __version__
import json
from src import GPA
import pytest




def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture    
def sample_GPA():
    path = "tests/data/test_grades.json"
    with open(path,"r") as file:
        courses = json.load(file)
    return GPA(courses)

def test_cumulative_unweighted_gpa(sample_GPA):
    assert sample_GPA.cumulative_unweighted_gpa() == pytest.approx(4.283, 0.001)

def test_yearly_unweighted_gpa(sample_GPA):
    assert sample_GPA.yearly_unweighted_gpa().iloc[0] == 4.33

def test_cumulative_weighted_gpa(sample_GPA):
    assert sample_GPA.cumulative_weighted_gpa() == pytest.approx(4.656, 0.001)

def test_yearly_weighted_gpa(sample_GPA):
    print(sample_GPA.yearly_weighted_gpa().head(10))
    assert sample_GPA.yearly_weighted_gpa().iloc[0] == 4.67