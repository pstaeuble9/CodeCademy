class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, new_numberOfStudents):
    self.numberOfStudents = new_numberOfStudents

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students.'
  

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "Primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    primaryRepr = super().__repr__()
    return (primaryRepr + f' The pickup policy is {self.pickupPolicy}')


class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    self.sports = sportsTeams

  def getSportsTeams(self):
    return self.sports

  def __repr__(self):
    highRepr = super().__repr__()
    return (highRepr + f' We have {self.sports}')

# Tests the school class
# a = School("Codecademy", "high", 100)
# print(a)
# print(a.get_name())
# print(a.get_level())
# a.set_numberOfStudents(200)
# print(a.get_numberOfStudents())

# Tests the primary school class
# b = PrimarySchool("Arteon", 300, "Pickup Allowed")
# print(b.getPickupPolicy())
# print(b)

# Tests the HighSchool class
# c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
# print(c.getSportsTeams())
# print(c)
