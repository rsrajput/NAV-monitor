import pandas as pd
import requests

# ------------------------------
# Step 1: Hardcoded MF details
# ------------------------------
mf_data = [
    {"SchemeCode": "127042", "SchemeName": "Motilal Oswal Midcap Fund-Direct Plan-Growth Option", "FirstNAV": 110.75, "FirstSIPDate": "24-01-2025"},
    {"SchemeCode": "125354", "SchemeName": "Axis Small Cap Fund - Direct Plan - Growth", "FirstNAV": 113.18, "FirstSIPDate": "28-04-2025"},
    {"SchemeCode": "147946", "SchemeName": "BANDHAN SMALL CAP FUND - DIRECT PLAN GROWTH", "FirstNAV": 48.38, "FirstSIPDate": "20-01-2025"},
    {"SchemeCode": "120164", "SchemeName": "Kotak-Small Cap Fund - Growth - Direct", "FirstNAV": 280.8, "FirstSIPDate": "28-04-2025"},
    {"SchemeCode": "120828", "SchemeName": "Quant Small Cap Fund - Growth Option - Direct Plan", "FirstNAV": 259.9, "FirstSIPDate": "28-04-2025"},
    {"SchemeCode": "119132", "SchemeName": "HDFC Gold ETF Fund of Fund - Direct Plan", "FirstNAV": 30.47, "FirstSIPDate": "09-05-2025"},
    {"SchemeCode": "152712", "SchemeName": "Motilal Oswal Nifty India Defence Index Fund Direct Plan Growth", "FirstNAV": 10.05, "FirstSIPDate": "14-05-2025"}
]

df_mf = pd.DataFrame(mf_data)

# ------------------------------
# Step 2: Fetch AMFI NAVAll.txt
# ------------------------------
url = "https://www.amfiindia.com/spages/NAVAll.txt"
response = requests.get(url)
lines = response.text.splitlines()

# ------------------------------
# Step 3: Parse NAV file
# ------------------------------
nav_rows = []
for line in lines[2:]:  # skip first 2 lines (metadata + header)
    parts = line.strip().split(";")
    if len(parts) >= 6:
        scheme_code = parts[0].strip()
        scheme_name = parts[3].strip()
        nav = parts[4].replace(",", "").strip()
        date = parts[5].strip()
        try:
            nav_float = float(nav)
            nav_rows.append({"SchemeCode": scheme_code, "NAV": nav_float, "NAVDate": date})
        except:
            continue  # skip if NAV is invalid

df_nav = pd.DataFrame(nav_rows)

# ------------------------------
# Step 4: Merge MF data with latest NAV
# ------------------------------
df = pd.merge(df_mf, df_nav, on="SchemeCode", how="left")

# ------------------------------
# Step 5: Calculate Return % and SIP Decision
# ------------------------------
df["Return%"] = (df["NAV"] / df["FirstNAV"]) * 100

def decide(return_percent):
    if return_percent >= 110:   # ≥10% increase
        return "Increase SIP"
    elif return_percent <= 90:  # ≥10% decrease
        return "Decrease SIP"
    else:
        return "Keep SIP as it is"

df["Decision"] = df["Return%"].apply(decide)

# Round Return% for readability
df["Return%"] = df["Return%"].round(2)

# ------------------------------
# Step 6: Display / Save
# ------------------------------
cols_order = ["SchemeCode", "SchemeName", "NAV", "NAVDate", "FirstNAV", "FirstSIPDate", "Return%", "Decision"]
df = df[cols_order]

print(df)
# Optionally save to Excel
# df.to_excel("mf_nav_decision_dynamic.xlsx", index=False)
