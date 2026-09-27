# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:32:22 2026

@author: lewis
"""

# =========================================================
# BREAK-EVEN BUDGET CALCULATOR
# User Input Version
# =========================================================

from datetime import datetime, timedelta

# -----------------------------
# USER INPUTS
# -----------------------------
item = input("Enter item name: ")

total_cost = float(input("Enter total cost: $"))

purchase_date_input = input("Enter purchase date (MM/DD/YYYY): ")

budgeted_per_day = float(input("Enter budgeted cost per day: $"))

monthly_income = float(input("Enter monthly income: $"))

# -----------------------------
# DATE CALCULATIONS
# -----------------------------
today = datetime.today()

purchase_date = datetime.strptime(purchase_date_input, "%m/%d/%Y")

elapsed_days = (today - purchase_date).days

# Prevent division by zero
if elapsed_days <= 0:
    elapsed_days = 1

# -----------------------------
# CALCULATIONS
# -----------------------------

# Actual cost per day
cost_per_day = total_cost / elapsed_days

# Break-even days
breakeven_days = total_cost / budgeted_per_day

# Break-even date
breakeven_date = purchase_date + timedelta(days=breakeven_days)

# Difference between actual elapsed and target
difference = int(breakeven_days - elapsed_days)

# Budget rate %
budget_rate = (budgeted_per_day / cost_per_day) * 100

# Monthly equivalent
per_month = cost_per_day * 30.44

# Percent of monthly income
percent_monthly_income = (per_month / monthly_income) * 100

# Status
if cost_per_day <= budgeted_per_day:
    status = "Budgeted cost reached 😊"
else:
    status = "Budgeted cost unreached 🤣"

# -----------------------------
# OUTPUT
# -----------------------------
print("\n==============================")
print("BREAK-EVEN REPORT")
print("==============================")

print(f"Today's Date:        {today.strftime('%A, %B %d, %Y')}")
print(f"Item:                {item}")

print(f"\nPurchase Date:       {purchase_date.strftime('%m/%d/%Y')}")
print(f"Break-even Date:     {breakeven_date.strftime('%A, %B %d, %Y')}")

print(f"\nTotal Cost:          ${total_cost:,.2f}")
print(f"Elapsed Days:        {elapsed_days}")

print(f"\nCost Per Day:        ${cost_per_day:.2f}")
print(f"Budgeted Per Day:    ${budgeted_per_day:.2f}")

print(f"\nBudget Rate:         {budget_rate:.2f}%")

print(f"\nPer Month:           ${per_month:,.2f}")
print(f"% Monthly Income:    {percent_monthly_income:.2f}%")

print(f"\nBreak-even Days:     {int(breakeven_days)}")
print(f"Difference:          {difference}")

print(f"\nStatus:              {status}")

print("==============================")