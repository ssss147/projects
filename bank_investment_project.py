#!/bin/python3
# Repeated symbol count for header messages
import investments

BORDER_CNT = 25
total_deposits= 0
total_Withdrawal=0 
total_penalty_count=0
# Menu options
DEPOSIT_FUNDS = "1"
WITHDRAW_FUNDS = "2"
VIEW_BALANCE = "3"
CLOSE_ACCOUNT = "4"
VIEW_INVESTMENTS = "5"
SELL_INVESTMENTS = "6"

# Setup Account
print(
    "\n" + ("*" * BORDER_CNT) + "\n" + "Welcome to Banco Popular!"
    "\n" + ("*" * BORDER_CNT)
)
print("\n" + ("-" * BORDER_CNT) + "\nAccount Setup\n" + ("-" * BORDER_CNT))

#This line of code is asking the user for their name.
name = input("Account name: ")
     

#We are using the "starting" variable to validate the input of the user in the starting balance later on.
starting = 0.00

#This block of code is asking the user for the startinb
while True:
    inbalance = input("Starting balance: $")
    try:
        # This line is converting the user input into a float.
        as_float = float(inbalance)
        # This line is converting the input into two decimals spaces.
        as_format = format(as_float,'.2f')
        # If the number is as a format or float that has two decimals or is an integer. 
        if as_format == inbalance or float(inbalance) == int(inbalance):
            # The starting variable which is cero will now be the verified value which is the variable as_float.
            starting = as_float
        # The variable starting now is being validated to check if is more than cero which it means that is a positive number.
        if starting > 0:
             # Break is being used to get out of the loop when we receive the value as an two decimal number or an integer.
            break
    except ValueError:
        continue
    #This continue is giving another chance for entering a new number. 
inbalance = float(inbalance)


# string == string lo que estamos buscando son enteros y 2 decimale sa

# This variable is the investment amount, which is going to be the percent of how much the user wants to invest. 
inv_p = float(input("Percentage of initial account balance to invest (0-100):")) / 100
 
# This is the total of what the user is investing because is calculating the money avaialble of the user and the 
# percent that they want to invest. 
inv_amt = inbalance * inv_p

# This calculation is going to give us what is left of the starting balance when the user does the investing. 
inbalance -= inv_amt

# We are asking the user to choose an investment option.
inv_name = input(
    "\nSelect investment option:\n"
    "(1) COLEGIO\n"
    "(2) MSFT\n"
    "(3) GOOG\n"
)
# This is the conditionals of what is going to get printed if they choose any of the investments.
if inv_name == "1":
    inv_name = "COLEGIO"
if inv_name == "2":
    inv_name = "MSFT"
if inv_name == "3":
    inv_name = "GOOG"

# This is giving me the hypotecal price of the share.
in_share = investments.get_share_price(inv_name)

