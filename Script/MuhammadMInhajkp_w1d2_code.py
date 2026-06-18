import streamlit as st
import pandas as pd

data = {
    "Name":["Aisha","Bob","Clara","Dev","Eva","Finn","Grace","Hiro","Ines","Jay"],
    "Math":[88,52,76,91,43,67,85,59,78,95],
    "Science":[72,45,88,83,38,71,90,62,55,80],
    "English":[65,70,82,77,60,58,74,88,91,73],
    "Art":[90,85,60,55,78,92,68,75,83,61]
}

df = pd.DataFrame(data)

df["Average"] = df[["Math","Science","English","Art"]].mean(axis=1).round(1)

st.title("🎓 Student Grade Dashboard")

st.write("Total Students:", len(df))

c1, c2, c3, c4 = st.columns(4)

c1.metric("Class Average", round(df["Average"].mean(),1))
c2.metric("Highest Average", df["Average"].max())
c3.metric("Lowest Average", df["Average"].min())
c4.metric("Above 70", len(df[df["Average"] >= 70]))

st.subheader("All Students")

st.dataframe(
    df.style.map(
        lambda v: "color:green" if v >= 70 else "color:red",
        subset=["Average"]
    ),
    hide_index=True,
    use_container_width=True
)

st.subheader("🏆 Top 3 Leaderboard")

top3 = df.sort_values("Average", ascending=False).head(3)

top3.index = [1,2,3]

st.table(top3)

summary = {
    "Math":{
        "min": df["Math"].min(),
        "max": df["Math"].max(),
        "mean": round(df["Math"].mean(),1)
    },
    "Science":{
        "min": df["Science"].min(),
        "max": df["Science"].max(),
        "mean": round(df["Science"].mean(),1)
    },
    "English":{
        "min": df["English"].min(),
        "max": df["English"].max(),
        "mean": round(df["English"].mean(),1)
    },
    "Art":{
        "min": df["Art"].min(),
        "max": df["Art"].max(),
        "mean": round(df["Art"].mean(),1)
    }
}

st.subheader("📊 Subject Summary")

st.json(summary)

st.markdown("---")

st.caption("Week 1 Day 2 Project")