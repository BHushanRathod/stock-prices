# Stock Data 

A flask application that visualises the open, high, low, close and volume (OHLCV) of a stock for the last 100 days

Source Code:
------------

`<https://github.com/BHushanRathod/stock-prices>`_


Installation and Usage
======================

Download the souce code::
       
    $ git clone https://github.com/BHushanRathod/stock-prices.git
   
Activate the Virtual Environment::

    source ~/path/to/ve/bin/activate

Install the Dependencies::

    pip install -r requirements.txt

Run server::

    $ export FLASK_APP=app.py
    $ flask run
        
Hit the server::

    https://localhost:<port>
    
* Steps to follow:
    
    * for viewing any company's pass stock data provide url parameter as ?c=<company_stock_code>
    * for eg. to get google's stock data query would be
        
        
        http://localhost:<port>/data?c=GOOG
