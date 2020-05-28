
import os
import csv
	

pybank_file = r"C:\Users\camer\Desktop\3 - PYTHON\HW\PyBank\Resources\Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv"
profit = pybank_file


total_months = 0
total_profit = 0
previous_profit = 0
profit_change = 0
change_average = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]	
profit_changes = []
	
with open(pybank_file) as profit:
	reader = csv.DictReader(profit)
       
    
	for row in reader:
            
            total_months = total_months + 1
            total_profit = total_profit + int(row["Profit/Losses"])
	       	        
            profit_change = int(row["Profit/Losses"]) - previous_profit
            change_average = change_average - profit_change
            profit_change_average = round((change_average/total_months), 2)
                 
            previous_profit = int(row["Profit/Losses"])
	        
	        
            if (profit_change > greatest_increase[1]):
                greatest_increase[1] = profit_change
                greatest_increase[0] = row["Date"]
	

            if (profit_change < greatest_decrease[1]):
                greatest_decrease[1] = profit_change
                greatest_decrease[0] = row["Date"]
                
                
                profit_changes.append(int(row["Profit/Losses"]))
	    
                profit_average = sum(profit_changes) / len(profit_changes)
	    

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${profit_change_average}")
print(f"Greatest Increase In Profits: {greatest_increase[0]} ${greatest_increase[1]})") 
print(f"Greatest Decrease In Profits: {greatest_decrease[0]} ${greatest_decrease[1]})")
       
       
write_output = r"C:\Users\camer\Desktop\3 - PYTHON\HW\PyBank\Analysis\pybank_profits.txt"

filewriter = open(write_output, mode = 'w')

filewriter.write("Financial Analysis\n")
filewriter.write("-------------------------\n")
filewriter.write(f"Total Months: {total_months}\n")
filewriter.write(f"Total: ${total_profit}\n")
filewriter.write(f"Average Change: ${profit_change_average}\n")
filewriter.write(f"Greatest Increase In Profits: {greatest_increase[0]} ${greatest_increase[1]})\n") 
filewriter.write(f"Greatest Decrease In Profits: {greatest_decrease[0]} ${greatest_decrease[1]})\n")

filewriter.close()
