from matplotlib import pyplot as plt

# line charts
months = [1, 2, 3, 4, 5, 6]
income1 = [1000, 40000, 50000, 76500, 95000, 200000]
income2 = [20000, 60000, 80000, 90000, 30000, 70000]
# decorating
plt.plot(months, income1, marker="*", color="red")
plt.plot(months, income2, marker="o", color="yellow")
plt.title("Income of company 1 and company 2\n")
plt.xlabel("\nMonths")
plt.ylabel("Income\n")
plt.legend(["Company 1", "Company 2"])
plt.grid()
plt.show()

# Bar Chart
days = ["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
day_temp = [23, 25, 34, 21, 22, 32, 12]
night_temp= [12,11,17,9,10,13,7]
# decorating
plt.bar(days, day_temp, color="orange")
plt.bar(days, night_temp,color="black")
plt.title("Temperature Record of Last Week\n")
plt.xlabel("\nDays")
plt.ylabel("Temperature (°C) \n")
plt.legend(["Day Temperature", "Night Temperature"])
plt.grid()
plt.show()

#Pie Chart
continents = ["North America","South America","Europe","Asia","Africa"]
population = [597000000, 422000000, 741000000, 4463000000, 1216000000]
explode=(0,0,0.1,0,0)
colors=("red","tomato","mistyrose","brown","maroon")
plt.pie(population, labels=continents, autopct="%1.1f%%", startangle=45, explode=explode, colors=colors)
plt.legend(continents)
plt.title("World Population by Continents\n")
plt.axis("equal")
plt.show()