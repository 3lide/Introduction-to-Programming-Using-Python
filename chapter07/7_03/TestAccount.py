from Account import Account

def main():
    account = Account(1122, 20000, 4.5)
    account.withdraw(2500)
    account.deposit(3000)
    print("account's id is", account.getId(), "balance is", 
    account.getBalance(), "monthly interest rate is", 
    format(account.getMonthlyInterestRate(), ".5f"), "monthly interest is", 
    format(account.getMonthlyInterest(), ".2f"))

if __name__ == "__main__":
    main()