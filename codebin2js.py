import struct

j = 0;

"""
for i in range(0x2000):
    print "0x90, ",
    if i%32 == 31:
        print ""
"""
print "["

try:
    f = open("wiiuhaxx_loader.bin", "rb")
    while True:
        B = struct.unpack(">B", f.read(1))[0];
        print "0x%02x," % (B),
        j+=1
except:
    print ""

for i in range(j&0x03):
    print "0x00, "
print ""

#print "0x48, 0x00, 0x00, 0x05, 0x7c, 0x68, 0x02, 0xa6, 0x38, 0x80, 0x00, 0x48, 0x7c, 0x84, 0x1a, 0x14, 0x80, 0xa4, 0x00, 0x00, 0x38, 0x84, 0x00, 0x04, 0x7f, 0xa3, 0xeb, 0x78, 0x38, 0xc0, 0x00, 0x02, 0x7c, 0xa5, 0x34, 0x30, 0x7c, 0xa9, 0x03, 0xa6, 0x80, 0xa4, 0x00, 0x00, 0x90, 0xa3, 0x00, 0x00, 0x38, 0x84, 0x00, 0x04, 0x38, 0x63, 0x00, 0x04, 0x42, 0x00, 0xff, 0xf0, 0x7c, 0x21, 0xf2, 0x14, 0x80, 0x61, 0x00, 0x04, 0x7c, 0x69, 0x03, 0xa6, 0x4e, 0x80, 0x04, 0x20,"
print "0x00, 0x20, 0x00, 0x00,"
j+=4
    
try:
    f = open("code550.bin", "rb")
    while True:
        B = struct.unpack(">B", f.read(1))[0];
        print "0x%02x," % (B),
        j+=1
except:
    print ""
    
for i in range(j&0x03):
    print "0x00,",
print ""

#padding
for i in range(j, 0x2000-4):
    print "0x90,",
print ""
print "]"