class GPA:
    def __init__(self, courses:dict):
        self.courses = courses
        self.data = None        
        
    def calc_stats(self,show=True):
        stats = [x.get_stats() for x in [Course(**x) for x in self.courses]]
        stats = pd.DataFrame(stats, columns=["name","UW", "W", "weight"])
        # self.data = pd.DataFrame.from_dict(self.courses).merge(stats)
        cum_uw=stats["W"].mean(skipna=True)
        credits = stats["weight"].sum()
        points= stats["W"].sum()
        print(points/credits)
        # cum_w=(self.stats["W"]*self.data["Weight"]).mean()
        # credits = self.d

        # yearly_data = self.data.groupby("year")
        if show:
            print(stats.head(20))
            print(f"Cumulative Unweighted GPA calc: {cum_uw:.3f}")
            print("Cumulative Unweighted GPA actual: 4.283")
            # print(f"Cumulative Weighted GPA: {cum_w:.3f}")