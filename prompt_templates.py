def generate_prompt(data, stage):

    tone_map = {
        "warm": "Warm and friendly",
        "firm": "Polite but firm",
        "formal": "Formal and serious",
        "stern": "Stern and urgent"
    }

    return f"""
    You are a finance collections assistant.

    Generate a professional payment reminder email.

    Tone:
    {tone_map.get(stage)}

    Client Name: {data['client_name']}
    Invoice Number: {data['invoice_no']}
    Amount Due: ₹{data['amount']}
    Due Date: {data['due_date']}
    Days Overdue: {data['days_overdue']}

    Requirements:
    - Keep email professional
    - Mention payment urgency appropriately
    - Include call to action
    - Do not hallucinate information
    - Keep under 200 words
    """