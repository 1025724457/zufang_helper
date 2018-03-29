import requests
import threading


url = 'http://sz.58.com/zufang/32346122361152x.shtml?from=1-list-73&iuType=z_2&PGTID=0d3090a7-0000-45be-001b-d445fde4318c&ClickID=20&adtype=3'
def get():
    r = requests.get(url)
    print(r.url)

for i in range(100):
    t = threading.Thread(target=get)
    t.start()
    print('end')

