#Blond lengths, angle and torsion angles of backbone atoms in a protein
import re
from math import acos, pi
atoms = ['HT1', 'HT2', 'HT3', 'N', 'CA', 'HA', 'C', 'O', 'HN', 'OXT']
coo = []
coo_ind = []
row = 0

#Extracting backbone atoms
print ("Backbone atoms and their x, y, z coordinates:")
with open (r"diala.pdb", "r") as f:
    for line in f.readlines():
        m = re.search ("^ATOM *[0-9]* *([NCAOHBTX123]*).*      ([ -][0-9]*[.][0-9]*) *([ -][0-9]*[.][0-9]*) *([ -][0-9]*[.][0-9]*)", line)
        if m and m.group(1) in atoms:
            coo.append (list (m.groups()))
            coo_ind.append (m.group(1))
            coo_ind.append (row)
            print (f"x, y, z coordinates of {m.group(1)}: {m.group(2)}, {m.group(3)}, {m.group(4)}")
            row += 1

#Defining the formula for bond length
def dist (row1, row2):
    return (((float(coo[row2][1]) - float(coo[row1][1]))**2 + (float(coo[row2][2]) - float(coo[row1][2]))**2 + (float(coo[row2][3]) - float(coo[row1][3]))**2)**0.5)

#Declaring the backbone connections
connect = [['N', 'HT1'], ['N', 'HT2'], ['N', 'HT3'], ['N', 'CA'], ['CA', 'HA'], ['CA', 'C'], ['C', 'O'], ['C', 'N'], ['N', 'HN'], ['C', 'OXT']]
l = []
a = []

#Bond lengths
print ("\nBond lengths:")
for i in range (row):
    for j in range (i+1, row):
        if [coo[i][0], coo[j][0]] in connect:
            length = dist (i, j)
            if length <= 2:
                l.append ([coo[i][0], coo[j][0], length])
                print (f"Distance between {coo[i][0]}, {coo[j][0]}: {length}")

#Bond angles
print ("\nBond angles:")
ind = coo_ind.copy ()
for i in range (len(l)):
    if l[i][0] == 'C' and l[i][1] == 'N':
        ind [ind.index('N')], ind [ind.index('CA')], ind [ind.index('HA')] = ' ' * 3
    for j in range (i+1, len(l)):
        if l[j][0] == 'C' and l[j][1] == 'N':
            break
        if len ({l[i][0], l[i][1], l[j][0], l[j][1]}) == 3:
            x = {l[i][0], l[i][1]}.difference ({l[j][0], l[j][1]}).pop()
            y = {l[j][0], l[j][1]}.difference ({l[i][0], l[i][1]}).pop()
            z = {l[i][0], l[i][1]}.intersection ({l[j][0], l[j][1]}).pop()
            cos = (l[i][2]**2 + l[j][2]**2 - dist(ind[ind.index(x)+1], ind[ind.index(y)+1])**2) / (2*l[i][2]*l[j][2])
            if cos >= -1 and cos <= 1:
                angle = (acos(cos))*(180/pi)
                a.append ([x, z, y, angle])
                print (f"Angle between {x}, {z}, {y}: {angle}")
    if l[i][0] == 'C' and l[i][1] == 'N':
        ind [ind.index('C')], ind [ind.index('O')] = ' ' * 2

