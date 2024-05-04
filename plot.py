from fetch_data import *

def circle_chart(df):

    chart = alt.Chart(df).mark_circle(size=200).encode(
        x=alt.X("date:T", title= "", axis=alt.Axis(labelAngle=-45)),
        y=alt.Y("hour:N", title="Hora"),
        color=alt.Color("name", title="")
    ).interactive()

    return chart    


def bar_distribution_chart(df):
    chart = alt.Chart(df).mark_bar().encode(
        y=alt.Y('week(date):O', title = "Semana" ),
        x=alt.X('count():Q', title = "Cacas"),
        color=alt.Color("name", title="")
    ).properties(width=700)
    return chart


def bar_distribution_per_person_chart(df):
    chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('hour:N', title = "Hora del Día"),
    y=alt.Y('count():Q', title = ""),
    color=alt.Color("name", title=""),
    row=alt.Row("name", title="")
    ).properties(width=700, height=100)

    return chart