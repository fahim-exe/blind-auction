import auction as Auc

#1-get auction bidders name
#2-get auction bidders bidding amount
#3-check if there is more bidders
#4-if yes , repeat 1 and 2
#5-if no, check max bidder
#6-print max bidders name and amount as winner


while True: 

    print("Welcome to the silent auction program.")
    name = input("What is your name: ")
    bid = int(input("What's your bid: $"))

    chk_new = input("Are there any other bidders? Type 'yes' or 'no' :")
    if chk_new.lower()=="yes":
        pass
