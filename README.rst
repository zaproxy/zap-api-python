# zap-api-python


# Install

.. code-block:: bash
        
    # pip install python-owasp-zap
 
# Basic usage

.. code-block:: python
        
    from zap import ZAPv24
    
    zap = ZAPv24()
    
    print('Spidering target %s' % target)
    scanid = zap.spider.scan(target)

    # Give the Spider a chance to start
    time.sleep(2)

    while int(zap.spider.status(scanid)) < 100:
        print('Spider progress %: ' + zap.spider.status(scanid))
        time.sleep(2)
