from LoanStreetCli import LoanStreetCli

cli = LoanStreetCli()

res1 = cli.getAllLoans()
createPayload = {
    "amount": 990000,
    "interestRate": 17,
    "lengthMonths": 3,
    "monthlyPayment": 200,
}
res2 = cli.createLoan(createPayload)
updatePayload = {
    "amount": 56000,
    "interestRate": 3
}
res3 = cli.updateLoan(11, updatePayload)
patchPayload = {
    "interestRate": 37
}
res4 = cli.patchLoan(11, patchPayload)
res5 = cli.getLoan(11)

for r in res1:
    print(r)
print('---------------------------------------------------------------------')
print(res2)
print('---------------------------------------------------------------------')
print(res3)
print('---------------------------------------------------------------------')
print(res4)
print('---------------------------------------------------------------------')
print(res5)