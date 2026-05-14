from datetime import datetime

def get_overdue_days(due_date):
    due = datetime.strptime(due_date, "%Y-%m-%d")
    today = datetime.today()
    return (today - due).days

def get_stage(days):
    if 1 <= days <= 7:
        return "warm"
    elif 8 <= days <= 14:
        return "firm"
    elif 15 <= days <= 21:
        return "formal"
    elif 22 <= days <= 30:
        return "stern"
    else:
        return "legal"