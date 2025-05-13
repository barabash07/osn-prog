from datetime import datetime

class MyName:
    def __init__(self, name=None, second_name=None, birth_yr=None):
        self.name = name
        self.second_name = second_name
        self.birth_yr = birth_yr
        print(self)

    def calculate_course(self):
        if self.birth_yr is None:
            return None
        this_year = datetime.now().year
        age = this_year - self.birth_yr
        course = age - 15
        return max(course, 1)

    def name_list(self):
        return [self.name, self.second_name]


obj = MyName("Валерія", "Барабаш", 2007)
a = MyName()
print(obj.birth_yr)
print(obj.name_list())
print(obj.calculate_course())