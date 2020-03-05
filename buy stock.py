A= [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

def buy_sell(a):
    max_profit =0
    min_price= a[0]

    for price in a:
        min_price =min(price, min_price)

        profit= price- min_price
        max_profit= max(profit, max_profit)
    return max_profit

print(buy_sell(A))
