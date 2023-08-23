#!/usr/bin/env python
# coding: utf-8

# In[160]:


import os
import pandas as pd

csvpath = "./election_data.csv"

output_file = os.path.join(".", "election_analysis.txt")


# In[161]:


election_df = pd.read_csv(csvpath)


# In[162]:


total_votes = len(election_df)
total_votes

candidates = election_df["Candidate"].unique()

candidate_count = election_df["Candidate"].value_counts()



# In[163]:


percentages = election_df["Candidate"].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'


# In[164]:


election_results = pd.concat([candidate_count, percentages], axis =1, keys = ["Count", "Percentage"])


# In[165]:


winner = election_df["Candidate"].mode()[0]


# In[166]:


with open(output_file, "w") as txt_file:
    output =  ("\nElection Results\n\n"
          "------------------------------------------\n\n"
          f"Total Votes: {total_votes}\n\n"
          "------------------------------------------\n"
          f"{election_results}\n"
          "------------------------------------------\n\n"
          f"Winner: {winner}")
    print(output)
    
    txt_file.write(output)


# In[167]:





# In[ ]:





# In[ ]:




