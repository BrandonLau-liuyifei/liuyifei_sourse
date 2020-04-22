import smtplib,email
from p_email import mypass

chst = email.charset.Charset(input_charset='utf-8')
header = ("From: %s\nTo: %s\nSubject: %s\n\n"
       % ("cloveses@163.com",
          "cloveses@163.com" ,
          chst.header_encode("Python smtplib 测试！")))
body = "你好！"
email_con = header.encode('utf-8') + body.encode('utf-8')
smtp = smtplib.SMTP("smtp.163.com")
smtp.login("cloveses@163.com",mypass)
smtp.sendmail("cloveses@163.com","cloveses@163.com",email_con)
smtp.quit()
