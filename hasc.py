from os import system as sy
from time import sleep as slp
import sys
import hashlib
import itertools
import threading
sy('clear')
red='\u001b[31m'
grn='\u001b[32m'
cyn='\u001b[36m'
re='\u001b[0m'
ban=cyn+'''
 /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$ 
| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  | $$| $$  \ $$| $$  \__/| $$  \__/
| $$$$$$$$| $$$$$$$$|  $$$$$$ | $$      
| $$__  $$| $$__  $$ \____  $$| $$      
| $$  | $$| $$  | $$ /$$  \ $$| $$    $$
| $$  | $$| $$  | $$|  $$$$$$/|  $$$$$$/
|__/  |__/|__/  |__/ \______/  \______/ 
 '''+re
print(ban)
def md5(wd,hah):
	try:
		open(wd,'rb')
	except:
		print(red+'Wordlist Not found!'+re)
		slp(2)
		sy('clear')
		sy('python hasc.py')
	f=open(wd,'rb')
	while True:
		rf=f.readline()
		rehash=hashlib.md5(rf).hexdigest()
		if hah==rehash:
			done = True
			print(grn+'Hash Found : '+rf.decode()); break
		else:
			pass
		if len(rf)==0:
			print(red+'Hash not in wordlist..'+re); break
def sha256(wd,hah):
	try:
		open(wd,'rb')
	except:
		print(red+'Wordlist Not found!'+re)
		slp(2)
		sy('clear')
		sy('python hasc.py')
	f=open(wd,'rb')
	while True:
		rf=f.readline()
		rehash=hashlib.sha256(rf).hexdigest()
		
		if hah==rehash:
			done = True
			print(grn+'Hash Found : '+rf.decode()); break
		else:
			pass
		if len(rf)==0:
			print(red+'Hash not in wordlist..'+re); break
def sha512(wd,hah):
	try:
		open(wd,'rb')
	except:
		print(red+'Wordlist Not found!'+re)
		slp(2)
		sy('clear')
		sy('python hasc.py')
	f=open(wd,'rb')
	while True:
		rf=f.readline()
		rehash=hashlib.sha512(rf).hexdigest()
		
		if hah==rehash:
			done = True
			print(grn+'Hash Found : '+rf.decode()); break
		else:
			pass
		if len(rf)==0:
			print(red+'Hash not in wordlist..'+re); break
def sha3_256(wd,hah):
	try:
		open(wd,'rb')
	except:
		print(red+'Wordlist Not found!'+re)
		slp(2)
		sy('clear')
		sy('python hasc.py')
	f=open(wd,'rb')
	while True:
		rf=f.readline()
		rehash=hashlib.sha3_256(rf).hexdigest()
		
		if hah==rehash:
			done = True
			print(grn+'Hash Found : '+rf.decode()); break
		else:
			pass
		if len(rf)==0:
			print(red+'Hash not in wordlist..'+re); break
def sha3_512(wd,hah):
	try:
		open(wd,'rb')
	except:
		print(red+'Wordlist Not found!'+re)
		slp(2)
		sy('clear')
		sy('python hasc.py')
	f=open(wd,'rb')
	while True:
		rf=f.readline()
		rehash=hashlib.sha3_512(rf).hexdigest()
		
		if hah==rehash:
			done = True
			print(grn+'Hash Found : '+rf.decode()); break
		else:
			pass
		if len(rf)==0:
			print(red+'Hash not in wordlist..'+re); break
def blake2b(wd,hah):
	try:
		open(wd,'rb')
	except:
		print(red+'Wordlist Not found!'+re)
		slp(2)
		sy('clear')
		sy('python hasc.py')
	f=open(wd,'rb')
	while True:
		rf=f.readline()
		rehash=hashlib.blake2b(rf).hexdigest()
		
		if hah==rehash:
			done = True
			print(grn+'Hash Found : '+rf.decode()); break
		else:
			pass
		if len(rf)==0:
			print(red+'Hash not in wordlist..'+re); break
def blake2s(wd,hah):
	try:
		open(wd,'rb')
	except:
		print(red+'Wordlist Not found!'+re)
		slp(2)
		sy('clear')
		sy('python hasc.py')
	f=open(wd,'rb')
	while True:
		rf=f.readline()
		rehash=hashlib.blake2s(rf).hexdigest(); print(rehash)
		if hah==rehash:
			done = True
			print(grn+'Hash Found : '+rf.decode()); break
		else:
			pass
		if len(rf)==0:
			print(red+'Hash not in wordlist..'+re); break
def opt(n,nm):
	print(cyn+'['+n+'] '+grn+nm+re)
opt('1','MD5')
opt('2','SHA-256')
opt('3','SHA-512')
opt('4','SHA-3-256')
opt('5','SHA-3-512')
opt('6','BLAKE2c')
opt('7','BLAKE2b')
opt('00','Exit')
opt = input(red+'\n[>] '+cyn+'Enter your option : '+re)
if opt=='1' or opt=='2' or opt=='3' or opt=='4' or opt=='5' or opt=='6' or opt=='7':
	pass
elif opt=='0' or opt=='00':
	slp(1)
	print(red+'Bye'+re)
	sys.exit()
else:
	print(red+'Option Not found!!'+re)
	slp(2)
	sy('clear')
	sy('python hasc.py')
hash=input(red+'[>] '+cyn+'Enter HASH : '+re)
wordlist=input(red+'[>] '+cyn+'Enter Wordlist path : '+re)
if opt=='1':
	md5(wordlist,hash)
elif opt=='2':
	sha256(wordlist,hash)
elif opt=='3':
	sha512(wordlist,hash)
elif opt=='4':
	sha3_256(wordlist,hash)
elif opt=='5':
	sha3_512(wordlist,hash)
elif opt=='6':
	blake2s(wordlist,hash)
elif opt=='7':
	blake2b(wordlist,hash)
else:
	print(red+'Not Found!!!')
