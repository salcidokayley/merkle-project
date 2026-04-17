import hashlib

files = input("Enter files: ").split()

hashes = []

# hash each file
for name in files:
    f = open(name, "rb")
    data = f.read()
    f.close()

    h = hashlib.sha1(data).hexdigest()
    hashes.append(h)

# build tree
while len(hashes) > 1:
    new = []
    i = 0

    while i < len(hashes):
        if i + 1 < len(hashes):
            combined = hashes[i] + hashes[i+1]
        else:
            combined = hashes[i] + hashes[i]

        h = hashlib.sha1(combined.encode()).hexdigest()
        new.append(h)

        i = i + 2

    hashes = new

print("Top Hash:", hashes[0])
