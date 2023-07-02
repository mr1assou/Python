import student
as1 = student.ArtsStudent('Peter Johnson', 'A19012', 'History', 11000, 'A')
cs1 = student.CommerceStudent('Alan Goh', 'C19111', 'Digital Marketing', 13400, 'Digital Consultancy')
ts1 = student.TechStudent('Larry Faith', 'T19126', 'Computer Science', 21000, 'A', 'Kyla Tech')
print(as1)
print()
print(cs1)
print()
print(ts1)
print()
if ts1 > cs1:
    print("Les frais annuels d'un étudiant technique sont plus élevés"
    " que ceux d'un étudiant en commerce.")
else:
    print("Les frais annuels d'un étudiant technique sont"
   "inférieurs à ceux d'un un étudiant de commerce.")