# This is providing me with the amount of shares that we can buy with the amount that we are investing.
shares = int(inv_amt // in_share)
# This is the balance of the left over after investing.
inbalance += inv_amt % in_share

# in this line i'm making sure that inbalance is a float before the accummulator "balance" starts. 
balance = float(inbalance)


print(f"Investment name: {inv_name}")
print(f"Shares purchased: {shares}")
print(f"Share price: ${in_share:.02f}")
print(f"Investment amount: ${shares * in_share:.02f}") #  The amount of shares with the prices is going to give us the .
print(f"Remaining account balance: ${inbalance:.02f}")


print(
    ("*" * BORDER_CNT) + "\nWelcome new account member!\n" + ("*" * BORDER_CNT)
)
print(f"Account {name} created with starting balance: ${inbalance:.2f}")


# Main Account Menu
# This code is printing the options for the user, they will have to choose one of the forth options.
# add an acummulator 
while True:
        print("\nSelect option:\n")
        print("(1) Deposit funds")
        print("(2) Withdraw funds")
        print("(3) View bank account balance")
        # If balance is more than cero print "close account".
        if balance >= 0:
            print("(4) Close account")
# If we have shares we print the share options.
        if shares != 0:
            print("(5) View investments")
            print("(6) Sell investments")
        
        choice = input("")


        # Deposit
        if choice == DEPOSIT_FUNDS:
                # header..
                print("\n" + ("-" * BORDER_CNT) + "\nDeposit Funds\n" + ("-" * BORDER_CNT) + "\n")

                # Ask for an amount to be deposited
                answer = input("Amount to deposit: $")
                try:
                    # We are using the variable d to turn answer into float. 
                    d = float(answer)

                    # If d is less than cero we are not taking the value since is negative value.
                    if d <= 0:
                        print("Transaction failed: Invalid deposit amount.")
                        continue
                except ValueError:
                    # If the amount can't be converted into a valid number, we print that it's invalid.
                    print("Transaction failed: Invalid deposit amount.")
                    continue
                # This rule is stating that if we have a period (".") which is a decimal and answer is not equal to two decimals is invalid!
                if "." in answer and answer != f"{d:.2f}":
                    print("Transaction failed: Invalid deposit amount.")
                    continue

                answer = float(answer)
                total_deposits += 1
                print("Account name:", name)
                print(f"Deposit Amount: ${answer:.2f}")
                balance += answer
                # This is the accumulator of the balance through all the transactions.
                print(f"New balance: ${balance:.2f}")
                

            
            
  
            
          
            
            



        # Withdrawal
        # if the user chooses "2" the withdraw funds menu is going to be printed.
        elif choice == WITHDRAW_FUNDS:
                print("\n" + ("-" * BORDER_CNT) + "\nWithdraw funds\n" + ("-" * BORDER_CNT) + "\n")
                # The variable answer is asking the user for the amount to withdraw.
                answer = input("Amount to Withdraw: $")
                try:
                    # We are using the variable w to turn answer into float. 
                    w = float(answer)
                    # If d is less than cero we are not taking the value since is negative value.
                    if w <= 0:
                        print("Transaction failed: Invalid withdrawal amount.")
                        continue
                except ValueError:
                    print("Transaction failed: Invalid withdrawal amount.")
                    continue
                # This rule is stating that if we have a period (".") which is a decimal and answer is not equal to two decimals is invalid
                if "." in answer and answer != f"{w:.02f}":
                    print("Transaction failed: Invalid withdrawal amount.")
                    continue
                # Now the validated amount is going to be again "answer".
                answer = w
                
                 # We calculate the hypothetical balance, if we were to withdraw the requested funds the equation is this....
                p_balance = balance - answer
                    
               
            
                # Ecuations for the "withdraw".
                answer = float(answer)
                per_dollar = 100
                change= round(answer * 100)
                h = change // (100 *  per_dollar)
                change = change % (100 *  per_dollar)
                f= change// ( 50 *  per_dollar)
                change=  change % ( 50 *  per_dollar)
                t= change// (20 *  per_dollar)
                change= change % (20 *  per_dollar)
                te= change// (10 *  per_dollar)
                change= change % (10 *  per_dollar)
                fi= change// (5 *  per_dollar)
                change= change % (5 *  per_dollar)
                on= change//per_dollar
                change= change %  per_dollar
                qu= change// 25
                change= change % 25
                di= change// 10
                change= change % 10
                ni= change// 5
                change= change % 5
                pen= change 
                answer = float(answer)
                # If the user balance is less or equal than -100 the penalty is 0.
                if p_balance >= -100.00:
                    total_Withdrawal += 1
                    penalty = 0
                    balance -= answer + penalty
                    print("Account name:", name)
                    print(f"Withdrawal Amount: ${answer:.2f}")
                    print(f"Penalties: ${penalty:.2f}")
                    print(f"New balance: ${balance:.2f}")
                    print(f"Currency withdrawn:" )
                    if h > 0:
                        print("$100s:",h)
                    if f > 0:
                        print("$50s:",f)
                    if t > 0:
                        print("$20s:",t)
                    if te > 0:          
                        print("$10s:",te)
                    if fi > 0:
                        print("$5s:", fi)
                    if on > 0:
                        print("$1s:",on)
                    if qu > 0:
                        print("quarters:",qu)
                    if di > 0:
                        print("dimes:", di)
                    if ni > 0:
                        print("nickels:", ni)
                    if pen > 0:
                        print("pennies:",pen)   
                # If the user balance is more than -1000 and less than -100 the penalty is going to be 0.01. 
                
                elif p_balance > -1000.00 and p_balance < -100.00:
                    total_Withdrawal += 1
                    total_penalty_count += 1
                    penalty = answer * 0.01
                    balance -= answer + penalty
                    print("Withdrawal amount is greater than account balance. Overdraft penalty of 1% applied.")
                    print("Account name:", name)
                    print(f"Withdrawal Amount: ${answer:.2f}")
                    print(f"Penalties: ${penalty:.2f}")
                    print(f"New balance: ${balance:.2f}")
                    print(f"Currency withdrawn:" )
                    if h > 0:
                        print("$100s:",h)
                    if f > 0:
                        print("$50s:",f)
                    if t > 0:
                        print("$20s:",t)
                    if te > 0:          
                        print("$10s:",te)
                    if fi > 0:
                        print("$5s:", fi)
                    if on > 0:
                        print("$1s:",on)
                    if qu > 0:
                        print("quarters:",qu)
                    if di > 0:
                        print("dimes:", di)
                    if ni > 0:
                        print("nickels:", ni)
                    if pen > 0:
                        print("pennies:",pen)     
                # If the user balance is more than -5000 and less than -10000 the penalty is going to be 0.03. 
                elif p_balance > -5000.00 and p_balance <= -1000.00: 
                    total_Withdrawal += 1
                    penalty = answer * 0.03
                    total_penalty_count += 1
                    balance -= answer + penalty


                    print("Withdrawal amount is greater than account balance. Overdraft penalty of 3% applied.")
                    print("Account name:", name)
                    print(f"Withdrawal Amount: ${answer:.2f}")
                    print(f"Penalties: ${penalty:.2f}")
                    print(f"New balance: ${balance:.2f}")
                    print(f"Currency withdrawn:" )
                    if h > 0:
                        print("$100s:",h)
                    if f > 0:
                        print("$50s:",f)
                    if t > 0:
                        print("$20s:",t)
                    if te > 0:          
                        print("$10s:",te)
                    if fi > 0:
                        print("$5s:", fi)
                    if on > 0:
                        print("$1s:",on)
                    if qu > 0:
                        print("quarters:",qu)
                    if di > 0:
                        print("dimes:", di)
                    if ni > 0:
                        print("nickels:", ni)
                    if pen > 0:
                        print("pennies:",pen)     
            # We are using the "else" function for a balance over -5,000 in which the transaction will not be executed. 
                else:
                # penalty is going to be -1 after the condition "else", because since penalty is less 
                # than 0 is not going to printed in the receipt.
                # we only need the "transaction failed" as output.
                    print("Transaction failed: withdrawal amount exceeds overdraft limit.")
                    penalty = -1 
                
        
                

    # View balance
        elif choice == VIEW_BALANCE:
            print("\n" + ("-" * BORDER_CNT) + "\nAccount balance\n" + ("-" * BORDER_CNT) + "\n")
            print("Account name:", name)
            print(f"Balance: ${balance:.2f}")



        # If they choose "4" we are closing the account.
        elif choice == CLOSE_ACCOUNT and balance >= 0:
            print("\n" + ("*" * BORDER_CNT) + "\nClosing Account\n" + ("*" * BORDER_CNT))  
            # If they choose to close the account and they still have shares they are going to be sold.
            if shares > 0:
                print("\n" + ("-" * BORDER_CNT) + "\nSell Investments\n" + ("-" * BORDER_CNT) + "\n")
                # This is the current hypothetical price of the share.
                curr_share_price = investments.get_share_price(inv_name)
                # This ecuation is the investment return between the current share price and the initial share price. 
                # (If we are winning or losing.)
                inv_value = (curr_share_price - in_share) / in_share
                if inv_value > 0:
                    add = "+"
                else:
                    add = ""
                # We are converting the return value into a percent with two decimals.
                inv_value = f"{inv_value * 100:.02f}"
           

                print(f"Investment name: {inv_name}")
                print(f"Shares sold: {shares}")
                print(f"Initial Share Price: ${in_share:.02f}")
                print(f"Current Share Price: ${curr_share_price:.02f}")
                print(f"Investment value: ${curr_share_price * shares:.02f} ({add}{inv_value}%)")
                print(f"Previous account balance: ${balance:.02f}")
                # After the user sells the investment this line of code is adding the money to the balance.
                balance += curr_share_price * shares
                # Since the user sold the shares, now shares are cero. 
                shares = 0
                print(f"New account balance: ${balance:.02f}")
            # This ecuation is printing the difference between the final balance and the initial balance.
            percent  = ((balance - inbalance) / inbalance) * 100
            # If percent is more than cero that means that is positive.
            if percent >= 0:
                add = "+"
            # else the number is negative because that's the exception.
            else:
                add= ""
            # This line of code is making sure that the number is a positive one by using "abs" which is an absolute value.
            # we are calculating the difference between the rounded number and the initial number if that difference is less than 0.05 
            # is going to round the number to the nearest integer.
            if abs(round(percent) - percent) < 0.05:
                percent = round(percent)
        
        
            print("\n" + ("-" * BORDER_CNT) + "\nFinal Account Statement\n" + ("-" * BORDER_CNT) + "\n")
            print("Account name:", name)
            print(f"Initial Balance: ${inbalance:.2f}")
            print(f"Final Balance: ${balance:.02f} ({add}{percent:.02f}%)")
            print(f"Deposit count: {total_deposits}")
            print(f"Withdrawal count: {total_Withdrawal}")
            print(f"Overdraft penalty count: {total_penalty_count}")

            print("\nThank you for banking with Banco Popular!")
            break
        
        elif choice == VIEW_INVESTMENTS and shares > 0:
            print("\n" + ("-" * BORDER_CNT) + "\nView Investments\n" + ("-" * BORDER_CNT) + "\n")
            # This is the current hypothetical price of the share.
            curr_share_price = investments.get_share_price(inv_name)
            # This ecuation is the investment return between the current share price and the initial share price. 
            # (If we are winning or losing.)
            inv_value = (curr_share_price - in_share) / in_share
            # If percent is more than cero that means that is positive.
            if inv_value > 0:
                add = "+"
            # else the number is negative because that's the exception.   
            else:
                add = ""
            # We are converting the return value into a percent with two decimals    
            inv_value = f"{inv_value * 100:.02f}"

            print("Your investment:")
            print(f"Name: {inv_name}")
            print(f"Shares: {shares}")
            print(f"Initial Share Price: ${in_share:.02f}")
            print(f"Current Share Price: ${curr_share_price:.02f}")
            print(f"Investment value: ${curr_share_price * shares:.02f} ({add}{inv_value}%)")
        
            print("Other investments:")
            #  I used the \t because is going to give me four spaces that a lined with each other.
            print("Name\tShare Price")
            
            #This is displaying the price of the other stocks that the user hasn't bought.
            if inv_name != "COLEGIO":
                print(f"COLEGIO\t${investments.get_share_price('COLEGIO'):.02f}")
            if inv_name != "MSFT":
                print(f"MSFT\t${investments.get_share_price('MSFT'):.02f}")
            if inv_name != "GOOG":
                print(f"GOOG\t${investments.get_share_price('GOOG'):.02f}")
        
        elif choice == SELL_INVESTMENTS and shares > 0:
            print("\n" + ("-" * BORDER_CNT) + "\nSell Investments\n" + ("-" * BORDER_CNT) + "\n")
            # This is the current hypothetical price of the share.
            curr_share_price = investments.get_share_price(inv_name)
            # This ecuation is the investment return between the current share price and the initial share price. 
            # (If we are winning or losing.)
            inv_value = (curr_share_price - in_share) / in_share
            # If percent is more than cero that means that is positive.
            if inv_value > 0:
                add = "+"
            # We are converting the return value into a percent with two decimals    
            else:
                add = ""
            # We are converting the return value into a percent with two decimals
            inv_value = f"{inv_value * 100:.02f}"

            print(f"Investment name: {inv_name}")
            print(f"Shares sold: {shares}")
            print(f"Initial Share Price: ${in_share:.02f}")
            print(f"Current Share Price: ${curr_share_price:.02f}")
            print(f"Investment value: ${curr_share_price * shares:.02f} ({add}{inv_value}%)")
            print(f"Previous account balance: ${balance:.02f}")
            # After selling the shares this is giving us the final balance which is basically the new account balance. 
            balance += curr_share_price * shares
            shares = 0

            print(f"New account balance: ${balance:.02f}")

