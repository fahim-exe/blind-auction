def bidders_dict(name:str, bid:int):
    bid_names = {}
    bid_names[name] = bid

    
    return bid_names

def winner(dict:dict):
    max_val = 0
    max_name = ""
    for key, value in dict.items():
        
        

        if value>max_val:
            max_val = value
            max_name = key

    winner = f"The winner is {max_name} with a bid of ${max_val}"
    return winner