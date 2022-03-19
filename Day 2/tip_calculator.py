#1 Ask How much the bill is
bill = float(input('How much is the bill? \n$'))
#2 Ask what percent tip they will be paying
tip_percentage = float(input('What will your tipping percentage be?\n%'))
#3 Ask how many people will be splitting the bill?
split = int(input('How many people will be splitting the bill?'))

#4 Display how much the tip will be
tip_amount = round(bill * (tip_percentage / 100),2)
tip_amount_formatted = "{:.2f}".format(tip_amount)
print(f'The amount to tip is ${tip_amount_formatted}')
#5 Display how much each person will have to pay
individual_bill = (bill + tip_amount) / split
#to Format it so you always display two decimals you do this
final_amount = "{:.2f}".format(individual_bill)
print(f'Each Person has to pay: ${final_amount}')