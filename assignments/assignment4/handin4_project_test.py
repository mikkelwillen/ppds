import handin4_project

decade_anomaly_data = handin4_project.read_data4(filename = "Land_and_Ocean_summary.txt", year_range = (1970, 2000), decade = True)

value = decade_anomaly_data

print(value)