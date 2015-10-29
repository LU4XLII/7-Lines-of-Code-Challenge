#42
from urllib.request import *
resp = urlopen(input("URL: ")).read()
arq = open(input("Arq: ")+'.html', 'wb')
arq.write(resp)
arq.close()
