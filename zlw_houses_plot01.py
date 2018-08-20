#! /Users/dgiglio/anaconda/bin/python3.4
# coding: utf-8

#!/usr/bin/env python

import zillow
import pprint
import zipcode
from address import AddressParser, Address
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, show
import numpy as np

#filename = 'zillow_addresses_07_17_2018.txt'
filename = 'zillow_addresses_08_19_2018.txt'
with open(filename) as f:
    addr_houses = f.readlines()


addr_houses = [x.strip() for x in addr_houses]

vars_extended_data = {'bathrooms', 'bedrooms', 'finished_sqft', 'last_sold_date', 'last_sold_price',
                      'lot_size_sqft', 'tax_assessment', 'tax_assessment_year', 'usecode', 'year_built'}
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

# for v in data_out.keys():
#     print(v)
#     print(data_out[v])

# this part of the code wanted to make a plot to compare the last sold price with the current amount
# (this difference should also by normalized by the corresponding times)
d_previous    = data_out['last_sold_price']#data_out['lot_size_sqft']
d_now         = data_out['amount']

d_indices     = [i for i, x in enumerate(d_previous) if x is not None]

d_previous2pl = [d_previous[i] for i in d_indices]
d_now2pl      = [d_now[i] for i in d_indices]

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
plt.plot(d_now2pl,d_previous2pl,'ok')

# the next two lines are to overlay the 1 on 1 comparison line on the plot
d_range = [np.min([min(d_now2pl),min(d_previous2pl)]),
           np.max([max(d_now2pl),max(d_previous2pl)])]

plt.plot(d_range, d_range,'-k')
plt.axis('equal')
fig.savefig('zlw_houses_amount_dots.png')   # save the figure to file
plt.close(fig)

# TO DO NEXT:
# the FIRST THING TO DO is to save the data using this script and move the plotting part of the code to another script...
# since the number of calls (to zillow) per day are limited
# check why few addresses (now removed from zillow_addresses_08_18_2018.txt) were failing: you could implement a try and catch statement and print out the ones that fail;
# merge different addresses files;
# make relevant plots

#print(type(data_out))

# In[ ]:

#print(getattr(data.extended_data,v))





