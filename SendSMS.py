import smtplib
import sys

#===========================
#EDIT: go to this link and select Enabled
#https://www.google.com/settings/security/lesssecureapps
#==========================
CarrierDic={
	"Verizon": "@vtext.com",
	"TMobile": "@tmomail.net",
	"ATT": "@txt.att.net",
	"Sprint": "@messaging.sprintpcs.com",
	"Cricket": "@sms.mycricket.com"
}

class Alert(object): 
	def __init__(self, username, password):
		self.mailserver = smtplib.SMTP('smtp.gmail.com:587')
		self.mailserver.ehlo()
		self.mailserver.starttls()
		self.mailserver.login(username,password)
		self.fromaddr = username+'@gmail.com'

	def __del__(self):
		self.mailserver.quit()
	#===========================================
	# SendSMS: providing subject, conetent Ph_num, carrier name 
	#==========================================
	def SendSMS(self,sub="Hi",content="Test",ph_num="1234567890", carrier="ATT"):
		carrieraddr=CarrierDic[carrier]		
		toaddrs  = ph_num + carrieraddr
		msg = "\r\n".join([
		  "From: "+self.fromaddr,
		  "To: "+toaddrs,
		  "Subject: "+sub,
		  "",
		  content
		  ])
		#=========send SMS ============
		print "sending SMS------"+ toaddrs
		self.mailserver.sendmail(self.fromaddr, toaddrs, msg)

	#================================================
	# SendEmail: providing subject, conetent
	#================================================
	def SendEmail(self, sub="Hi",content="Test",toemail=" "):
		msg = "\r\n".join([
		  "From: "+self.fromaddr,
		  "To: "+toemail,
		  "Subject: "+sub,
		  "",
		  content
		  ])
		#=========send SMS ============
		print "sending Email------"+ toemail
		self.mailserver.sendmail(self.fromaddr, toemail, msg)

