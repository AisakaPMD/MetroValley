import struct

w = int(input("Width: "))
h = int(input("Height: "))
f = int(input("Fill with: "))
r = "assets/maps/farm_map.bin"  # input("Filename: ")

fi = open(r, "wb")

fi.write(struct.pack(">I", w))
fi.write(struct.pack(">I", h))

for y in range(h):
    for x in range(w):
        fi.write(struct.pack(">B", f))

fi.close()

print("Done!")
