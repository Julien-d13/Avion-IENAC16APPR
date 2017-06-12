###################################################################
# Fichier projet-avion-HRJ.py
# Projet avion semestre 6
# BITTERMANN Hugo, LOUISE Romain et RAPIN Julien - Date de début : 04/06/2017 - Date de fin :
###################################################################


###################################################################
# Importations
###################################################################

import numpy as np, matplotlib.pyplot as plt, matplotlib.patches as patches
import dynamic as dyn, utils as ut


###################################################################
# Fonctions
###################################################################

# Séance 1

# 1
def evol_poussee(P):
    U = [0,1,0,0]
    hs = np.linspace(3000,11000,5)
    machs = np.linspace(0.5,0.8,30)
    for h in hs:
        Poussee = [dyn.propulsion_model([0,h,dyn.va_of_mach(mach,h),0,0,0], U, P) for mach in machs]
        plt.plot(machs, Poussee)
    ut.decorate(plt.gca(), title='Poussée maximale en fonction du Mach', xlab='Mach', ylab='Poussee (N)', legend=['{} m'.format(h) for h in hs])
    plt.show()

# 2
def evol_coeff_portance(P):
    alphas = np.arange(ut.rad_of_deg(-10),ut.rad_of_deg(20),ut.rad_of_deg(1))
    dphrs = [ut.rad_of_deg(-30),ut.rad_of_deg(20)]
    q=0
    Cz_tab1=[]
    Cz_tab2=[]
    for alpha in alphas:
        coeff_portance1= dyn.get_aero_coefs(dyn.va_of_mach(0.7,7000), alpha, q, dphrs[0], P)
        Cz_tab1.append(coeff_portance1[0])
        coeff_portance2= dyn.get_aero_coefs(dyn.va_of_mach(0.7,7000), alpha, q, dphrs[1], P)
        Cz_tab2.append(coeff_portance2[0])
    plt.plot(ut.deg_of_rad(alphas),Cz_tab1,'r')
    plt.plot(ut.deg_of_rad(alphas), Cz_tab2,'b')
    label1 = patches.Patch(color='red',label='dPHR1 = -30°')
    label2 = patches.Patch(color='blue',label='dPHR2 = 20°')
    plt.legend(loc='upper left',handles=[label1,label2])
    ut.decorate(plt.gca(), title="Evolution du Cz en fonction de l'incidence", xlab='Incidence', ylab='Cz')
    plt.show()
    
# 3
def evol_Cm(P):
    ms = [-0.1,0,0.2,1]
    dphr = 0 
    alphas = np.arange(ut.rad_of_deg(-10),ut.rad_of_deg(20),ut.rad_of_deg(1))
    Cm_tab1 = []
    Cm_tab2 = []
    Cm_tab3 = []
    Cm_tab4 = []
    q = 0
    for alpha in alphas:
        Cm1 = P.Cm0 - ms[0]*P.CLa*(alpha-P.a0) + P.Cmq*P.lt/dyn.va_of_mach(0.7,7000)*q + P.Cmd*dphr
        Cm_tab1.append(Cm1)
        Cm2 = P.Cm0 - ms[1]*P.CLa*(alpha-P.a0) + P.Cmq*P.lt/dyn.va_of_mach(0.7,7000)*q + P.Cmd*dphr
        Cm_tab2.append(Cm2)
        Cm3 = P.Cm0 - ms[2]*P.CLa*(alpha-P.a0) + P.Cmq*P.lt/dyn.va_of_mach(0.7,7000)*q + P.Cmd*dphr
        Cm_tab3.append(Cm3)
        Cm4 = P.Cm0 - ms[3]*P.CLa*(alpha-P.a0) + P.Cmq*P.lt/dyn.va_of_mach(0.7,7000)*q + P.Cmd*dphr
        Cm_tab4.append(Cm4)
    plt.plot(ut.deg_of_rad(alphas),Cm_tab1)
    plt.plot(ut.deg_of_rad(alphas),Cm_tab2)
    plt.plot(ut.deg_of_rad(alphas),Cm_tab3)
    plt.plot(ut.deg_of_rad(alphas),Cm_tab4)
    label1 = patches.Patch(color='blue',label='ms = -0.1')
    label2 = patches.Patch(color='green',label='ms = 0')
    label3 = patches.Patch(color='red',label='ms = 0.2')
    label4 = patches.Patch(color='cyan',label='ms = 1')
    plt.legend(loc='upper right',handles=[label1,label2,label3,label4])
    ut.decorate(plt.gca(), title="Evolution du Cm en fonction de l'incidence", xlab='Incidence', ylab='Cm')
    plt.show()
        
    
###################################################################
# Script principal de test
###################################################################

aircraft = dyn.Param_A321()

#evol_poussee(aircraft)
#evol_coeff_portance(aircraft)
evol_Cm(aircraft)


###################################################################