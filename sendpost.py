import requests
import random
import time
payload = {'param1':2,'total':25}
A0 = 608.2 + random.randrange(-600, 100)
A1 = 708.2 + random.randrange(-600, 100)
A2 = 808.2 + random.randrange(-600, 100)
A3 = 908.2 + random.randrange(-600, 100)
A4 = 608.2 + random.randrange(-600, 100)
print(A0)
while True:
    r = requests.post("http://enerbiz.drssjischool.org/Default.aspx?apiparam=" + str(A0) + "?" + str(A1) + "?" + str(A2) + "?" + str(A3)+ "?" + str(A4))
    print(r.text)
    print(r.url)
    time.sleep(0.8)

### pass A0 and A2 to api given
    ##http://enerbiz.drssjischool.org/Default.aspx?apiparam=param1?param2?param3?param4?param5
