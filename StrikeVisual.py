import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Airplane_Strikes_Dataset.csv')

##### Displays strike frequency each year #####
# YearColumn = df['Incident Year']
# number_counts = YearColumn.value_counts()

# number_counts_sorted= number_counts.sort_index()

# plt.figure(figsize=(12, 6)) 
# number_counts_sorted.plot(kind='bar')
# plt.title('Strike Frequency each year')
# plt.xlabel('Year')
# plt.ylabel('Strike Frequency')


##### Displays all data #####
# df.plot.line(x = 'Incident Year')


###### Displays frequency of each type of engine in each strike ######
# column_to_analyze = df['Engine Type']

# letter_counts = column_to_analyze.str.lower().str.replace(r'[^a-z]', '', regex=True).value_counts()

# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
# letter_counts.plot(kind='bar')
# plt.title('Engine Type Strike Frequency')
# plt.xlabel('Engine Type')
# plt.ylabel('Frequency')



# data = (3, 6, 9, 12)

# fig, simple_chart = plt.subplots()

# simple_chart.plot(data)

plt.show()