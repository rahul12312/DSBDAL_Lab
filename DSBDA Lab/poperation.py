'''
        A school maintains student exam scores for multiple subjects. The data is stored in a Pandas DataFrame where each row represents a student, and each column represents a subject.
import pandas as pd
 # Sample data: Student exam scores 
data = { "Math": [85, 78, 92, 60, 74, 88],
 "Science": [80, 82, 89, 65, 70, 90],
  "English": [75, 85, 78, 55, 72, 88], 
  "History": [70, 75, 80, 50, 68, 82] }
 students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6"] exam_scores = pd.DataFrame(data, index=students)
·  Display the first three rows of the exam_scores DataFrame.
·  Get the total number of students and subjects recorded in the DataFrame.
·  List all subject names and student names.
·  Display the data type of each column in the DataFrame.
·  Check if there are any missing values in the DataFrame.
·  Retrieve the scores of "Student 3" in all subjects.
·  Extract the scores of all students in "Math".
·  Retrieve the scores of "Student 1" and "Student 4" in "Science" and "English".
·  Slice the DataFrame to get the first 4 students and the first 3 subjects.
·  Retrieve the score of "Student 5" in "History" using .loc or .iloc.
·  Update the score of "Student 2" in "Math" to 85.
·  Add a new student, "Student 7", with scores [90, 85, 88, 80] for all subjects.
·  Add 5 bonus marks to all students' scores.
·  Deduct 3 marks from the scores of "Student 4" in all subjects.
·  Calculate the percentage of marks obtained by each student, assuming each subject has a maximum of 100 marks.
·  Calculate the total marks obtained by each student.
·  Determine the total marks scored in each subject.
·  Identify the student with the highest total marks.
·  Find the subject with the lowest total marks.
·  Compute the average marks scored by each student across all subjects
'''


import pandas as pd



data = {
    "Math": [85, 78, 92, 60, 74, 88],
    "Science": [80, 82, 89, 65, 70, 90],
    "English": [75, 85, 78, 55, 72, 88],
    "History": [70, 75, 80, 50, 68, 82]
}
students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6"]
x = pd.DataFrame(data, index=students)
num_subjects = x.shape[1]

# Display the first three rows of the exam_scores DataFrame.
print(x.head(3))

# Get the total number of students and subjects recorded in the DataFrame.
a, b = x.shape
print(f"Number of students: {a}, Number of subjects: {b}")

# List all subject names and student names.
subjects = x.columns.tolist()
students = x.index.tolist()
print(f"Subjects: {subjects}")
print(f"Students: {students}")

# Display the data type of each column in the DataFrame.
print(x.dtypes)

# Check if there are any missing values in the DataFrame.
print(x.isnull().sum())

# Retrieve the scores of "Student 3" in all subjects.
print(x.loc["Student 3"])

# Extract the scores of all students in "Math".
print(x["Math"])

#  Retrieve the scores of "Student 1" and "Student 4" in "Science" and "English".
print(x.loc[["Student 1", "Student 4"], ["Science", "English"]])

# slice the DataFrame to get the first 4 students and the first 3 subjects.
print(x.iloc[:4, :3])

#  Retrieve the score of "Student 5" in "History" using .loc or .iloc.
print(x.loc["Student 5", "History"])

# Update the score of "Student 2" in "Math" to 85.
x.loc["Student 2", "Math"] = 85
print(x)

# Add a new student, "Student 7", with scores [90, 85, 88, 80] for all subjects.
x.loc["Student 7"] = [90, 85, 88, 80]
print(x)

#  Add 5 bonus marks to all students' scores.
x = x + 5
print(x)

# Deduct 3 marks from the scores of "Student 4" in all subjects.
x.loc["Student 4"] = x.loc["Student 4"] - 3
print(x)

# Calculate the percentage of marks obtained by each student, assuming each subject has a maximum of 100 marks.
percentage = x.sum(axis=1) / ( num_subjects * 100) * 100
print(percentage)

# Calculate the total marks obtained by each student.
total_marks = x.sum(axis=1)
print(total_marks)

#  Determine the total marks scored in each subject.
q = x.sum(axis=0)
print(q)

#  Identify the student with the highest total marks.
z = total_marks.idxmax()
print(f"Student with the highest total marks: {z}")

# Find the subject with the lowest total marks.
h = q.idxmin()
print(f"Subject with the lowest total marks: {h}")

# Compute the average marks scored by each student across all subjects.
average_marks = x.mean(axis=1)
print(average_marks)