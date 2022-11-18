from src import GPA
import json 
import pandas as pd

students = {"Luke S":"data/luke_grades.json","Mikhail R":"data/mikhail_grades.json","Paul N":"data/paul_grades.json"}
yearly_unweighted, yearly_weighted,cumulative_unweighted,cumulative_weighted  = [],[],[],[]

for s, path in students.items():
    with open(path,"r") as file:
        courses = json.load(file)
    gpa =  GPA(courses)
    yuw, yw,cuw,cw = gpa.stats(name=s, show=False)
    yearly_unweighted.append(yuw)
    yearly_weighted.append(yw)
    cumulative_unweighted.append(cuw)
    cumulative_weighted.append(cw)

print(f"Cumulative Unweigted GPA:\n\n{pd.concat(cumulative_unweighted)}\n\n")
print(f"Cumulative Weighted GPA:\n\n{pd.concat(cumulative_weighted)}\n\n")

print(f"Yearly Unweigted GPA:\n\n{pd.concat(yearly_unweighted,axis=1)}\n\n")
print(f"Yearly Weighted GPA:\n\n{pd.concat(yearly_weighted,axis=1)}\n\n")
