A = float(input("Enter the monthly SIP amount: "))
YR = float(input("Enter the yearly rate of return: "))
Y = int(input("Enter the number of years: "))

MR = YR/12/100
M = Y * 12

FV = A * ((((1 + MR)**(M))-1) * (1 + MR))/MR
FV = round(FV)
print("The expected amount you will get is:",FV)
