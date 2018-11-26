# -*- coding: utf-8 -*-
import math
import pyidf as pf
pf.validation_level = pf.ValidationLevel.no
import logging
logging.info("start")
from pyidf.idf import IDF

import pandas as pd


def main(zone_area = 10, zone_ratio = 1.5, zone_height = 3, absorptance = .5, shading = 1, azimuth = 0,
    corr_width = 2, wall_u = 2.5, corr_vent = 1, zone_feat = None, floor_height=0, room_type=0,
	thermal_loads=20, glass_fs=.87, wwr=.33, open_fac=.5, input = "modelo_single.idf", output = 'output.idf'):
    
    print(output)

    idf=dict()

    # Making sure numbers are not srings ----------

    zone_area = float(zone_area)
    zone_ratio = float(zone_ratio)
    zone_height = float(zone_height)
    absorptance = float(absorptance)
    shading = float(shading)
    azimuth = int(azimuth)
    corr_width = float(corr_width)
    wall_u = float(wall_u)
    floor_height = float(floor_height)
    thermal_loads = float(thermal_loads)
    glass_fs = float(glass_fs)
    wwr = float(wwr)
    open_fac = float(open_fac)

    # editing subdf thermal load

    electric = thermal_loads*.1124
    people = (thermal_loads*.7076)*math.pow(120, -1)
    lights = thermal_loads*.18

    # Defining U

    R_mat = (1-.17*wall_u)*math.pow(wall_u, -1)
    c_plaster = .025*math.pow((.085227272727273 * R_mat), -1)
    c_brick = .066*math.pow((.2875 * R_mat), -1)
    R_air = (.62727273 * R_mat)

    # Defining dependent variables ----------

    zone_length = math.sqrt(zone_area *math.pow(zone_ratio,-1))
    zone_width = (zone_area *math.pow(zone_length,-1))

    x0_second_row = (zone_width) + (corr_width) 

    window_x1 = zone_width*.001
    window_x2 = zone_width*.999
    window_y1 = zone_length*.001
    window_y2 = zone_length*.999

    door_width = .9
    dist_door_wall = .5
    door_height = 2.1

    # Surfaces creation --------------------

    # Create dict
    BldgSurface = {
    'Name': [],
    'SurfaceType':[],
    'ConstructionName': [],
    'ZoneName': [],
    'OutsideBoundryCond': [],
    'OutsideBoundryCondObj': [],
    'SunExposure': [],
    'WindExposure': [],
    'V1x': [],
    'V1y': [],
    'V1z': [],
    'V2x': [],
    'V2y': [],
    'V2z': [],
    'V3x': [],
    'V3y': [],
    'V3z': [],
    'V4x': [],
    'V4y': [],
    'V4z': []
    }

    for i in range(n_zones):

        # Surface name
        BldgSurface['Name'].append('floor_zn_'+str(i))
        BldgSurface['Name'].append('ceiling_zn_'+str(i))
        BldgSurface['Name'].append('wall-0_zn_'+str(i)) # wall N
        BldgSurface['Name'].append('wall-1_zn_'+str(i)) # wall L
        BldgSurface['Name'].append('wall-2_zn_'+str(i)) # wall S
        BldgSurface['Name'].append('wall-3_zn_'+str(i)) # wall O
        
        # Surface type
        BldgSurface['SurfaceType'].append('Floor')
        if i >= n_zones-zones_x_floor:
            BldgSurface['SurfaceType'].append('Roof')
        else:
            BldgSurface['SurfaceType'].append('Ceiling')
            
        for j in range(4):
            BldgSurface['SurfaceType'].append('Wall')
        
        # Surface construction name
        if i < zones_x_floor:
            BldgSurface['ConstructionName'].append('Exterior Floor')
        else:
            BldgSurface['ConstructionName'].append('Interior Floor')

        if BldgSurface['SurfaceType'][i*6+1] == 'Roof':
            BldgSurface['ConstructionName'].append('Exterior Roof')
        else:
            BldgSurface['ConstructionName'].append('Interior Ceiling')

        if i%2 == 0:
            if i%zones_x_floor == 0:
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['ConstructionName'].append('Exterior Wall')

            elif i%zones_x_floor == zones_x_floor-2:
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Exterior Wall')

            else:
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Exterior Wall')
        else:
            if i%zones_x_floor == 1:
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')

            elif i%zones_x_floor == zones_x_floor-1:
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')

            else:
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')
                BldgSurface['ConstructionName'].append('Interior Wall')

        # zone name
        for j in range(6):
            BldgSurface['ZoneName'].append(zones_list[i])
            
    # Surface outside boundary condition
    for i in range(len(BldgSurface['ConstructionName'])):

        if BldgSurface['ConstructionName'][i] == 'Exterior Floor':
            BldgSurface['OutsideBoundryCond'].append('Ground')

        elif BldgSurface['ConstructionName'][i][0:3] == 'Ext':
            BldgSurface['OutsideBoundryCond'].append('Outdoors')

        else:
            BldgSurface['OutsideBoundryCond'].append('Surface')
                
    # sun explosed and wind exposed
    for i in range(len(BldgSurface['OutsideBoundryCond'])):
        if BldgSurface['OutsideBoundryCond'][i] == 'Outdoors':
            BldgSurface['SunExposure'].append('SunExposed')
            BldgSurface['WindExposure'].append('WindExposed')
        else:
            BldgSurface['SunExposure'].append('NoSun')
            BldgSurface['WindExposure'].append('NoWind')
            
    # Surface outside boundary condition name
    for i in range(len(BldgSurface['OutsideBoundryCond'])):
        if BldgSurface['OutsideBoundryCond'][i] == 'Surface':
            if BldgSurface['Name'][i][0:5] == 'floor':
                BldgSurface['OutsideBoundryCondObj'].append('ceiling_zn_'+str((i//6)-zones_x_floor))
            if BldgSurface['Name'][i][0:4] == 'ceil':
                BldgSurface['OutsideBoundryCondObj'].append('floor_zn_'+str((i//6)+zones_x_floor))
            if BldgSurface['Name'][i][0:6] == 'wall-0':
                BldgSurface['OutsideBoundryCondObj'].append('wall-2_zn_'+str((i//6)+2))
            if BldgSurface['Name'][i][0:6] == 'wall-2':
                BldgSurface['OutsideBoundryCondObj'].append('wall-0_zn_'+str((i//6)-2))
            if BldgSurface['Name'][i][0:6] == 'wall-1' or BldgSurface['Name'][i][0:6] == 'wall-3':
                BldgSurface['OutsideBoundryCondObj'].append('wall-corr_zn_'+str(i//6))
        else:
            BldgSurface['OutsideBoundryCondObj'].append(' ')

    # Surface geometry
    for i in range(len(BldgSurface['Name'])):
        if BldgSurface['Name'][i][0:5] == 'floor':
            BldgSurface['V1x'].append(zone_width)
            BldgSurface['V1y'].append(zone_length)
            BldgSurface['V1z'].append(0)
            BldgSurface['V2x'].append(zone_width)
            BldgSurface['V2y'].append(0)
            BldgSurface['V2z'].append(0)
            BldgSurface['V3x'].append(0)
            BldgSurface['V3y'].append(0)
            BldgSurface['V3z'].append(0)
            BldgSurface['V4x'].append(0)
            BldgSurface['V4y'].append(zone_length)
            BldgSurface['V4z'].append(0)

        if BldgSurface['Name'][i][0:4] == 'ceil':
            BldgSurface['V1x'].append(0)
            BldgSurface['V1y'].append(zone_length)
            BldgSurface['V1z'].append(zone_height)
            BldgSurface['V2x'].append(0)
            BldgSurface['V2y'].append(0)
            BldgSurface['V2z'].append(zone_height)
            BldgSurface['V3x'].append(zone_width)
            BldgSurface['V3y'].append(0)
            BldgSurface['V3z'].append(zone_height)
            BldgSurface['V4x'].append(zone_width)
            BldgSurface['V4y'].append(zone_length)
            BldgSurface['V4z'].append(zone_height)

        if BldgSurface['Name'][i][0:6] == 'wall-0':
            BldgSurface['V1x'].append(zone_width)
            BldgSurface['V1y'].append(zone_length)
            BldgSurface['V1z'].append(zone_height)
            BldgSurface['V2x'].append(zone_width)
            BldgSurface['V2y'].append(zone_length)
            BldgSurface['V2z'].append(0)
            BldgSurface['V3x'].append(0)
            BldgSurface['V3y'].append(zone_length)
            BldgSurface['V3z'].append(0)
            BldgSurface['V4x'].append(0)
            BldgSurface['V4y'].append(zone_length)
            BldgSurface['V4z'].append(zone_height)

        if BldgSurface['Name'][i][0:6] == 'wall-1':
            BldgSurface['V1x'].append(zone_width)
            BldgSurface['V1y'].append(0)
            BldgSurface['V1z'].append(zone_height)
            BldgSurface['V2x'].append(zone_width)
            BldgSurface['V2y'].append(0)
            BldgSurface['V2z'].append(0)
            BldgSurface['V3x'].append(zone_width)
            BldgSurface['V3y'].append(zone_length)
            BldgSurface['V3z'].append(0)
            BldgSurface['V4x'].append(zone_width)
            BldgSurface['V4y'].append(zone_length)
            BldgSurface['V4z'].append(zone_height)

        if BldgSurface['Name'][i][0:6] == 'wall-2':
            BldgSurface['V1x'].append(0)
            BldgSurface['V1y'].append(0)
            BldgSurface['V1z'].append(zone_height)
            BldgSurface['V2x'].append(0)
            BldgSurface['V2y'].append(0)
            BldgSurface['V2z'].append(0)
            BldgSurface['V3x'].append(zone_width)
            BldgSurface['V3y'].append(0)
            BldgSurface['V3z'].append(0)
            BldgSurface['V4x'].append(zone_width)
            BldgSurface['V4y'].append(0)
            BldgSurface['V4z'].append(zone_height)

        if BldgSurface['Name'][i][0:6] == 'wall-3':
            BldgSurface['V1x'].append(0)
            BldgSurface['V1y'].append(zone_length)
            BldgSurface['V1z'].append(zone_height)
            BldgSurface['V2x'].append(0)
            BldgSurface['V2y'].append(zone_length)
            BldgSurface['V2z'].append(0)
            BldgSurface['V3x'].append(0)
            BldgSurface['V3y'].append(0)
            BldgSurface['V3z'].append(0)
            BldgSurface['V4x'].append(0)
            BldgSurface['V4y'].append(0)
            BldgSurface['V4z'].append(zone_height)

    # corridor surfaces
    for i in range(len(corridors)):
        
        for j in range(4+zones_x_floor):
            BldgSurface['ZoneName'].append(corridors[i])
            
        BldgSurface['Name'].append('floor_corr_'+str(i))
        BldgSurface['Name'].append('ceil_corr_'+str(i))
        BldgSurface['Name'].append('wall-0_corr_'+str(i))
        BldgSurface['Name'].append('wall-2_corr_'+str(i))
        
        BldgSurface['SurfaceType'].append('Floor')
        BldgSurface['SunExposure'].append('NoSun')
        BldgSurface['WindExposure'].append('NoWind')

        if i == 0:
            BldgSurface['ConstructionName'].append('Exterior Floor')
            BldgSurface['OutsideBoundryCond'].append('Ground')
            BldgSurface['OutsideBoundryCondObj'].append(' ')
        else:
            BldgSurface['ConstructionName'].append('Interior Floor')
            BldgSurface['OutsideBoundryCond'].append('Surface')
            BldgSurface['OutsideBoundryCondObj'].append('ceil_corr_'+str(i-1))
            
        if i == n_floors-1:
            BldgSurface['SurfaceType'].append('Roof')
            BldgSurface['ConstructionName'].append('Exterior Roof')        
            BldgSurface['OutsideBoundryCond'].append('Outdoors')
            BldgSurface['SunExposure'].append('SunExposed')
            BldgSurface['WindExposure'].append('WindExposed')
            BldgSurface['OutsideBoundryCondObj'].append(' ')
        else:
            BldgSurface['SurfaceType'].append('Ceiling')
            BldgSurface['ConstructionName'].append('Interior Ceiling')
            BldgSurface['OutsideBoundryCond'].append('Surface')
            BldgSurface['SunExposure'].append('NoSun')
            BldgSurface['WindExposure'].append('NoWind')
            BldgSurface['OutsideBoundryCondObj'].append('floor_corr_'+str(i+1))

        for j in range(2):

            if corr_vent > 0:
                BldgSurface['SurfaceType'].append('Wall')        
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['OutsideBoundryCond'].append('Outdoors')
                BldgSurface['SunExposure'].append('SunExposed')
                BldgSurface['WindExposure'].append('WindExposed')
                BldgSurface['OutsideBoundryCondObj'].append(' ')
            else:
                BldgSurface['SurfaceType'].append('Wall')        
                BldgSurface['ConstructionName'].append('Exterior Wall')
                BldgSurface['OutsideBoundryCond'].append('Adiabatic')
                BldgSurface['SunExposure'].append('NoSun')
                BldgSurface['WindExposure'].append('NoWind')
                BldgSurface['OutsideBoundryCondObj'].append(' ')
            
        for j in range(zones_x_floor):
            BldgSurface['SurfaceType'].append('Wall')        
            BldgSurface['ConstructionName'].append('Interior Wall')
            BldgSurface['OutsideBoundryCond'].append('Surface')
            BldgSurface['SunExposure'].append('NoSun')
            BldgSurface['WindExposure'].append('NoWind')
            if j%2 == 0:
                BldgSurface['OutsideBoundryCondObj'].append('wall-1_zn_'+str(i*zones_x_floor+j))
            else:
                BldgSurface['OutsideBoundryCondObj'].append('wall-3_zn_'+str(i*zones_x_floor+j))

        BldgSurface['V1x'].append(corr_width)
        BldgSurface['V1y'].append(zone_length*zones_in_sequence)
        BldgSurface['V1z'].append(0)
        BldgSurface['V2x'].append(corr_width)
        BldgSurface['V2y'].append(0)
        BldgSurface['V2z'].append(0)
        BldgSurface['V3x'].append(0)
        BldgSurface['V3y'].append(0)
        BldgSurface['V3z'].append(0)
        BldgSurface['V4x'].append(0)
        BldgSurface['V4y'].append(zone_length*zones_in_sequence)
        BldgSurface['V4z'].append(0)
        
        BldgSurface['V1x'].append(0)
        BldgSurface['V1y'].append(zone_length*zones_in_sequence)
        BldgSurface['V1z'].append(zone_height)
        BldgSurface['V2x'].append(0)
        BldgSurface['V2y'].append(0)
        BldgSurface['V2z'].append(zone_height)
        BldgSurface['V3x'].append(corr_width)
        BldgSurface['V3y'].append(0)
        BldgSurface['V3z'].append(zone_height)
        BldgSurface['V4x'].append(corr_width)
        BldgSurface['V4y'].append(zone_length*zones_in_sequence)
        BldgSurface['V4z'].append(zone_height)
        
        BldgSurface['V1x'].append(corr_width)
        BldgSurface['V1y'].append(zone_length*zones_in_sequence)
        BldgSurface['V1z'].append(zone_height)
        BldgSurface['V2x'].append(corr_width)
        BldgSurface['V2y'].append(zone_length*zones_in_sequence)
        BldgSurface['V2z'].append(0)
        BldgSurface['V3x'].append(0)
        BldgSurface['V3y'].append(zone_length*zones_in_sequence)
        BldgSurface['V3z'].append(0)
        BldgSurface['V4x'].append(0)
        BldgSurface['V4y'].append(zone_length*zones_in_sequence)
        BldgSurface['V4z'].append(zone_height)
        
        BldgSurface['V1x'].append(0)
        BldgSurface['V1y'].append(0)
        BldgSurface['V1z'].append(zone_height)
        BldgSurface['V2x'].append(0)
        BldgSurface['V2y'].append(0)
        BldgSurface['V2z'].append(0)
        BldgSurface['V3x'].append(corr_width)
        BldgSurface['V3y'].append(0)
        BldgSurface['V3z'].append(0)
        BldgSurface['V4x'].append(corr_width)
        BldgSurface['V4y'].append(0)
        BldgSurface['V4z'].append(zone_height)
        
        for j in range(zones_in_sequence):
            
            BldgSurface['Name'].append('wall-corr_zn_'+str(i*zones_x_floor+j*2))
            BldgSurface['V1x'].append(0)
            BldgSurface['V1y'].append(zone_length*(j+1))
            BldgSurface['V1z'].append(zone_height)
            BldgSurface['V2x'].append(0)
            BldgSurface['V2y'].append(zone_length*(j+1))
            BldgSurface['V2z'].append(0)
            BldgSurface['V3x'].append(0)
            BldgSurface['V3y'].append(zone_length*(j))
            BldgSurface['V3z'].append(0)
            BldgSurface['V4x'].append(0)
            BldgSurface['V4y'].append(zone_length*(j))
            BldgSurface['V4z'].append(zone_height)
            
            BldgSurface['Name'].append('wall-corr_zn_'+str(i*zones_x_floor+j*2+1))
            BldgSurface['V1x'].append(corr_width)
            BldgSurface['V1y'].append(zone_length*(j))
            BldgSurface['V1z'].append(zone_height)
            BldgSurface['V2x'].append(corr_width)
            BldgSurface['V2y'].append(zone_length*(j))
            BldgSurface['V2z'].append(0)
            BldgSurface['V3x'].append(corr_width)
            BldgSurface['V3y'].append(zone_length*(j+1))
            BldgSurface['V3z'].append(0)
            BldgSurface['V4x'].append(corr_width)
            BldgSurface['V4y'].append(zone_length*(j+1))
            BldgSurface['V4z'].append(zone_height)
            
    # FenestrationSurdace:Detailed --------------------
    
    # Create dictionary 
    FenSurface = {
    'Name': [],
    'SurfaceType': [],
    'ConstructionName': [],
    'BuildingSurfaceName': [],
    'OutsideBoundryCondObj': [],
    'V1x': [],
    'V1y': [],
    'V1z': [],
    'V2x': [],
    'V2y': [],
    'V2z': [],
    'V3x': [],
    'V3y': [],
    'V3z': [],
    'V4x': [],
    'V4y': [],
    'V4z': []
    }

    doors_list = []
    windows_list = []
        
    for i in range(n_zones):

        wwr = float(zone_feat['wwr'][i])
        window_z1 = zone_height*(1-wwr)*.5
        window_z2 = window_z1+(zone_height*wwr)
        
        if i%zones_x_floor == zones_x_floor-2: # upper left corner

            opening_i = 'window-0_zn_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)

            opening_i = 'window-3_zn_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)
            
            opening_i = 'door_zn_'+str(i)    
            doors_list.append(opening_i)
            FenSurface['Name'].append(opening_i)
                
            FenSurface['SurfaceType'].append('Window')
            FenSurface['SurfaceType'].append('Window')
            FenSurface['SurfaceType'].append('Door')
            
            FenSurface['ConstructionName'].append('glass_construction_zone_'+str(i))
            FenSurface['ConstructionName'].append('glass_construction_zone_'+str(i))
            FenSurface['ConstructionName'].append('Interior Door')
            
            FenSurface['OutsideBoundryCondObj'].append(' ')
            FenSurface['OutsideBoundryCondObj'].append(' ')
            FenSurface['OutsideBoundryCondObj'].append('door-corr_zn_'+str(i))
                
            FenSurface['BuildingSurfaceName'].append('wall-0_zn_'+str(i))
            FenSurface['BuildingSurfaceName'].append('wall-3_zn_'+str(i))
            FenSurface['BuildingSurfaceName'].append('wall-1_zn_'+str(i))
     
            # window
            FenSurface['V1x'].append(window_x2)
            FenSurface['V1y'].append(zone_length)
            FenSurface['V1z'].append(window_z2)
            FenSurface['V2x'].append(window_x2)
            FenSurface['V2y'].append(zone_length)
            FenSurface['V2z'].append(window_z1)
            FenSurface['V3x'].append(window_x1)
            FenSurface['V3y'].append(zone_length)
            FenSurface['V3z'].append(window_z1)
            FenSurface['V4x'].append(window_x1)
            FenSurface['V4y'].append(zone_length)
            FenSurface['V4z'].append(window_z2)

            FenSurface['V1x'].append(0)
            FenSurface['V1y'].append(window_y2)
            FenSurface['V1z'].append(window_z2)
            FenSurface['V2x'].append(0)
            FenSurface['V2y'].append(window_y2)
            FenSurface['V2z'].append(window_z1)
            FenSurface['V3x'].append(0)
            FenSurface['V3y'].append(window_y1)
            FenSurface['V3z'].append(window_z1)
            FenSurface['V4x'].append(0)
            FenSurface['V4y'].append(window_y1)
            FenSurface['V4z'].append(window_z2)
            
            # door
            FenSurface['V1x'].append(zone_width)
            FenSurface['V1y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(zone_width)
            FenSurface['V2y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V2z'].append(0)
            FenSurface['V3x'].append(zone_width)
            FenSurface['V3y'].append(zone_length-dist_door_wall)
            FenSurface['V3z'].append(0)
            FenSurface['V4x'].append(zone_width)
            FenSurface['V4y'].append(zone_length-dist_door_wall)
            FenSurface['V4z'].append(door_height)

        elif i%zones_x_floor == 1: # lower right corner

            opening_i = 'window-1_zn_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)

            opening_i = 'window-2_zn_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)
            
            opening_i = 'door_zn_'+str(i)    
            doors_list.append(opening_i)
            FenSurface['Name'].append(opening_i)
                
            FenSurface['SurfaceType'].append('Window')
            FenSurface['SurfaceType'].append('Window')
            FenSurface['SurfaceType'].append('Door')
            
            FenSurface['ConstructionName'].append('glass_construction_zone_'+str(i))
            FenSurface['ConstructionName'].append('glass_construction_zone_'+str(i))
            FenSurface['ConstructionName'].append('Interior Door')
            
            FenSurface['OutsideBoundryCondObj'].append(' ')
            FenSurface['OutsideBoundryCondObj'].append(' ')
            FenSurface['OutsideBoundryCondObj'].append('door-corr_zn_'+str(i))

                
            FenSurface['BuildingSurfaceName'].append('wall-1_zn_'+str(i))
            FenSurface['BuildingSurfaceName'].append('wall-2_zn_'+str(i))
            FenSurface['BuildingSurfaceName'].append('wall-3_zn_'+str(i))
     
            # window
            FenSurface['V1x'].append(zone_width)
            FenSurface['V1y'].append(window_y1)
            FenSurface['V1z'].append(window_z2)
            FenSurface['V2x'].append(zone_width)
            FenSurface['V2y'].append(window_y1)
            FenSurface['V2z'].append(window_z1)
            FenSurface['V3x'].append(zone_width)
            FenSurface['V3y'].append(window_y2)
            FenSurface['V3z'].append(window_z1)
            FenSurface['V4x'].append(zone_width)
            FenSurface['V4y'].append(window_y2)
            FenSurface['V4z'].append(window_z2)

            FenSurface['V1x'].append(window_x1)
            FenSurface['V1y'].append(0)
            FenSurface['V1z'].append(window_z2)
            FenSurface['V2x'].append(window_x1)
            FenSurface['V2y'].append(0)
            FenSurface['V2z'].append(window_z1)
            FenSurface['V3x'].append(window_x2)
            FenSurface['V3y'].append(0)
            FenSurface['V3z'].append(window_z1)
            FenSurface['V4x'].append(window_x2)
            FenSurface['V4y'].append(0)
            FenSurface['V4z'].append(window_z2)
            
            # door
            FenSurface['V1x'].append(0)
            FenSurface['V1y'].append(zone_length-dist_door_wall)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(0)
            FenSurface['V2y'].append(zone_length-dist_door_wall)
            FenSurface['V2z'].append(0)
            FenSurface['V3x'].append(0)
            FenSurface['V3y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V3z'].append(0)
            FenSurface['V4x'].append(0)
            FenSurface['V4y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V4z'].append(door_height)

        elif i%zones_x_floor == zones_x_floor-1: # upper right corner

            opening_i = 'window-0_zn_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)
            
            opening_i = 'door_zn_'+str(i)    
            doors_list.append(opening_i)
            FenSurface['Name'].append(opening_i)
                
            FenSurface['SurfaceType'].append('Window')
            FenSurface['SurfaceType'].append('Door')
            
            FenSurface['ConstructionName'].append('glass_construction_zone_'+str(i))
            FenSurface['ConstructionName'].append('Interior Door')
            
            FenSurface['OutsideBoundryCondObj'].append(' ')
            FenSurface['OutsideBoundryCondObj'].append('door-corr_zn_'+str(i))

                
            FenSurface['BuildingSurfaceName'].append('wall-0_zn_'+str(i))
            FenSurface['BuildingSurfaceName'].append('wall-3_zn_'+str(i))
     
            # window

            FenSurface['V1x'].append(window_x2)
            FenSurface['V1y'].append(zone_length)
            FenSurface['V1z'].append(window_z2)
            FenSurface['V2x'].append(window_x2)
            FenSurface['V2y'].append(zone_length)
            FenSurface['V2z'].append(window_z1)
            FenSurface['V3x'].append(window_x1)
            FenSurface['V3y'].append(zone_length)
            FenSurface['V3z'].append(window_z1)
            FenSurface['V4x'].append(window_x1)
            FenSurface['V4y'].append(zone_length)
            FenSurface['V4z'].append(window_z2)
            
            # door
            FenSurface['V1x'].append(0)
            FenSurface['V1y'].append(zone_length-dist_door_wall)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(0)
            FenSurface['V2y'].append(zone_length-dist_door_wall)
            FenSurface['V2z'].append(0)
            FenSurface['V3x'].append(0)
            FenSurface['V3y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V3z'].append(0)
            FenSurface['V4x'].append(0)
            FenSurface['V4y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V4z'].append(door_height)
        
        elif i%2 == 0: # lower left corner and left middle

            opening_i = 'window-3_zn_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)
            
            opening_i = 'door_zn_'+str(i)    
            doors_list.append(opening_i)
            FenSurface['Name'].append(opening_i)
                
            FenSurface['SurfaceType'].append('Window')
            FenSurface['SurfaceType'].append('Door')
            
            FenSurface['ConstructionName'].append('glass_construction_zone_'+str(i))
            FenSurface['ConstructionName'].append('Interior Door')
            
            FenSurface['OutsideBoundryCondObj'].append(' ')
            FenSurface['OutsideBoundryCondObj'].append('door-corr_zn_'+str(i))
                
            FenSurface['BuildingSurfaceName'].append('wall-3_zn_'+str(i))
            FenSurface['BuildingSurfaceName'].append('wall-1_zn_'+str(i))
     
            # window
            FenSurface['V1x'].append(0)
            FenSurface['V1y'].append(window_y2)
            FenSurface['V1z'].append(window_z2)
            FenSurface['V2x'].append(0)
            FenSurface['V2y'].append(window_y2)
            FenSurface['V2z'].append(window_z1)
            FenSurface['V3x'].append(0)
            FenSurface['V3y'].append(window_y1)
            FenSurface['V3z'].append(window_z1)
            FenSurface['V4x'].append(0)
            FenSurface['V4y'].append(window_y1)
            FenSurface['V4z'].append(window_z2)
            
            # door
            FenSurface['V1x'].append(zone_width)
            FenSurface['V1y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(zone_width)
            FenSurface['V2y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V2z'].append(0)
            FenSurface['V3x'].append(zone_width)
            FenSurface['V3y'].append(zone_length-dist_door_wall)
            FenSurface['V3z'].append(0)
            FenSurface['V4x'].append(zone_width)
            FenSurface['V4y'].append(zone_length-dist_door_wall)
            FenSurface['V4z'].append(door_height)
            
        else: # right middle

            opening_i = 'window-1_zn_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)
            
            opening_i = 'door_zn_'+str(i)    
            doors_list.append(opening_i)
            FenSurface['Name'].append(opening_i)
                
            FenSurface['SurfaceType'].append('Window')
            FenSurface['SurfaceType'].append('Door')
            
            FenSurface['ConstructionName'].append('glass_construction_zone_'+str(i))
            FenSurface['ConstructionName'].append('Interior Door')
            
            FenSurface['OutsideBoundryCondObj'].append(' ')
            FenSurface['OutsideBoundryCondObj'].append('door-corr_zn_'+str(i))

                
            FenSurface['BuildingSurfaceName'].append('wall-1_zn_'+str(i))
            FenSurface['BuildingSurfaceName'].append('wall-3_zn_'+str(i))
     
            #Janela
            FenSurface['V1x'].append(zone_width)
            FenSurface['V1y'].append(window_y1)
            FenSurface['V1z'].append(window_z2)
            FenSurface['V2x'].append(zone_width)
            FenSurface['V2y'].append(window_y1)
            FenSurface['V2z'].append(window_z1)
            FenSurface['V3x'].append(zone_width)
            FenSurface['V3y'].append(window_y2)
            FenSurface['V3z'].append(window_z1)
            FenSurface['V4x'].append(zone_width)
            FenSurface['V4y'].append(window_y2)
            FenSurface['V4z'].append(window_z2) 
            
            #Porta
            FenSurface['V1x'].append(0)
            FenSurface['V1y'].append(zone_length-dist_door_wall)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(0)
            FenSurface['V2y'].append(zone_length-dist_door_wall)
            FenSurface['V2z'].append(0)
            FenSurface['V3x'].append(0)
            FenSurface['V3y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V3z'].append(0)
            FenSurface['V4x'].append(0)
            FenSurface['V4y'].append(zone_length-dist_door_wall-door_width)
            FenSurface['V4z'].append(door_height)

    # corridor doors
    for i in range(len(corridors)):
        
        for j in range(zones_in_sequence):
            
            FenSurface['Name'].append('door-corr_zn_'+str(i*zones_x_floor+j*2))
            FenSurface['Name'].append('door-corr_zn_'+str(i*zones_x_floor+j*2+1))
            
            FenSurface['SurfaceType'].append('Door')
            FenSurface['SurfaceType'].append('Door')
                    
            FenSurface['ConstructionName'].append('Interior Door')
            FenSurface['ConstructionName'].append('Interior Door')
            
            FenSurface['BuildingSurfaceName'].append('wall-corr_zn_'+str(i*zones_x_floor+j*2))
            FenSurface['BuildingSurfaceName'].append('wall-corr_zn_'+str(i*zones_x_floor+j*2+1))
            
            FenSurface['OutsideBoundryCondObj'].append('door_zn_'+str(i*zones_x_floor+j*2))
            FenSurface['OutsideBoundryCondObj'].append('door_zn_'+str(i*zones_x_floor+j*2+1))
            
            # door wall-3
            FenSurface['V1x'].append(0)
            FenSurface['V1y'].append(zone_length*(j+1)-dist_door_wall)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(0)
            FenSurface['V2y'].append(zone_length*(j+1)-dist_door_wall)
            FenSurface['V2z'].append(0)
            FenSurface['V3x'].append(0)
            FenSurface['V3y'].append(zone_length*(j+1)-dist_door_wall-door_width)
            FenSurface['V3z'].append(0)
            FenSurface['V4x'].append(0)
            FenSurface['V4y'].append(zone_length*(j+1)-dist_door_wall-door_width)
            FenSurface['V4z'].append(door_height)
            # door wall-1
            FenSurface['V1x'].append(corr_width)
            FenSurface['V1y'].append(zone_length*(j+1)-dist_door_wall-door_width)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(corr_width)
            FenSurface['V2y'].append(zone_length*(j+1)-dist_door_wall-door_width)
            FenSurface['V2z'].append(0)
            FenSurface['V3x'].append(corr_width)
            FenSurface['V3y'].append(zone_length*(j+1)-dist_door_wall)
            FenSurface['V3z'].append(0)
            FenSurface['V4x'].append(corr_width)
            FenSurface['V4y'].append(zone_length*(j+1)-dist_door_wall)
            FenSurface['V4z'].append(door_height)

        # corridor ventilation 

        if corr_vent > 0:

            opening_i = 'window-0_corr_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)
            
            opening_i = 'window-2_corr_'+str(i)
            FenSurface['Name'].append(opening_i)
            windows_list.append(opening_i)
                
            FenSurface['SurfaceType'].append('Window')
            FenSurface['SurfaceType'].append('Window')
            
            FenSurface['ConstructionName'].append('Exterior Window')
            FenSurface['ConstructionName'].append('Exterior Window')
            
            FenSurface['OutsideBoundryCondObj'].append(' ')
            FenSurface['OutsideBoundryCondObj'].append(' ')
                
            FenSurface['BuildingSurfaceName'].append('wall-0_corr_'+str(i))
            FenSurface['BuildingSurfaceName'].append('wall-2_corr_'+str(i))
     
            #'window-0
            FenSurface['V1x'].append(corr_width*.75)
            FenSurface['V1y'].append(zone_length*zones_in_sequence)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(corr_width*.75)
            FenSurface['V2y'].append(zone_length*zones_in_sequence)
            FenSurface['V2z'].append(door_height-1)
            FenSurface['V3x'].append(corr_width*.25)
            FenSurface['V3y'].append(zone_length*zones_in_sequence)
            FenSurface['V3z'].append(door_height-1)
            FenSurface['V4x'].append(corr_width*.25)
            FenSurface['V4y'].append(zone_length*zones_in_sequence)
            FenSurface['V4z'].append(door_height) 
            
            #'window-2
            FenSurface['V1x'].append(corr_width*.25)
            FenSurface['V1y'].append(0)
            FenSurface['V1z'].append(door_height)
            FenSurface['V2x'].append(corr_width*.25)
            FenSurface['V2y'].append(0)
            FenSurface['V2z'].append(door_height-1)
            FenSurface['V3x'].append(corr_width*.75)
            FenSurface['V3y'].append(0)
            FenSurface['V3z'].append(door_height-1)
            FenSurface['V4x'].append(corr_width*.75)
            FenSurface['V4y'].append(0)
            FenSurface['V4z'].append(door_height) 

        # Stairs

        if stairs > 0:

            if i > 0: # not ground floor

                FenSurface['Name'].append('stair-inf_'+str(i))
                FenSurface['SurfaceType'].append('Door')
                FenSurface['ConstructionName'].append('InfraRed')
                FenSurface['BuildingSurfaceName'].append('floor_corr_'+str(i))
                FenSurface['OutsideBoundryCondObj'].append('stair-sup_'+str(i-1))
                # stair has width = 0.98*corr_width [m] and length = 4.5 [m]
                FenSurface['V1x'].append(0.99*corr_width)
                FenSurface['V1y'].append(0.01)
                FenSurface['V1z'].append(0)
                FenSurface['V2x'].append(0.01*corr_width)
                FenSurface['V2y'].append(0.01)
                FenSurface['V2z'].append(0)
                FenSurface['V3x'].append(0.01*corr_width)
                FenSurface['V3y'].append(4.51)
                FenSurface['V3z'].append(0)
                FenSurface['V4x'].append(0.99*corr_width)
                FenSurface['V4y'].append(4.51)
                FenSurface['V4z'].append(0)

            if i < len(corridors)-1: # not roof floor
                FenSurface['Name'].append('stair-sup_'+str(i))
                FenSurface['SurfaceType'].append('Door')
                FenSurface['ConstructionName'].append('InfraRed')                    
                FenSurface['BuildingSurfaceName'].append('ceil_corr_'+str(i))
                FenSurface['OutsideBoundryCondObj'].append('stair-inf_'+str(i+1))
                # stair has width = 0.98*corr_width [m] and length = 4.5 [m]
                FenSurface['V1x'].append(0.01*corr_width)
                FenSurface['V1y'].append(0.01)
                FenSurface['V1z'].append(zone_height)
                FenSurface['V2x'].append(0.99*corr_width)
                FenSurface['V2y'].append(0.01)
                FenSurface['V2z'].append(zone_height)
                FenSurface['V3x'].append(0.99*corr_width)
                FenSurface['V3y'].append(4.51)
                FenSurface['V3z'].append(zone_height)
                FenSurface['V4x'].append(0.01*corr_width)
                FenSurface['V4y'].append(4.51)
                FenSurface['V4z'].append(zone_height)

    # Shading ----------------------------------------------------
 
    if shading > 0:
 
        # Shading:Building:Detailed
 
        ShadingBuildingDetailed = {
        'Name': [],
        'Transmittance Schedule Name': [],
        'Number of Vertices': [],
        'V1x': [],
        'V1y': [],
        'V1z': [],
        'V2x': [],
        'V2y': [],
        'V2z': [],
        'V3x': [],
        'V3y': [],
        'V3z': [],
        'V4x': [],
        'V4y': [],
        'V4z': []
        }
 
        for i in range(len(corridors)):

             # Shading Face 0            
            ShadingBuildingDetailed['Name'].append('shading-0_'+str(i))
            ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
            ShadingBuildingDetailed['Number of Vertices'].append(4)
            ShadingBuildingDetailed['V1x'].append(0) 
            ShadingBuildingDetailed['V1y'].append(zone_length*zones_in_sequence+shading)
            ShadingBuildingDetailed['V1z'].append((i+1)*zone_height)                            
            ShadingBuildingDetailed['V2x'].append(0)
            ShadingBuildingDetailed['V2y'].append(zone_length*zones_in_sequence)        
            ShadingBuildingDetailed['V2z'].append((i+1)*zone_height)
            ShadingBuildingDetailed['V3x'].append(2*zone_width+corr_width)                    
            ShadingBuildingDetailed['V3y'].append(zone_length*zones_in_sequence)
            ShadingBuildingDetailed['V3z'].append((i+1)*zone_height)
            ShadingBuildingDetailed['V4x'].append(2*zone_width+corr_width)
            ShadingBuildingDetailed['V4y'].append(zone_length*zones_in_sequence+shading)
            ShadingBuildingDetailed['V4z'].append((i+1)*zone_height)
     
            # Shading Face 1            
            ShadingBuildingDetailed['Name'].append('shading-1_'+str(i))
            ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
            ShadingBuildingDetailed['Number of Vertices'].append(4)
            ShadingBuildingDetailed['V1x'].append(2*zone_width+corr_width+shading) 
            ShadingBuildingDetailed['V1y'].append(zone_length*zones_in_sequence)
            ShadingBuildingDetailed['V1z'].append((i+1)*zone_height)                            
            ShadingBuildingDetailed['V2x'].append(2*zone_width+corr_width)
            ShadingBuildingDetailed['V2y'].append(zone_length*zones_in_sequence)        
            ShadingBuildingDetailed['V2z'].append((i+1)*zone_height)
            ShadingBuildingDetailed['V3x'].append(2*zone_width+corr_width)                    
            ShadingBuildingDetailed['V3y'].append(0)
            ShadingBuildingDetailed['V3z'].append((i+1)*zone_height)
            ShadingBuildingDetailed['V4x'].append(2*zone_width+corr_width+shading)
            ShadingBuildingDetailed['V4y'].append(0)
            ShadingBuildingDetailed['V4z'].append((i+1)*zone_height)
     
            # Shading Face 2
            
            ShadingBuildingDetailed['Name'].append('shading-2_'+str(i))
            ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
            ShadingBuildingDetailed['Number of Vertices'].append(4)
            ShadingBuildingDetailed['V1x'].append(2*zone_width+corr_width) 
            ShadingBuildingDetailed['V1y'].append(-shading)
            ShadingBuildingDetailed['V1z'].append((i+1)*zone_height)                            
            ShadingBuildingDetailed['V2x'].append(2*zone_width+corr_width)
            ShadingBuildingDetailed['V2y'].append(0)        
            ShadingBuildingDetailed['V2z'].append((i+1)*zone_height)
            ShadingBuildingDetailed['V3x'].append(0)                    
            ShadingBuildingDetailed['V3y'].append(0)
            ShadingBuildingDetailed['V3z'].append((i+1)*zone_height)
            ShadingBuildingDetailed['V4x'].append(0)
            ShadingBuildingDetailed['V4y'].append(-shading)
            ShadingBuildingDetailed['V4z'].append((i+1)*zone_height)
     
            # Shading Face 3
            
            ShadingBuildingDetailed['Name'].append('shading-3_'+str(i))
            ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
            ShadingBuildingDetailed['Number of Vertices'].append(4)
            ShadingBuildingDetailed['V1x'].append(-shading) 
            ShadingBuildingDetailed['V1y'].append(0)
            ShadingBuildingDetailed['V1z'].append((i+1)*zone_height)                            
            ShadingBuildingDetailed['V2x'].append(0)
            ShadingBuildingDetailed['V2y'].append(0)        
            ShadingBuildingDetailed['V2z'].append((i+1)*zone_height)
            ShadingBuildingDetailed['V3x'].append(0)                    
            ShadingBuildingDetailed['V3y'].append(zone_length*zones_in_sequence)
            ShadingBuildingDetailed['V3z'].append((i+1)*zone_height)
            ShadingBuildingDetailed['V4x'].append(-shading)
            ShadingBuildingDetailed['V4y'].append(zone_length*zones_in_sequence)
            ShadingBuildingDetailed['V4z'].append((i+1)*zone_height)
        
    # Dictionaries to IDF --------------------

    for i in range(len(BldgSurface['Name'])):
        obj = IDF._create_datadict("BuildingSurface:Detailed")
        obj['Name'] = BldgSurface['Name'][i]
        obj['Surface Type'] = BldgSurface['SurfaceType'][i]
        obj['Construction Name'] = BldgSurface['ConstructionName'][i]
        obj['Zone Name'] = BldgSurface['ZoneName'][i]
        obj['Outside Boundary Condition'] = BldgSurface['OutsideBoundryCond'][i]
        obj['Outside Boundary Condition Object'] = BldgSurface['OutsideBoundryCondObj'][i]
        obj['Sun Exposure'] = BldgSurface['SunExposure'][i]
        obj['Wind Exposure'] = BldgSurface['WindExposure'][i]
        obj['Number of Vertices'] = 4
        obj[u'Vertex 1 X-coordinate', 0] = BldgSurface['V1x'][i]
        obj[u'Vertex 1 Y-coordinate', 0] = BldgSurface['V1y'][i]
        obj[u'Vertex 1 Z-coordinate', 0] = BldgSurface['V1z'][i]
        obj[u'Vertex 1 X-coordinate', 1] = BldgSurface['V2x'][i]
        obj[u'Vertex 1 Y-coordinate', 1] = BldgSurface['V2y'][i]
        obj[u'Vertex 1 Z-coordinate', 1] = BldgSurface['V2z'][i]
        obj[u'Vertex 1 X-coordinate', 2] = BldgSurface['V3x'][i]
        obj[u'Vertex 1 Y-coordinate', 2] = BldgSurface['V3y'][i]
        obj[u'Vertex 1 Z-coordinate', 2] = BldgSurface['V3z'][i]
        obj[u'Vertex 1 X-coordinate', 3] = BldgSurface['V4x'][i]
        obj[u'Vertex 1 Y-coordinate', 3] = BldgSurface['V4y'][i]
        obj[u'Vertex 1 Z-coordinate', 3] = BldgSurface['V4z'][i]  
        idf.add(obj)

    for i in range(len(FenSurface['Name'])):
        obj = IDF._create_datadict("FenestrationSurface:Detailed")
        obj["Name"] = FenSurface['Name'][i]
        obj["Surface Type"] = FenSurface['SurfaceType'][i]
        obj["Construction Name"] = FenSurface["ConstructionName"][i]
        obj["Building Surface Name"] = FenSurface['BuildingSurfaceName'][i]
        obj["Outside Boundary Condition Object"] = FenSurface['OutsideBoundryCondObj'][i]
        obj['Number of Vertices'] = 4
        obj['Vertex 1 X-coordinate'] = FenSurface['V1x'][i]
        obj['Vertex 1 Y-coordinate'] = FenSurface['V1y'][i]
        obj['Vertex 1 Z-coordinate'] = FenSurface['V1z'][i]
        obj['Vertex 2 X-coordinate'] = FenSurface['V2x'][i]
        obj['Vertex 2 Y-coordinate'] = FenSurface['V2y'][i]
        obj['Vertex 2 Z-coordinate'] = FenSurface['V2z'][i]
        obj['Vertex 3 X-coordinate'] = FenSurface['V3x'][i]
        obj['Vertex 3 Y-coordinate'] = FenSurface['V3y'][i]
        obj['Vertex 3 Z-coordinate'] = FenSurface['V3z'][i]
        obj['Vertex 4 X-coordinate'] = FenSurface['V4x'][i]
        obj['Vertex 4 Y-coordinate'] = FenSurface['V4y'][i]
        obj['Vertex 4 Z-coordinate'] = FenSurface['V4z'][i] 
        idf.add(obj)

    for i in range(len(zones_list)):
        obj = IDF._create_datadict('Zone')
        obj['Name'] = zones_list[i]
        obj['Direction of Relative North'] = 0
        obj['Multiplier'] = 1
        obj['X Origin'] = zones_x[i]
        obj['Y Origin'] = zones_y[i]
        obj['Z Origin'] = zones_z[i] 
        idf.add(obj)

    for i in range(len(offices)):
        obj = IDF._create_datadict('ElectricEquipment')
        obj[0] = 'equip_'+zones_list[i]
        obj[1] = zones_list[i]
        obj[2] = 'Sch_Equip_Computador'
        obj[3] = 'Watts/Area'
        obj[4] = ''
        obj[5] = electric[i]
        obj[6] = ''
        obj[7] = 0
        obj[8] = .5
        obj[9] = 0
        obj[10] = 'General'
        idf.add(obj)

        obj = IDF._create_datadict('People')
        obj[0] = 'people_'+zones_list[i]
        obj[1] = zones_list[i]
        obj[2] = 'Sch_Ocupacao'
        obj[3] = 'People/Area'
        obj[4] = ''
        obj[5] = people[i]
        obj[6] = ''
        obj[7] = .3
        obj[8] = 'autocalculate'
        obj[9] = 'Sch_Atividade'
        #obj[10] = 'General'
        idf.add(obj)

        obj = IDF._create_datadict('Lights')
        obj[0] = 'lights_'+zones_list[i]
        obj[1] = zones_list[i]
        obj[2] = 'Sch_Iluminacao'
        obj[3] = 'Watts/Area'
        obj[4] = ''
        obj[5] = lights[i]
        obj[6] = ''
        obj[7] = 0
        obj[8] = .72
        obj[9] = .18
        obj[10] = 1
        idf.add(obj)

        glass_material = 'glass_material_'+zones_list[i]
        obj = IDF._create_datadict('WindowMaterial:SimpleGlazingSystem')
        obj[0] = glass_material
        obj[1] = 5.7
        obj[2] = zone_feat['glass'][i]
        idf.add(obj)

        obj = IDF._create_datadict('Construction')
        obj[0] = 'glass_construction_'+zones_list[i]
        obj[1] = glass_material
        idf.add(obj)

    obj = IDF._create_datadict('ZoneList')
    obj['Name'] = 'Offices'
    for i in range(len(offices)):
        obj[i+1] = offices[i]
    idf.add(obj)

    obj = IDF._create_datadict('Zonelist')
    obj['Name'] = 'All'
    for i in range(len(zones_list)):
        obj[i+1] = zones_list[i]
    idf.add(obj)

    obj = IDF._create_datadict('Zonelist')
    obj['Name'] = 'Corridors'
    for i in range(len(corridors)):
        obj[i+1] = corridors[i]
    idf.add(obj)

    for i in range(len(zones_list)):
        obj = IDF._create_datadict('AirflowNetwork:MultiZone:Zone')
        obj['Zone Name'] = zones_list[i]
        obj[5] = 100
        obj[7] = 300000
        idf.add(obj)

    open_fac_i = 0
    for i in range(len(windows_list)):
        obj = IDF._create_datadict('AirflowNetwork:MultiZone:Surface')
        obj[0] = windows_list[i]
        obj[1] = 'Janela'

        if windows_list[i][9:13]  == 'corr':
            open_fac = .5
        else:
            open_fac = zone_feat['open_fac'][open_fac_i]

            if i > 0 and windows_list[i][-4:] != windows_list[i-1][-4:]:
                open_fac_i += 1
        obj[3] = open_fac
        obj[4] = 'Temperature'
        obj[5] = 'Temp_setpoint'
        obj[8] = 100
        obj[10] = 300000
        obj[11] = 'Sch_Ocupacao'
        idf.add(obj)
        
    for i in range(len(doors_list)):
        obj = IDF._create_datadict('AirflowNetwork:MultiZone:Surface')
        obj[0] = doors_list[i]
        obj[1] = 'Porta'
        obj[3] = 1
        obj[4] = 'NoVent'
        obj[5] = ' '
        obj[8] = 100
        obj[10] = 300000
        obj[11] = 'Sch_Ocupacao'
        idf.add(obj)
    
    if stairs > 0:
        for i in range(len(corridors)-1):
            obj = IDF._create_datadict('AirflowNetwork:MultiZone:Surface')
            obj[0] = 'stair-sup_'+str(i)
            obj[1] = 'HorizontalOpening'
            obj[3] = 1
            obj[4] = 'Constant'
            obj[5] = 'Temp_setpoint'
            obj[8] = 100
            obj[10] = 300000
            obj[11] = 'Always On'
            idf.add(obj)

        obj = IDF._create_datadict('AirflowNetwork:MultiZone:Component:HorizontalOpening')
        obj[0] = 'HorizontalOpening'
        obj[1] = 0.001
        obj[2] = .65
        obj[3] = 25
        obj[4] = 0.6
        idf.add(obj)

    if shading > 0:
        for i in range(len(ShadingBuildingDetailed['Name'])):
            obj = IDF._create_datadict('Shading:Building:Detailed')
            obj['Name'] = ShadingBuildingDetailed['Name'][i]
            obj['Transmittance Schedule Name'] = ShadingBuildingDetailed['Transmittance Schedule Name'][i]
            obj['Number of Vertices'] = 4
            obj[u'Vertex 1 X-coordinate', 0] = ShadingBuildingDetailed['V1x'][i]
            obj[u'Vertex 1 Y-coordinate', 0] = ShadingBuildingDetailed['V1y'][i]
            obj[u'Vertex 1 Z-coordinate', 0] = ShadingBuildingDetailed['V1z'][i]
            obj[u'Vertex 1 X-coordinate', 1] = ShadingBuildingDetailed['V2x'][i]
            obj[u'Vertex 1 Y-coordinate', 1] = ShadingBuildingDetailed['V2y'][i]
            obj[u'Vertex 1 Z-coordinate', 1] = ShadingBuildingDetailed['V2z'][i]
            obj[u'Vertex 1 X-coordinate', 2] = ShadingBuildingDetailed['V3x'][i]
            obj[u'Vertex 1 Y-coordinate', 2] = ShadingBuildingDetailed['V3y'][i]
            obj[u'Vertex 1 Z-coordinate', 2] = ShadingBuildingDetailed['V3z'][i]
            obj[u'Vertex 1 X-coordinate', 3] = ShadingBuildingDetailed['V4x'][i]
            obj[u'Vertex 1 Y-coordinate', 3] = ShadingBuildingDetailed['V4y'][i]
            obj[u'Vertex 1 Z-coordinate', 3] = ShadingBuildingDetailed['V4z'][i]
            idf.add(obj)

    obj = IDF._create_datadict('Material')
    obj[0] = 'ArgamassaReboco(25mm)'
    obj[1] = 'Rough'
    obj[2] = .025
    obj[3] = c_plaster
    obj[4] = 2000
    obj[5] = 1000
    obj[6] = .9
    obj[7] = absorptance
    obj[8] = absorptance
    idf.add(obj)

    obj = IDF._create_datadict('Material')
    obj[0] = 'TelhaCeramica'
    obj[1] = 'Rough'
    obj[2] = .01
    obj[3] = 1.05
    obj[4] = 2000
    obj[5] = 920
    obj[6] = .9
    obj[7] = absorptance
    obj[8] = absorptance
    idf.add(obj)

    obj = IDF._create_datadict('Material')
    obj[0] = 'Ceram Tij 8 fur circ (10 cm)'
    obj[1] = 'Rough'
    obj[2] = .033
    obj[3] = c_brick
    obj[4] = 1103
    obj[5] = 920
    obj[6] = .9
    idf.add(obj)

    obj = IDF._create_datadict('Material:AirGap')
    obj[0] = 'CavidadeBloco:CamaradeAr(20-50mm)'
    obj[1] = R_air
    idf.add(obj)

    obj = IDF._create_datadict('Building')
    obj[0] = output[:-4]
    obj[1] = azimuth
    obj[2] = 'City'
    obj[3] = .04
    obj[4] = .4
    obj[5] = 'FullInteriorAndExterior'
    obj[6] = 25
    idf.add(obj)

    out = [idf, output]

    return(out)

# out = main(n_floors = 3, output = 'output-teste.idf')

# idf = out[0]
# outputname = out[1]
# idf.save(outputname)