import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Airplane_Strikes_Dataset.csv')

##### Displays strike frequency each year #####
YearColumn = df['Incident Year']
number_counts = YearColumn.value_counts()

number_counts_sorted= number_counts.sort_index()

plt.rcParams['figure.figsize'] = (12, 6)

fig, ax = plt.subplots()

number_counts_sorted.plot(kind='bar')

# bar_color = color
# for bar in bars:
#   ax.text(
#       bar.get_x() + bar.get_width() / 2,
#       bar.get_height() + 0.3,
#       round(bar.get_height(), 1),
#       horizontalalignment='center',
#       color=bar_color,
#       weight='bold'
#   )


plt.title('Strike Frequency each year')

plt.xlabel('Year')
plt.ylabel('Strike Frequency')

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

fig.tight_layout()



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