import matplotlib.pyplot as plt

names = ["Bhoomi", "Priya", "Rahul", "Anjali"]
marks = [85, 90, 78, 92]

# Bar chart
plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Line chart
plt.plot(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie chart
plt.pie(marks, labels=names, autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()
