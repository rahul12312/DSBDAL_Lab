import numpy as np

# A school maintains a record of students' exam scores for 5 subjects in a 2D NumPy array. Each row represents a student, and each column represents a subject:    import numpy as np      # Student scores: rows = students, columns = subjects      scores = np.array([    [85, 90, 78, 92, 88],   # Student 1    [72, 75, 80, 68, 74],   # Student 2    [95, 88, 92, 96, 90],   # Student 3    [60, 65, 70, 58, 62],   # Student 4    [88, 84, 86, 89, 87]    # Student 5 ])     
# 1.Retrieve the scores of Student 3 for all subjects.
# 2.Retrieve the scores for Subject 2 (column 2) across all students.
# 3 Extract the scores of the first 3 students for the first 2 subjects..Extract the scores of the last 2 students for the last 3 subjects.
# 4.Add 5 bonus marks to all scores. 
# 5.Subtract 10 marks from scores of Subject 4 for all students.
# 6.Calculate the percentage scores of each student assuming each subject is out of 100. 
# 7.Calculate the average score for each student across all subjects. 
# 8.Find the total marks scored by each student. 
# 9.Identify the highest score in the entire array. 
# 10.Determine the average score for each subject. 
# 11.Find the student with the lowest average score.
   
   

   

scores = np.array([
    [85, 90, 78, 92, 88],  # Student 1
    [72, 75, 80, 68, 74],  # Student 2
    [95, 88, 92, 96, 90],  # Student 3
    [60, 65, 70, 58, 62],  # Student 4
    [88, 84, 86, 89, 87]   # Student 5
])

#Q1
s3 = scores[2]
print("S3:", s3)

#Q2
sub2 = scores[:, 1]
print("Sub2:", sub2)

#Q3
f3_f2 = scores[:3, :2]
print("F3_F2:\n", f3_f2)

l2_l3 = scores[3:, 2:]
print("L2_L3:\n", l2_l3)

#Q4
bonus = scores + 5
print("Bonus:\n", bonus)

#Q5
sub4 = scores.copy()
sub4[:, 3] -= 10
print("Sub4 :\n", sub4)

#Q6
percent = (scores.sum(axis=1) / 500) * 100
print("Pct:", percent)

#Q7
avg = scores.mean(axis=1)
print("Avg:", avg)

#Q8
total = scores.sum(axis=1)
print("Total:", total)

#Q9
high = scores.max()
print("High:", high)

#Q10
avg_sub = scores.mean(axis=0)
print("Avg_Sub:", avg_sub)

#Q11
low_avg_idx = np.argmin(avg)
print("Low Avg Student:", low_avg_idx + 1)
