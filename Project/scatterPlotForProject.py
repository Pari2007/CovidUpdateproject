import pandas as pd
import plotly.express as px

df = pd.read_csv("dataForproject.csv")
fig = px.scatter(df, x="date", y="cases",
	            color="country",
                 title="Global Covid Update")
fig.show()
