import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file = input("What is the full path to the file to be visualized?\n")
file = file.strip('"')
# print(file)
def headers():
    has_headers = input('Does the data have headers?(Y/N)\n').lower()
    if has_headers == 'y' or has_headers == 'yes':
        has_headers = True
    elif has_headers == 'n' or has_headers == 'no':
        has_headers = False
    else:
        headers()
    return has_headers
has_headers = headers()
def make_headers(file):
    headers = input("Name headers separated by commas\n")
    headers = headers.split(',')
    return headers
if has_headers:
    headers = pd.read_excel(file).columns
else:
    headers = make_headers(file)

all_data = pd.read_excel(file)
#time series
#have user select which values to keep in the plot
keep = input("Select which item to plot as column:value separated by commas\n")
# main_plot
# list1 = 'Country:Canada,Product:VTT,Segment:Government'
keep = keep.split(',')
p = all_data
for item in keep:
    item = item.split(':')
    p = p.loc[(p[item[0]]==item[1])]
sort = input('What field do you want the data sorted by?\n')
p = p.sort_values(by=sort)
ax_x, ax_y = input('What fields should be the X and Y axis (separated by comma)?\n').split(',')
p.plot(x=ax_x, y=ax_y)

fig = plt.gcf()
plt.show()
if something:
    fig.savefig('fig1',dpi='figure')