import json
from datetime import datetime

def save_log(row, stage):

    log = {
        "client": row["client_name"],
        "invoice": row["invoice_no"],
        "stage": stage,
        "timestamp": str(datetime.now()),
    }

    with open("logs/audit_log.json", "a") as f:
        json.dump(log, f)
        f.write("\n")