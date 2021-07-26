'''Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction 
if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction 
(including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's 
account balance after an attempted transaction.'''

# input -> withdrawal amt and intial amt balance

withdrawal = int(input('Enter withdraw amt: '))
initial = float(input('Enter initial amt: '))

# Insufficient Funds
if withdrawal+0.5 > initial:
    print(initial)

# Incorrect Withdrawal Amount (not multiple of 5)
elif withdrawal%5 != 0:
    print(initial)

# Successful Transaction
else:
    print(round((initial - (withdrawal+0.5)), 2))