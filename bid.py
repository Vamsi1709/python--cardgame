print('''



             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
          jgs `"""""""`




''')
print("Welcome to Trophy bidding")
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary [bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids={}
continue_bidding =True
while continue_bidding:
    name=input("enter your name:")
    price= int(input("enter your price:$"))
    bids[name]=price
    others=input("Are there any other bidders ? type 'yes' or 'no' .\n ")
    if others =="no":
        continue_bidding=False
        find_highest_bidder(bids)
    elif others=="yes":
        print("\n"*50)
    else:
        print("enter correct input")
        
        


