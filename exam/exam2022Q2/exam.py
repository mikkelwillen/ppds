import random
import pandas as pd
import matplotlib.pyplot as plt
import itertools

# Q1a
def dice_roller(sides, bonus=0):
    return random.randint(1, sides) + bonus

# Q1b
# I assume the teams wins, if they have equal score
def game_play():
    monster = dice_roller(20, 10)
    team = dice_roller(8)
    team += dice_roller(12, 5)
    team += dice_roller(6)
    if (monster > team):
        return ("monster wins", monster, "team loses", team)
    else:
        return ("team wins", team, "monster loses", monster)

# Q2a
dia_list=[['PatientNumber',14568,22368,30168,37968,45768,53568,61368,69168,76968,84768,92568,50368,18168,15968,33768,41315,39368,14168,54968],        ['Glucose',148,85,183,89,137,116,78,115,197,125,110,168,139,189,166,100,118,107,103],
['BloodPressure',72,66,64,66,40,74,50,0,70,96,92,74,80,60,72,0,84,74,30],
['SkinThickness',35,29,0,23,35,0,32,0,45,0,0,0,0,23,19,0,47,0,38],
['Insulin',0,0,0,94,168,0,88,0,543,0,0,0,0,846,175,0,230,0,83],      ['BMI',33.6,26.6,23.3,28.1,43.1,25.6,31,35.3,30.5,0,37.6,38,27.1,30.1,25.8,30,45.8,29.6,43.3],         ['DiabetesPedigreeFunction',0.627,0.351,0.672,0.167,2.288,0.201,0.248,0.134,0.158,0.232,0.191,0.537,1.441,0.398,0.587,0.484,0.551,0.254,0.183],
['Age',50,31,32,21,33,30,26,29,53,54,30,34,57,59,51,32,31,31,33],
['Outcome',1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0]]

# Q4a
def data_cleaning(df):
    res = df.dropna(subset=["Lat", "Long"])
    res.iloc[:,4:].columns = pd.to_datetime(res.iloc[:,4:].columns)
    return res

# Q4b
def get_countries_by_earth_quadrant(df):
    res = {"NW": [], "NE": [], "SW": [], "SE": []}
    for index, row in df.iterrows():
        if (row["Lat"] >= 0):
            if (row["Long"] >= 0):
                res["NE"].append(row["Country/Region"])
            else:
                res["NW"].append(row["Country/Region"])
        else:
            if (row["Long"] >= 0):
                res["SE"].append(row["Country/Region"])
            else:
                res["SW"].append(row["Country/Region"])
    return res

# Q4c
def group_table_by_country(df):
    return df.groupby("Country/Region").sum(numeric_only = True).reset_index()

# Q4d
def plot_new_cases_daily(df, earth_quadrant):
    assert(earth_quadrant in {"NW", "NE", "SW", "SE"})
    quadrants = get_countries_by_earth_quadrant(df)
    countries_in_quadrant = quadrants[earth_quadrant]
    tmp = df[df["Country/Region"].isin(countries_in_quadrant)]
    cases = []
    dates = []
    for column in tmp.columns[3:]:
        dates.append(column)
        cases.append(tmp[column].sum())
    fig = plt.figure()
    plt.plot(dates, cases)
    plt.xlabel("date")
    plt.ylabel("number of cases")
    plt.title("Number of cases in {earth_quadrant} quadrant")
    plt.show()
    return fig

# Q4e
# Den er langsom, men der kommer et svar
def get_top_new_case_countries_by_month(df, year, month, k_val):
    print("den er lidt langsom, giv den en chance:)")
    res = {}
    start_date = pd.to_datetime("01/" + str(month) + "/" + str(year), dayfirst=True)
    end_date = pd.to_datetime("28/" + str(month) + "/" + str(year), dayfirst=True)
    for index, row in df.iterrows():
        sum = 0
        for index2, value in row[3:].items():
            tmp = pd.to_datetime(index2)
            if (start_date <= tmp <= end_date):
                sum += value
        res[row[0]] = sum
    res = sorted(res.items(), key=lambda x:x[1], reverse=True)
    res = dict(res)
    return dict(itertools.islice(res.items(), k_val))
    