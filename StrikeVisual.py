import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np
from scipy import stats
from scipy.stats import linregress

df = pd.read_csv('Airplane_Strikes_Dataset.csv')

##### frequency of which operator hit the bird #####
# operator_counts = df['Operator'].value_counts()

# # Select the top n values
# top_15_operators = operator_counts.head(15)

# # Create a bar graph to display the frequency of each unique entry
# plt.figure(figsize=(12, 6))
# operator_counts.plot(kind='bar', x='Operator', y='Frequency')
# plt.title('Frequency of Each Operator')
# plt.xlabel('Operator')
# plt.ylabel('Frequency')
# plt.xticks(rotation=90)


##### Displays the wildlife that was struck #####
# species_counts = df['Species Name'].value_counts()

# top_30_species = species_counts.head(30)

# # Create a bar graph to display the occurrence of each unique entry
# plt.figure(figsize=(12, 6))
# top_30_species.plot(kind='bar', x='Flight Phase', y='Count')
# plt.title('Species strike frequency')
# plt.xlabel('Species')
# plt.ylabel('Count')

##### Displays the phase where the strikes took place #####
# flight_phase_counts = df['Flight Phase'].value_counts()

# # Create a bar graph to display the occurrence of each unique entry
# plt.figure(figsize=(12, 6))
# flight_phase_counts.plot(kind='bar', x='Flight Phase', y='Count')
# plt.title('Occurrence of Strikes in Each Flight Phase')
# plt.xlabel('Flight Phase')
# plt.ylabel('Count')
# plt.xticks(rotation=45)



##### Displays the frequency of each State #####
# state_counts = df['State'].value_counts()

# # Create a bar graph to display the frequency of each state
# plt.figure(figsize=(12, 6))
# state_counts.plot(kind='bar', x='State', y='Frequency')
# plt.title('Frequency of Each State in Incidents')
# plt.xlabel('State')
# plt.ylabel('Frequency')
# plt.xticks(rotation=90)  # Rotate x-axis labels for better readability


##### Displays the number of strikes in each state each month #####
# df['YearMonth'] = df['Incident Year'].astype(str) + '-' + df['Incident Month'].astype(str)
# df['Incident Month'] = df['Incident Month'].apply(lambda x: calendar.month_name[x])

# # Create a custom order for months
# month_order = [calendar.month_name[i] for i in range(1, 13)]

# # Group the data by 'State' and 'Month' and count the occurrences
# state_month_counts = df.groupby(['State', 'Incident Month']).size().unstack().fillna(0)
# state_month_counts = state_month_counts.reindex(columns=month_order)  # Reorder the columns

# # Limit the number of displayed states to the top N states with the highest occurrences
# top_n_states = 20
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

# month_counts = df['Incident Month'].value_counts()

# # Shift the months down by one (start from February and end in January)
# sorted_months = [calendar.month_name[i] for i in range(2, 13)] + ['January']
# month_counts = month_counts.reindex(sorted_months, fill_value=0)

# num_years = df['Incident Year'].nunique()
# average_month_counts = month_counts / num_years

# plt.figure(figsize=(12, 6))

# # Create a bar graph to display the average occurrences of each month
# ax = average_month_counts.plot(kind='bar', x='Incident Month', y='Average Count')
# plt.title('Average Number of Strikes Each Month')
# plt.xlabel('Incident Month')
# plt.ylabel('Number of Strikes')
# plt.xticks(rotation=45)

# # Create a probability plot to assess normality
# plt.figure(figsize=(12, 6))
# stats.probplot(average_month_counts, dist='norm', plot=plt)
# plt.title('Normal Probability Plot for Average Monthly Strikes')
# plt.xlabel('Theoretical Quantiles')
# plt.ylabel('Sample Quantiles')

# # Display the values on top of each bar
# for p in ax.patches:
#     ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
#                 textcoords='offset points')

# plt.tight_layout()




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


##### Shows where damage occurs on the plane #####
# locations = ['Radome Damage' , 'Windshield Damage' , 'Nose Damage' , 'Engine1 Damage' , 'Engine2 Damage' , 'Engine3 Damage' , 'Engine4 Damage' , 'Propeller Damage' , 'Wing or Rotor Damage' , 'Fuselage Damage' , 'Landing Gear Damage' , 'Tail Damage' , 'Lights Damage' , 'Other Damage']
# filtered_df = df[locations]
# column_sums = filtered_df.sum()
# column_sums_sorted = column_sums.sort_values(ascending=False)

# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
# ax = column_sums_sorted.plot(kind='bar')
# plt.title('Number of Damages in each location')
# plt.xlabel('Location')
# plt.ylabel('Number of Damages')
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels and align them to the right
# plt.tight_layout()  # Ensure all labels are visible within the plot

# for i, v in enumerate(column_sums_sorted):
#     ax.text(i, v, str(v), ha='center', va='bottom')

# for spine in ['top', 'right']:
#     ax.spines[spine].set_visible(False)



##### Displays strike frequency each year #####
YearColumn = df['Incident Year']
number_counts = YearColumn.value_counts()

number_counts_sorted = number_counts.sort_index()

plt.rcParams['figure.figsize'] = (12, 6)

fig, ax = plt.subplots()

number_counts_sorted.plot(kind='line')

# Calculate the trend line
x_values = number_counts_sorted.index
y_values = number_counts_sorted.values

slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)
trend_line = slope * x_values + intercept

# Plot the trend line
plt.plot(x_values, trend_line, label=f'Trend Line (y = {slope:.2f}x + {intercept:.2f})', color='red')

plt.title('Strike Frequency each year')
plt.xlabel('Year')
plt.ylabel('Strike Frequency')

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.legend()  # Display the legend with the trend line

fig.tight_layout()
plt.show()

# Print the formula of the trend line
print(f'Trend Line Formula: y = {slope:.2f}x + {intercept:.2f}')



#### Displays all data #####
df.plot.line(x = 'Incident Year')


##### Displays frequency of each type of engine in each strike ######
column_to_analyze = df['Engine Type']

letter_counts = column_to_analyze.str.lower().str.replace(r'[^a-z]', '', regex=True).value_counts()

plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
letter_counts.plot(kind='bar')
plt.title('Engine Type Strike Frequency')
plt.xlabel('Engine Type')
plt.ylabel('Frequency')
ax.set_xticklabels(ax.get_xticks(), rotation=90)



data = (3, 6, 9, 12)

fig, simple_chart = plt.subplots()

simple_chart.plot(data)




##### Displays the probability a part of a plane is damaged if struck #####

# # Define the list of locations for strikes and damages
# strike_locations = ['Radome Strike' , 'Windshield Strike' , 'Nose Strike' , 'Engine1 Strike' , 'Engine2 Strike' , 'Engine3 Strike' , 'Engine4 Strike' , 'Propeller Strike' , 'Wing or Rotor Strike' , 'Fuselage Strike' , 'Landing Gear Strike' , 'Tail Strike' , 'Lights Strike' , 'Other Strike']

# damage_locations = ['Radome Damage' , 'Windshield Damage' , 'Nose Damage' , 'Engine1 Damage' , 'Engine2 Damage' , 'Engine3 Damage' , 'Engine4 Damage' , 'Propeller Damage' , 'Wing or Rotor Damage' , 'Fuselage Damage' , 'Landing Gear Damage' , 'Tail Damage' , 'Lights Damage' , 'Other Damage']

# # Filter the DataFrame to include only the relevant columns for strikes and damages
# filtered_strike_df = df[strike_locations]
# filtered_damage_df = df[damage_locations]

# # Calculate the total number of strikes and damages for each location
# strike_counts = filtered_strike_df.sum()
# damage_counts = filtered_damage_df.sum()

# strike_counts.index = strike_counts.index.str.split().str[0]
# damage_counts.index = damage_counts.index.str.split().str[0]

# # Calculate the probability of damage if struck for each location
# probability_damage_if_struck = damage_counts.divide(strike_counts)

# # # Sort the locations by probability in descending order
# # probability_damage_if_struck_sorted = probability_damage_if_struck.sort_values(ascending=False)

# print("Strike Counts:")
# print(strike_counts)
# print(strike_counts.dtype)
# print("Damage Counts:")
# print(damage_counts)
# print(damage_counts.dtype)

# # Calculate the probability of damage if struck for each location
# probability_damage_if_struck = damage_counts.divide(strike_counts)
# probability_damage_if_struck_sorted = probability_damage_if_struck.sort_values(ascending=False)

# # Create a bar graph to display the probabilities
# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
# ax = probability_damage_if_struck_sorted.plot(kind='bar')
# plt.title('Probability of Damage if Struck for Each Location')
# plt.xlabel('Location')
# plt.ylabel('Probability')
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels and align them to the right
# plt.tight_layout()  # Ensure all labels are visible within the plot

# for i, v in enumerate(probability_damage_if_struck_sorted):
#     ax.text(i, v, f'{v:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()