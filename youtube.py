#import requests
#import pyodbc
import _mysql_connector
#import os

print(' [*]startpython')
productId = 'MP-C85F2M8366520'
headers = {'Cache-Control': 'no-cache',}
params = {'apiversion': '5.4', 'passkey':'caXiU0Idh0iPhwXH2iJnDRJ7OGGEIYEfLKYp2O8czRbCg', 'locale':'fr_FR', 'Filter':'ProductId:'+productId}

#os.chdir("C:\\Users\\alexandre.planchot\Documents\python_BZV")
#file_MPID = open("BZV_MPID_update.txt", "w")
#file_MPID.write("MPID;iNbReviews")

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = _mysql_connector.connect("DRIVER={MySQL ODBC 5.3 ANSI Driver}; SERVER=localhost;DATABASE=symfony; UID=root; PASSWORD=;")
cursor = cnxn.cursor()
cursor.execute("select top 5 title from article")
print ('toto enter sql')
while row:
    print(row[0])
    row = cursor.fetchone()

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=neosql;DATABASE=Neolane511;Trusted_Connection=yes;')
#cnxn_update = pyodbc.connect('DRIVER={SQL Server};SERVER=neosql;DATABASE=Neolane511;Trusted_Connection=yes;')

# Create a cursor from the connection
#cursorUpdate = cnxn_update.cursor()
#cursor = cnxn.cursor()
#cursor.execute("select top 5000 smpid from neolane.rdcBZV_ReviewsByMPID with (nolock) where iNbReviewsToReach > iNbReviews and iactif = 1 and sysmoddate < neolane.dateonly(getdate())")
#row = cursor.fetchone()
#while row:
#    params['Filter'] = 'ProductId:'+row[0]
#    #print(params['Filter'])
#    response = requests.get('https://api.bazaarvoice.com/data/reviews.json', headers=headers, params=params)
##    json = response.json()
#    TotalResults = json['TotalResults']
#    strTotalResults = str(TotalResults)
#    file_MPID.write("\n"+row[0]+";"+strTotalResults)
#    if strTotalResults.startswith('None'):
###        print("nothing;" + row[0])
#    else:
#        cursorUpdate.execute("update neolane.rdcBZV_ReviewsByMPID set sysModDate = getdate(), iNbReviews = ? where sMpid = ?",(strTotalResults, row[0]))
#        cnxn_update.commit()
#        dataUpdate = cursorUpdate.description
#        print("updated;"+row[0]+";"+strTotalResults+";"+str(dataUpdate))
#        file_MPID.write(";updated")
#    row = cursor.fetchone()
#file_MPID.close()




