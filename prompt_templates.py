def generate_prompt(data, stage):

    tone_map = {
        "warm": "Warm and friendly",
        "firm": "Polite but firm",
        "formal": "Formal and serious",
        "stern": "Stern and urgent"
    }

    cta_map = {
    "warm": "Use the payment portal below to complete the payment.",
    "firm": "Please confirm your payment date at the earliest.",
    "formal": "Please respond within the next 48 hours regarding this invoice.",
    "stern": "Immediate payment is required to avoid escalation."
    }

    payment_link = "https://payments.finflow.com/pay"

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

    CTA:
    {cta_map.get(stage)}

    Payment Link:
    {payment_link}

    Sender Details: 
    Name: Dimple Rogha,
    Department: Finance Team,
    Company: XYZ Corporation,
    Email: dimplerogha@gmail.com

    Requirements:
    - Keep email professional
    - Mention payment urgency appropriately
    - Include call to action
    - Do not hallucinate information
    - Keep under 200 words
    """