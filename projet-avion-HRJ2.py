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

# Séance 2

hs=[3000,11000]
ms=[0.2,1]
machs=[0.5,0.8]
km=[0.1,0.9]
couples=[[ms[0],km[0]],[ms[0],km[1]],[ms[1],km[0]],[ms[1],km[1]]
for h in hs:
    args = {'va':100., 'h': h}
    ac = dyn.Param_A321()
    ac.set_mass_and_static_margin(ms[0],km[0])
    Xe, Ue = dyn.trim(ac, args)
    print('h {} {} gaz {:.1f} %'.format(h, Xe,Ue[dyn.i_dth]*100))



###################################################################
# Script principal de test
###################################################################

aircraft = dyn.Param_A321()




###################################################################