import pandas as pd
import numpy as np

# Подгрузим данные из степика (но этот же файл есть и в рабочей директории)
students_performanse = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')

students_performanse_with_names = students_performanse.iloc[[0, 3, 4, 7, 8]]
students_performanse_with_names.index = ['Cersei', 'Tywin', 'Gregor', 'Joffrey', 'Ilyn Payne']

students_performanse = students_performanse \
    .rename(columns =
           {'parental level of education': 'parental_level_of_education',
            'test preparation course': 'test_preparation_course',
            'math score': 'math_score',
            'writing score': 'writing_score',
            'reading score': 'reading_score'})

# print(students_performanse.query('writing_score > 78').head())
score_columns = [i for i in list(students_performanse) if 'score' in i]
# print(students_performanse[score_columns].head())
# print(students_performanse_with_names.filter(like='co')) # выделение всех колонок, у которых есть "со" в названии
print(students_performanse_with_names.filter(like='y', axis=0).head()) # выделение всех колонок, у которых есть "со" в названии




