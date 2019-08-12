# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 21:04:15 2019

@author: CeciliaGJ
"""

from __future__ import division             # hace que se utilice la división en punto flotante
import numpy as np                          
import matplotlib.pyplot as plt             
from PIL import Image                      
from numpy.fft import fft2, fftshift, ifft2 
#matplotlib inline 
#creando una imagen periódica de tamaño  (601,1201)
#El periodo,  10.5 , aparece en la dirección horizontal.
# En vertical, la imagen es constante
hW, hH = 600, 300    
hFrec = 10.5     

# Crea una malla en el cuadrado de dimensiones [0,1)x[0,1)
x = np.linspace( 0, 2*hW/(2*hW +1), 2*hW+1)     # columnas (Anchura)
y = np.linspace( 0, 2*hH/(2*hH +1), 2*hH+1)     # filas    (Altura)
#################################
[X,Y] = np.meshgrid(x,y)
A = np.sin(hFrec*2*np.pi*X)
B = np.cos(hFrec*2*np.pi*X)
#################################
#################################
#plt.imshow(A, extent=[0,1,0,1], cmap ='seismic');
#plt.imshow(B, extent=[0,1,0,1], cmap ='seismic');
#plt.savefig('001.2.jpg')
################################
################################
H,W = np.shape(A)   # Dimensiones de la imagen A
print("La dimensión de la imagen A",H,W)
################################
################################
#Representando la función  (A y B)=f(X,Y)  
#como una superficie, un corte por un plano paralelo 
#al plano  OXZ  de dicha superficie sería....
################################
xx = np.linspace(0,1,1200)
AA = np.sin(hFrec*2*np.pi*xx)
BB = np.cos(hFrec*2*np.pi*xx)
################################
#plt.plot(AA, color="red", linewidth=2.5, linestyle="-", label="Señal 1-Seno")
#plt.plot(BB, color="blue",  linewidth=2.5, linestyle="-", label="Señal 2-Coseno")
#plt.legend(loc='upper left')
# =============================================================================
# ~
# =============================================================================
#plt.ylabel('V(t)')
#plt.xlabel('Dominio del tiempo(s)')
#plt.savefig('001.3.jpg')
#Calcular la DFT centrada en el origen y mostrar la figura del espectro de potencia (su raíz cuadrada)
FA1 = fft2(A)
FA = fft2(A)/(W*H)                          
FA = fftshift(FA)
PA = np.abs(FA)                            
#plt.imshow(P, extent = [-hW,hW,-hH,hH]);
#plt.savefig('001.4.jpg')
###################
#plt.imshow(PA[hH-25:hH+25,hW-25:hW+25], extent=[-25,25,-25,25]);
#plt.savefig('001.5.jpg')
#######################################
FB1 = fft2(B)
FB = fft2(B)/(W*H)                          
FB = fftshift(FB)
PB = np.abs(FB)                            
#plt.imshow(PB, extent = [-hW,hW,-hH,hH]);
#plt.savefig('001.6.jpg')
###################
#plt.imshow(PB[hH-25:hH+25,hW-25:hW+25], extent=[-25,25,-25,25]);
#plt.savefig('001.7.jpg')
##################
#plt.plot(range(-25,25),PA[hH,hW-25:hW+25])
#plt.savefig('001.6.1.jpg')
#plt.show()
#############################
plt.plot(range(-25,25),PA[hH,hW-25:hW+25])
plt.savefig('001.7.1.jpg')
plt.show()
###################################
#Calculo del espectro cuadrado de potencia
Gms=[]
Gmm=[]
Gss=[]
Gms=[A1.conjugate()*B1 for a,b in zip(FA1,FB1)]
print("La dimensión de la imagen A",Gms)
