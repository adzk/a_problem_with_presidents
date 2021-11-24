# importing libraries
import psycopg2
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

conn = psycopg2.connect(
    host='localhost',
    database='xyz',
    user='********',
    password='********'
)

# President table with additional columns
president_additions = f"""select id, name, birth_date, birth_place, death_date, death_location, birth_year, lived_years, lived_months, lived_days, alive from public.president_additions order by id ASC"""

df_president_additions = pd.read_sql_query(president_additions, con=conn)
print(df_president_additions.to_string())

# President Longest Lived
president_longest_lived = f"""select id, name, birth_date, birth_place, death_date, death_location, birth_year, lived_years, lived_months, lived_days, alive from public.president_longest_lived """

df_president_longest_lived = pd.read_sql_query(president_longest_lived, con=conn)
print(df_president_longest_lived.to_string())

# President Longest Lived
president_shortest_lived = f"""select id, name, birth_date, birth_place, death_date, death_location, birth_year, lived_years, lived_months, lived_days, alive from public.president_shortest_lived """

df_president_shortest_lived = pd.read_sql_query(president_shortest_lived, con=conn)
print(df_president_shortest_lived.to_string())

# President Statistics
president_statistics = f"""select mean, weighted_mean, median, mode, min, max, standard_deviation from public.president_statistics"""

df_president_statistics = pd.read_sql_query(president_statistics, con=conn)
print(df_president_statistics.to_string())

# TABLES
fig1 = ff.create_table(df_president_additions)
fig1.show()

fig1a = ff.create_table(df_president_longest_lived)
fig1a.show()

fig1b = ff.create_table(df_president_shortest_lived)
fig1b.show()

fig3 = ff.create_table(df_president_statistics)
fig3.show()

# PLOT
fig2 = px.scatter(df_president_additions, x="name", y="lived_days", color="alive")

fig2.add_hline(
    y=26371.6444444,
    line_dash='dot',
    annotation_text='Mean: 26371.6444444',
    annotation_position='top right',
    annotation_font_color="black",
    line_color="black"
)

fig2.add_hline(
    y=26227,
    line_dash='solid',
    annotation_text='Median: 26227',
    annotation_position='bottom left',
    annotation_font_color="blue",
    line_color="blue"
)

fig2.add_hline(
    y=16978,
    line_dash='dash',
    annotation_text='Mode: 16978',
    annotation_position='bottom right',
    annotation_font_color="red",
    line_color="red"
)

fig2.add_hline(
    y=16978,
    line_dash='dot',
    annotation_text='Min: 16978',
    annotation_position='top right',
    annotation_font_color="green",
    line_color="green"
)

fig2.add_hline(
    y=35480,
    line_dash='dot',
    annotation_text='Max: 35480',
    annotation_position='top right',
    annotation_font_color="orange",
    line_color="orange"
)

std1 = 26371.644444 - 4566.857449
std2 = 26371.644444 + 4566.857449

fig2.add_hrect(y0=std1,
               y1=std2,
               line_width=0,
               fillcolor="yellow",
               opacity=0.2,
               annotation_text="Standard Deviation",
               annotation_position='top right',
               annotation=dict(font_color="gold"))

fig2.show()

conn.close()