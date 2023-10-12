# Import pandas and matplotlib libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a dataframe
df = pd.read_csv("nycflights.csv")

# Count the number of late and non-late flights at airports
df["late"] = df["dep_delay"] > 0 # Create a new column to indicate if the flight is late or not
late_count = df.groupby("origin")["late"].sum() # Sum up the number of late flights by origin
total_count = df.groupby("origin")["late"].count() # Count the total number of flights by origin
non_late_count = total_count - late_count # Subtract the number of late flights from the total to get the number of non-late flights

# Create a table showing the number of late flights vs. not late
table = pd.DataFrame({"Late": late_count, "Not Late": non_late_count}) # Create a dataframe with the two columns
print(table) # Print the table

# Draw a chart showing the number of late flights vs. not late
table.plot.bar(stacked=True) # Plot a stacked bar chart with the table data
plt.title("Number of Late Flights vs. Not Late Flights by Airport") # Add a title to the chart
plt.xlabel("Airport") # Add a label to the x-axis
plt.ylabel("Number of Flights") # Add a label to the y-axis
plt.show() # Show the chart

# Do the same with airlines
late_count = df.groupby("carrier")["late"].sum() # Sum up the number of late flights by carrier
total_count = df.groupby("carrier")["late"].count() # Count the total number of flights by carrier
non_late_count = total_count - late_count # Subtract the number of late flights from the total to get the number of non-late flights

# Create a table showing the number of late flights vs. not late
table = pd.DataFrame({"Late": late_count, "Not Late": non_late_count}) # Create a dataframe with the two columns
print(table) # Print the table

# Draw a chart showing the number of late flights vs. not late
table.plot.bar(stacked=True) # Plot a stacked bar chart with the table data
plt.title("Number of Late Flights vs. Not Late Flights by Airline") # Add a title to the chart
plt.xlabel("Airline") # Add a label to the x-axis
plt.ylabel("Number of Flights") # Add a label to the y-axis
plt.show() # Show the chart

# Calculate the average delay time of the firms
df["delay"] = df["dep_delay"] + df["arr_delay"] # Create a new column to indicate the total delay time
avg_delay = df.groupby("carrier")["delay"].mean() # Calculate the mean delay time by carrier

# Calculate average delay time from airports
avg_delay_origin = df.groupby("origin")["delay"].mean() # Calculate the mean delay time by origin

# Plot the results on a graph
avg_delay.plot.bar() # Plot a bar chart with the average delay time by carrier
plt.title("Average Delay Time by Airline") # Add a title to the chart
plt.xlabel("Airline") # Add a label to the x-axis
plt.ylabel("Delay Time (minutes)") # Add a label to the y-axis
plt.show() # Show the chart

avg_delay_origin.plot.bar() # Plot a bar chart with the average delay time by origin
plt.title("Average Delay Time by Airport") # Add a title to the chart
plt.xlabel("Airport") # Add a label to the x-axis
plt.ylabel("Delay Time (minutes)") # Add a label to the y-axis
plt.show() # Show the chart

# Calculate the total, average, mean, median of each airline's flight distance
total_distance = df.groupby("carrier")["distance"].sum() # Calculate the sum of distance by carrier
avg_distance = df.groupby("carrier")["distance"].mean() # Calculate the mean of distance by carrier
median_distance = df.groupby("carrier")["distance"].median() # Calculate the median of distance by carrier

# Create a table showing these statistics
table = pd.DataFrame({"Total Distance": total_distance, "Average Distance": avg_distance, "Median Distance": median_distance}) # Create a dataframe with these columns
print(table) # Print the table

