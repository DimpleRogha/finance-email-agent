# Finance Credit Follow-Up Agent

An AI-powered finance collections assistant built using Streamlit and OpenRouter APIs. The system automates overdue invoice follow-ups by generating escalation-based reminder emails with dynamic tone control, audit logging, and dashboard analytics.

The application demonstrates workflow automation, prompt engineering, and business-rule-driven AI integration for finance operations.

## Features

* CSV-based invoice ingestion
* Overdue payment analysis
* Multi-stage escalation workflow
* AI-generated finance follow-up emails
* Dynamic tone escalation
* CTA-aware payment reminders
* Mock-send email simulation
* Audit logging system
* Streamlit dashboard interface
* Environment-based secret management

## Tech Stack

| Component              | Technology       |
| ---------------------- | ---------------- |
| Frontend Dashboard     | Streamlit        |
| Data Processing        | Pandas           |
| LLM Provider           | OpenRouter       |
| Model                  | GPT-4o Mini      |
| Environment Management | python-dotenv    |
| Logging                | JSONL Audit Logs |
| Language               | Python           |

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/DimpleRogha/finance-email-agent.git
cd finance-email-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

## Project Structure

```text
finance-email-agent/
│
├── app.py
├── email_agent.py
├── prompt_templates.py
├── audit_log.py
├── requirements.txt
├── .env.example
│
├── logs/
│   └── audit_log.jsonl
│
├── sample_data/
│   └── invoices.csv
```


1. LLM Chosen
      The application uses GPT-4o Mini via OpenRouter API for AI-generated finance follow-up emails.

      Why This Model
        * Cost-efficient for high-volume email generation
        * Fast response time suitable for dashboard workflows
        * Strong professional language generation
        * Reliable instruction following for tone escalation

      Alternative Models Evaluated
        * Gemini 2.0 Flash
        * Llama 3.1 8B
        * DeepSeek R1

      GPT-4o Mini was selected due to stability, output consistency, and lower latency during testing.


2. Agent Framework
     The system uses a modular single-agent workflow architecture.

     Workflow
       1. Invoice CSV ingestion
       2. Overdue analysis
       3. Escalation stage classification
       4. Prompt construction
       5. AI email generation
       6. Mock send simulation
       7. Audit log generation

     The application combines deterministic business rules with LLM-based language generation.

    Architecture Style
      * Rule-based orchestration
      * Prompt-driven generation
      * Human-in-the-loop escalation for legal cases

    Escalation cases beyond 30 days are intentionally excluded from automated email generation and flagged for manual review.


3. Prompt Design
   
    The prompts were structured using:
     * Role prompting
     * Tone conditioning
     * Structured invoice context
     * Controlled sender identity

    Prompt Inputs:
      * Client name
      * Invoice number
      * Due amount
      * Days overdue
      * Escalation stage
      * CTA instructions
      * Sender details

    Tone Escalation Strategy:
      The prompt dynamically changes tone based on overdue duration:
      * Warm
      * Firm
      * Formal
      * Stern

    Guardrails
      * Prevent placeholder outputs
      * Restrict excessive email length
      * Enforce professional formatting
      * Disable automated legal escalation emails


4. Security Risk Mitigation
   ## Security Risk Mitigation

| Risk                 | Description                                                                         | Mitigation Strategy                                                                                                                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompt Injection     | Malicious invoice/client inputs could manipulate AI-generated email behaviour.      | User-controlled invoice data is inserted into structured prompts only. Prompt instructions are fixed and controlled within backend templates.                                                                    |
| Data Privacy / PII   | Invoice and client records may contain sensitive financial or personal information. | Application processes data locally using CSV files. Sensitive credentials are excluded using `.env` files and `.gitignore`. Audit logs avoid storing confidential financial details beyond operational metadata. |
| API Key Exposure     | API keys may leak through source code or public repositories.                       | API keys are stored using environment variables via `.env` and excluded from GitHub using `.gitignore`. No secrets are hardcoded in the codebase.                                                                |
| Hallucination Risk   | LLM may generate inaccurate payment language or unintended content.                 | Prompt structure restricts email format, tone, sender identity, and CTA behaviour. Human review is enforced for legal escalation cases beyond 30 days overdue.                                                   |
| Unauthorized Access  | External users could trigger the workflow if deployed publicly.                     | Current prototype runs locally in Streamlit development mode only. Production deployment would require authentication and endpoint protection.                                                                   |
| Email Spoofing       | AI-generated emails could appear misleading if sent directly.                       | Current implementation uses mock-send simulation only and does not transmit real emails. Real deployment would require verified sender domains and SMTP authentication.                                          |
| Audit & Traceability | Missing logs may reduce accountability for generated communications.                | Every generated email action is recorded with timestamp, invoice number, and escalation stage using structured audit logs.                                                                                       |


## Future Improvements

* Real SMTP email integration
* Authentication layer
* Database-backed invoice storage
* Role-based access control
* PDF invoice attachment support
* Analytics dashboard charts
* Human approval workflow
