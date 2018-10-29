import sys

serial_number = int(sys.argv[1])
field_width = int(sys.argv[2])

prefix_bytes = [ field_width, 0x13, 0xf0, 0x00 ]

ihx_line = []
for byte in prefix_bytes:
  ihx_line.append("%02x" % byte)

bytes = []
while serial_number > 0:
  byte = serial_number & 0xff
  bytes.append(byte)
  serial_number = serial_number >> 8

for i in range(field_width - len(bytes)):
  ihx_line.append("%02x" % 0)

checksum = 0x100 - (sum(prefix_bytes + bytes) & 0xff)

for byte in bytes:
  ihx_line.append("%02x" % byte)

ihx_line.append("%02x" % checksum)

print ':' + ''.join(ihx_line)
print ":00000001FF"
