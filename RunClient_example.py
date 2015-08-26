import TCPSocket
import SendSMS

serverobj = TCPSocket.ClientSocket()
serverobj.ConnectToServer()
print "sending data"
recvdata=serverobj.SendMsg("Hi")
print "receved data " + str(recvdata)
#====optional to send SMS to your phone====
#smsobj = SendSMS.Alert(username = "", password= '') 
#smsobj.SendEmail(content = data,toemail ="liuliu0807@gmail.com")
#SendSMS(sub="Hi",content="Test",ph_num="1234567890", carrier="ATT"):
	