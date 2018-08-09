from idf_creator import main
import pandas as pd

# number of simulations
MODELS = 30800

# min's and max's
MIN_AREA = 15
MAX_AREA = 80

MIN_RATIO = .4
MAX_RATIO = 2.5

MIN_HEIGHT = 2.4
MAX_HEIGHT = 2.7

MIN_ABS = .2
MIN_ABS = .8

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

# means and sd



# when simulations change number of floors
n_floors_2 = (1/5)*MODELS
n_floors_3 = (2/5)*MODELS
n_floors_4 = (3/5)*MODELS
n_floors_5 = (4/5)*MODELS

# load samples
bldg_feat = pd.read_csv('sa/sample0.csv')
office_feat = pd.read_csv('sa/sample1.csv')

# when to start reading office_feat
office_feat_line = 0

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

    out = main(zone_area=area,zone_ratio=ratio,zone_height=height,absorptance=absorptance,
    shading=shading,azimuth= azimuth,corr_width=2,wall_u=wall_u,corr_vent=corr_vent,
    stairs=stairs,zone_feat=subdf,zones_x_floor=6,n_floors=n_floors,input="modelo.idf",output=output)

    idf = out[0]
    outputname = out[1]
    idf.save(outputname)