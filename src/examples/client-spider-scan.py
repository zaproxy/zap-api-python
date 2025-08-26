#!/usr/bin/env python

from zapv2 import ZAPv2
import time


target = 'http://127.0.0.1' # Change to match the target URL you want to scan
apikey = 'changeme' # Change to match the API key set in ZAP, or use None if the API key is disabled


zap = ZAPv2(apikey=apikey)

print(f'Spidering target {target}')
scanid = zap.clientSpider.scan(url=target)

while (int(zap.clientSpider.status(scanid)) < 100):
    print(f"Spider progress %: {zap.clientSpider.status(scanid)}")
    time.sleep(2)
    
print('Spider completed')
