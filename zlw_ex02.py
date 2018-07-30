#! /Users/dgiglio/anaconda/bin/python3.4
# coding: utf-8

# In[1]:

#!/usr/bin/env python

import zillow
import pprint
import zipcode
from address import AddressParser, Address
import matplotlib.pyplot as plt


# In[2]:

with open('out3.txt') as f:
    addr_houses = f.readlines()


# In[3]:

addr_houses = [x.strip() for x in addr_houses] 


# In[4]:

#addr_houses[0:3]


# In[5]:

#addr_houses[3][:-5]


# In[6]:

#addr_houses[3][-5:]


# In[7]:

vars_extended_data = {'bathrooms', 'bedrooms', 'finished_sqft', 'last_sold_date', 'last_sold_price', 'lot_size_sqft', 'tax_assessment', 'tax_assessment_year', 'usecode', 'year_built'}
vars_full_address  = {'latitude', 'longitude'}
vars_zestimate     = {'amount','amount_change_30days'}
# In[8]:

#address = "5164 Gallatin Pl, Boulder, CO"
#postal_code = "80303"
#n = 0

# allocate vars
data_out = dict()

for v in vars_extended_data:
    data_out[v] = []
for v in vars_full_address:
    data_out[v] = []
for v in vars_zestimate:
    data_out[v] = []

for nm in addr_houses:
    address = nm[:-5]
    postal_code = nm[-5:]
    #if __name__=="__main__":
    key = ""
    with open("/Users/giglio/Desktop/ACC_JISAO/code/zillow_us/zillow_env/bin/config/zillow_key.conf", 'r') as f:
        key = f.readline().replace("\n", "")

    api = zillow.ValuationApi()
    data = api.GetDeepSearchResults(key, address, postal_code)

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(data.get_dict())

    for v in vars_extended_data:
        data_out[v].append(getattr(data.extended_data,v))

    for v in vars_full_address:
        data_out[v].append(getattr(data.full_address,v))

    for v in vars_zestimate:
        data_out[v].append(getattr(data.zestimate,v))

    # for v in vars_extended_data:
    #     if n==0:
    #         data_out[v] = getattr(data.extended_data,v)
    #         data_out
    #     else:
    #         data_out[v] = [data_out[v], (getattr(data.extended_data,v))]
    #
    # n = n+1


# In[9]:

for v in data_out.keys():
    print(v)
    print(data_out[v])

ciao
plt.plot(data_out['amount'])
plt.show()
# In[ ]:

#print(type(data_out))

# In[ ]:

#print(getattr(data.extended_data,v))





