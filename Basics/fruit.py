dozen = 12
#discount = -2
#GST = 12.5
applequnatity = 5 * dozen
mangoqunatity = 3 * dozen
applepeice = 12
mangopeice = 34
Appleamount = applequnatity*applepeice
Mangoamount = mangoqunatity*mangopeice
Total_Price = Appleamount+Mangoamount
print('Total_Price = ',Total_Price)
discount = (Total_Price*(-2))/100
dp = Total_Price+(discount)
print('After discount price is =',dp)
gst = (dp*12.5)/100
print('after gst price is =',gst)
final_price = dp+gst
print('Final Price is =',round(final_price , 2))
