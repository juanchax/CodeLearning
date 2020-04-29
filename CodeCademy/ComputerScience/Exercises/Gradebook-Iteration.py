# Python Gradebook
#
# You are a student and you are trying to organize your subjects
# and grades using Python. Let’s explore what we’ve learned about
# lists to organize your subjects and scores.

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

subjects.append('computer science')
grades.append(100)

gradebook = zip(subjects, grades)

subjects.append('visual arts')
grades.append(93)

gradebook = zip(subjects, grades)

print(list(gradebook))

full_gradebook = list(gradebook) + last_semester_gradebook

print(full_gradebook)
