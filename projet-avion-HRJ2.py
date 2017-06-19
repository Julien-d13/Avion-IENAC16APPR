###################################################################
# Fichier projet-avion-HRJ.py
# Projet avion semestre 6
# BITTERMANN Hugo, LOUISE Romain et RAPIN Julien - Date de début : 04/06/2017 - Date de fin :
###################################################################


###################################################################
# Importations
###################################################################

from math import *
import numpy as np, matplotlib.pyplot as plt, matplotlib.patches as patches
import dynamic as dyn, utils as ut
import scipy

###################################################################
# Fonctions
###################################################################

# Séance 2

# hs=[3000,11000]
x = np.linspace(3000,11000,16)
hs=x
ms=[0.2,1]
machs=[0.5,0.8]
km=[0.1,0.9]
Xe=[]
Ue=[]
alphatab1, alphatab2, dphrtab1, dphrtab2, dthtab1, dthtab2 = [], [], [], [], [], []
couples = [[0.2,0.1],[0.2,0.9],[1.,0.1],[1.,0.9]]

def evol_trym(P):
    for couple in couples:
        P.set_mass_and_static_margin(couple[1],couple[0])
        alpha1, alpha2, dphr1, dphr2, dth1, dth2 = [], [], [], [], [], []
        for h in hs:
            arg1 = {'va': dyn.va_of_mach(machs[0], h, k=1.4, Rs=287.05), 'h': h}
            alpha1.append(ut.deg_of_rad(dyn.trim(P,arg1)[0][3]))
            dphr1.append(ut.deg_of_rad(dyn.trim(P,arg1)[1][0]))
            dth1.append(dyn.trim(P,arg1)[1][1]*100)
            arg2 = {'va': dyn.va_of_mach(machs[1], h, k=1.4, Rs=287.05), 'h': h}
            alpha2.append(ut.deg_of_rad(dyn.trim(P,arg2)[0][3]))
            dphr2.append(ut.deg_of_rad(dyn.trim(P,arg2)[1][0]))
            dth2.append(dyn.trim(P,arg2)[1][1]*100)
        alphatab1.append(alpha1)
        alphatab2.append(alpha2)
        dthtab1.append(dth1)
        dthtab2.append(dth2)
        dphrtab1.append(dphr1)
        dphrtab2.append(dphr2)
    al1 = np.array(alphatab1)
    al2 = np.array(alphatab2)
    f, axarr = plt.subplots(4,3)
    axarr[0, 0].plot(x, al1[0],'b')
    axarr[0, 0].set_title('Alpha')
    axarr[1, 0].plot(x, al1[1],'b')
    axarr[2, 0].plot(x, al1[2],'b')
    axarr[3, 0].plot(x, al1[3],'b')
    axarr[0, 0].plot(x, al2[0],'r')
    axarr[1, 0].plot(x, al2[1],'r')
    axarr[2, 0].plot(x, al2[2],'r')
    axarr[3, 0].plot(x, al2[3],'r')
    dp1 = np.array(dphrtab1)
    dp2 = np.array(dphrtab2)
    axarr[0, 1].plot(x, dp1[0],'b')
    axarr[0, 1].set_title('Dphr')
    axarr[1, 1].plot(x, dp1[1],'b')
    axarr[2, 1].plot(x, dp1[2],'b')
    axarr[3, 1].plot(x, dp1[3],'b')
    axarr[0, 1].plot(x, dp2[0],'r')
    axarr[1, 1].plot(x, dp2[1],'r')
    axarr[2, 1].plot(x, dp2[2],'r')
    axarr[3, 1].plot(x, dp2[3],'r')
    dt1 = np.array(dthtab1)
    dt2 = np.array(dthtab2)
    axarr[0, 2].plot(x, dt1[0],'b')
    axarr[0, 2].set_title('Dth')
    axarr[1, 2].plot(x, dt1[1],'b')
    axarr[2, 2].plot(x, dt1[2],'b')
    axarr[3, 2].plot(x, dt1[3],'b')
    axarr[0, 2].plot(x, dt2[0],'r')
    axarr[1, 2].plot(x, dt2[1],'r')
    axarr[2, 2].plot(x, dt2[2],'r')
    axarr[3, 2].plot(x, dt2[3],'r')
    f.suptitle("Valeur de Alpha, Dphr et Dth pour un vol en palier en fonction de l'Altitude pour les couples \n [ms, km] suivants : [0.2, 0.1], [0.2, 0.9], [1., 0.1], [1., 0.9].      En bleu pour Mach = 0.5 et en rouge pour Mach = 0.8")
    plt.show()
            # print('h {} {} gaz {:.1f} %'.format(h, Xe,Ue[dyn.i_dth]*100))
            # plt.subplot(
            
            
