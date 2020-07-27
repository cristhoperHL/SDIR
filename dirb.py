# -*- coding: utf-8 -*-
import requests
import sys

if(sys.argv[1]=="-h" or sys.argv[1]=="--help"):
	print("-h : menu de ayuda.")
	print("-u <url> : utilizar url")
	print("-x <type of file> : add type o files ")
	print("-w <wordlist> : add wordlist")
elif(sys.argv[1]=="-u" or sys.argv[1]=="--url"):
	session = requests.Session()
	session.trust_env = False
	url=sys.argv[2]
	f=open("wordlist_simple.txt","r")
	palabra=""
	for x in f:
		palabra=str(x)
		new_palabra=""
		for i in range(len(palabra)):
			if(i!=(len(palabra)-1)):
				new_palabra=new_palabra+palabra[i]
		new_url=url+new_palabra
		page=session.get(new_url)
		print(new_url,"-> Status code : ",page.status_code)

