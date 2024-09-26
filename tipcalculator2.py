bill=float(input('How much was the bill?'))
service_quality=(input('How was the service? Bad, Okay, Good, Great?'))
if service_quality == "Bad":
    print(float(bill))
elif service_quality == "Okay":
    print(float(bill*1.15))
elif service_quality == "Good":
    print(float(bill*1.20))
elif service_quality == "Great":
    print(float(bill*1.25))
else:
    print('invalid input')