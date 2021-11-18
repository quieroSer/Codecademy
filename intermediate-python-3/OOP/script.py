class School():
  def __init__(self, name, level, num):
    self.name=name
    self.level=level
    self.numberOfStudents=num
  
  def __repr__(self):
    return "A {0} school named {1} with {2} students".format(self.level, self.name, self.numberOfStudents)
  
  def getName(self):
    return self.name
  
  def getLevel(self):
    return self.level

  def getStudents(self):
    return self.numberOfStudents

  def setName(self, n):
    self.name=n

  def setLevel(self, l):
    self.level=l

  def setStudents(self, s):
    self.numberOfStudents=s

#testing, testing...  
#s1 = School("la salle", 'high', 1000)
#print(s1)
#print(s1.getName())
#print(s1.getLevel())
#s1.setStudents(1500)
#print(s1.getStudents())

class PrimarySchool(School):
  def __init__(self, name, stu, pickup):
    super().__init__(name, 'primary', stu)
    self.pickupPolicy=pickup
  def __repr__(self):
    return super().__repr__() + ", which has a pickup policy of {0}".format(self.pickupPolicy)

  def getPolicy(self):
    return self.pickupPolicy

#testing, testing...
#s2=PrimarySchool("jardin sanito", 20, "all are welcome")
#print(s2)
#print(s2.getPolicy())

class MiddleSchool(School):
  def __init__(self, name, stu):
    super().__init__(name, 'middle', stu)

class HighSchool(School):
  def __init__(self, name, stu, teams):
    super().__init__(name, 'high', stu)
    self.sportTeams=teams
  def __repr__(self):
    return super().__repr__() + ", which has the following sport teams: {0}".format(', '.join(self.sportTeams))
  
  def getSports(self):
    return self.sportTeams


#testing, testing...
s3=HighSchool('la salle', 500, ['balonmano', 'basket', 'jurgol'])
print(s3)
print(s3.getSports())

