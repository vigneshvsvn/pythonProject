import smtplib

#Step1: Create Connection Object
conn=smtplib.SMTP('smtp.gmail.com',587) ## Using Gmail
print(type(conn))
#Step2: Start the Connection
print(conn.ehlo())
print(conn.starttls())
conn.login('vigneshvsvn@gmail.com','')
#conn.sendmail('vigneshvsvn@gmail.com','vigneshvsvn@gmail.com')
