from roster import student_roster
import itertools

# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

###### Iterator protocol --- task number 3
  def __iter__(self):
    self.c = 0
    return self
  
  def __next__(self):
    if self.c < len(student_roster):
      x = self.sorted_names[self.c]
      self.c += 1
      return x
    else:
      raise StopIteration

####task number 4
  def combi(self):
    x = iter(self)
    y = itertools.combinations(x, 2)
    z = [', '.join(i) for i in y]
    return z
    

##### Iterator protocol test code
#a = ClassroomOrganizer()
#aIter = iter(a)
#print(aIter)
#for s in aIter:
#  print(next(aIter))

#### task number 4 test code
#print(a.combi())

