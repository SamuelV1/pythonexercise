from collections import Counter
import json
import math

from bokeh.plotting import figure, show, output_file


output_file("plot.html")

with open("info2.json", "r") as f:
    DATA = json.load(f)

month_Value = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

months = []
for name, birthday_string in DATA.items():
    
    month = int(birthday_string.split("/")[0])
    
    months.append(month_Value[month])
months = Counter(months)

months, counts = list(zip(*months.items()))

categories = list(month_Value.values())

p = figure(x_range=categories)

p.xaxis.major_label_orientation = math.pi/4

p.vbar(x=months, top=counts)

show(p)