
import sys

units_consumed = 357
if units_consumed < 0:
   print("INVALID INPUT")
   sys.exit(0)

if 0 < units_consumed < 60:
    billable_amount = units_consumed * 1.25
elif 0 < units_consumed < 100: 
   remaining_units = units_consumed - 60 
   billable_amount = 60 * 1.25 + remaining_units * 2.00
elif 0 < units_consumed < 150:
   remaining_units = units_consumed - 60 - 40
   billable_amount = 60 * 1.25 +  40 * 2.00 + remaining_units * 4.00
elif 0 < units_consumed < 250:
   remaining_units = units_consumed - 60 - 40 - 50
   billable_amount = 60 * 1.25 + 40 * 2.00 + 50 * 4.00 + remaining_units * 7.00 
elif 0 < units_consumed > 250:
   remaining_units = units_consumed - 60 -40 - 50 -100
   billable_amount= 60 * 1.25 + 40 * 2.00 + 50 * 4.00 + 100 * 7.00 + remaining_units * 10.00

   print(f"""
                units_consumed : {units_consumed}
                Amount         : {billable_amount}
            """)