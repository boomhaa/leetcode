# link to the problem - https://leetcode.com/problems/simple-bank-system/submissions/

# You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].
# Execute all the valid transactions. A transaction is valid if:
# The given account number(s) are between 1 and n, and
# The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
# Implement the Bank class:
# Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
# boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
# boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
# boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.

# link to submission - https://leetcode.com/submissions/detail/747571338/

from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance=dict()
        for i in range(len(balance)):
            self.balance[i+1]=balance[i]
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        money_have=self.balance.get(account1,-1)
        account2_have=self.balance.get(account2,-1)
        if money_have==-1:
            return False
        else:
            if money_have<money:
                return False
            else:
                if account2_have==-1:
                    return False
                else:
                    self.balance[account1]-=money
                    self.balance[account2]+=money
                    return True
    def deposit(self, account: int, money: int) -> bool:
        account_have=self.balance.get(account,-1)
        if account_have==-1:
            return False
        else:
            self.balance[account]+=money
            return True
    def withdraw(self, account: int, money: int) -> bool:
        account_have = self.balance.get(account, -1)
        if account_have == -1:
            return False
        else:
            if account_have<money:
                return False
            else:
                self.balance[account]-=money
                return True