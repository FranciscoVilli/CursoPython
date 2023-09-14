acl = int(input("Ingrese el vato del # de ACL: "))
if acl >= 1 and acl <=99:
    print("Es un ACL estnadar")
elif acl >= 100 and acl <=199:
    print("Es un ACL extendida")
else:
    print("El valor ingresado no es un ACL")

