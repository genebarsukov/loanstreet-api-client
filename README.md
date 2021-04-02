## Loanstreet API Client

Supports GET, POST, PUT, and PATCH requests to the loanstreet-demo api

## Usage

You can execute runner.py to view ouput of all basic requests

```python
from LoanStreetCli import LoanStreetCli

cli = LoanStreetCli()

# GET all loans
for loan in cli.getAllLoans():
    print(loan)

# GET a loan
print(cli.getLoan(11))

# POST a new loan
createPayload = {
    "amount": 990000,
    "interestRate": 17,
    "lengthMonths": 3,
    "monthlyPayment": 200,
}
print(cli.createLoan(createPayload))

# PUT a loan
updatePayload = {
    "amount": 56000,
    "interestRate": 3
}
print(cli.updateLoan(11, updatePayload))

# PATCH a loan
patchPayload = {
    "interestRate": 37
}
print(cli.patchLoan(11, patchPayload))
```