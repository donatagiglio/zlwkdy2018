#! /bin/bash

rm -f out?.*


# Run python code to scrape html source code from zillow for addresses: Uncomment 
#rm -f zillow_source*.html
#python3.4 zillow_scrape_html_source.py

cat zillow_source_??.html > out0.html

perl -pe 's/data-address=\"/\nciaostart=/g' out0.html > out1.txt
perl -pe 's/\"\ class=\"save-home-operation\"/\n\ ciao/g' out1.txt > out2.txt

grep "ciaostart" out2.txt |sed 's/ciaostart=//g' > out3.txt
now=$(date +"%m_%d_%Y")
mv out3.txt zillow_addresses_$now.txt
rm -f out?.*

