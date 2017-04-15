import md5 #Must be run in python 2.7.x
import sys

seed = sys.argv[1] #"3501672ebc68a5524629080e3ef60aef"
match = sys.argv[2] # "e26d7e19b69192b94af14c4b208c8c9a"
#this will find the 5th hash in the hashchain. This would be the correct response if prompted with the 6th hash in the hashchain
hashc = seed
prevc = ""
for _ in xrange(100):
	prevc = hashc
	hashc = md5.new(hashc).hexdigest()
	if hashc in match:
		break;
print prevc