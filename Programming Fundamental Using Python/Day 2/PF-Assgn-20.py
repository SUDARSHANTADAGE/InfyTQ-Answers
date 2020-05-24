#PF-Assgn-20
def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    #eligible_loan_amount=0
    
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected
    if 1000<=account_number<1999:
       if account_balance>=100000:
           if salary>25000 and loan_type=="Car":
               if loan_amount_expected<=500000 and customer_emi_expected<=36:
                    eligible_loan_amount=500000
                    bank_emi_expected=36
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
               else:
                   print("The customer is not eligible for the loan")
           elif salary>50000 and loan_type=="House":
               if loan_amount_expected<=6000000 and customer_emi_expected<=60:
                   eligible_loan_amount=6000000
                   bank_emi_expected=60
                   print("Account number:", account_number)
                   print("The customer can avail the amount of Rs.", eligible_loan_amount)
                   print("Eligible EMIs :", bank_emi_expected)
                   print("Requested loan amount:", loan_amount_expected)
                   print("Requested EMI's:",customer_emi_expected)
               else:
                   print("The customer is not eligible for the loan")
           elif salary>75000 and loan_type=="Business":
               if customer_emi_expected<=84 and loan_amount_expected<=7500000:
                   eligible_loan_amount=7500000
                   bank_emi_expected=84
                   print("Account number:", account_number)
                   print("The customer can avail the amount of Rs.", eligible_loan_amount)
                   print("Eligible EMIs :", bank_emi_expected)
                   print("Requested loan amount:", loan_amount_expected)
                   print("Requested EMI's:",customer_emi_expected)
               else:
                   print("The customer is not eligible for the loan")
           else:
               print("Invalid loan type or salary")
       else:
           print("Insufficient account balance")
    else:
        print("Invalid account number")
     
    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1005,26000,255000,"Car1",300000,30)
