# try:
#     price = input("What is the sales price?")
#     com = input("What is the commis in percentage?")
#     priceint = float(price)
#     comint = float(com)

#     comper = comint / 100
#     commis = comper * priceint
#     aftertax = commis * .2
#     atax = commis - aftertax
#     print(atax)
# except:
#     print("you added a charactor or something only numbers")



try:
    price = float(input("What is the sales price? "))
    com = float(input("What is the commission in percentage? ")) / 100

    commission = com * price
    after_tax = commission * 0.8  # Directly subtracting 20% tax

    print(after_tax)
except ValueError:
    print("An error occurred. Please ensure you enter only numbers.")