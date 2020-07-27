# -*- coding: utf-8 -*-
import requests
import sys

cnt=len(sys.argv)

def separador(palabra):
	list_palabras=[]
	new_palabra=""
	for i in range(len(palabra)):
		if(palabra[i]!=','):
			new_palabra=new_palabra+palabra[i]
			if(i == len(palabra)-1):
				list_palabras.append(new_palabra)
		else:
			list_palabras.append(new_palabra)
			new_palabra=""
	return list_palabras

def menu_de_ayuda():
	print("-h : menu de ayuda.")
	print("-u <url> : utilizar url.")
	print("-x <type of file> : add type o files.")
	print("-w <wordlist> : add wordlist.")
	print("Example:")
	print("python sdir.py -u <url> : Use common.txt como wordlist por default")
	print("python sdir.py -u <url> -w <wordlist> : Chose wordlist.")
	print("python sdir.py -u <url> -w <wordlist> -x <filetype> : add extension")

if(sys.argv[1]=="-h" or sys.argv[1]=="--help"):
	menu_de_ayuda()
elif(sys.argv[1]=="-u" or sys.argv[1]=="--url" and cnt>1):
	session = requests.Session()
	session.trust_env = False
	url=sys.argv[2]
	wl=""
	if(cnt>3): #si los argumentos son mayores a 3
		if(sys.argv[3]=="-w" or sys.argv[3]=="--wordlist"):
			wl=sys.argv[4]
		else:
			wl="/usr/share/wordlists/dirb/common.txt"
	else :
		wl="/usr/share/wordlists/dirb/common.txt"
	f=open(wl,"r")
	palabra=""
	new_file=open("sdir_result.txt","w")
	for x in f:
		palabra=str(x)
		new_palabra=""
		for i in range(len(palabra)):
			if(i!=(len(palabra)-1)):
				new_palabra=new_palabra+palabra[i]
		# opcion -x

		if(cnt>5):
			if(sys.argv[5]=="-x"):
				list_pal=separador(sys.argv[6])
				for j in list_pal:
					new_url=url+new_palabra+"."+j
					page=session.get(new_url)
					print(new_url,"  -> Status code : ",page.status_code)
					if(page.status_code==200 or page.status_code==403):
						new_file.write(new_url + "  -> Status code :" + str(page.status_code))
						new_file.write("\n")
			else:
				print("Error al colocar los argumentos")
				menu_de_ayuda()
		else:
			new_url=url+new_palabra
			page=session.get(new_url)
			print(new_url,"  -> Status code : ",page.status_code)
			if(page.status_code==200 or page.status_code==403):
				new_file.write(new_url + "  -> Status code :" + str(page.status_code))
				new_file.write("\n")
else:
	print("Error al colocar los argumentos")
	menu_de_ayuda()
