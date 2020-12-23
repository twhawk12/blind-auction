from replit import clear
from art import logo
print(logo)

def find_hi_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
     bid_amount = bidding_record[bidder]
     if bid_amount > highest_bid:
         highest_bid = bid_amount
         winner = bidder 
    print(f"The winner is {winner} with a bid of ${highest_bid} ")

bid_ledger = {}

should_continue = True 
while should_continue:

    name = input("What is your name?: ")
    bid = int(input("How much would you like to bid?:$"))
    bid_ledger[name] = bid
    more_bidder = input("Will there be another bidder? Type 'Yes' or 'No'.?\n")
    if more_bidder == 'Yes':
        clear()
    elif more_bidder == 'No':
        should_continue = False
        find_hi_bidder(bid_ledger)







