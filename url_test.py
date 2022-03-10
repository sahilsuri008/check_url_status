#!/usr/bin/python3

from urllib import request
from urllib.error import HTTPError
import re
import os

if os.path.exists("site_status.csv"):
    os.remove("site_status.csv")

site_list = open("site_list.txt", "r")
csv_output_file = open("site_status.csv", "a")

#Add header line#
csv_output_file.write("URL, Redirected URL/Original URL, Status\n")

for sites in site_list:
    site = sites.split()
    url = site[0]
    try:
        response = request.urlopen(url)
        pattern_match_un='sws-unavailable'
        pattern_match_in='sws-invalid'

        check_status = re.search(pattern_match_un,response.geturl())
        check_status_in = re.search(pattern_match_in,response.geturl())

        if check_status:
            status='URL redirected to outage page. SWS-Unavailable'
        elif check_status_in:
            status='Connected but blocked by ACL or not in internal DNS'
        else:
            status='URL OK'

        csv_output_file.write(url+","+response.geturl()+","+status+"\n")

    except:
        csv_output_file.write(url+","+"The site is not reachable, DNS issue or URL not in use\n")

csv_output_file.close()
site_list.close()

