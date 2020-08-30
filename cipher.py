import sys

if(len(str(sys.argv[1])) != 26):
    print("invalid KEY. KEY must contain 26 characters")
else:
    normal = input("TEXT:")
    normal = str(normal)
    key = str(sys.argv[1])
    alpha ="abcdefghigklmnopqrstuvwxyz"
    cipher= ""
    for i in normal:
        if(i.isalpha()):
            if(i.isupper()):
                subt = key[alpha.upper().find(i)]
                cipher = cipher + subt.upper()
            else:
                subt = key[alpha.find(i)]
                cipher = cipher + subt.lower()
        else:
            cipher = cipher + i


    print("normal text: ", normal)
    print("cipher text: ", cipher)
