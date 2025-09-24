# Mutual Fund NAV Monitor

This NAV monitor downloads the latest NAV of your mutual fund schemes (scheme codes are hardcoded).  
It then provides a **decision for adjusting the SIP amount** based on the rules below:

> I would like to increase (decrease) my installment value by 10% when the NAV on the installment date is higher (lower) by 10% from the first installment NAV.

---

## Requirements

A `requirements.txt` file is included. You can generate it using:

```bash
pip freeze > requirements.txt

Installation

To run the NAV monitor on your computer:
# Option 1: Install from requirements.txt
pip install -r requirements.txt

# Option 2: Install manually
pip install pandas
pip install requests

Usage

Open the Python script (.py) in a text editor.

Modify the scheme codes and mutual fund names as needed for your portfolio.

Run the script to fetch the latest NAV and receive SIP recommendations.