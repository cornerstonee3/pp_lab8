import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
data = {
 "Traveler_ID": range(1, 21),
 "Destination": np.random.choice(["Paris", "Tokyo", "Rome", "Istanbul", "New York",
"Dubai"], 20),
 "Days_Spent": np.random.randint(2, 14, 20),
 "Total_Cost": np.random.randint(500, 5000, 20),
 "Age": np.random.randint(18, 60, 20),
 "Travel_Type": np.random.choice(["Solo", "Family", "Friends", "Couple"], 20),
 "Transport_Mode": np.random.choice(["Plane", "Train", "Car", "Bus"], 20),
 "Satisfaction_Rating": np.random.randint(1, 6, 20) # 1–5 scale
}
df=pd.DataFrame(data)
#Part1
#task1
# print("First 5:")
# print(df.head())
# print("Last 5:")
# print(df.tail())
# #task2
# total_travelers=df["Traveler_ID"].nunique()
# uni_dest=df["Destination"].nunique()
# print(f"Travelers: {total_travelers}")
# print(f"Destinations: {uni_dest}")
# #task3
# days_cost=df.groupby("Travel_Type")[["Days_Spent", "Total_Cost"]].mean()
# print("average number of days spent and total cost per travel type:")
# print(round(days_cost, 2))
# #task4
# best_dest=df.groupby("Destination")["Satisfaction_Rating"].mean().idxmax()
# best_rating=df.groupby("Destination")["Satisfaction_Rating"].mean().max()
# print(f"Highest satisfaction rating(avg) destination: {best_dest} ({best_rating:.2f})")
# #task5
# rich=df.loc[df["Total_Cost"].idxmax()]
# print("Traveler who spent the most money:")
# print(rich)
#Part2
# #task6
# avg_cost_per_dest = df.groupby("Destination")["Total_Cost"].mean().sort_values(ascending=False)
# sns.barplot(x=avg_cost_per_dest.index, y=avg_cost_per_dest.values)
# plt.title("avg cost per destination")
# plt.xlabel("Destination")
# plt.ylabel("Average Cost")
# plt.show()
# #task7
# plt.hist(df["Satisfaction_Rating"], bins=5, color="orange", edgecolor="black")
# plt.title("Distribution of Satisfaction Ratings")
# plt.xlabel("Satisfaction Rating")
# plt.ylabel("Number of Travelers")
#plt.grid(True)
# plt.show()
# #task8
# sns.scatterplot(data=df, x="Days_Spent", y="Total_Cost", hue="Travel_Type", style="Transport_Mode")
# plt.title("Days Spent vs Total Cost")
# plt.grid(True)
# plt.show()
#task9
# sns.boxplot(data=df, x="Travel_Type", y="Total_Cost", palette="Set2")
# plt.title("Total Cost Distribution by Travel Type")
# plt.grid(True)
# plt.show()
# #task10
# corr = df[["Days_Spent", "Total_Cost", "Age", "Satisfaction_Rating"]].corr()
# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()
#Part3
# #task11
# transport=df["Transport_Mode"].value_counts()
# plt.pie(
#     transport,
#     labels=transport.index
# )
# plt.title("Proportion of Travelers by Transport Mode")
# plt.show()
# #task12
# df_sorted = df.sort_values("Traveler_ID")
# ax = df_sorted.plot(
#     x="Traveler_ID",
#     y="Total_Cost",
#     kind="line",
#     marker="o",
#     color="blue",
#     grid=True,
#     title="Total Cost per Traveler",
# )
# ax.set_xlabel("Traveler ID")
# ax.set_ylabel("Total Cost ($)")
# plt.show()
# #task13
# num_cols = ["Days_Spent", "Total_Cost", "Age", "Satisfaction_Rating"]
# sns.pairplot(df[num_cols], corner=True)
# plt.suptitle("Pairplot of Numeric Variables", y=1.02)
# plt.show()
#task14
sns.countplot(data=df, x="Destination", hue="Travel_Type")
plt.title("Count of Travel Types per Destination")
plt.xlabel("Destination")
plt.ylabel("Number of Travelers")
plt.grid(True)
plt.show()
