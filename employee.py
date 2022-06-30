"""
3. Employee class - time estimate 15mn
Create a class Employee which constructor will take a full name as argument, as well as a set of
none, one or more arguments. Each instance should have a ‘name’ and a ‘lastname’ attribute
plus one more attribute for each of the additional arguments, if any.
Note:
- First and last names will be separated by a whitespace. The test will not include any
middle names or initials.
- The value of the arguments can be an int, a str or a list.

"""

class Employee:
    def __init__(self,name,**kwargs):

        name,last_name = name.split()
        self.name = name
        self.lastname = last_name
        for key in kwargs:
            setattr(self, key, kwargs[key])


joe = Employee("Joe Dalton")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182,
nationality="Italian")


print(joe.name,mary.lastname,giancarlo.nationality)