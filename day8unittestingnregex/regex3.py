

import re




text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern = 'at' # todo: type your regex here

print(re.findall(pattern, text))


# **2. Extract Concentration Risk Types. It will be a text that appears after "Concentration Risk:", In below example, your regex should extract these two strings**
# 
# (1) Credit Risk
# 
# (2) Supply Rish

# In[ ]:


text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern = 'have' # todo: type your regex here

print(re.findall(pattern, text))


# **3. Companies in europe reports their financial numbers of semi annual basis and you can have a document like this. To exatract quarterly and semin annual period you can use a regex as shown below**
# 
# Hint: you need to use (?:) here to match everything enclosed

# In[ ]:


text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern = 'of' # todo: type your regex here
matches = re.findall(pattern, text)
matches


# __[Solution](https://github.com/codebasics/py/blob/master/Advanced/regex/regex_tutorial_exercise_answer.ipynb)__
