lista = {}

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    lista[ext.lower()] = mt

for i in range(q):
    plik = input()  # One file name per line.

    plik_ext = plik
    if "." in plik:
        name, plik_ext = plik.rsplit(".", 1)
        found = False
        if plik_ext.lower() in lista:
            print(lista[plik_ext.lower()])
            found = True
        if not found:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
