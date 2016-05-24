Example Code
============
::

   #!/usr/bin/env python
   import time
   from pprint import pprint
   from zapv2 import ZAPv2

   target = 'http://127.0.0.1'
   zap = ZAPv2()
   # Use the line below if ZAP is not listening on 8090
   # zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8090', 'https': 'http:127.0.0.1:8090'})

   # do stuff
   print ('Accessing target ' + target)
   # try have a unique enough session...
   zap.urlopen(target)
   # Give the sites tree a chance to get updated
   time.sleep(2)

   print ('Spidering target ' + target)
   spider_scan_id = zap.spider.scan(target)
   # Give the Spider a chance to start
   time.sleep(5)
   while (int(zap.spider.status(spider_scan_id)) < 100):
       print ('Spider progress %: ' + zap.spider.status(spider_scan_id))
       time.sleep(5)
   print ('Spider completed')
   
   # Wait for passive scanning to complete
   while (int(zap.pscan.records_to_scan) > 0):
     print ('Records to passive scan : ' + zap.pscan.records_to_scan)
     time.sleep(2)
   print ('Passive scanning complete')

   print ('Scanning target ' + target)
   ascan_id = zap.ascan.scan(target)
   while (int(zap.ascan.status(ascan_id)) < 100):
       print ('Scan progress %: ' + zap.ascan.status(ascan_id))
       time.sleep(5)

   print ('Scan completed')

   # Report the results

   print ('Hosts: ' + ', '.join(zap.core.hosts))
   print ('Sites: ' + ', '.join(zap.core.sites))
   print ('Urls: ' + ', '.join(zap.core.urls))
   print ('Alerts: ')
   pprint (zap.core.alerts())
