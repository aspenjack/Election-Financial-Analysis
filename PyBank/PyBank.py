#!/usr/bin/env python
# coding: utf-8

# In[32]:


import os
import csv

bank_path = os.path.join(".", "budget_data.csv")

output_file = os.path.join(".", "budget_analysis.txt")


# In[29]:


with open(bank_path) as bank_file:

    bank_reader = csv.reader(bank_file, delimiter=",")
    
    
    bank_header = next(bank_reader)
    
    
    month_sum = 0
    
    for data in bank_reader:
        month_sum = month_sum + 1
   
   


# In[33]:


with open(bank_path) as bank_file:

    bank_reader = csv.reader(bank_file, delimiter=",")
    
    
    bank_header = next(bank_reader)
    
    
    net_profit = 0
    
    
    first_row = next(bank_reader)
    net_profit += int(first_row[1])
    previous_net = int(first_row[1])
    
    net_change_list = []
    
    
    for profit in bank_reader:
        net_profit += int(profit[1])
        net_change = int(profit[1]) - previous_net
        previous_net = int(profit[1])
        net_change_list.append(net_change) 
        
        if net_change == 1862002:
            increase_month = profit[0]
            
        if net_change == -1825558:
            decrease_month = profit[0]
    
    
    average_change = sum(net_change_list) / len(net_change_list)
    
    
    max_increase = max(net_change_list)
    max_decrease = min(net_change_list)    
    
with open(output_file, "w") as txt_file:  
    output = (
    "Financial Analysis:\n\n"
    "--------------------------------------------------\n\n"
    f"Total months: {month_sum}\n\n"
    f"Net Profits/Losses: ${net_profit}\n\n"
    f"Changes in Profits/Losses: {net_change_list}\n\n"
    f"Average Change: ${average_change}\n\n"
    f"Greatest Increase in Profits: {increase_month} ${max_increase}\n\n"
    f"Greatest Decrease in Profits: {decrease_month} ${max_decrease}\n\n"
)

    print(output)
    
    txt_file.write(output)
    


# In[ ]:





# In[ ]:




