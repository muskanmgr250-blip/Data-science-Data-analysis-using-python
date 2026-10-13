import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student-mat.csv', sep=';')
print(df.shape)
print("\n")
df.info()
print(df.isnull().sum())
df = df.drop_duplicates()
print("\n", df.shape)

avg_g3 = df['G3'].mean()
print(f"G3 average: {avg_g3:.2f}")

student_above_15 = df[df['G3'] > 15].shape[0]
print(f"Students with G3 > 15: {student_above_15}")

correation=df['studytime'].corr(df['G3'])
print(f"Study time{correation:.2f}")
df = pd.read_csv('student-mat.csv', sep=';')

gender_performance=df.groupby('sex')['G3'].mean()
print("\n")
print(gender_performance)
plt.figure(figsize=(8,5))
sns.histplot(df['G3'],kde=True,color='blue')
plt.title('Distribution of Final Grade(G3)')
plt.xlabel('Grades')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x='studytime',y='G3',data=df,alpha=0.6,color='purple')
plt.title('Study Time vs Final Grades')
plt.xlabel('Weekly Study Time Grades')
plt.ylabel('Final Grade(G3)')
plt.show()

plt.figure(figure=(6,5))
sns.barplot(x='sex',y='G3',data=df,errorbar=None,palette='pastel')
plt.title('Average Score:Male vs Female')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade')
plt.show()

