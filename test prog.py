###################################################################
# Fichier projet-avion-HRJ.py
# Projet avion semestre 6
# BITTERMANN Hugo, LOUISE Romain et RAPIN Julien - Date de début : 04/06/2017 - Date de fin :
###################################################################


###################################################################
# Importations
###################################################################

import numpy as np, matplotlib.pyplot as plt, matplotlib.patches as mpatches
import dynamic as dyn, utils as ut


###################################################################
# Fonctions
###################################################################

def Trim_dyn(P):
    hs = [3000,11000]
    x = np.linspace(3000,11000,2)
    Ms = [0.5,0.8]
    couples = [[0.2,0.1],[0.2,0.9],[1.,0.1],[1.,0.9]]
    alphatab1, alphatab2, dphrtab1, dphrtab2, dthtab1, dthtab2 = [], [], [], [], [], []
    for couple in couples:
        P.set_mass_and_static_margin(couple[1], couple[0])
        alpha1, alpha2, dphr1, dphr2, dth1, dth2 = [], [], [], [], [], []
        for h in hs:
            param1 = {'va':dyn.va_of_mach(Ms[0],h), 'gamma':0, 'h':h}
            alpha1.append(dyn.trim(P,param1)[0][3])
            param2 = {'va':dyn.va_of_mach(Ms[1],h), 'gamma':0, 'h':h}
            alpha2.append(dyn.trim(P,param2)[0][3])
        alphatab1.append(alpha1)
        alphatab2.append(alpha2)
        for h in hs:
            param1 = {'va':dyn.va_of_mach(Ms[0],h), 'gamma':0, 'h':h}
            dphr1.append(dyn.trim(P,param1)[1][0])
            param2 = {'va':dyn.va_of_mach(Ms[1],h), 'gamma':0, 'h':h}
            dphr2.append(dyn.trim(P,param2)[1][0])
        dphrtab1.append(dphr1)
        dphrtab2.append(dphr2)
        for h in hs:
            param1 = {'va':dyn.va_of_mach(Ms[0],h), 'gamma':0, 'h':h}
            dth1.append(dyn.trim(P,param1)[1][1])
            param2 = {'va':dyn.va_of_mach(Ms[1],h), 'gamma':0, 'h':h}
            dth2.append(dyn.trim(P,param2)[1][1])
        dthtab1.append(dth1)
        dthtab2.append(dth2)
    print('alpha1 :',alphatab1)
    print('alpha2 :',alphatab2)
    print('dphr1 :',dphrtab1)
    print('dphr2 :',dphrtab2)
    print('dth1 :',dthtab1)
    print('dth2 :',dthtab2)
    al1 = np.array(alphatab1)
    al2 = np.array(alphatab2)
    f, axarr = plt.subplots(4,3)
    axarr[0, 0].plot(x, al1[0])
    axarr[0, 0].set_title('Alpha')
    axarr[1, 0].plot(x, al1[1])
    axarr[2, 0].plot(x, al1[2])
    axarr[3, 0].plot(x, al1[3])
    axarr[0, 0].plot(x, al2[0])
    axarr[1, 0].plot(x, al2[1])
    axarr[2, 0].plot(x, al2[2])
    axarr[3, 0].plot(x, al2[3])
    dp1 = np.array(dphrtab1)
    dp2 = np.array(dphrtab2)
    axarr[0, 1].plot(x, dp1[0])
    axarr[0, 1].set_title('Dphr')
    axarr[1, 1].plot(x, dp1[1])
    axarr[2, 1].plot(x, dp1[2])
    axarr[3, 1].plot(x, dp1[3])
    axarr[0, 1].plot(x, dp2[0])
    axarr[1, 1].plot(x, dp2[1])
    axarr[2, 1].plot(x, dp2[2])
    axarr[3, 1].plot(x, dp2[3])
    dt1 = np.array(dthtab1)
    dt2 = np.array(dthtab2)
    axarr[0, 2].plot(x, dt1[0])
    axarr[0, 2].set_title('Dth')
    axarr[1, 2].plot(x, dt1[1])
    axarr[2, 2].plot(x, dt1[2])
    axarr[3, 2].plot(x, dt1[3])
    axarr[0, 2].plot(x, dt2[0])
    axarr[1, 2].plot(x, dt2[1])
    axarr[2, 2].plot(x, dt2[2])
    axarr[3, 2].plot(x, dt2[3])
    f.suptitle("Valeur de Alpha, Dphr et Dth pour un vol en palier en fonction de l'Altitude pour les couples \n [ms, km] suivants : [0.2, 0.1], [0.2, 0.9], [1., 0.1], [1., 0.9]")
    plt.show()



###################################################################
# Script principal de test
###################################################################

aircraft = dyn.Param_A321()

Trim_dyn(aircraft)



###################################################################