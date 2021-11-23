from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools

#studentIte = iter(student_roster)
#for s in studentIte:
#  print(next(studentIte))


a = ClassroomOrganizer()
aIter = iter(a)
for s in aIter:
  print(next(aIter))

#------------------task number 5
#print(a.combi())
#print(a.get_students_with_subject('Math'))
#print(a.get_students_with_subject('Science'))
b = a.get_students_with_subject('Math') + a.get_students_with_subject('Science')
print(b)
c = itertools.combinations(b, 4)
print(list(c))
