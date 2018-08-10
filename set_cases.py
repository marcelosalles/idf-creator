from idf_creator import main
import pandas as pd

# load samples
bldg_feat = pd.read_csv('sa/sample0.csv')
office_feat = pd.read_csv('sa/sample1.csv')

n_models = len(bldg_feat)

# min's and max's
MIN_AREA = 15
MAX_AREA = 80

MIN_RATIO = .4
MAX_RATIO = 2.5

MIN_HEIGHT = 2.4
MAX_HEIGHT = 2.7

MIN_ABS = .2
MAX_ABS = .8

MIN_SHADING = 0
MAX_SHADING = 1

MIN_AZIMUTH = 0
MAX_AZIMUTH = 359.9

MIN_UWALL = 0.5
MAX_UWALL = 3.5

MIN_WWR = .1
MAX_WWR = .5

MIN_OPENFAC = 0
MAX_OPENFAC = 1

MIN_THERMALLOAD = 10
MAX_THERMALLOAD = 250

MIN_FS = .35
MAX_FS = .87

BOUNDS = {
    'area':{
        'min': MIN_AREA,
        'max': MAX_AREA
    },
    'ratio':{
        'min': MIN_RATIO,
        'max': MAX_RATIO
    },
    'height':{
        'min': MIN_HEIGHT,
        'max': MAX_HEIGHT
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
    'u_wall':{
        'min': MIN_UWALL,
        'max': MAX_UWALL
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
    'glass':{
        'min': MIN_FS,
        'max': MAX_FS
    }
}

# means and sd

for parameter in BOUNDS:
    mean = (BOUNDS[parameter]['max']+BOUNDS[parameter]['min'])/2
    sd = BOUNDS[parameter]['max']-mean
    BOUNDS[parameter]['mean'] = mean
    BOUNDS[parameter]['sd'] = sd

# prepare inputs
bldg_feat['area'] = BOUNDS['area']['mean']+BOUNDS['area']['sd']*bldg_feat['area']
bldg_feat['ratio'] = BOUNDS['ratio']['mean']+BOUNDS['ratio']['sd']*bldg_feat['ratio']
bldg_feat['height'] = BOUNDS['height']['mean']+BOUNDS['height']['sd']*bldg_feat['height']
bldg_feat['abs'] = BOUNDS['abs']['mean']+BOUNDS['abs']['sd']*bldg_feat['abs']
bldg_feat['shading'] = BOUNDS['shading']['mean']+BOUNDS['shading']['sd']*bldg_feat['shading']
bldg_feat['azimuth'] = BOUNDS['azimuth']['mean']+BOUNDS['azimuth']['sd']*bldg_feat['azimuth']
bldg_feat['u_wall'] = BOUNDS['u_wall']['mean']+BOUNDS['u_wall']['sd']*bldg_feat['u_wall']
'''
if bldg_feat['corr_vent'] < 0:
    bldg_feat['corr_vent'] = 0
else:
    bldg_feat['corr_vent'] = 1
if bldg_feat['stairs'] < 0:
    bldg_feat['stairs'] = 0
else:
    bldg_feat['stairs'] = 1
'''
office_feat['wwr'] = BOUNDS['wwr']['mean']+BOUNDS['wwr']['sd']*office_feat['wwr']
office_feat['open_fac'] = BOUNDS['open_fac']['mean']+BOUNDS['open_fac']['sd']*office_feat['open_fac']
office_feat['thermal_loads'] = BOUNDS['thermal_loads']['mean']+BOUNDS['thermal_loads']['sd']*office_feat['thermal_loads']
office_feat['glass'] = BOUNDS['glass']['mean']+BOUNDS['glass']['sd']*office_feat['glass']

# when simulations change number of floors
n_floors_2 = (1/5)*n_models
n_floors_3 = (2/5)*n_models
n_floors_4 = (3/5)*n_models
n_floors_5 = (4/5)*n_models

# when to start reading office_feat
office_feat_line = 0

bldg_feat.to_csv('saida.csv')

'''
# start iteration
for line in range(len(bldg_feat)):

    # define number of floors
    if line < n_floors_2:
        n_floors = 1
    elif line < n_floors_3:
        n_floors = 2
    elif line < n_floors_4:
        n_floors = 3
    elif line < n_floors_5:
        n_floors = 4
    else:
        n_floors = 5

    # number of offices in model and subdf 
    n_offices = n_floors*6

    sub_df_last_row = office_feat_line+n_offices
    sub_df = office_feat[office_feat_line:sub_df_last_row]

    office_feat_line = sub_df_last_row

    # prepare inputs
    area = bldg_feat['area'][i]
    ratio = bldg_feat['ratio'][i]
    height = bldg_feat['height'][i]
    absorptance = bldg_feat['abs'][i]
    shading = bldg_feat['shading'][i]
    shading = bldg_feat['azimuth'][i]
    u_wall = bldg_feat['u_wall'][i]
    corr_vent = bldg_feat['corr_vent'][i]
    stairs = bldg_feat['stairs'][i]
    
    out = main(zone_area=area,zone_ratio=ratio,zone_height=height,absorptance=absorptance,
    shading=shading,azimuth= azimuth,corr_width=2,wall_u=u_wall,corr_vent=corr_vent,
    stairs=stairs,zone_feat=subdf,zones_x_floor=6,n_floors=n_floors,input="modelo.idf",output=output)

    idf = out[0]
    outputname = out[1]
    idf.save(outputname)
    '''