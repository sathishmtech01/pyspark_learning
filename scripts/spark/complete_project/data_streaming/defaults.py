cellsite_id = ["cellsite_"+str(i).zfill(4) for i in range(0,100)]
customer_number = "['812360'+str(i).zfill(4) for i in range(0,1000)]"
types = ["onnet","offnet","crossnet","international","recharge","data"]
host = "localhost"
port = 9999

import ast
print(ast.literal_eval("['a']"))
