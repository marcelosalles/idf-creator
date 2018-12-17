from idf_creator_json_eq import main_whole
from idf_creator_eq_cp_singlezone import main
import pandas as pd
import random

print('FIM DA IMPORTACAO')

random.seed(53)

cases =[]
zones =[]

# start iteration
for line in range(100):

    # prepare inputs
    azimuth = random.randint(0,359)
    zone_ratio = .25+random.random()*3.75
    zn = random.randint(0,5)
    
    area = 10
    zone_height = 3
    floor_height = 12
    absorptance = .5
    shading = 0
    wall_u = 2.5
    wall_ct = 100
    wwr = .5
    open_fac = 1    
    people = .2
    glass = .87
    corr_width = 2
    roof = 0
    ground = 0
    n_floors=6
    len_zones = n_floors*6
    
    corner_window_n = random.random()
    if corner_window_n > .5:
        corner_window = True
    else:
        corner_window = False
        
    if zn%2 ==0:
        azimuth_zn = (azimuth+270)%360
        zn_side='even'
    else:
        azimuth_zn = (azimuth+90)%360
        zn_side='odd'
        
    if zn == 0:
        if corner_window:
            room_type = '3_window'
        else:
            room_type = '3_wall'
    elif zn == 1:
        if corner_window:
            room_type = '1_window'
        else:
            room_type = '1_wall'
    elif zn == 2:
        room_type = '0_window'
    elif zn == 3:
        room_type = '0_window'
    elif zn == 4:
        if corner_window:
            room_type = '1_window'
        else:
            room_type = '1_wall'
    elif zn == 5:
        if corner_window:
            room_type = '3_window'
        else:
            room_type = '3_wall'
        
    L = (area/zone_ratio)**(1/2)
    W = (area /L)
    
    bldg_ratio = (L*3)/(W*2+corr_width)
    
    zone_feat = pd.DataFrame({
        'people':[people for _ in range(len_zones)],
        'wwr':[wwr for _ in range(len_zones)],
        'open_fac':[open_fac for _ in range(len_zones)],
        'glass':[glass for _ in range(len_zones)]
    })
    
    caso = '{:02.0f}'.format(line)
    output = ('eq_compare/single_{}.epJSON'.format(caso))
    output_whole = ('eq_compare/whole_{}.epJSON'.format(caso))

    main(zone_area=area, zone_ratio=zone_ratio, zone_height=zone_height,
    absorptance=absorptance, shading=shading, azimuth=azimuth_zn,
    bldg_ratio=bldg_ratio, wall_u=wall_u, wall_ct=wall_ct, zn=zn,
    floor_height=floor_height, corner_window=corner_window, ground=ground,
    roof=roof, people=people, glass_fs=glass, wwr=wwr, open_fac=open_fac,
    input_file="seed_single_U-conc-eps.json", output=output)
        
    main_whole(zone_area=area, zone_ratio=zone_ratio, zone_height=zone_height, 
    absorptance=absorptance, shading=shading, azimuth=azimuth, corr_width=corr_width,
    wall_u=wall_u, wall_ct=wall_ct, corr_vent=1, stairs=0, zone_feat=zone_feat,
    concrete_eps=True, zones_x_floor=6, n_floors=n_floors,
    corner_window=corner_window, input_file="seed_single.json",output=output_whole)
    
    cases.append(caso)
    zones.append(zn)

zones_list = pd.DataFrame({'case': cases, 'zone': zones})
zones_list.to_csv('eq_compare/zones_list.csv')
