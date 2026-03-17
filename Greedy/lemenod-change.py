class LemonadeStand:
    # Function to check if all customers can be given correct change
    def lemonade_change(self, bills):
        five = 0  # Counter for $5 bills
        ten = 0   # Counter for $10 bills

        # Process each customer's bill
        for bill in bills:
            if bill == 5:
                five += 1  # Accept $5, no change needed
            elif bill == 10:
                if five > 0:
                    five -= 1  # Give one $5 as change
                    ten += 1   # Accept $10
                else:
                    return False  # Cannot provide change
            else:  # bill == 20
                if five > 0 and ten > 0:
                    five -= 1  # Use one $5
                    ten -= 1   # Use one $10
                elif five >= 3:
                    five -= 3  # Use three $5 bills
                else:
                    return False  # Cannot provide change
        return True  # All customers received change


# Driver code
if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    print("Queue of customers:", bills)

    stand = LemonadeStand()
    ans = stand.lemonade_change(bills)

    if ans:
        print("It is possible to provide change for all customers.")
    else:
        print("It is not possible to provide change for all customers.")
