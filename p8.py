n = int(input())
faces = 0
for i in range(n):
    s = input()
    if (s == "Tetrahedron"):
        faces += 4
    elif (s == "Cube"):
        faces += 6
    elif (s == "Octahedron"):
        faces += 8
    elif (s == "Dodecahedron"):
        faces += 12 
    elif (s == "Icosahedron") :
        faces += 20
print(faces)

