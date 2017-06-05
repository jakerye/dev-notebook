# Python Bytes

## Print bytearray (useful for logging)
```
a = bytearray((0x00, 0x01, 0x02))
print(''.join('{:02x} '.format(x) for x in a))
```
