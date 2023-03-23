def etat0(string):
	if string[0]=='+'or'-':
		return etat1(string[1:])
	elif string[0]=='1' or string[0]=='2' or string[0]=='3' or string[0]=='4' or string[0]=='5' or string[0]=='6' or string[0]=='7' or string[0]=='8' or string[0]=='9':
		return etat2(string[1:])
	else:
		return False
def etat1(string):
	if string[0]=='1' or string[0]=='2' or string[0]=='3' or string[0]=='4' or string[0]=='5' or string[0]=='6' or string[0]=='7' or string[0]=='8' or string[0]=='9':
		return etat2(string[1:])
	else:
		return False

def etat2(string):
	if string[0]=='1' or string[0]=='2' or string[0]=='3' or string[0]=='4' or string[0]=='5' or string[0]=='6' or string[0]=='7' or string[0]=='8' or string[0]=='9':
		return etat2(string[1:])
	elif string[0]=='.':
		return etat3(string[1:])
	elif string[0]=='\n':
		return True
	else:
		return False
def etat3(string):
	if string[0]=='1' or string[0]=='2' or string[0]=='3' or string[0]=='4' or string[0]=='5' or string[0]=='6' or string[0]=='7' or string[0]=='8' or string[0]=='9':
		return etat4(string[1:])
	else:
		return False
def etat4(string):
	if string[0]=='1' or string[0]=='2' or string[0]=='3' or string[0]=='4' or string[0]=='5' or string[0]=='6' or string[0]=='7' or string[0]=='8' or string[0]=='9':
		return etat4(string[1:])
	elif string[0]=='e' or string[0]=='E':
		return etat5(string[1:])
	elif string[0]=='\n':
		return True
	else:
		return False
def etat5(string):
	if string[0]=='1' or string[0]=='2' or string[0]=='3' or string[0]=='4' or string[0]=='5' or string[0]=='6' or string[0]=='7' or string[0]=='8' or string[0]=='9':
		return etat7(string[1:])
	elif string[0]=='+' or string[0]=='-':
		return etat6(string[1:])
	else:
		return False
def etat6(string):
	if string[0]=='1' or string[0]=='2' or string[0]=='3' or string[0]=='4' or string[0]=='5' or string[0]=='6' or string[0]=='7' or string[0]=='8' or string[0]=='9':
		return etat7(string[1:])
	else:
		return False
def etat7(string):
	if string[0]=='1' or string[0]=='2' or string[0]=='3' or string[0]=='4' or string[0]=='5' or string[0]=='6' or string[0]=='7' or string[0]=='8' or string[0]=='9':
		return etat7(string[1:])
	elif string[0]=='\n':
		return True
	else:
		return False

def op(string):

	if string[0]=='<' and string[1]=='=' and string[2]=='\n':
		return True
	elif string[0]=='>' and string[1]=='=' and string[2]=='\n':
		return True
	elif string[0]=='<' and string[1]=='>' and string[2]=='\n':
		return True
	elif string[0]=='=' and string[1]=='=' and string[2]=='\n':
		return True
	elif (string[0]=='<' and string[1]=='\n') or (string[0]=='>' and string[1]):
		return True
	else:
		return False

def nomcommande(string):
	if string[0]>='a' and string[0]<='z':
		return nomcommande1(string[1:])
	else:
		return False
def nomcommande1(string):
	if string[0]>='a' and string[0]<='z':
		return nomcommande1(string[1:])
	elif string[0]==' ':
		return arg(string[1:])
	elif string[0]=='\n':
		return True
	else:
		return False
def arg(string):
	if string[0]>='a' and string[0]<='z':
		return arg2(string[1:])
	elif string[0]=='[':
		return opt(string[1:])
	elif string[0]=='\n':
		return True
	else:
		return False
def arg2(string):
	if string[0]>='a' and string[0]<='z':
		return arg2(string[1:])
	elif string[0]==' ':
		return arg(string[1:])
	elif string[0]=='\n':
		return True
	else:
		return False
def opt(string):
	if string[0]=='-':
		return opt2(string[1:])
	else:
		return False
def opt2(string):
	if string[0]>='a' and string[0]<='z':
		return opt3(string[1:])
	else:
		return False
def opt3(string):
	if string[0]==']':
		return True
	else: 
		return False

string=input("entrer une chaine:")
string= string+"\n"


if(etat0(string)):
	print("number")
elif(op(string)):
	print("operator")
elif(nomcommande(string)):
	print("commande")
else:
	print("flase")