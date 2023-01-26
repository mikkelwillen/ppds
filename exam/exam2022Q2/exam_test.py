import exam
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Q1c
print(exam.game_play())

# Q2b
# Første udgave af opgaven
def tranpose_list(matrix):
    res = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for item in range(len(matrix)):
        for subitem in range(len(matrix[0])):
            res[subitem][item] = matrix[item][subitem]
    return res

transposed_new = tranpose_list(exam.dia_list)
print(transposed_new[3:6])

# Q2c
# Første udgave af opgaven
def get_patients(transposed_new):
    res = [[0 for j in range(3)] for i in range(len(transposed_new))]
    for rows in range(len(transposed_new)):
        res[rows][0] = transposed_new[rows][0]
        res[rows][1] = transposed_new[rows][5]
        if (transposed_new[rows][8] == "Outcome"):
            res[rows][2] = transposed_new[rows][8]
        elif (transposed_new[rows][8] == 1):
            res[rows][2] = "positiv"
        else:
            res[rows][2] = "negativ"
    return res

age_bmi = get_patients(transposed_new)

# Q2d
print(age_bmi)

# Q3a
# Første udgave af opgaven
data = np.genfromtxt("health_data2.CSV", delimiter=",", skip_header=True)
print(data.shape)

# Q3b
# Første udgave af opgaven
age = []
weight = []
height = []
exercise = []
obesity = []
for i in range(data.shape[0]):
    age.append(data[i][0])
    weight.append(data[i][1])
    height.append(data[i][2])
    exercise.append(data[i][3])
    obesity.append(data[i][4])

# Q3c
# Første udgave af opgaven
plt.figure
plt.scatter(x=weight, y=age, c=exercise)
plt.xlabel("Age (years)")
plt.ylabel("Weight (lbs)")
plt.title("Weight vs. Age with Exercise Level")
plt.colorbar(label="Exercise Level (hours per week", orientation="horizontal")
plt.show()

# Q3d
# Første udgave af opgaven
obese = ["Not Obese", "Obese"]
age_counts = [0, 0]
for i in range(len(obesity)):
    if (age[i] == 10 and obesity[i] == 1):
        age_counts[1] += 1
    else:
        age_counts[0] += 1

plt.figure
plt.bar(obese[0], age_counts[0], color="blue")
plt.bar(obese[1], age_counts[1], color="red")
plt.legend(["Not obese", "Obese"])
plt.xlabel("Obesity")
plt.ylabel("Age 10 count")
plt.show()

# Q3e
print(np.correlate(weight, exercise))

# Q4a
covid_df = pd.read_csv("time_series_covid19_confirmed_global.CSV")

cleaned_covid_df = exam.data_cleaning(covid_df)

# Q4b
country_dict = exam.get_countries_by_earth_quadrant(covid_df)

# Q4c
country_wise_df = exam.group_table_by_country(covid_df)

# Q4d
ax_ne = exam.plot_new_cases_daily(country_wise_df, "NE")

# Q5e
top_k_countries_dict = exam.get_top_new_case_countries_by_month(country_wise_df, year=2021, month=2, k_val=10)
print(top_k_countries_dict)