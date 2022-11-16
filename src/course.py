import yaml


class Course:
    def __init__(self, name: str, year: int, letter_grade: str, credits: float, gpa_weight: float, scale: str):
        """Manage cumulative course grade

        Args:
            name (str): name of the course
            year (int): grade year of the course ie. 11 - 11th Grade
            letter_grade (str): letter grade
            weight (float): credits 
            gpa_weight (float): gpa weight
            scale (str): level of class - ie. Advanced Placement
        """
        self.name = name
        self.year = year
        self.credits = credits
        self.gpa_weight = gpa_weight

        self.letter_grade = letter_grade
        self.scale = scale

        config = self._load_config("config")
        self.grade_conversion = config["conversions"]
        self.scale_conversion = config["scale"]

        assert letter_grade in self.grade_conversion.keys()
        assert scale in self.scale_conversion.keys()

    def _load_config(self, root: str):
        """Load config

        Args:
            root (str): path to config file

        Returns:
            dict: yaml file contents
        """
        with open(f"{root}/config.yaml", "r") as file:
            config = yaml.safe_load(file)
        return config

    def calc_weighted_grade(self) -> float:
        """Calculate numerical weighted grade based on scale

        Returns:
            float: numerical weighted grade
        """
        num_grade = self.grade_conversion[self.letter_grade]
        curve = self.scale_conversion[self.scale]
        return num_grade+curve

    def calc_unweighted_grade(self) -> float:
        """Calculate numerical unweighted grade

        Returns:
            float: numerical unweighted grade
        """
        num_grade = self.grade_conversion[self.letter_grade]
        curve = self.scale_conversion["BASE"]
        return num_grade+curve

    def get_credits(self) -> float:
        """Get course credits

        Returns:
            float: credits
        """
        return self.credit

    def to_dict(self) -> dict:
        return {"name": self.name, "year": self.year, "letter_grade": self.letter_grade, "weighted_grade": self.calc_weighted_grade(), "unweighted_grade": self.calc_unweighted_grade(),
                "credits": self.credits, "gpa_weight": self.gpa_weight, "scale": self.credits}
