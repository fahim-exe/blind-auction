d = {'fahim': 20, 'mostafa': 50, 'mamun': 10}
max_val = 0
for key, value in d.items():
    max_name = ""
    

    if value>max_val:
        max_val = value
        max_name = key


winner = f"The winner is {max_name} with a bid of ${max_val}"
print(winner)
