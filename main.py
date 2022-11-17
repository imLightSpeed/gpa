import argparse
from src import GPA
import json 

path = "tests/data/test_grades copy.json"
with open(path,"r") as file:
    courses = json.load(file)
gpa =  GPA(courses)
print(f"CUW: {gpa.cumulative_unweighted_gpa():.3f}")
print(f"CW: {gpa.cumulative_weighted_gpa():.3f}")

print(gpa.yearly_unweighted_gpa().head(20))
print(gpa.yearly_weighted_gpa().head(20))


path = "tests/data/test_grades.json"
with open(path,"r") as file:
    courses = json.load(file)
gpa =  GPA(courses)
print(f"CUW: {gpa.cumulative_unweighted_gpa():.3f}")
print(f"CW: {gpa.cumulative_weighted_gpa():.3f}")

print(gpa.yearly_unweighted_gpa().head(20))
print(gpa.yearly_weighted_gpa().head(20))