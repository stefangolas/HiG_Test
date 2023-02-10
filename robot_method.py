# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, 
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging,
 hig_connect, hig_spin)

liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'



lmgr = LayoutManager('deck.lay')


if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        
        hig_connect(ham_int, device_id = "Device_ID", adapter_device_id =  "Adapter_Device_ID", simulation_mode = True)
        hig_spin(ham_int, Gs = 1000.0, acceleration_pct = 80.0, deceleration_pct =  60.0, time= 20.0)

        