#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[225]:


import random
import time

stock_names_dict = {}

class Portfolio:
    def __init__(self):
        self.cash = 0
        self.stock_dict = {}
        self.mf_dict = {}
        self.transaction = {} 
        
    def addCash(self, amount):
        self.cash += amount
        self.transaction[f'addCash={amount}'] = time.time()
        
    def withdrawCash(self, amount):
        self.cash -= amount
        self.transaction[f'withdrawCash={amount}'] = time.time()  
        
    def buyStock(self, shares, objectstock):
        self.cash -= objectstock.price * shares
        if objectstock.stockname in self.stock_dict:
            self.stock_dict[objectstock.stockname] += shares
        else:
            self.stock_dict[objectstock.stockname] = shares
        self.transaction[f'buyStock={shares}'] = time.time()
        
    def buyMutualFund(self, shares, mf_object):
        self.cash -= shares
        if mf_object.mfname in self.stock_dict:
            self.mf_dict[mf_object.mfname] += shares
        else:
            self.mf_dict[mf_object.mfname] = shares
        self.transaction[f'buyMutualFund={shares}'] = time.time()
        
    def sellMutualFund(self, mfname , shares):
        random_price = random.uniform(0.9,1.2)
        self.cash += random_price * shares
        if mfname in self.mf_dict:
            self.mf_dict[mfname] -= shares
        else:
            self.mf_dict[mfname] = shares 
        self.transaction[f'sellMutualFund={shares}'] = time.time()
        
    def sellStock(self, stockname , shares):
        random_price = random.uniform(0.5 * stock_names_dict[stockname],1.5 * stock_names_dict[stockname])
        self.cash += random_price  * shares
        if stockname in self.stock_dict:
            self.stock_dict[stockname] += shares
        else:
            self.stock_dict[stockname] = shares
        self.transaction[f'sellStock={shares}'] = time.time()
    def __str__(self):
        return f'Your current cash: ${self.cash} \nYour current stocks: {self.stock_dict} \nYour current mutual funds: {self.mf_dict}'
    
class Stock:
    def __init__(self, price, stockname):
        self.price = price
        self.stockname = stockname
        stock_names_dict[stockname] = price
        
class MutualFund:
    def __init__(self, mfname):
        self.mfname = mfname
        


# In[226]:


portfolio = Portfolio()
portfolio.addCash(300.50)
print(portfolio)


# In[232]:


portfolio.withdrawCash(50)
print(portfolio)
s = Stock(20,"HFH")
portfolio.buyStock(5,s)
print(portfolio)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
print(portfolio)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT", 3)
print(portfolio)
portfolio.sellStock("HFH", 1)
print(portfolio)


# In[204]:





# In[ ]:





# In[205]:





# In[206]:





# In[207]:





# In[208]:





# In[209]:





# In[235]:


portfolio = Portfolio()


# In[234]:


portfolio.addCash(300.50)
print(portfolio)


# In[233]:


s = Stock(20, "HFH")
print(portfolio)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




