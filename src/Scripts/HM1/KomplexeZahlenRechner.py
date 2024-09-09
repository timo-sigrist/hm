import numpy as np

z1 = (3 - 11j)
z2 = (3 + 4j)

calc = False

winkelInGrad = np.arctan2(z1.imag, z1.real)*360/(2* (np.pi))
bogenmass = np.arctan2(z1.imag,z1.real)
bogenmass_durch_pi = bogenmass / np.pi
r = np.sqrt(z1.imag**2 + z1.real**2)

if calc:
    print()
    print("Addiert       z1 + z2 = " + str(z1+z2))
    print("Subtrahiert   z1 - z2 = " + str(z1-z2))
    print("Multipliziert z1 * z2 = " + str(z1*z2))
    print("Dividiert     z1 / z2 = " + str(z1/z2))

print()
print("Bogenmass ohne Pi z1 = " + str(bogenmass))
print("Bogenmass z1 =         " + str(bogenmass_durch_pi)+ " * Pi")
print("Gradmass  z1 =         " + str(winkelInGrad)+" Grad")
print("r = |z| =              " + str(r))
print()
print("Trigonometrische Form; z = r * (cos(phi) + i*sin(phi):           " + "z = "+str(r)+" * (cos("+str(winkelInGrad)+") + i*sin("+str(winkelInGrad)+"))")
print("Trigonometrische Form; Realteil x = r * cos(phi):                " + "x = "+str(r)+" * cos("+str(winkelInGrad)+")")
print("Trigonometrische Form; Imaginärteil y = r * sin(phi):            " + "x = "+str(r)+" * sin("+str(winkelInGrad)+")")
print("Exponentialform von z= r*e^i*phi = cos(phi) + i * sin(phi):      " + "z = "+str(r)+"*e^(i*"+str(winkelInGrad)+") = cos("+str(winkelInGrad)+") + sin("+str(winkelInGrad)+")")
print("Exponentialform von z*= r*e^i*phi = cos(phi) + i * sin(phi):     " + "z = "+str(r)+"*e^(i*"+str(winkelInGrad*-1)+")"+" = cos("+str(winkelInGrad*-1)+") + sin("+str(winkelInGrad*-1)+")")


comp = complex(z1)
real = complex(z1).real
print("Komplexe Zahl: " + str(comp))
print("Reelle Zahl: " + str(real))


