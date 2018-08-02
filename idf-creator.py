# -*- coding: utf-8 -*-
import math
import pyidf as pf
pf.validation_level = pf.ValidationLevel.no
import logging
logging.info("start")
from pyidf.idf import IDF


def main(zone_area = 10, zone_ratio = 1.5, zone_height = 3, absorptance = .5, shading = 1, azimuth = 0,
    corr_width = 2, wall_u = 2.5, corr_vent = True, stairs = True, zone_feat = .5,#zone_dict,
    zones_x_floor = 6, n_floors = 1, input = "modelo.idf",output = 'output.idf'):
    
    print(output)

    idf=IDF(input)

    # Making sure numbers are not srings ----------

    zone_area = float(zone_area)
    zone_ratio = float(zone_ratio)
    zone_height = float(zone_height)
    absorptance = float(absorptance)
    shading = float(shading)
    azimuth = int(azimuth)
    corr_width = float(corr_width)
    wall_u = float(wall_u)
    wwr = float(zone_feat) # MUDAR DEPOIS!!!

    zones_x_floor = int(zones_x_floor)
    n_floors = int(n_floors)

    # Defining dependent variabloes ----------

    zone_length = math.sqrt(zone_area / zone_ratio)
    zone_width = (zone_area / zone_length)
    n_zones = zones_x_floor * n_floors
    zones_in_sequence = int(zones_x_floor/2)

    x0_second_row = (zone_width) + (corr_width) 

    window_z1 = zone_height*(1-wwr)/2
    window_z2 = window_z1+(zone_height*wwr)
    window_x1 = zone_width*.001
    window_x2 = zone_width*.999
    window_y1 = zone_length*.001
    window_y2 = zone_length*.999

    door_width = .9
    dist_door_wall = .5
    door_height = 2.1

    # Zones --------------------

    zones_list = []

    for i in range(n_zones):
        zones_list.append( 'Zone_' + str(i) )

    for i in range(n_floors):
        zones_list.append( 'Corridor_floor_' + str(i) )

    # x,y,z of zones' origins

    zones_x = []
    zones_y = []
    zones_z = []

    for i in range(n_floors):
        
        y = 0

        for j in range(zones_in_sequence):
            
            
            zones_x.append(0)
            zones_y.append(y)
            zones_z.append(i*zone_height)
            
            zones_x.append(x0_second_row)
            zones_y.append(y)
            zones_z.append(i*zone_height)
            
            y += zone_length

    for i in range(n_floors):
        zones_x.append(zone_width)
        zones_y.append(0)
        zones_z.append(i*zone_height)
   
    offices = zones_list[:-n_floors]
    corridors = zones_list[-n_floors:]

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
        BldgSurface['Name'].append('wall-0_zn_'+str(i))
        BldgSurface['Name'].append('wall-1_zn_'+str(i))
        BldgSurface['Name'].append('wall-2_zn_'+str(i))
        BldgSurface['Name'].append('wall-3_zn_'+str(i))
        
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
                BldgSurface['OutsideBoundryCondObj'].append('wall-S_zn_'+str((i//6)+2))
            if BldgSurface['Name'][i][0:6] == 'wall-2':
                BldgSurface['OutsideBoundryCondObj'].append('wall-N_zn_'+str((i//6)-2))
            if BldgSurface['Name'][i][0:6] == 'wall-1' or BldgSurface['Name'][i][0:6] == 'wall-3':
                BldgSurface['OutsideBoundryCondObj'].append('wall-corr_zn'+str(i//6))
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
            BldgSurface['SurfaceType'].append('Wall')        
            BldgSurface['ConstructionName'].append('Exterior Wall')
            BldgSurface['OutsideBoundryCond'].append('Outdoors')
            BldgSurface['SunExposure'].append('SunExposed')
            BldgSurface['WindExposure'].append('WindExposed')
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
            
            FenSurface['ConstructionName'].append('Exterior Window')
            FenSurface['ConstructionName'].append('Exterior Window')
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
            
            FenSurface['ConstructionName'].append('Exterior Window')
            FenSurface['ConstructionName'].append('Exterior Window')
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
            
            FenSurface['ConstructionName'].append('Exterior Window')
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
            
            FenSurface['ConstructionName'].append('Exterior Window')
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
            
            FenSurface['ConstructionName'].append('Exterior Window')
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

    for i in range(len(windows_list)):
        obj = IDF._create_datadict('AirflowNetwork:MultiZone:Surface')
        obj[0] = windows_list[i]
        obj[1] = 'Janela'
        obj[3] = .5
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
        obj[4] = 'Temperature'
        obj[5] = 'Temp_setpoint'
        obj[8] = 100
        obj[10] = 300000
        obj[11] = 'Sch_Ocupacao'
        idf.add(obj)

    out = [idf, output]

    return(out)

out = main(zones_x_floor = 20, n_floors = 4)
idf = out[0]
outputname = out[1]
idf.save(outputname)