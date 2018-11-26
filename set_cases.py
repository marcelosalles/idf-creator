from idf_creator import main
import pandas as pd
print('FIM DA IMPORTACAO')

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

MIN_OPENFAC = 0.1
MAX_OPENFAC = 1

MIN_THERMALLOAD = 10
MAX_THERMALLOAD = 150

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
    mean = (BOUNDS[parameter]['max']+BOUNDS[parameter]['min'])*.5
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

office_feat['wwr'] = BOUNDS['wwr']['mean']+BOUNDS['wwr']['sd']*office_feat['wwr']
office_feat['open_fac'] = BOUNDS['open_fac']['mean']+BOUNDS['open_fac']['sd']*office_feat['open_fac']
office_feat['thermal_loads'] = BOUNDS['thermal_loads']['mean']+BOUNDS['thermal_loads']['sd']*office_feat['thermal_loads']
office_feat['glass'] = BOUNDS['glass']['mean']+BOUNDS['glass']['sd']*office_feat['glass']

# when simulations change number of floors
# n_floors_2 = (.25)*n_models
# n_floors_3 = (.5)*n_models
# n_floors_4 = (.75)*n_models
n_floors_list =[1,2,3,4]

# when to start reading office_feat
office_feat_line = 0

# start iteration
for line in range(len(bldg_feat)):

    # define number of floors
    # if line%2 < n_floors_2:
    #     n_floors = 1
    # elif line < n_floors_3:
    #     n_floors = 2
    # elif line < n_floors_4:
    #     n_floors = 3
    # elif line < n_floors_5:
    #     n_floors = 4
    # else:
    #     n_floors = 5

    n_floors = n_floors_list[line%len(n_floors_list)]
    print(n_floors)

    # number of offices in model and sub_df 
    n_offices = n_floors*6

    sub_df_last_row = office_feat_line+n_offices
    sub_df = office_feat[office_feat_line:sub_df_last_row]
    sub_df = sub_df.reset_index()

    office_feat_line = sub_df_last_row

    # prepare inputs
    area = bldg_feat['area'][line]
    ratio = bldg_feat['ratio'][line]
    height = bldg_feat['height'][line]
    absorptance = bldg_feat['abs'][line]
    shading = bldg_feat['shading'][line]
    azimuth = bldg_feat['azimuth'][line]
    u_wall = bldg_feat['u_wall'][line]
    corr_vent = bldg_feat['corr_vent'][line]
    stairs = bldg_feat['stairs'][line]
    caso = '{:04.0f}'.format(line)
    output = ('pre-analise_{}.idf'.format(caso))

    out = main(zone_area=area,zone_ratio=ratio,zone_height=height,absorptance=absorptance,
    shading=shading,azimuth= azimuth,corr_width=2,wall_u=u_wall,corr_vent=corr_vent,
    stairs=stairs,zone_feat=sub_df,zones_x_floor=6,n_floors=n_floors,input="modelo_08-13.idf",output=output)

    idf = out[0]
    outputname = 'pre-analise/'+out[1]
    idf.save(outputname)
