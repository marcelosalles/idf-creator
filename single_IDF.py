from idf_creator import main
import pandas as pd

# inputs
area = 40
ratio = .625
height = 3
absorptance = .7
shading = 0
azimuth = 90
u_wall = 2.35
corr_vent = 1
stairs = 1
n_floors = 12
output = 'cp-test_3.idf'

sub_df = {'wwr':[],'open_fac':[],'thermal_loads':[],'glass':[]}

for _ in range(n_floors*6):
	
	sub_df['wwr'] = .15
	sub_df['open_fac'] = 1
	sub_df['thermal_loads'].append(70)
	sub_df['glass'].append(.87)

sub_df = pd.DataFrame(sub_df)

out = main(zone_area=area,zone_ratio=ratio,zone_height=height,absorptance=absorptance,
shading=shading,azimuth= azimuth,corr_width=2,wall_u=u_wall,corr_vent=corr_vent,
stairs=stairs,zone_feat=sub_df,zones_x_floor=6,n_floors=n_floors,input="modelo_08-13.idf",output=output)

idf = out[0]
outputname = out[1]
idf.save(outputname)