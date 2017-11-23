print ('''
############################################################################################
#                          								   #	
#  __    __                      __              __        __  __  __                      #           
# |  \  |  \                    |  \            |  \      |  \|  \|  \                     #           
# | $$  | $$  ______    _______ | $$____        | $$   __  \$$| $$| $$  ______    ______   #           
# | $$__| $$ |      \  /       \| $$    \       | $$  /  \|  \| $$| $$ /      \  /      \  #           
# | $$    $$  \$$$$$$\|  $$$$$$$| $$$$$$$\      | $$_/  $$| $$| $$| $$|  $$$$$$\|  $$$$$$\ #           
# | $$$$$$$$ /      $$ \$$    \ | $$  | $$      | $$   $$ | $$| $$| $$| $$    $$| $$   \$$ #           
# | $$  | $$|  $$$$$$$ _\$$$$$$\| $$  | $$      | $$$$$$\ | $$| $$| $$| $$$$$$$$| $$       #           
# | $$  | $$ \$$    $$|       $$| $$  | $$      | $$  \$$\| $$| $$| $$ \$$     \| $$       #           
#  \$$   \$$  \$$$$$$$ \$$$$$$$  \$$   \$$       \$$   \$$ \$$ \$$ \$$  \$$$$$$$ \$$       #           
#                                                                                          #          
#          Coded By: Ismail Al_safadi              *random passwords*                      #          
############################################################################################               
''')


def info():
    print "information"
    print "This tool coded by: Ismael Al-safadi"
    print "to use the tool "
    print "[*] -chr = the possibilities"
    print "[*] -len = the length of password"
    print "[*] -num = the number of passwords that you want to generate"
    print "[*] -t = the type of the hash"
    print "[*] -hash = the value of the hash"
    print "[+] Example"
    print "python hash-kill-random.py -chr 1234567890 -len 5 -num 50000 -t md5 -hash d3eb9a9233e52948740d7eb8c3062d14"
	


import os
import sys
import time
import string
import argparse
import itertools

import hashlib
import random
def sound():
	try:
		import winsound
		winsound.Beep(1000,1000)
	except:
		pass
def hash_kill_random(chrs, the_length, the_number, type_type, myhash):
    
    print ('[i] Starting time: %s' % time.strftime('%H:%M:%S'))
    start = time.time()
    print "[+]Cracking..."
    count = 0
    for i in range(1,the_number):
        i=i*10
        string_rand=''.join((random.choice(chrs.format(str(i)))for i in range(the_length)))
        g=hashlib.new(type_type)
        g.update(string_rand)
        f=string_rand.encode("utf-8")
        p=g.hexdigest()
        if p == myhash:
            end = time.time()
            print ('[*]Hash is : ' + string_rand)
            print "[*]Time: %s seconds" % round((end - start), 2)
            print "[*]Words tried:" + (str(count))
            sound()
            break
        else:
            count += 1
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Python hash kill random generatore')
    parser.add_argument(
        '-chr', '--chars',
        default=None, help='characters to iterate')
    parser.add_argument(
        '-len', '--the_length', type=int,
        default=1, help='minimum length of characters')
    parser.add_argument(
        '-num', '--the_number', type=int,
        default=2, help='maximum length of characters')
    parser.add_argument(
        '-t', '--type_type', type=str,
        default=3, help='the type of the hash')

    parser.add_argument(
        '-hash', '--myhash',type=str,
        default=4, help='the hash value')

    args = parser.parse_args()
    if args.chars is None:
        args.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
    try:    
        hash_kill_random(args.chars, args.the_length, args.the_number, args.type_type,args.myhash)
    except:
        info()
