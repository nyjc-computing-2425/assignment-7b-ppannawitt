# Built-in imports
import math

# Your code below
GRADE = {}
#init dictionary
for i in range(0, 40):
  GRADE[i] = 'U'
for i in range(40, 45):
  GRADE[i] = 'S'
for i in range(45, 50):
  GRADE[i] = 'E'
for i in range(50, 55):
  GRADE[i] = 'D'
for i in range(55, 60):
  GRADE[i] = 'C'
for i in range(60, 70):
  GRADE[i] = 'B'
for i in range(70, 101):
  GRADE[i] = 'A'

def read_testscores(filename):
  """
  return a list of data of each student as dictaionary

  filename -> str
  return -> list of dictionary
  """
  list = []
  with open(filename, 'r') as f:
    f.readline()
    for line in f:
      dict = {}
      data = line.strip().split(",")
      dict['class'] = data[0]
      dict['name'] = data[1]
      overall = math.ceil(int(data[2])/30*15 + int(data[3])/40*30 + int(data[4])/80*35 + int(data[5])/30*20)
      dict['overall'] = overall
      dict['grade'] = GRADE[overall]
      list.append(dict)
  return list


def analyze_grades(studentdata):
  """
  return count of no. of students with certain grade in each class

  studentdata -> list of dictionary
  return -> dictionary of dictionary
  """
  class_grade = {}
  for dict in studentdata:
    if dict['class'] not in class_grade:
      class_grade[dict['class']] = {}
      class_grade[dict['class']]['A'] = 0
      class_grade[dict['class']]['B'] = 0
      class_grade[dict['class']]['C'] = 0
      class_grade[dict['class']]['D'] = 0
      class_grade[dict['class']]['E'] = 0
      class_grade[dict['class']]['S'] = 0
      class_grade[dict['class']]['U'] = 0
  for dict in studentdata:
    class_grade[dict['class']][dict['grade']] += 1
  return class_grade
#Sample Grader
"""
studentdata = read_testscores('testscores.csv')
print(studentdata[0]['class'])
print(studentdata[0]['name'])
print(studentdata[0]['overall'])
print(studentdata[0]['grade'])
analysis = analyze_grades(studentdata)
print(analysis['Class1']['A'])
print(analysis['Class18']['U'])
"""