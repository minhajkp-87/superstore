import streamlit as st
import pandas as pd
import datetime

st.title("💳 Personal Expense Tracker")
st.write("Track your expenses with filters, KPIs and downloads")

uploaded = st.file_uploader("Upload expenses.csv", type="csv")

if uploaded:

    df = pd.read_csv(uploaded)
    st.write(df.columns)

    df["Date"] = pd.to_datetime(df["Date"])

    categories = [
        "Food & Dining",
        "Transport",
        "Utilities",
        "Entertainment",
        "Healthcare",
        "Shopping"
    ]

    with st.sidebar:

        date_range = st.date_input(
            "Date Range",
            value=(
                datetime.date(2024, 1, 1),
                datetime.date(2024, 5, 31)
            )
        )

        if isinstance(date_range, tuple) and len(date_range) == 2:
            start, end = date_range

        selected_categories = st.multiselect(
            "Category",
            categories,
            default=categories
        )

        if len(selected_categories) == 0:
            selected_categories = categories

    filtered = df[
        (df["Date"].dt.date >= start) &
        (df["Date"].dt.date <= end)
    ]

    filtered = filtered[
        filtered["Category"].isin(selected_categories)
    ]

    total_spend = filtered["Amount"].sum()
    transactions = len(filtered)
    avg_transaction = filtered["Amount"].mean()
    largest_expense = filtered["Amount"].max()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Spend", f"₹{total_spend:.2f}")
    c2.metric("Transactions", transactions)
    c3.metric("Average", f"₹{avg_transaction:.2f}")
    c4.metric("Largest", f"₹{largest_expense:.2f}")

    st.subheader("Filtered Transactions")

    st.dataframe(
        filtered,
        hide_index=True,
        use_container_width=True
    )

    st.download_button(
        "Download CSV",
        filtered.to_csv(index=False),
        file_name=f"expenses_{start}_{end}.csv",
        mime="text/csv",
        type="primary"
    )

    st.subheader("Spend by Category")

    bar_color = st.color_picker(
        "Pick a bar colour",
        "#3B82F6"
    )

    st.write("Selected Colour:", bar_color)

    category_spend = (
        filtered.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(category_spend)

    st.subheader("Monthly Summary")

    monthly = (
        filtered.groupby(
            filtered["Date"].dt.month_name()
        )
        .agg(
            Total_Spend=("Amount", "sum"),
            Transactions=("Amount", "count")
        )
    )

    st.table(monthly)

    st.markdown("---")

    st.caption(f"Week 1 Day 4 Project")

else:
    st.info("Upload expenses.csv to get started")