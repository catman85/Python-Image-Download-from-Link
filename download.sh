!/bin/bash

python urlmorf.py links >> fixedlinks.txt
wget -i fixedlinks.txt -P images/
rm fixedlinks.txt
> links
