# Mutual Fund NAV Monitor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.0%2B-green)
![Requests](https://img.shields.io/badge/Requests-2.0%2B-orange)

This NAV monitor downloads the latest NAV of your mutual fund schemes (scheme codes are hardcoded) and provides a **decision for adjusting your SIP amount** based on the rules below:

> I would like to increase (decrease) my installment value by 10% when the NAV on the installment date is higher (lower) by 10% from the first installment NAV.

---

## Requirements

A `requirements.txt` file is included. You can generate it using:

```bash
pip freeze > requirements.txt

Installation
Option 1: Install from requirements.txt

pip install -r requirements.txt
Option 2: Install manually
bash
Copy code
pip install pandas
pip install requests
Usage
Open the Python script (mf_nav_monitor.py) in a text editor.

Modify the scheme codes and mutual fund names in the script to match your portfolio.

Run the script to fetch the latest NAV and receive SIP recommendations:

bash
Copy code
python mf_nav_monitor.py
```