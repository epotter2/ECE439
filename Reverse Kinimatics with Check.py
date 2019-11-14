# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:33:22 2019

@author: eannp
"""
import numpy as np

#Constants for robot 
L1 = .1026
x1 = .031
L2 = .118
L3 = .1350
z1 = .02
L4 = .0290
penX = .008
penZ = .035

#input coords:
desTip = [.15,.05,0.0]
#desTip =  [.2,-.1,0]
#desTip =   [.2,-.02,0]
#desTip =  [.1,-.05,.2]

print("desired Point")
print(desTip)
print(" ")
print(" ")

#Reverse kinimatics calculations 
Xsqr = desTip[0]**2
Ysqr = desTip[1]**2

Alpha = np.arctan2(desTip[1],desTip[0])

deltaZ = desTip[2]-L1+penZ
deltaZsqr = deltaZ**2

deltaR = np.sqrt((Xsqr)+(Ysqr))-x1-penX-L4
deltaRsqr = deltaR**2

d = np.sqrt((deltaZsqr)+(deltaRsqr))

delta = np.arccos(((deltaZsqr)+(deltaRsqr)-(L2**2)-(L3**2))/(-2*L2*L3))

beta2 = (np.pi-(delta-np.radians(8.54)))

psi = np.arctan2(deltaZ,deltaR)

phi = np.arccos(((L3**2)-(d**2)-(L2**2))/(-2*L2*d))

beta1 = -(psi + phi)

beta4 = -(beta1+beta2)

gamma3 = 0
  
gamma5 = 0

angles = [Alpha,beta1,beta2,gamma3,beta4,gamma5]

#self verify with forward kinimatics equations 

beta2F = beta2 - np.radians(8.54)

X = (L3*(np.cos(beta1)*np.cos(beta2F)+(-np.sin(beta1))*np.sin(beta2F))+L2*np.cos(beta1)+penX+L4+x1)*np.cos(Alpha)
Y = (L3*(np.cos(beta1)*np.cos(beta2F)+(-np.sin(beta1))*np.sin(beta2F))+L2*np.cos(beta1)+penX+L4+x1)*np.sin(Alpha)
Z = L3*(np.sin(beta1)*np.cos(beta2F)+np.cos(beta1)*np.sin(beta2F))+L2*np.sin(beta1)-L1+penZ

#print to console 
print("angles ")
print(angles )
print(" ")
print(" ")

print("Self check, point: ")
print(X ,Y,Z)