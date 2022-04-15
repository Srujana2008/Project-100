class atm:
    def __init__(self, access_token, atm_card_number, pin_number):
        self.access_token = access_token
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number

def CashWithdrawl():
    print("Cash Withdrawl")
CashWithdrawl()

def BalanceEnquiry():
    print("Balance Enquiry")
BalanceEnquiry()