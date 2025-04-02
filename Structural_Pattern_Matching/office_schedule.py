Day = input(str("ENTER YOUR DAY !!! ="))
match Day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("TIMINGS: 6:00 AM TO 5:00 PM")
    case "Saturday":
        print(" TIMINGS: 6:00 AM TO 1:00 PM")
    case "Sunday":
        print(" OFFICE CLOSED !!!")
    case _:
       print("PLEASE TRY AGAIN")

Day = input(str("ENTER YOUR DAY !!! ="))
if Day in "Monday, Tuesday , Wednesday  ,Thursday ,Friday":
  print("TIMINGS: 6:00 AM TO 5:00 PM")
elif Day=="Saturday":
    print(" TIMINGS: 6:00 AM TO 1:00 PM")
elif Day == "Sunday":
    print(" OFFICE CLOSED !!!")
else :
    print("PLEASE TRY AGAIN")
