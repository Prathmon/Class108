import plotly.figure_factory as ff
import pandas as pd
import csv

file1 = pd.read_csv("data.csv")
figure = ff.create_distplot([file1["Height(Inches)"].tolist()], ["Height"], show_hist = False)
figure.show()