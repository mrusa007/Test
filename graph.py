import matplotlib.pyplot as plt
import numpy as np
# students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
# scores = [85, 92, 78, 90, 88]   
# # Create a bar chart
# plt.bar(students, scores, color='blue')
# # Add labels and title
# plt.xlabel('Students')
# plt.ylabel('Scores')
# plt.title('Student Scores')
# Show the plot
plt.show()
#piechart
# piechart
subjects = ['Math', 'Science', 'English', 'History', 'Art']
scores = [85, 90, 78, 92, 88]

# Create a pie chart
plt.pie(scores, labels=subjects)

# Show the plot
plt.show()
#scatter plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
plt.scatter(x, y,color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()