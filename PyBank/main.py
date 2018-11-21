import os
import csv

#enjoins the CSV file
budgetCSV = os.path.join('..', 'PyBank', 'budget_data.csv')

#opens the CSV file in "READ" mode delimiting each line with " "
with open(budgetCSV, "r", newline="") as csvfile:
    #Return a reader object 'budgetCSV' and will iterate over lines in csvfile
    csvreader = csv.reader(csvfile, delimiter=",")

    #skips header
    next(csvreader)

    total_months = 0
    total = 0
    profit_losses = []
    delta = []
    months = []

    for row in csvreader:
        #adds one to integer variable "total" for every line after header for total month count
        total_months += 1
        #append each month in the first column to list "months"
        months.append(row[0])
        #convert every value in the second column into an integer
        row[1] = int(row[1])
        #continuously add each value in the second column to get the total
        total += row[1]
        #append each value in the second column as a separate item in list "profit_losses"
        profit_losses.append(row[1])

    #loop through each item in list "profit_losses" and find the difference between itself and the item before it to find the profit/loss delta; then append each delta to list "delta"
    for x in range(1,len(profit_losses)):
        delta.append(profit_losses[x]-profit_losses[x-1])

    avg_delta = sum(delta)/len(delta)
    numformat_avgdelta = "{:.2f}".format(avg_delta)
    max_profit = max(delta)
    max_loss = min(delta)

    #obtain the index of the highest/lowest delta in the list "delta" plus one to match with the corresponding month
    max_profit_month_index = delta.index(max_profit) + 1
    max_loss_month_index = delta.index(max_loss) + 1
    #use the max profit/loss indexes to find the corresponding months in the list "months"
    max_profit_month = str(months[max_profit_month_index])
    max_loss_month = str(months[max_loss_month_index])


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${numformat_avgdelta}")
print(f"Greatest Increase in Profits: {max_profit_month} ${max_profit}")
print(f"Greatest Decrease in Profits: {max_loss_month} ${max_loss}")