#Bond torsions
print ("\nBond torsions:")
ind = coo_ind.copy ()    
for i in range (len(a)):
    for j in range (i+1, len(a)):
        if a[j][0] == 'C' and a[j][1] == 'N':
            break
        if len ({a[i][0], a[i][1], a[i][2], a[j][0], a[j][1], a[j][2]}) == 4:
            x = {a[i][0], a[i][1], a[i][2]}.difference ({a[j][0], a[j][1], a[j][2]}).pop()
            y = {a[j][0], a[j][1], a[j][2]}.difference ({a[i][0], a[i][1], a[i][2]}).pop()
            z = list ({a[i][0], a[i][1], a[i][2]}.intersection ({a[j][0], a[j][1], a[j][2]}))
            if (([x, z[0]] in connect or [z[0], x] in connect) and ([y, z[1]] in connect or [z[1], y] in connect)) or (([x, z[1]] in connect or [z[1], x] in connect) and ([y, z[0]] in connect or [z[0], y] in connect)):
                one = ind[ind.index(x)+1]
                if ([x, z[0]] in connect or [z[0], x] in connect) and ([y, z[1]] in connect or [z[1], y] in connect):
                    two = ind[ind.index(z[0])+1]
                    three = ind[ind.index(z[1])+1]
                elif ([x, z[1]] in connect or [z[1], x] in connect) and ([y, z[0]] in connect or [z[0], y] in connect):
                    two = ind[ind.index(z[1])+1]
                    three = ind[ind.index(z[0])+1]
                four = ind[ind.index(y)+1]
                print (one, two, three, four)
                v1_x = float(coo[one][1]) - float(coo[two][1])
                v1_y = float(coo[one][2]) - float(coo[two][2])
                v1_z = float(coo[one][3]) - float(coo[two][3])
                v2_x = float(coo[two][1]) - float(coo[three][1])
                v2_y = float(coo[two][2]) - float(coo[three][2])
                v2_z = float(coo[two][3]) - float(coo[three][3])
                v3_x = float(coo[three][1]) - float(coo[four][1])
                v3_y = float(coo[three][2]) - float(coo[four][2])
                v3_z = float(coo[three][3]) - float(coo[four][3])
                v4_x = (v1_y*v2_z) - (v1_z*v2_y)
                v4_y = -(v1_x*v2_z) + (v1_z*v2_x)
                v4_z = (v1_x*v2_y) - (v1_y*v2_x)
                v4 = ((v4_x**2) + (v4_y**2) + (v4_z**2))**0.5
                v5_x = (v2_y*v3_z) - (v2_z*v3_y)
                v5_y = -(v2_x*v3_z) + (v2_z*v3_x)
                v5_z = (v2_x*v3_y) - (v2_y*v3_x)
                v5 = ((v5_x**2) + (v5_y**2) + (v5_z**2))**0.5
                v4_v5 = (v4_x*v5_x) + (v4_y*v5_y) + (v4_z*v5_z)
                torsion = (acos (v4_v5 / (v4*v5))) * (180/pi)
                print (f"Dihedral angle between {coo[one][0]}, {coo[two][0]}, {coo[three][0]}, {coo[four][0]}: {torsion}")

'''
for i in range (row):
    c = connect.copy ()
    for j in range (i+1, row):
        if [coo[i][0], coo[j][0]] in c or [coo[j][0], coo[i][0]] in c:
            try:
                c[c.index([coo[i][0], coo[j][0]])] = []
            except:
                c[c.index([coo[j][0], coo[i][0]])] = []
            for k in range (j+1, row):
                if [coo[j][0], coo[k][0]] in c or [coo[k][0], coo[j][0]] in c:
                    try:
                        c[c.index([coo[j][0], coo[k][0]])] = []
                    except:
                        c[c.index([coo[k][0], coo[j][0]])] = []
                    for l in range (k+1, row):
                        if [coo[k][0], coo[l][0]] in c or [coo[l][0], coo[k][0]] in c:
                            v1_x = float(coo[i][1]) - float(coo[j][1])
                            v1_y = float(coo[i][2]) - float(coo[j][2])
                            v1_z = float(coo[i][3]) - float(coo[j][3])
                            v2_x = float(coo[j][1]) - float(coo[k][1])
                            v2_y = float(coo[j][2]) - float(coo[k][2])
                            v2_z = float(coo[j][3]) - float(coo[k][3])
                            v3_x = float(coo[k][1]) - float(coo[l][1])
                            v3_y = float(coo[k][2]) - float(coo[l][2])
                            v3_z = float(coo[k][3]) - float(coo[l][3])
                            v4_x = (v1_y*v2_z) - (v1_z*v2_y)
                            v4_y = -(v1_x*v2_z) + (v1_z*v2_x)
                            v4_z = (v1_x*v2_y) - (v1_y*v2_x)
                            v4 = (v4_x**2 + v4_y**2 + v4_z**2)**0.5
                            v5_x = (v2_y*v3_z) - (v2_z*v3_y)
                            v5_y = -(v2_x*v3_z) + (v2_z*v3_x)
                            v5_z = (v2_x*v3_y) - (v2_y*v3_x)
                            v5 = (v5_x**2 + v5_y**2 + v5_z**2)**0.5
                            v4_v5 = (v4_x*v5_x) + (v4_y*v5_y) + (v4_z*v5_z)
                            torsion = (acos (v4_v5 / (v4*v5))) * (180/pi)
                            print (i, j, k, l)
                            #print (torsion)
                            t.append ([coo[i][0], coo[j][0], coo[k][0], coo[l][0], torsion])
                            if [coo[k][0], coo[l][0]] in c:
                                c[c.index([coo[k][0], coo[l][0]])] = []
                            elif [coo[l][0], coo[k][0]] in c:
                                c[c.index([coo[l][0], coo[k][0]])] = []
'''
