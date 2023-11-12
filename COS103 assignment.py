Print=("Yusuf & Sons")
Principal = float(input("Enter principal: "))
Rate = float(input("Entere rate: "))
Time = float(input("Enter time: "))

simple_interest = (Principal * Rate * Time)/100
compound_interest = (Principal * (1 + Rate/100) * (Time-1))

print('simple_interest is: %f' %(simple_interest))
print('cokmpound_interest is: %f' %(compound_interest))

print("You have calculated your simple interest")
print("You have calculated your compound interest")