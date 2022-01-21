import numpy as np
import pandas as pd
import squarify
import matplotlib
import matplotlib.pyplot as plt
import datapane as dp

# Volumes per day
df_day = pd.read_csv('data/volumes per day.csv')
# Bar Plot: Orders/Lines
orderlines = ([dp.Plot(df_day[df_day['WEEK'] ==wk].plot.bar(figsize=(8, 6), edgecolor='black', x='DAY', y=['ORDERS', 'LINES'], color=['tab:blue', 'tab:red'], legend= True), 
label = wk)
for wk in df_day['WEEK'].unique()])
plt.xlabel('DAY', fontsize = 12)
plt.title('Workload per day (Lines/day)', fontsize = 12)
plt.show()
# Bar Plot: Lines/Pcs
linespcs = ([dp.Plot(df_day[df_day['WEEK'] ==wk].plot.bar(figsize=(8, 6), edgecolor='black', x='DAY', y=['LINES', 'PCS'], 
color=['tab:orange', 'tab:green'], legend= True), 
label = wk)
for wk in df_day['WEEK'].unique()])
plt.xlabel('DAY', fontsize = 12)
plt.title('Volumes per day (Pieces/day)', fontsize = 12)
plt.show()
# Line Plot: Cities Delivered
cities = df_day.plot(figsize=(10, 6), 
                 x='DATE', y='CITIES', color=['darkblue'], legend= True)
plt.xlabel('DAY', fontsize = 12)
plt.axhline(y = df_day['CITIES'].mean(), color = 'red', linestyle='--')
plt.title('Cities delivered per day', fontsize = 12)
plt.show()

# Lines per Order Split
df_lior = pd.read_csv('data/lines per order.csv', index_col = 0)
df_lior.reset_index(inplace = True)
COLS_IN = list(df_lior.columns[2:8])
# Bar Plot: split per lines per orders
lines_orders = df_lior.plot.bar(figsize=(10, 6), edgecolor='black', x='WEEK', y=COLS_IN[0], color='tab:blue', legend= True)
df_lior.plot.bar(figsize=(10, 6), edgecolor='black', x='WEEK', y=COLS_IN[1], color='tab:red', legend= True, ax = lines_orders)
df_lior.plot.bar(figsize=(10, 6), edgecolor='black', x='WEEK', y=COLS_IN[2], color='tab:orange', legend= True, ax = lines_orders)
df_lior.plot.bar(figsize=(10, 6), edgecolor='black', x='WEEK', y=COLS_IN[3], color='darkblue', legend= True, ax = lines_orders)
df_lior.plot.bar(figsize=(10, 6), edgecolor='black', x='WEEK', y=COLS_IN[4], color='brown', legend= True, ax = lines_orders)
df_lior.plot.bar(figsize=(10, 6), edgecolor='black', x='WEEK', y=COLS_IN[5], color='grey', legend= True, ax = lines_orders)
plt.xlabel('Week', fontsize = 12)
plt.ylabel('Number of Orders', fontsize = 12)
plt.title('Split of orders by number of lines/order', fontsize = 12)
plt.show()

# Pareto Analysis
df_pareto = pd.read_csv('data/pareto.csv', index_col = 0)
WEEKS = df_day['WEEK'].unique()
# Line Plot
paretoplot1 = df_pareto.plot(figsize=(12, 7), y=WEEKS[0], color='tab:orange', legend = False)
plt.xlabel('Number of SKU', fontsize = 12)
plt.title('Pareto of Sales (%SKU)', fontsize = 12)
plt.axhline(y = 80, color = 'black', linestyle='--')
plt.axvline(x = 20, color = 'blue', linestyle='--')
plt.axvline(x = df_pareto[df_pareto[WEEKS[0]]>80].index[0], color = 'black', linestyle='--')
plt.xlabel('SKU (%)')
plt.ylabel('PCS (%)')
plt.show()
# Line Plot
paretoplot2 = df_pareto.plot(figsize=(12, 7), y=WEEKS[1], color='black', legend = False)
plt.xlabel('Number of SKU', fontsize = 12)
plt.title('Pareto of Sales (%SKU)', fontsize = 12)
plt.axhline(y = 80, color = 'black', linestyle='--')
plt.axvline(x = 20, color = 'blue', linestyle='--')
plt.axvline(x = df_pareto[df_pareto[WEEKS[1]]>80].index[0], color = 'black', linestyle='--')
plt.xlabel('SKU (%)')
plt.ylabel('PCS (%)')
plt.show()
# Line Plot
paretoplot3 = df_pareto.plot(figsize=(12, 7), y=WEEKS[2], color='tab:purple', legend = False)
plt.xlabel('Number of SKU', fontsize = 12)
plt.title('Pareto of Sales (%SKU)', fontsize = 12)
plt.axhline(y = 80, color = 'black', linestyle='--')
plt.axvline(x = 20, color = 'blue', linestyle='--')
plt.axvline(x = df_pareto[df_pareto[WEEKS[2]]>80].index[0], color = 'black', linestyle='--')
plt.xlabel('SKU (%)')
plt.ylabel('PCS (%)')
plt.show()
# Line Plot
paretoplot4 = df_pareto.plot(figsize=(12, 7), y=WEEKS[3], color='tab:blue', legend = False)
plt.xlabel('Number of SKU', fontsize = 12)
plt.title('Pareto of Sales (%SKU)', fontsize = 12)
plt.axhline(y = 80, color = 'black', linestyle='--')
plt.axvline(x = 20, color = 'blue', linestyle='--')
plt.axvline(x = df_pareto[df_pareto[WEEKS[3]]>80].index[0], color = 'black', linestyle='--')
plt.xlabel('SKU (%)')
plt.ylabel('PCS (%)')
plt.show()
# Line Plot
paretoplot5 = df_pareto.plot(figsize=(12, 7), y=WEEKS[4], color='tab:green', legend = False)
plt.xlabel('Number of SKU', fontsize = 12)
plt.title('Pareto of Sales (%SKU)', fontsize = 12)
plt.axhline(y = 80, color = 'black', linestyle='--')
plt.axvline(x = 20, color = 'blue', linestyle='--')
plt.axvline(x = df_pareto[df_pareto[WEEKS[4]]>80].index[0], color = 'black', linestyle='--')
plt.xlabel('SKU (%)')
plt.ylabel('PCS (%)')
plt.show()

# Number of replenishments
df_repcount = pd.read_csv('data/replenishments.csv', index_col = 0)
# Bar Plot
repldays = ([dp.Plot(df_repcount.plot.bar(figsize=(8, 6), edgecolor='blue', y=wk, color=['tab:green'], legend= True), 
label = wk)
for wk in df_day['WEEK'].unique()])
plt.xlabel('DAY', fontsize = 12)
plt.title('Number of Replenishments per day', fontsize = 12)
plt.show()

# Replenishments per Picking Cell
df_repl = pd.read_csv('data/replenishments details.csv')
dict_color = dict(zip(['A06', 'A07', 'A05', 'A04', 'A02', 'R04', 'A03', 'A01', 'A08','R05', 'A09', 'A10', 'A11', 'H02', 'B03', 'R06'],
['blue', 'red', 'yellow', 'orange', 'brown', 'cyan', 'tab:blue', 'tab:red', 'lightblue', 'tab:orange', 'grey', 'tab:green', 'purple', 'darkblue', 'white', 'magenta']))
# Treemap 1
wk = df_day['WEEK'].unique()[0]
df_plot = df_repl[df_repl[wk]>0][['Alley', wk]].copy()
df_plot = pd.DataFrame(df_plot.groupby(['Alley'])[wk].sum())
df_plot['%'] = (100*df_plot[wk]/df_plot[wk].sum()).round(2)
df_plot.reset_index(inplace = True)
df_plot['LABEL'] = df_plot[['Alley','%']].apply(lambda t: t['Alley'] +'\n' + str(t['%']) + '%', axis = 1)

plt.figure(figsize=(15, 12))
tree_map1 = squarify.plot(sizes = df_plot[wk], color=df_plot['Alley'].map(dict_color)
            , label = df_plot['LABEL']
            , edgecolor="#222222", text_kwargs={'fontsize':12})
plt.axis('on')
plt.title('Number of Replenishments per Picking Cell' +'\n', fontsize=12)
tree_map1.axes.xaxis.set_visible(False)
tree_map1.axes.yaxis.set_visible(False)
plt.show()
del df_plot
# Treemap 2
wk = df_day['WEEK'].unique()[1]
df_plot = df_repl[df_repl[wk]>0][['Alley', wk]].copy()
df_plot = pd.DataFrame(df_plot.groupby(['Alley'])[wk].sum())
df_plot['%'] = (100*df_plot[wk]/df_plot[wk].sum()).round(2)
df_plot.reset_index(inplace = True)
df_plot['LABEL'] = df_plot[['Alley','%']].apply(lambda t: t['Alley'] +'\n' + str(t['%']) + '%', axis = 1)

plt.figure(figsize=(15, 12))
tree_map2 = squarify.plot(sizes = df_plot[wk], color=df_plot['Alley'].map(dict_color)
            , label = df_plot['LABEL']
            , edgecolor="#222222", text_kwargs={'fontsize':12})
plt.axis('on')
plt.title('Number of Replenishments per Picking Cell' +'\n', fontsize=12)
tree_map2.axes.xaxis.set_visible(False)
tree_map2.axes.yaxis.set_visible(False)
plt.show()
del df_plot
# Treemap 3
wk = df_day['WEEK'].unique()[2]
df_plot = df_repl[df_repl[wk]>0][['Alley', wk]].copy()
df_plot = pd.DataFrame(df_plot.groupby(['Alley'])[wk].sum())
df_plot['%'] = (100*df_plot[wk]/df_plot[wk].sum()).round(2)
df_plot.reset_index(inplace = True)
df_plot['LABEL'] = df_plot[['Alley','%']].apply(lambda t: t['Alley'] +'\n' + str(t['%']) + '%', axis = 1)

