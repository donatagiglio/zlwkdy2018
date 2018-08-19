#! /Users/dgiglio/anaconda/bin/python3.4
# coding: utf-8

#!/usr/bin/env python

import zillow
import pprint
import zipcode
from address import AddressParser, Address
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, show

with open('addresses_17Jul2018.txt') as f:
    addr_houses = f.readlines()


addr_houses = [x.strip() for x in addr_houses]

vars_extended_data = {'bathrooms', 'bedrooms', 'finished_sqft', 'last_sold_date', 'last_sold_price', 'lot_size_sqft', 'tax_assessment', 'tax_assessment_year', 'usecode', 'year_built'}
vars_full_address  = {'latitude', 'longitude'}
vars_zestimate     = {'amount','amount_change_30days'}

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

for v in data_out.keys():
    print(v)
    print(data_out[v])

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
plt.plot(data_out['amount'])
fig.savefig('foo.png')   # save the figure to file
plt.close(fig)

# plt.show(block=True)
# plt.show()
# In[ ]:

#print(type(data_out))

# In[ ]:

#print(getattr(data.extended_data,v))





