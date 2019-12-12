from mkmsdk.mkm import Mkm
from mkmsdk.api_map import _API_MAP
import pandas as pd
from pandas.io.json import json_normalize
from pathlib import Path
import json
import config

mkm = Mkm(_API_MAP["2.0"]["api"], _API_MAP["2.0"]["api_root"])
start = 1
OK = 206
all = []
while True:
	response = mkm.order_management.filter_order_paginated(actor="buyer",state="received",start=start)
	print(response.status_code)
	if(response.status_code!=OK):
		break
	start+=100
	orders = response.json()["order"]
	all.extend(orders)

#for i in range(len(orders)):
#	orders[i].pop("seller.legalInformation", None)

dataframe = json_normalize(all)
dataframe.to_csv("order.csv",index=False,encoding="utf-8")
