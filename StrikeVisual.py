import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np

df = pd.read_csv('Airplane_Strikes_Dataset.csv')


##### Displays the phase where the strikes took plave #####
flight_phase_counts = df['Flight Phase'].value_counts()

# Create a bar graph to display the occurrence of each unique entry
plt.figure(figsize=(12, 6))
flight_phase_counts.plot(kind='bar', x='Flight Phase', y='Count')
plt.title('Occurrence of Each Flight Phase')
plt.xlabel('Flight Phase')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



##### Displays the number of strikes in each state each month #####
# df['YearMonth'] = df['Incident Year'].astype(str) + '-' + df['Incident Month'].astype(str)
# df['Incident Month'] = df['Incident Month'].apply(lambda x: calendar.month_name[x])

# # Create a custom order for months
# month_order = [calendar.month_name[i] for i in range(1, 13)]

# # Group the data by 'State' and 'Month' and count the occurrences
# state_month_counts = df.groupby(['State', 'Incident Month']).size().unstack().fillna(0)
# state_month_counts = state_month_counts.reindex(columns=month_order)  # Reorder the columns

# # Limit the number of displayed states to the top N states with the highest occurrences
# top_n_states = 25
# top_states = state_month_counts.sum(axis=1).nlargest(top_n_states).index

# # Create the line graph for the top N states
# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
# for state in top_states:
#     plt.plot(state_month_counts.columns, state_month_counts.loc[state], label=state)

# plt.title('Occurrences of Top States for Each Month')
# plt.xlabel('Incident Month')
# plt.ylabel('Number of Occurrences')
# plt.xticks(rotation=45)
# plt.legend(loc='upper right')
# plt.grid(True, linestyle='--', alpha=0.7)



##### Average strikes a month #####
# df['YearMonth'] = df['Incident Year'].astype(str) + '-' + df['Incident Month'].astype(str)
# df['Incident Month'] = df['YearMonth'].str.split('-').str[1].astype(int)
# df['Incident Month'] = df['Incident Month'].apply(lambda x: calendar.month_name[x])

# # Count the occurrences of each month
# month_counts = df['Incident Month'].value_counts()
# sorted_months = [calendar.month_name[i] for i in range(1, 13)]
# month_counts = month_counts.reindex(sorted_months, fill_value=0)

# # Calculate the number of unique years in the dataset
# num_years = df['Incident Year'].nunique()

# # Calculate the average occurrences of each month every year
# average_month_counts = month_counts / num_years

# plt.figure(figsize=(12, 6))
# average_month_counts.plot(kind='bar', x='Incident Month', y='Average Count')
# plt.title('Average number of strikes each Month')
# plt.xlabel('Incident Month')
# plt.ylabel('Number of strikes')
# plt.xticks(rotation=45)

# plt.tight_layout()
# plt.show()




##### Display where strikes occured most often #####

# locations = ['Radome Strike' , 'Windshield Strike' , 'Nose Strike' , 'Engine1 Strike' , 'Engine2 Strike' , 'Engine3 Strike' , 'Engine4 Strike' , 'Propeller Strike' , 'Wing or Rotor Strike' , 'Fuselage Strike' , 'Landing Gear Strike' , 'Tail Strike' , 'Lights Strike' , 'Other Strike']
# filtered_df = df[locations]
# column_sums = filtered_df.sum()
# column_sums_sorted = column_sums.sort_values(ascending=False)

# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
# ax = column_sums_sorted.plot(kind='bar')
# plt.title('Number of strikes in each location')
# plt.xlabel('Location')
# plt.ylabel('Number of Strikes')
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels and align them to the right
# plt.tight_layout()  # Ensure all labels are visible within the plot

# for i, v in enumerate(column_sums_sorted):
#     ax.text(i, v, str(v), ha='center', va='bottom')

# for spine in ['top', 'right']:
#     ax.spines[spine].set_visible(False)



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

plt.tight_layout()
plt.show()