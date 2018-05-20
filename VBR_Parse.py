f = open('\\\\.\\C:', 'rb')
w_f = open("C:\\VBR_Parse.txt", 'w')

f.seek(0)
buf = f.read(3)
print ("Jump Instruction: ")
w_f.write("Jump Instruction: ")
for i in range(0, 3):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

w_f.write("\n-----------------------------------")
f.seek(3)
buf = f.read(8)
print ("\nOEM ID: ")
w_f.write("\nOEM ID: ")
for i in range(0, 8):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

w_f.write("\n-----------------------------------")
f.seek(11)
buf = f.read(2)
print ("\nBPB(Bytes Per Sector): ")
w_f.write("\nBPB(Bytes Per Sector): ")
for i in range(0, 2):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(13)
buf = f.read(1)
print ("\nBPB(Sector Per Cluster): ")
w_f.write("\nBPB(Sector Per Cluster): ")
for i in range(0, 1):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(14)
buf = f.read(2)
print ("\nBPB(Reserved Sectors): ")
w_f.write("\nBPB(Reserved Sectors): ")
for i in range(0, 2):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(16)
buf = f.read(5)
print ("\nBPB(Unused): ")
w_f.write("\nBPB(Unused): ")
for i in range(0, 5):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(21)
buf = f.read(1)
print ("\nBPB(Media Descriptor): ")
w_f.write("\nBPB(Media Descriptor): ")
for i in range(0, 1):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(22)
buf = f.read(2)
print ("\nBPB(Always 0): ")
w_f.write("\nBPB(Always 0): ")
for i in range(0, 2):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(24)
buf = f.read(2)
print ("\nBPB(Sector Per Track): ")
w_f.write("\nBPB(Sector Per Track): ")
for i in range(0, 2):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(26)
buf = f.read(2)
print ("\nBPB(Number of Heads): ")
w_f.write("\nBPB(Number of Heads): ")
for i in range(0, 2):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(28)
buf = f.read(4)
print ("\nBPB(Hidden Sectors): ")
w_f.write("\nBPB(Hidden Sectors): ")
for i in range(0, 4):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(32)
buf = f.read(8)
print ("\nBPB(Unused): ")
w_f.write("\nBPB(Unused): ")
for i in range(0, 8):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(40)
buf = f.read(8)
print ("\nBPB(Total Sectors): ")
w_f.write("\nBPB(Total Sectors): ")
for i in range(0, 8):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(48)
buf = f.read(8)
print ("\nBPB(Start Cluster for $MFT): ")
w_f.write("\nBPB(Start Cluster for $MFT): ")
for i in range(0, 8):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(56)
buf = f.read(8)
print ("\nBPB(Start Cluster for $MFTMirr): ")
w_f.write("\nBPB(Start Cluster for $MFTMirr): ")
for i in range(0, 8):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(64)
buf = f.read(1)
print ("\nBPB(Cluster Per Record): ")
w_f.write("\nBPB(Cluster Per Record): ")
for i in range(0, 1):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(65)
buf = f.read(3)
print ("\nBPB(Unused): ")
w_f.write("\nBPB(Unused): ")
for i in range(0, 3):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(68)
buf = f.read(1)
print ("\nBPB(Cluster Per Index): ")
w_f.write("\nBPB(Cluster Per Index): ")
for i in range(0, 1):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(69)
buf = f.read(3)
print ("\nBPB(Unused): ")
w_f.write("\nBPB(Unused): ")
for i in range(0, 3):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(72)
buf = f.read(8)
print ("\nBPB(Volume Serial Number): ")
w_f.write("\nBPB(Volume Serial Number): ")
for i in range(0, 8):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

f.seek(80)
buf = f.read(3)
print ("\nBPB(Unused): ")
w_f.write("\nBPB(Unused): ")
for i in range(0, 3):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')

w_f.write("\n-----------------------------------")
f.seek(84)
buf = f.read(426)
print ("\nBootstrap Code: ")
w_f.write("\nBootstrap Code: ")
for i in range(0, 426):
	print (hex(buf[i]))	
	w_f.write(hex(buf[i])+ ' ')

w_f.write("\n-----------------------------------")
f.seek(510)
buf = f.read(2)
print ("\nSignature: ")
w_f.write("\nSignature: ")
for i in range(0, 2):
	print (hex(buf[i]))
	w_f.write(hex(buf[i])+ ' ')
