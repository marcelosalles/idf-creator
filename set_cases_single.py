from idf_creator_siglezone import main
import pandas as pd
print('FIM DA IMPORTACAO')

# load samples
sample = pd.read_csv('sample_sobol_11-26.csv')
# sample = sample[:300]  # para teste

# min's and max's
MIN_AREA = 12
MAX_AREA = 100

MIN_RATIO = .4
MAX_RATIO = 2.5

MIN_ZONE_HEIGHT = 2.4
MAX_ZONE_HEIGHT = 3.2

MIN_ABS = .1
MAX_ABS = .9

MIN_SHADING = 0
MAX_SHADING = 1.5

MIN_AZIMUTH = 0
MAX_AZIMUTH = 359.9

MIN_WALL_U = 0.5
MAX_WALL_U = 4.7

MIN_WALL_CT = 20
MAX_WALL_CT = 400

MIN_WWR = .1
MAX_WWR = .9

MIN_OPENFAC = 0.1
MAX_OPENFAC = 1

MIN_THERMALLOAD = 0
MAX_THERMALLOAD = 30

MIN_PEOPLE = .05
MAX_PEOPLE = 1

MIN_FS = .3
MAX_FS = .87

MIN_FLOOR_HEIGHT = 0
MIN_FLOOR_HEIGHT = 50

MIN_BLDG_RATIO = .3
MAX_BLDG_RATIO = 1

BOUNDS = {
    'area':{
        'min': MIN_AREA,
        'max': MAX_AREA
    },
    'ratio':{
        'min': MIN_RATIO,
        'max': MAX_RATIO
    },
    'zone_height':{
        'min': MIN_ZONE_HEIGHT,
        'max': MAX_ZONE_HEIGHT
    },
    'abs':{
        'min': MIN_ABS,
        'max': MAX_ABS
    },
    'shading':{
        'min': MIN_SHADING,
        'max': MAX_SHADING
    },
    'azimuth':{
        'min': MIN_AZIMUTH,
        'max': MAX_AZIMUTH
    },
    'wall_u':{
        'min': MIN_WALL_U,
        'max': MAX_WALL_U
    },
    'wall_ct':{
        'min': MIN_WALL_CT,
        'max': MAX_WALL_CT
    },
    'wwr':{
        'min': MIN_WWR,
        'max': MAX_WWR
    },
    'open_fac':{
        'min': MIN_OPENFAC,
        'max': MAX_OPENFAC
    },
    'thermal_loads':{
        'min': MIN_THERMALLOAD,
        'max': MAX_THERMALLOAD
    },
    'people':{
        'min': MIN_PEOPLE,
        'max': MAX_PEOPLE
    },
    'glass':{
        'min': MIN_FS,
        'max': MAX_FS
    },
    'floor_height':{
        'min': MIN_FLOOR_HEIGHT,
        'max': MIN_FLOOR_HEIGHT
    },
    'bldg_ratio':{
        'min': MIN_BLDG_RATIO,
        'max': MAX_BLDG_RATIO
    }
}

# means and sd
for parameter in BOUNDS:
    mean = (BOUNDS[parameter]['max']+BOUNDS[parameter]['min'])*.5
    sd = BOUNDS[parameter]['max']-mean
    BOUNDS[parameter]['mean'] = mean
    BOUNDS[parameter]['sd'] = sd

# prepare inputs
for col in sample:
    if col in list(BOUNDS):
        sample[col] = BOUNDS[col]['mean']+BOUNDS[col]['sd']*sample[col]


# start iteration
for line in range(len(sample)):

    # prepare inputs
    area = sample['area'][line]
    ratio = sample['ratio'][line]
    zone_height = sample['zone_height'][line]
    absorptance = sample['abs'][line]
    shading = sample['shading'][line]
    azimuth = sample['azimuth'][line]
    wall_u = sample['wall_u'][line]
    wall_ct = sample['wall_ct'][line]
    wwr = sample['wwr'][line]
    open_fac = sample['open_fac'][line]
    thermal_loads = sample['thermal_loads'][line]
    people = sample['people'][line]
    glass = sample['glass'][line]
    floor_height = sample['floor_height'][line]
    bldg_ratio = sample['bldg_ratio'][line]
    
    if sample['room_type'][line] < -.6:
        room_type = '1_window'
    elif sample['room_type'][line] < -.2:
        room_type = '3_window'
    elif sample['room_type'][line] < .2:
        room_type = '1_wall'
    elif sample['room_type'][line] < .6:
        room_type = '3_wall'
    else:
        room_type = '0_window'
    
    if sample['ground'][line] < 0:
        ground = 0
    else:
        ground = 1
        
    if sample['roof'][line] < 0:
        roof = 0
    else:
        roof = 1
    
    caso = '{:05.0f}'.format(line)
    output = ('sobol_single/sobol_single_{}.epJSON'.format(caso))

    main(zone_area=area, zone_ratio=ratio, zone_height=zone_height,
    absorptance=absorptance, shading=shading, azimuth=azimuth,
    bldg_ratio=bldg_ratio, corr_width=2, wall_u=wall_u, wall_ct=wall_ct,
    floor_height=floor_height, room_type=room_type, ground=ground,
    roof=roof, thermal_loads=thermal_loads, people=people,
    glass_fs=glass, wwr=wwr, open_fac=open_fac,
    input="seed_single_U-conc-eps.json", output=output)
