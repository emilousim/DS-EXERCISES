"""Functions to parse a file containing student data."""
from os import dup

def all_houses(filename):
    # """Return a set of all house names in the given file.
    houses = set()

    cohort_data = open(filename)

    for line in cohort_data:
        house = line.rstrip().split('|')[2]
        if house:
          houses.add(house)

    return houses


def students_by_cohort(filename, cohort='All'):
    #Return a list of students' full names by cohort.

    students = []
    
    cohort_data = open(filename)

    for line in cohort_data:
      firstName, lastName, _, _, cohort_name = line.rstrip().split('|')
      if cohort_name not in ('I', 'G') and cohort in ('All', cohort_name):
        students.append(f'{firstName} {lastName}')

    return sorted(students)


def all_names_by_house(filename):
    #Return a list that contains rosters for all houses, ghosts, instructors.

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    cohort_data = open(filename)

    for line in cohort_data:
        first, last, house, _, cohort_name = line.rstrip().split('|')

        full_name = f'{first} {last}'

        if house:
            if house in "Dumbledore's Army":
                dumbledores_army.append(full_name)
            elif house in 'Gryffindor':
                gryffindor.append(full_name)
            elif house in 'Hufflepuff':
                hufflepuff.append(full_name)
            elif house in 'Ravenclaw':
                ravenclaw.append(full_name)
            elif house in 'Slytherin':
                slytherin.append(full_name)
        else:
            if cohort_name in 'G':
              ghosts.append(full_name)
            elif cohort_name in 'I':
              instructors.append(full_name)
      
    return [sorted(dumbledores_army),
            sorted(gryffindor), 
            sorted(hufflepuff), 
            sorted(ravenclaw), 
            sorted(slytherin), 
            sorted(ghosts), 
            sorted(instructors),]

def all_data(filename):
    #Return all the data in a file.

    all_data = []

    cohort_data = open(filename)

    for line in cohort_data:
      first, last, house, advisor, cohort_name = line.rstrip().split('|')
      full_name = f'{first} {last}'
      all_data.append((full_name, house, advisor, cohort_name))

    return all_data


def get_cohort_for(filename, name):
    #Given someone's name, return the cohort they belong to. 
    for full_name, _, _, cohort_name in all_data(filename):
      if (full_name) == name:
        return cohort_name



def find_duped_last_names(filename):
    #Return a set of duplicated last names that exist in the data.
    duplicates = set()
    checked = set()
    for full_name, _, _, _ in all_data(filename):
      last = full_name.split(' ')[-1]
      if last in checked:
        duplicates.add(last)
        
      checked.add(last)

    return duplicates



def get_housemates_for(filename, name):
    #Return a set of housemates for the given student.

    housemates = set()

    student = None
    for housemate in all_data(filename):
        full_name, house, advisor, cohort_name = housemate

        if full_name == name:
            student = housemate
            break

    if student:
        student_name, student_house, _, student_cohort = student

        for full_name, house, _, cohort_name in all_data(filename):
          if ((house, cohort_name) == (student_house, student_cohort) and
                full_name != name):
              housemates.add(full_name)

    return housemates
      

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
