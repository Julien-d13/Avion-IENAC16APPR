###################################################################
# Fichier projet-avion-HRJ.py
# Projet avion semestre 6
# BITTERMANN Hugo, LOUISE Romain et RAPIN Julien - Date de début : 04/06/2017 - Date de fin :
###################################################################


###################################################################
# Importations
###################################################################

import numpy as np, matplotlib.pyplot as plt
import dynamic as dyn, utils as ut


###################################################################
# Fonctions
###################################################################

def plot_motor(P, filename=None):
    figure = ut.prepare_fig(None, u'Poussee {}'.format(P.name))
    U, hs, machs = [0, 1., 0, 0], np.linspace(3000,11000,5), np.linspace(0.5, 0.8, 30)
    for h in hs:
        thrusts = [dyn.propulsion_model([0, h, dyn.va_of_mach(mach, h), 0, 0, 0], U, P) for mach in machs]
        plt.plot(machs, thrusts)
    legends = ['{:.0f} m'.format(h) for h in hs]
    ut.decorate(plt.gca(), u'Poussee maximum {}'.format(P.eng_name), 'Mach', 'SNS', legends)
    if filename is not None : plt.savefig(filename, dpi=160)
    


        
    
###################################################################
# Script principal de test
###################################################################

if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True, linewidth=200)
    aircraft = dyn.Param_A321()
    plot_motor(aircraft)
    plt.show()



###################################################################