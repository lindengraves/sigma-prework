import datetime

dob = input("Enter Birthday in the form YYYY-MM-DD: ")
dob = datetime.date.fromisoformat(dob)
today = datetime.date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

print(f"If you were born on {dob.isoformat()} you would be {age} today.")
