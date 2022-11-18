from src import Course
import pandas as pd


class GPA:
    def __init__(self, courses: dict):
        self.courses = [Course(**x) for x in courses]
        self.df = pd.DataFrame.from_dict([c.to_dict() for c in self.courses])

    def cumulative_unweighted_gpa(self):
        return self._unweighted_gpa(self.df)

    def cumulative_weighted_gpa(self):
        return self._weighted_gpa(self.df)

    def _weighted_gpa(self, df):
        credits = (df["weighted_grade"]*df["gpa_weight"]).sum()
        points = df["gpa_weight"].sum()
        return round(credits/points, 3)

    def _unweighted_gpa(self, df):
        credits = (df["unweighted_grade"]*df["gpa_weight"]).sum()
        points = df["gpa_weight"].sum()
        return round(credits/points, 3)

    def yearly_unweighted_gpa(self):
        s = self.df.groupby("year").apply(self._unweighted_gpa)
        return pd.Series(s, name="yearly_unweighted_gpa")

    def yearly_weighted_gpa(self):
        s = self.df.groupby("year").apply(self._weighted_gpa)
        return pd.Series(s, name="yearly_weighted_gpa")

    def stats(self, name="", show=True):
        df1 = self.yearly_unweighted_gpa()
        df2 = self.yearly_weighted_gpa()
        df1.name = name
        df2.name = name
        if show:
            print("All Classes")
            print(self.df)

            print(
                f"Cumulative Unweigted GPA: {self.cumulative_unweighted_gpa():.3f}")
            print(
                f"Cumulative Weighted GPA: {self.cumulative_weighted_gpa():.3f}")

            print("Yearly GPA Breakdown")
            print(pd.concat([df1, df2], axis=1))

        return df1, df2, pd.Series({name: self.cumulative_unweighted_gpa()}), pd.Series({name: self.cumulative_weighted_gpa()}, name=name)
