import pandas as pd
import numpy as np
data ={'ученик':["Анна","Петр","Иван","Сидор","Ольга","Катя","Елена","Федор","Ева","Яков"],
    "математика":[4,3,5,4,3,4,5,5,4,3],'физика':[3,4,5,4,3,5,4,4,5,5],'химия':[4,3,5,3,4,5,5,4,3,5],
       'литература':[4,4,3,5,5,4,3,4,5,4],'история':[5,3,4,5,3,4,5,5,4,3]}
df = pd.DataFrame(data)
print(df.head())
grade_mat = df['математика'].mean()
grade_phi = df['физика'].mean()
grade_che = df['химия'].mean()
grade_lit = df['математика'].mean()
grade_his = df['математика'].mean()
print(f'Среднее: математика {grade_mat}, физика {grade_phi}, химия {grade_che}, литература {grade_lit}, история{grade_his}')
grade_mat = df['математика'].median()
grade_phi = df['физика'].median()
grade_che = df['химия'].median()
grade_lit = df['математика'].median()
grade_his = df['математика'].median()
print(f'Медиана: математика {grade_mat}, физика {grade_phi}, химия {grade_che}, литература {grade_lit}, история{grade_his}')
Q1_math = df['математика'].quantile(0.25)

Q3_math = df['математика'].quantile(0.75)
iqr = Q3_math - Q1_math
print(f'Q1={Q1_math}, Q2={Q3_math}, iqr={iqr}')

grade_mat = df['математика'].std()
grade_phi = df['физика'].std()
grade_che = df['химия'].std()
grade_lit = df['математика'].std()
grade_his = df['математика'].std()
print(f'Дисперсия: математика {grade_mat}, физика {grade_phi}, химия {grade_che}, литература {grade_lit}, история{grade_his}')