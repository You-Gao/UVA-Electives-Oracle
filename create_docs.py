import pandas as pd

file = "Fun Electives.csv"

df = pd.read_csv(file)

with open("test.html", "w") as w:
    w.write(df.to_html())