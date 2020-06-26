#!/bin/python

import sys
import socket
from datetime import datetime

#სამიზნის განსაზღვრა

if len (sys.argv) == 2:
         target = socket.gethostbyname(sys.argv[1]) #ჰოსტნეიმის აიპი 4-ში გადათარგმნა
else:
        print("არასწორ არგუმენტთა რაოდენობა.")
        print("სინტაქსი: python3 scanner.py <ip>")

#ლამაზი ბანერი
print("-" * 50)
print("ვასკანირებ სამიზნეს "+target)
print("დაწყების დრო: "+str(datetime.now()))
print("-" * 50)

try:
       for port in range (1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port)) #აბრუნებს შეცდომის ინდიკატორს
                if result == 0:
                        print("პორტი {} ღიაა".format(port))
                s.close()

except KeyboardInterrupt:
       print("\nვთიშავ პროგრამას.")
       sys.exit()

except socket.gaierror:
       print("ჰოსტი ვერ იქნა გადაწყვეტილი.")
       sys.exit()

except socket.error:
       print("ვერ ვუკავშირდები სერვერს.")
       sys.exit()
