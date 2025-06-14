import smtplib

#Step1: Create Connection Object
conn=smtplib.SMTP('smtp.gmail.com',587) ## Using Gmail
print(type(conn))
#Step2: Start the Connection
print(conn.ehlo())
print(conn.starttls())
conn.login('gvkaitechnology@gmail.com','')
conn.sendmail('gvkaitechnology@gmail.com','vigneshvsvn@gmail.com','Mail from Python')
conn.close()
