#! /bin/bash

rm -f out?.txt
#rm -f in0.html

#wget -q -O in0.html --max-redirect=1 "https://www.zillow.com/homes/for_sale/Boulder-CO/house_type/30543_rid/3-_beds/0-900000_price/0-3594_mp/globalrelevanceex_sort/40.20169,-105.067062,39.834114,-105.561447_rect/10_zm/"

#curl -O -J -L https://www.zillow.com/homes/for_sale/Boulder-CO/house_type/30543_rid/3-_beds/0-900000_price/0-3594_mp/globalrelevanceex_sort/40.20169,-105.067062,39.834114,-105.561447_rect/10_zm/ >> in0.html

perl -pe 's/data-address=\"/\nciaostart=/g' in0.html > out1.txt
perl -pe 's/\"\ class=\"fm-save-event\"/\n\ ciao/g' out1.txt > out2.txt

grep "ciaostart" out2.txt |sed 's/ciaostart=//g' > out3.txt
