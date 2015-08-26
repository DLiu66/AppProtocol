import socket
import sys
import time
import random
#=========for integrity====
#import hashlib
#import hmac
server_address = ('localhost', 10000)

class ServerSocket(object): 
	def __init__(self, serverid = 0):
		#server_address = ('localhost', 10000)
		self.id = serverid
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(server_address)
		self.sock.listen(2)

	def __del__(self):
		self.sock.close()

	# def RunServer(self):
	# 	while True:
	# 		print "---waiting for a connection---"
	# 		connection, client_address = self.sock.accept()
	# 		data = connection.recv(16)
	# 		print "received: "+str(data)
	# 		if data == "check":	
	# 			#tempnum = random.randint(1,10)						
	# 			connection.sendall(str(self.id) + ":"+"10"
			#if data == "Hi":
				#connection.sendall(str(self.id) + ":"+"0")
			#else:
				#print "null received on server"

class ClientSocket(object): 
	def __init__(self):		
		self.csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.maxretry = 1

	def __del__(self):
		self.csock.close()

	def ConnectToServer(self, timeout=1000):
		self.csock.connect(server_address)
		self.csock.settimeout(timeout)

	def SendMsg(self, msg):
		#======================================
		# Timeout and retry
		#======================================
		try:
			self.csock.sendall(msg)
			rec_data = self.csock.recv(16)
		except socket.timeout:
 			print("timeout error")	 			#return "out"
		try:
			print rec_data
			return rec_data
		except:
			print "no data"
			return "NULL"

	def SendMsgRetry(self, msg):
		#======================================
		# Timeout and retry
		#======================================
		for retry in range(1,self.maxretry):
			try:
				self.csock.sendall(msg)
				rec_data = self.csock.recv(16)
				break
			except socket.timeout:
	 			print("timeout error")	 			#return "out"
			try:
				print rec_data
				return rec_data
			except:
				print "no data"
				return "NULL"


#============================================
#   For integrity
#============================================
# def Hash(key = 'key', msg = 'msg'):
# 	hobj = Hmac.new(key, msg)
# 	return hobj.hexdigest()

# #=====================================
# #  For Privacy
# #  How to use: 
# # encrypted = encode("key", 'msg')
# # decrypted = decode("key", encrypted)
# #=====================================
# def encode(key, string):
# 	encoded_chars = ""
# 	for i in range(len(string)):
# 		key_c = key[i % len(key)]
# 		encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
# 		encoded_chars+=encoded_c
# 		encoded_string = "".join(encoded_chars)
# 	return encoded_string
	
# def decode(key, string):
# 	decoded_chars = ""
# 	for i in range(len(string)):
# 		key_c = key[i % len(key)]
# 		decoded_c = chr(ord(string[i]) - ord(key_c) % 256)
# 		decoded_chars+=decoded_c
# 		decoded_string = "".join(decoded_chars)
# 	return decoded_string

# def Authentication(username, password):
# 	#=====build a small dic to store your username password
# 	# can use data base of course :)
# 	AuthDic ={
# 		"Mike": "124",
# 		"Monica":"244"
# 	}
# 	try: 
# 		expectedpw = AuthDic[username]
# 	except:
# 		return "Error: wrong Username"
# 	if (expectedpw != password):
# 		return "Error: wrong passwrod"
# 	else:
# 		return "Authentication Pass"
