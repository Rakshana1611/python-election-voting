import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="election"
)
voter_id=input("enter ur voter id: ")
voter_name=str(input("enter ur voter name: "))
voter_age=int(input("enter ur age: "))
if voter_age>=18:
    print("you can vote..")
    address=str(input("enter ur address: "))
    candidate_name=str(input("enter the candidate name u want to vote: "))
    f=open("voterlist.txt","a")
    f.write(f"{voter_name} is voted successfully.. on ")
    import datetime
    f=open("voterlist.txt","a")
    x=datetime.datetime.now()
    f.write(f"date:{x}\n")
    import smtplib
    def email_sending():
      try:
        receiver_mails=["kmugil0507@gmail.com"]
        for i in receiver_mails:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("rakshana0211@gmail.com","gckn txyn wqzr uztu")
            message=f"Voting is not only our right-It is our duty. Thanks for voting {voter_name}"
            s.sendmail("rakshana0211@gmail.com", i, message)
            s.quit()
            print("mail sent successfully")
      except:
        print("mail not sending")
    email_sending()
else:
       print("you don't have proper age to vote.")
def insert():
  mycursor=mydb.cursor()
  sql="insert into voting_list values (%s,%s)"
  val=(candidate_name,address)
  mycursor.execute(sql,val)
  mydb.commit()
  print("data saved successfully")
insert()
  