import pandas as pd
import streamlit as st
from utils import get_overdue_days, get_stage
from prompt_templates import generate_prompt
from email_agent import generate_email
from audit_log import save_log

st.title("Finance Credit Follow-Up Agent")

df = pd.read_csv("sample_data/invoices.csv")

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
    st.success(f"Mock email sent to {row['email']}")