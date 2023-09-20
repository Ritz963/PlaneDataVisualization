import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Airplane_Strikes_Dataset.csv')

##### Display where strikes occured most often #####

# locations = ['Radome Strike' , 'Windshield Strike' , 'Nose Strike' , 'Engine1 Strike' , 'Engine2 Strike' , 'Engine3 Strike' , 'Engine4 Strike' , 'Propeller Strike' , 'Wing or Rotor Strike' , 'Fuselage Strike' , 'Landing Gear Strike' , 'Tail Strike' , 'Lights Strike' , 'Other Strike']
# locationSum = df[locations].sum
# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed

# locationSum = pd.Series(locationSum)


# locationSum.plot(kind = 'b ar')
# plt.title('Location strike frequency')
# plt.xlabel('Locations')
# plt.ylabel('Frequency')
# plt.xticks(rotation=45)


##### Displays strike frequency each year #####
# YearColumn = df['Incident Year']
# number_counts = YearColumn.value_counts()

# number_counts_sorted= number_counts.sort_index()

# plt.rcParams['figure.figsize'] = (12, 6)

# fig, ax = plt.subplots()

# number_counts_sorted.plot(kind='bar')

# plt.title('Strike Frequency each year')

# plt.xlabel('Year')
# plt.ylabel('Strike Frequency')

# for spine in ['top', 'right']:
#     ax.spines[spine].set_visible(False)

# fig.tight_layout()



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
# ax.set_xticklabels(ax.get_xticks(), rotation=90)



# data = (3, 6, 9, 12)

# fig, simple_chart = plt.subplots()

# simple_chart.plot(data)

plt.show()