#Q3
def trajectoire(M,h,ms,km,P):
    t = np.arange(0,100,0.5)
    P.set_mass_and_static_margin(km,ms)
    va = dyn.va_of_mach(M,h,k=1.4, Rs=287.05)
    param = {'va':va, 'h':h, 'gamma':0}
    Xe, Ue = dyn.trim(P,param)
    X = scipy.integrate.odeint(dyn.dyn, Xe, t, args=(Ue,P))
    trace = dyn.plot(t,X)
    plt.suptitle("Trajectoire de l'avion", fontsize = 22)
    plt.show()
    
    
#4
def trace_vpropres(liste,km,ms,M,h):
    plt.xlabel('partie reelle')
    plt.ylabel('partie imaginaire')
    # plt.title('M={}, h={}, ms={} et km={}'.format(M,h,ms,km))
    liste2 = np.array(liste)
    x,y = [], []
    for i in range(len(liste2)):
        x += [liste2[i].real]
        y += [liste2[i].imag]
    plt.plot(x,y,'bs')
    plt.suptitle("Variation des valeurs propres", fontsize=22)
    plt.show()

def reduire(m):
    i,j = 2,2
    matrice_red = np.array([[m[i][j],m[i][j+1],m[i,j+2],m[i,j+3]],[m[i+1,j],m[i+1,j+1],m[i+1,j+2],m[i+1,j+3]],[m[i+2,j],m[i+2,j+1],m[i+2,j+2],m[i+2,j+3]],[m[i+3,j],m[i+3,j+1],m[i+3,j+2],m[i+3,j+3]]])
    return matrice_red

def obtain_matrices(km,ms,M,h,P):
    P.set_mass_and_static_margin(km,ms)
    va = dyn.va_of_mach(M,h)
    param = {'va':va,'gamma':0,'h':h}
    X,U = dyn.trim(P,param)
    A,B = ut.num_jacobian(X,U,P,dyn.dyn)
    print('\n \n A et B pour M={}, h={}, ms={} et km={}'.format(M,h,ms,km))
    A2 = reduire(A)
    print(np.linalg.eig(A2))
    liste = np.linalg.eig(A2)[0]
    trace_vpropres(liste,km,ms,M,h)

def obtain_all_matrices(P):
    idx=1
    for km in kms:
        for ms in mss:
            for M in Ms:
                for h in hs:
                    plt.subplot(4,4,idx)
                    idx+=1
                    obtain_matrices(km,ms,M,h,P)
                    ax=plt.gca()
                    ax.set_ylim(-1, 1)
                    ax.set_xlim(-6, 6)
                    plt.text(-1,1 ,'M={}, h={} \n ms={} et km={}'.format(M,h,ms,km))
                    


# Tracés
hs = [3000, 11000]
Ms = [0.5, 0.8]
kms = [0.1,0.9]
mss = [0.2,1]
avion = dyn.Param_A321()
obtain_all_matrices(avion)

    
###################################################################
# Script principal de test
###################################################################

aircraft = dyn.Param_A321()
#evol_trym(aircraft)

#trajectoire(0.8,3000,0.2,0.1,aircraft)

#vitesse de convergence : exp(-Oméga * Xi * t)


###################################################################