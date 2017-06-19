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
        
#4

def evol_dphre(P):
    mss=[-0.1,0,0.2,1]
    alphas = np.arange(ut.rad_of_deg(-10),ut.rad_of_deg(20),ut.rad_of_deg(1))
    km=0.1
    for ms in mss:
        P.set_mass_and_static_margin(km, ms)
        dphrs=[]
        dphrs = np.array([(P.ms*P.CLa*(alpha-P.a0)-P.Cm0)/P.Cmd for alpha in alphas]  )  
        plt.plot(ut.deg_of_rad(alphas),ut.deg_of_rad(dphrs))
    legends=['ms {}'.format(ms) for ms in mss]
    ut.decorate(plt.gca(), "Evolution de DPHRe en fonction de l'incidence", 'Incidence', 'Delta de braquage équilibré', legend=legends)
    plt.figure()
    Vts=[0.9,1,1.1]
    for Vt in Vts:
        P.Vt=Vt
        P.Cmd=-P.Vt*P.CLat
        dphrs = np.array([(P.ms*P.CLa*(alpha-P.a0)-P.Cm0)/P.Cmd for alpha in alphas] ) 
        plt.plot(ut.deg_of_rad(alphas),ut.deg_of_rad(dphrs))
    legends=['Vt {}'.format(Vt) for Vt in Vts]
    ut.decorate(plt.gca(), "Evolution de DPHRe en fonction de l'incidence", 'Incidence', 'Delta de braquage équilibré', legend=legends)
    plt.show()
    
#5    
def evol_CLe(P):
    q=0
    mss=[0.2,1]
    alphas = np.arange(ut.rad_of_deg(-10),ut.rad_of_deg(20),ut.rad_of_deg(1))
    km=0.1
    for ms in mss:
        P.set_mass_and_static_margin(km, ms)
        dphrs=[]
        dphrs = np.array([(P.ms*P.CLa*(alpha-P.a0)-P.Cm0)/P.Cmd for alpha in alphas]  )
        CLe=[]
        CLe = [dyn.get_aero_coefs(dyn.va_of_mach(0.7,7000), alpha, q, dphr, P)[0] for alpha,dphr in zip(alphas,dphrs)]
        plt.plot(ut.deg_of_rad(alphas), CLe)
    label1 = patches.Patch(color='blue',label='ms = 0.2')
    label2 = patches.Patch(color='green',label='ms = 1')
    plt.legend(loc='upper left',handles=[label1,label2])
    ut.decorate(plt.gca(), "Evolution de CLe en fonction de l'incidence", 'Incidence', 'Coefficient de portance équilibrée')
    plt.show
    
#6
def polaire_equi(P):
    q=0
    mss=[0.2,1]
    alphas = np.arange(ut.rad_of_deg(-10),ut.rad_of_deg(20),ut.rad_of_deg(1))
    km=0.1
    for ms in mss:
        P.set_mass_and_static_margin(km, ms)
        dphrs=[]
        dphrs = np.array([(P.ms*P.CLa*(alpha-P.a0)-P.Cm0)/P.Cmd for alpha in alphas]  )
        CLe=[]
        CLe = [dyn.get_aero_coefs(dyn.va_of_mach(0.7,7000), alpha, q, dphr, P)[0] for alpha,dphr in zip(alphas,dphrs)]
        Cxe=[dyn.get_aero_coefs(dyn.va_of_mach(0.7,7000), alpha, q, dphr, P)[1] for alpha,dphr in zip(alphas,dphrs)]
        finesse=[CL/Cx for Cx,CL in zip(Cxe,CLe)]
        fmax=np.max(finesse)
        idmax=np.argmax(finesse)
        print(fmax)
        plt.plot([0,Cxe[idmax]],[0,CLe[idmax]])
        plt.plot(Cxe, CLe)
    label1 = patches.Patch(color='blue',label='fmax (ms = 0.2)')
    label2 = patches.Patch(color='green',label='Polaire (ms = 0.2)')
    label3 = patches.Patch(color='red',label='fmax (ms = 1)')
    label4 = patches.Patch(color='cyan',label='Polaire (ms = 1)')
    plt.legend(loc='upper left',handles=[label1,label2,label3,label4])
    ut.decorate(plt.gca(), "Evolution de la polaire équilibrée", 'Coefficient de trainée équilibrée', 'Coefficient de portance équilibrée')
    plt.show
    
    
###################################################################
# Script principal de test
###################################################################

aircraft = dyn.Param_A321()

evol_CLe(aircraft)
plt.figure()
evol_dphre(aircraft)
plt.figure()
polaire_equi(aircraft)


###################################################################