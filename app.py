import pandas as pd
import streamlit as st
from utils import get_overdue_days, get_stage
from prompt_templates import generate_prompt
from email_agent import generate_email
from audit_log import save_log

st.title("Finance Credit Follow-Up Agent")
st.caption("AI-powered invoice reminder automation dashboard")

df = pd.read_csv("sample_data/invoices.csv")
total_invoices = len(df)

payment_link = "https://payments.finflow.com/pay"

overdue_count = 0
escalated_count = 0
emails_generated = 0

for index, row in df.iterrows():

    days = get_overdue_days(row["due_date"])

    if days > 0:
        overdue_count += 1

    stage = get_stage(days)

    if stage == "legal":
        escalated_count += 1
    else:
        emails_generated += 1

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Invoices", total_invoices)
col2.metric("Overdue", overdue_count)
col3.metric("Escalated", escalated_count)
col4.metric("Emails Generated", emails_generated)



for index, row in df.iterrows():

    days = get_overdue_days(row["due_date"])

    if days <= 0:
        continue

    stage = get_stage(days)

    st.subheader(row["client_name"])

    if stage == "legal":
        st.error("Escalate to Legal Team")
        continue

    data = {
        "client_name": row["client_name"],
        "invoice_no": row["invoice_no"],
        "amount": row["amount"],
        "due_date": row["due_date"],
        "days_overdue": days
    }

    prompt = generate_prompt(data, stage)

    email = generate_email(prompt)
    save_log(row, stage)
    st.subheader("Generated Email")

    st.write(email)
    st.link_button("Pay Now", payment_link)
    st.success(f"Mock email sent to {row['email']}")
    st.divider()