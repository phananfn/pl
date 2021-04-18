import urllib.request
### order
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSAHjKky31CQqtyR35cLKKU9M_j8VgNU0QyDivsKsI57PraKTwt8Ix4GnBFlLbVQGkAswPbblz94_5v/pub?gid=1709414950&single=true&output=csv'
urllib.request.urlretrieve(url,'data/order/order.csv')
print('downloaded order...')
### report
report_csv = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSAHjKky31CQqtyR35cLKKU9M_j8VgNU0QyDivsKsI57PraKTwt8Ix4GnBFlLbVQGkAswPbblz94_5v/pub?gid=935476844&single=true&output=csv"
urllib.request.urlretrieve(report_csv,'data/report/report.csv')
print('downloaded report...')   