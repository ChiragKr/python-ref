from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1500035503&period2=1502713903&interval=1d&events=history&crumb=RZBdEhFhRRX'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str  = str(csv)
    lines = csv_str.split("\\n")

    dest_url = r'goog.csv'
    fw = open(dest_url, 'w')

    for line in lines:
        fw.write(line)

    fw.close()

download_stock_data(goog_url)