plt.figure(figsize=(15, 12))
tree_map3 = squarify.plot(sizes = df_plot[wk], color=df_plot['Alley'].map(dict_color)
            , label = df_plot['LABEL']
            , edgecolor="#222222", text_kwargs={'fontsize':12})
plt.axis('on')
plt.title('Number of Replenishments per Picking Cell' +'\n', fontsize=12)
tree_map3.axes.xaxis.set_visible(False)
tree_map3.axes.yaxis.set_visible(False)
plt.show()
del df_plot
# Treemap 4
wk = df_day['WEEK'].unique()[3]
df_plot = df_repl[df_repl[wk]>0][['Alley', wk]].copy()
df_plot = pd.DataFrame(df_plot.groupby(['Alley'])[wk].sum())
df_plot['%'] = (100*df_plot[wk]/df_plot[wk].sum()).round(2)
df_plot.reset_index(inplace = True)
df_plot['LABEL'] = df_plot[['Alley','%']].apply(lambda t: t['Alley'] +'\n' + str(t['%']) + '%', axis = 1)

plt.figure(figsize=(15, 12))
tree_map4 = squarify.plot(sizes = df_plot[wk], color=df_plot['Alley'].map(dict_color)
            , label = df_plot['LABEL']
            , edgecolor="#222222", text_kwargs={'fontsize':12})
plt.axis('on')
plt.title('Number of Replenishments per Picking Cell' +'\n', fontsize=12)
tree_map4.axes.xaxis.set_visible(False)
tree_map4.axes.yaxis.set_visible(False)
plt.show()
del df_plot
# Treemap 5
wk = df_day['WEEK'].unique()[4]
df_plot = df_repl[df_repl[wk]>0][['Alley', wk]].copy()
df_plot = pd.DataFrame(df_plot.groupby(['Alley'])[wk].sum())
df_plot['%'] = (100*df_plot[wk]/df_plot[wk].sum()).round(2)
df_plot.reset_index(inplace = True)
df_plot['LABEL'] = df_plot[['Alley','%']].apply(lambda t: t['Alley'] +'\n' + str(t['%']) + '%', axis = 1)

plt.figure(figsize=(15, 12))
tree_map5 = squarify.plot(sizes = df_plot[wk], color=df_plot['Alley'].map(dict_color)
            , label = df_plot['LABEL']
            , edgecolor="#222222", text_kwargs={'fontsize':12})
plt.axis('on')
plt.title('Number of Replenishments per Picking Cell' +'\n', fontsize=12)
tree_map5.axes.xaxis.set_visible(False)
tree_map5.axes.yaxis.set_visible(False)
plt.show()
del df_plot

# # Plot Orders Lines per day
# dp.Report(
#   dp.Page(
#     dp.Select(blocks = orderlines)
#   )
# ).upload(name='orders/lines per day')
# # Plot Pieces per day
# dp.Report(
#   dp.Page(
#     dp.Select(blocks = linespcs)
#   )
# ).upload(name='pieces per day')
# # Cities delivered per day
# dp.Report(
#   dp.Page(
#     title="Page 1",
#     blocks=[ cities]
#   )
# ).upload(name='cities per day')
# # Lines per order
# dp.Report(
#   dp.Page(
#     title="Page 1",
#     blocks=[ lines_orders]
#   )
# ).upload(name='lines per order')
# dp.Report(
#   dp.Page(
#     title="WEEK-1",
#     blocks=[paretoplot1]
#   ),
#   dp.Page(
#     title="WEEK-2",
#     blocks=[paretoplot2]
#   ),
#   dp.Page(
#     title="WEEK-3",
#     blocks=[paretoplot3]
#   ),
#   dp.Page(
#     title="WEEK-4",
#     blocks=[paretoplot4]
#   ),
#     dp.Page(
#     title="WEEK-5",
#     blocks=[paretoplot5]
#   )
# ).upload(name='pareto analysis')
# # Plot Replenishments
# dp.Report(
#   dp.Page(
#     dp.Select(blocks = repldays)
#   )
# ).upload(name='replenishments per day')
# Replenishment per cell
dp.Report(
    dp.Page(
    title="WEEK-1",
    blocks=[tree_map1]
  ),
    dp.Page(
    title="WEEK-2",
    blocks=[tree_map2]
  ),
    dp.Page(
    title="WEEK-3",
    blocks=[tree_map3]
  ),
    dp.Page(
    title="WEEK-4",
    blocks=[tree_map4]
  ),
    dp.Page(
    title="WEEK-5",
    blocks=[tree_map5]
  )
).upload(name='treemap replenishment')