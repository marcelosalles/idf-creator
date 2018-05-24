# -*- coding: utf-8 -*-

import pyidf as pf
pf.validation_level = pf.ValidationLevel.no
import logging
logging.info("start")
from pyidf.idf import IDF


def main(n_salas_x_pvtos = 12,n_pvtos = 1,pvto_height = 3,corr_width = 3,bdg_length = 55.2,bdg_width = 22.9,input = "modelo.idf",output = 'output.idf'):
	
	idf=IDF(input)

	bdg_length = float(bdg_length)
	bdg_width = float(bdg_width)
	corr_width = float(corr_width)
	pvto_height = float(pvto_height)

	sala_width = (bdg_width-corr_width)/2
            
	n_zonas = n_salas_x_pvtos * n_pvtos

	n_salas_x_lenght = int(n_salas_x_pvtos/2)

	sala_length = bdg_length/n_salas_x_lenght

	x2 = (bdg_width/2) + (corr_width/2)
	            
	lJanela = sala_length-1
	print(output)
	print('Blength ',bdg_length)
	print('salas ',n_salas_x_pvtos)
	print('Length ',sala_length)
	print(lJanela)
	hJanela = 1.2
	parapeito = 1.2

	lPorta = .9
	distPortaParede = .5
	hPorta = 2.1

	#Lista das Zonas



	listaZonas = []

	for i in range(n_zonas):
		listaZonas.append( 'Zona' + str(i) )

	for i in range(n_pvtos):
		listaZonas.append( 'CorredorPvto' + str(i) )

	#x,y,z das Zonas

	ZonasX = []
	ZonasY = []
	ZonasZ = []

	for i in range(n_pvtos):
		
		y = 0

		for j in range(n_salas_x_lenght):
			
			
			ZonasX.append(0)
			ZonasY.append(y)
			ZonasZ.append(i*pvto_height)
			
			ZonasX.append(x2)
			ZonasY.append(y)
			ZonasZ.append(i*pvto_height)
			
			y += sala_length

	xCorredor = (bdg_width/2) - (corr_width/2)

	for i in range(n_pvtos):
	    ZonasX.append(xCorredor)
	    ZonasY.append(0)
	    ZonasZ.append(i*pvto_height)

	#Zone Lists
	    
	#Tudo = ['Tudo'] + listaZonas
	Salas = listaZonas[:-n_pvtos]
	ListaCorredor = listaZonas[-n_pvtos:]

	#Surfaces

	BldgSurface = dict()
	BldgSurface['Name'] = []
	BldgSurface['SurfaceType'] =[]
	BldgSurface['ConstructionName'] = []
	BldgSurface['ZoneName'] = []
	BldgSurface['OutsideBoundryCond'] = []
	BldgSurface['OutsideBoundryCondObj'] = []
	BldgSurface['SunExposure'] = []
	BldgSurface['WindExposure'] = []
	BldgSurface['V1x'] = []
	BldgSurface['V1y'] = []
	BldgSurface['V1z'] = []
	BldgSurface['V2x'] = []
	BldgSurface['V2y'] = []
	BldgSurface['V2z'] = []
	BldgSurface['V3x'] = []
	BldgSurface['V3y'] = []
	BldgSurface['V3z'] = []
	BldgSurface['V4x'] = []
	BldgSurface['V4y'] = []
	BldgSurface['V4z'] = []

	for i in range(n_zonas):

	    BldgSurface['Name'].append('Chao_Zn'+str(i))
	    BldgSurface['Name'].append('Teto_Zn'+str(i))
	    BldgSurface['Name'].append('ParNorte_Zn'+str(i))
	    BldgSurface['Name'].append('ParSul_Zn'+str(i))
	    BldgSurface['Name'].append('ParLeste_Zn'+str(i))
	    BldgSurface['Name'].append('ParOeste_Zn'+str(i))
	    
	    BldgSurface['SurfaceType'].append('Floor')
	    if i >= n_zonas-n_salas_x_pvtos:
	        BldgSurface['SurfaceType'].append('Roof')
	    else:
	        BldgSurface['SurfaceType'].append('Ceiling')
	        
	    for j in range(4):
	        BldgSurface['SurfaceType'].append('Wall')
	    
	    if i < n_salas_x_pvtos:
	        BldgSurface['ConstructionName'].append('Exterior Floor')
	    else:
	        BldgSurface['ConstructionName'].append('Interior Floor')
	    if BldgSurface['SurfaceType'][i*6+1] == 'Roof':
	        BldgSurface['ConstructionName'].append('Exterior Roof')
	    else:
	        BldgSurface['ConstructionName'].append('Interior Ceiling')    
	    if i%2 == 0:
	        if i%n_salas_x_pvtos == 0:
	            BldgSurface['ConstructionName'].append('Interior Wall')
	            BldgSurface['ConstructionName'].append('Exterior Wall')
	            BldgSurface['ConstructionName'].append('Interior Wall')
	            BldgSurface['ConstructionName'].append('Exterior Wall')
	        else:
	            if i%n_salas_x_pvtos == n_salas_x_pvtos-2:
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
	        if i%n_salas_x_pvtos == 1:
	            BldgSurface['ConstructionName'].append('Interior Wall')
	            BldgSurface['ConstructionName'].append('Exterior Wall')
	            BldgSurface['ConstructionName'].append('Exterior Wall')
	            BldgSurface['ConstructionName'].append('Interior Wall')
	        else:
	            if i%n_salas_x_pvtos == n_salas_x_pvtos-1:
	                BldgSurface['ConstructionName'].append('Exterior Wall')
	                BldgSurface['ConstructionName'].append('Interior Wall')
	                BldgSurface['ConstructionName'].append('Exterior Wall')
	                BldgSurface['ConstructionName'].append('Interior Wall')
	            else:
	                BldgSurface['ConstructionName'].append('Interior Wall')
	                BldgSurface['ConstructionName'].append('Interior Wall')
	                BldgSurface['ConstructionName'].append('Exterior Wall')
	                BldgSurface['ConstructionName'].append('Interior Wall')
	    for j in range(6):
	        BldgSurface['ZoneName'].append(listaZonas[i])
	        
	for i in range(len(BldgSurface['ConstructionName'])):
	    if BldgSurface['ConstructionName'][i] == 'Exterior Floor':
	        BldgSurface['OutsideBoundryCond'].append('Ground')
	    else:
	        if BldgSurface['ConstructionName'][i][0:3] == 'Ext':
	            BldgSurface['OutsideBoundryCond'].append('Outdoors')
	        else:
	            BldgSurface['OutsideBoundryCond'].append('Surface')
	            
	for i in range(len(BldgSurface['OutsideBoundryCond'])):
	    if BldgSurface['OutsideBoundryCond'][i] == 'Outdoors':
	        BldgSurface['SunExposure'].append('SunExposed')
	        BldgSurface['WindExposure'].append('WindExposed')
	    else:
	        BldgSurface['SunExposure'].append('NoSun')
	        BldgSurface['WindExposure'].append('NoWind')
	        
	for i in range(len(BldgSurface['OutsideBoundryCond'])):
	    if BldgSurface['OutsideBoundryCond'][i] == 'Surface':
	        if BldgSurface['Name'][i][0:4] == 'Chao':
	            BldgSurface['OutsideBoundryCondObj'].append('Teto_Zn'+str((i//6)-n_salas_x_pvtos))
	        if BldgSurface['Name'][i][0:4] == 'Teto':
	            BldgSurface['OutsideBoundryCondObj'].append('Chao_Zn'+str((i//6)+n_salas_x_pvtos))
	        if BldgSurface['Name'][i][0:4] == 'ParN':
	            BldgSurface['OutsideBoundryCondObj'].append('ParSul_Zn'+str((i//6)+2))
	        if BldgSurface['Name'][i][0:4] == 'ParS':
	            BldgSurface['OutsideBoundryCondObj'].append('ParNorte_Zn'+str((i//6)-2))
	        if BldgSurface['Name'][i][0:4] == 'ParL':
	            BldgSurface['OutsideBoundryCondObj'].append('ParCor_Zn'+str(i//6))
	        if BldgSurface['Name'][i][0:4] == 'ParO':
	            BldgSurface['OutsideBoundryCondObj'].append('ParCor_Zn'+str(i//6))            
	    else:
	        BldgSurface['OutsideBoundryCondObj'].append(' ')
	        
	for i in range(len(BldgSurface['Name'])):
	    if BldgSurface['Name'][i][0:4] == 'Chao':
	        BldgSurface['V1x'].append(sala_width)
	        BldgSurface['V1y'].append(sala_length)
	        BldgSurface['V1z'].append(0)
	        BldgSurface['V2x'].append(sala_width)
	        BldgSurface['V2y'].append(0)
	        BldgSurface['V2z'].append(0)
	        BldgSurface['V3x'].append(0)
	        BldgSurface['V3y'].append(0)
	        BldgSurface['V3z'].append(0)
	        BldgSurface['V4x'].append(0)
	        BldgSurface['V4y'].append(sala_length)
	        BldgSurface['V4z'].append(0)
	    if BldgSurface['Name'][i][0:4] == 'Teto':
	        BldgSurface['V1x'].append(0)
	        BldgSurface['V1y'].append(sala_length)
	        BldgSurface['V1z'].append(pvto_height)
	        BldgSurface['V2x'].append(0)
	        BldgSurface['V2y'].append(0)
	        BldgSurface['V2z'].append(pvto_height)
	        BldgSurface['V3x'].append(sala_width)
	        BldgSurface['V3y'].append(0)
	        BldgSurface['V3z'].append(pvto_height)
	        BldgSurface['V4x'].append(sala_width)
	        BldgSurface['V4y'].append(sala_length)
	        BldgSurface['V4z'].append(pvto_height)
	    if BldgSurface['Name'][i][0:4] == 'ParN':
	        BldgSurface['V1x'].append(sala_width)
	        BldgSurface['V1y'].append(sala_length)
	        BldgSurface['V1z'].append(pvto_height)
	        BldgSurface['V2x'].append(sala_width)
	        BldgSurface['V2y'].append(sala_length)
	        BldgSurface['V2z'].append(0)
	        BldgSurface['V3x'].append(0)
	        BldgSurface['V3y'].append(sala_length)
	        BldgSurface['V3z'].append(0)
	        BldgSurface['V4x'].append(0)
	        BldgSurface['V4y'].append(sala_length)
	        BldgSurface['V4z'].append(pvto_height)
	    if BldgSurface['Name'][i][0:4] == 'ParS':
	        BldgSurface['V1x'].append(0)
	        BldgSurface['V1y'].append(0)
	        BldgSurface['V1z'].append(pvto_height)
	        BldgSurface['V2x'].append(0)
	        BldgSurface['V2y'].append(0)
	        BldgSurface['V2z'].append(0)
	        BldgSurface['V3x'].append(sala_width)
	        BldgSurface['V3y'].append(0)
	        BldgSurface['V3z'].append(0)
	        BldgSurface['V4x'].append(sala_width)
	        BldgSurface['V4y'].append(0)
	        BldgSurface['V4z'].append(pvto_height)
	    if BldgSurface['Name'][i][0:4] == 'ParL':
	        BldgSurface['V1x'].append(sala_width)
	        BldgSurface['V1y'].append(0)
	        BldgSurface['V1z'].append(pvto_height)
	        BldgSurface['V2x'].append(sala_width)
	        BldgSurface['V2y'].append(0)
	        BldgSurface['V2z'].append(0)
	        BldgSurface['V3x'].append(sala_width)
	        BldgSurface['V3y'].append(sala_length)
	        BldgSurface['V3z'].append(0)
	        BldgSurface['V4x'].append(sala_width)
	        BldgSurface['V4y'].append(sala_length)
	        BldgSurface['V4z'].append(pvto_height)
	    if BldgSurface['Name'][i][0:4] == 'ParO':
	        BldgSurface['V1x'].append(0)
	        BldgSurface['V1y'].append(sala_length)
	        BldgSurface['V1z'].append(pvto_height)
	        BldgSurface['V2x'].append(0)
	        BldgSurface['V2y'].append(sala_length)
	        BldgSurface['V2z'].append(0)
	        BldgSurface['V3x'].append(0)
	        BldgSurface['V3y'].append(0)
	        BldgSurface['V3z'].append(0)
	        BldgSurface['V4x'].append(0)
	        BldgSurface['V4y'].append(0)
	        BldgSurface['V4z'].append(pvto_height)

	for i in range(len(ListaCorredor)):
	    
	    for j in range(4+n_salas_x_pvtos):
	        BldgSurface['ZoneName'].append(ListaCorredor[i])
	        
	    BldgSurface['Name'].append('Chao_CorPvto'+str(i))
	    BldgSurface['Name'].append('Teto_CorPvto'+str(i))
	    BldgSurface['Name'].append('ParNorte_CorPvto'+str(i))
	    BldgSurface['Name'].append('ParSul_CorPvto'+str(i))
	    
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
	        BldgSurface['OutsideBoundryCondObj'].append('Teto_CorPvto'+str(i-1))
	        
	    if i == n_pvtos-1:
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
	        BldgSurface['OutsideBoundryCondObj'].append('Chao_CorPvto'+str(i+1))
	    for j in range(2):
	        BldgSurface['SurfaceType'].append('Wall')        
	        BldgSurface['ConstructionName'].append('Exterior Wall')
	        BldgSurface['OutsideBoundryCond'].append('Outdoors')
	        BldgSurface['SunExposure'].append('SunExposed')
	        BldgSurface['WindExposure'].append('WindExposed')
	        BldgSurface['OutsideBoundryCondObj'].append(' ')
	        
	    for j in range(n_salas_x_pvtos):
	        BldgSurface['SurfaceType'].append('Wall')        
	        BldgSurface['ConstructionName'].append('Interior Wall')
	        BldgSurface['OutsideBoundryCond'].append('Surface')
	        BldgSurface['SunExposure'].append('NoSun')
	        BldgSurface['WindExposure'].append('NoWind')
	        if j%2 == 0:
	        	BldgSurface['OutsideBoundryCondObj'].append('ParLeste_Zn'+str(i*n_salas_x_pvtos+j))
	        else:
	        	BldgSurface['OutsideBoundryCondObj'].append('ParLeste_Zn'+str(i*n_salas_x_pvtos+j))

	    BldgSurface['V1x'].append(corr_width)
	    BldgSurface['V1y'].append(bdg_length)
	    BldgSurface['V1z'].append(0)
	    BldgSurface['V2x'].append(corr_width)
	    BldgSurface['V2y'].append(0)
	    BldgSurface['V2z'].append(0)
	    BldgSurface['V3x'].append(0)
	    BldgSurface['V3y'].append(0)
	    BldgSurface['V3z'].append(0)
	    BldgSurface['V4x'].append(0)
	    BldgSurface['V4y'].append(bdg_length)
	    BldgSurface['V4z'].append(0)
	    
	    BldgSurface['V1x'].append(0)
	    BldgSurface['V1y'].append(bdg_length)
	    BldgSurface['V1z'].append(pvto_height)
	    BldgSurface['V2x'].append(0)
	    BldgSurface['V2y'].append(0)
	    BldgSurface['V2z'].append(pvto_height)
	    BldgSurface['V3x'].append(corr_width)
	    BldgSurface['V3y'].append(0)
	    BldgSurface['V3z'].append(pvto_height)
	    BldgSurface['V4x'].append(corr_width)
	    BldgSurface['V4y'].append(bdg_length)
	    BldgSurface['V4z'].append(pvto_height)
	    
	    BldgSurface['V1x'].append(corr_width)
	    BldgSurface['V1y'].append(bdg_length)
	    BldgSurface['V1z'].append(pvto_height)
	    BldgSurface['V2x'].append(corr_width)
	    BldgSurface['V2y'].append(bdg_length)
	    BldgSurface['V2z'].append(0)
	    BldgSurface['V3x'].append(0)
	    BldgSurface['V3y'].append(bdg_length)
	    BldgSurface['V3z'].append(0)
	    BldgSurface['V4x'].append(0)
	    BldgSurface['V4y'].append(bdg_length)
	    BldgSurface['V4z'].append(pvto_height)
	    
	    BldgSurface['V1x'].append(0)
	    BldgSurface['V1y'].append(0)
	    BldgSurface['V1z'].append(pvto_height)
	    BldgSurface['V2x'].append(0)
	    BldgSurface['V2y'].append(0)
	    BldgSurface['V2z'].append(0)
	    BldgSurface['V3x'].append(corr_width)
	    BldgSurface['V3y'].append(0)
	    BldgSurface['V3z'].append(0)
	    BldgSurface['V4x'].append(corr_width)
	    BldgSurface['V4y'].append(0)
	    BldgSurface['V4z'].append(pvto_height)
	    
	    for j in range(n_salas_x_lenght):
	        
	        BldgSurface['Name'].append('ParCor_Zn'+str(i*n_salas_x_pvtos+j*2))
	        BldgSurface['V1x'].append(0)
	        BldgSurface['V1y'].append(sala_length*(j+1))
	        BldgSurface['V1z'].append(pvto_height)
	        BldgSurface['V2x'].append(0)
	        BldgSurface['V2y'].append(sala_length*(j+1))
	        BldgSurface['V2z'].append(0)
	        BldgSurface['V3x'].append(0)
	        BldgSurface['V3y'].append(sala_length*(j))
	        BldgSurface['V3z'].append(0)
	        BldgSurface['V4x'].append(0)
	        BldgSurface['V4y'].append(sala_length*(j))
	        BldgSurface['V4z'].append(pvto_height)
	        
	        BldgSurface['Name'].append('ParCor_Zn'+str(i*n_salas_x_pvtos+j*2+1))
	        BldgSurface['V1x'].append(corr_width)
	        BldgSurface['V1y'].append(sala_length*(j))
	        BldgSurface['V1z'].append(pvto_height)
	        BldgSurface['V2x'].append(corr_width)
	        BldgSurface['V2y'].append(sala_length*(j))
	        BldgSurface['V2z'].append(0)
	        BldgSurface['V3x'].append(corr_width)
	        BldgSurface['V3y'].append(sala_length*(j+1))
	        BldgSurface['V3z'].append(0)
	        BldgSurface['V4x'].append(corr_width)
	        BldgSurface['V4y'].append(sala_length*(j+1))
	        BldgSurface['V4z'].append(pvto_height)
	        
	#FenestrationSurdace:Detailed
	 
	FenSurface = dict()
	FenSurface['Name'] = []
	FenSurface['SurfaceType'] = []
	FenSurface['ConstructionName'] = []
	FenSurface['BuildingSurfaceName'] = []
	FenSurface['OutsideBoundryCondObj'] = []
	FenSurface['V1x'] = []
	FenSurface['V1y'] = []
	FenSurface['V1z'] = []
	FenSurface['V2x'] = []
	FenSurface['V2y'] = []
	FenSurface['V2z'] = []
	FenSurface['V3x'] = []
	FenSurface['V3y'] = []
	FenSurface['V3z'] = []
	FenSurface['V4x'] = []
	FenSurface['V4y'] = []
	FenSurface['V4z'] = []

	listaPortas = []
	listaJanelas = []
	    
	for i in range(n_zonas):
	    
	    nomei = 'Jan_Zn'+str(i)
	    FenSurface['Name'].append(nomei)
	    listaJanelas.append(nomei)
	    
	    nomei = 'Porta_Zn'+str(i)    
	    listaPortas.append(nomei)
	    FenSurface['Name'].append(nomei)
	        
	    FenSurface['SurfaceType'].append('Window')
	    FenSurface['SurfaceType'].append('Door')
	    
	    FenSurface['ConstructionName'].append('Exterior Window')
	    FenSurface['ConstructionName'].append('Interior Door')
	    
	    FenSurface['OutsideBoundryCondObj'].append(' ')
	    FenSurface['OutsideBoundryCondObj'].append('PortaCor_Zn'+str(i))
	    
	    if i%2 == 0:
	        
	        FenSurface['BuildingSurfaceName'].append('ParOeste_Zn'+str(i))
	        FenSurface['BuildingSurfaceName'].append('ParLeste_Zn'+str(i))
	 
	        #Janela
	        FenSurface['V1x'].append(0)
	        FenSurface['V1y'].append(sala_length/2+lJanela/2)
	        FenSurface['V1z'].append(parapeito+hJanela)
	        FenSurface['V2x'].append(0)
	        FenSurface['V2y'].append(sala_length/2+lJanela/2)
	        FenSurface['V2z'].append(parapeito)
	        FenSurface['V3x'].append(0)
	        FenSurface['V3y'].append(sala_length/2-lJanela/2)
	        FenSurface['V3z'].append(parapeito)
	        FenSurface['V4x'].append(0)
	        FenSurface['V4y'].append(sala_length/2-lJanela/2)
	        FenSurface['V4z'].append(parapeito+hJanela) 
	        
	        #Porta
	        FenSurface['V1x'].append(sala_width)
	        FenSurface['V1y'].append(sala_length-distPortaParede-lPorta)
	        FenSurface['V1z'].append(hPorta)
	        FenSurface['V2x'].append(sala_width)
	        FenSurface['V2y'].append(sala_length-distPortaParede-lPorta)
	        FenSurface['V2z'].append(0)
	        FenSurface['V3x'].append(sala_width)
	        FenSurface['V3y'].append(sala_length-distPortaParede)
	        FenSurface['V3z'].append(0)
	        FenSurface['V4x'].append(sala_width)
	        FenSurface['V4y'].append(sala_length-distPortaParede)
	        FenSurface['V4z'].append(hPorta)
	        
	    else:
	        
	        FenSurface['BuildingSurfaceName'].append('ParLeste_Zn'+str(i))
	        FenSurface['BuildingSurfaceName'].append('ParOeste_Zn'+str(i))
	 
	        #Janela
	        FenSurface['V1x'].append(sala_width)
	        FenSurface['V1y'].append(sala_length/2-lJanela/2)
	        FenSurface['V1z'].append(parapeito+hJanela)
	        FenSurface['V2x'].append(sala_width)
	        FenSurface['V2y'].append(sala_length/2-lJanela/2)
	        FenSurface['V2z'].append(parapeito)
	        FenSurface['V3x'].append(sala_width)
	        FenSurface['V3y'].append(sala_length/2+lJanela/2)
	        FenSurface['V3z'].append(parapeito)
	        FenSurface['V4x'].append(sala_width)
	        FenSurface['V4y'].append(sala_length/2+lJanela/2)
	        FenSurface['V4z'].append(parapeito+hJanela) 
	        
	        #Porta
	        FenSurface['V1x'].append(0)
	        FenSurface['V1y'].append(sala_length-distPortaParede)
	        FenSurface['V1z'].append(hPorta)
	        FenSurface['V2x'].append(0)
	        FenSurface['V2y'].append(sala_length-distPortaParede)
	        FenSurface['V2z'].append(0)
	        FenSurface['V3x'].append(0)
	        FenSurface['V3y'].append(sala_length-distPortaParede-lPorta)
	        FenSurface['V3z'].append(0)
	        FenSurface['V4x'].append(0)
	        FenSurface['V4y'].append(sala_length-distPortaParede-lPorta)
	        FenSurface['V4z'].append(hPorta)

	for i in range(len(ListaCorredor)):
	    
	    for j in range(n_salas_x_lenght):
	        
	        FenSurface['Name'].append('PortaCor_Zn'+str(i*n_salas_x_pvtos+j*2))
	        FenSurface['Name'].append('PortaCor_Zn'+str(i*n_salas_x_pvtos+j*2+1))
	        
	        FenSurface['SurfaceType'].append('Door')
	        FenSurface['SurfaceType'].append('Door')
	                
	        FenSurface['ConstructionName'].append('Interior Door')
	        FenSurface['ConstructionName'].append('Interior Door')
	        
	        FenSurface['BuildingSurfaceName'].append('ParCor_Zn'+str(i*n_salas_x_pvtos+j*2))
	        FenSurface['BuildingSurfaceName'].append('ParCor_Zn'+str(i*n_salas_x_pvtos+j*2+1))
	        
	        FenSurface['OutsideBoundryCondObj'].append('Porta_Zn'+str(i*n_salas_x_pvtos+j*2))
	        FenSurface['OutsideBoundryCondObj'].append('Porta_Zn'+str(i*n_salas_x_pvtos+j*2+1))
	        
	                #Porta Oeste
	        FenSurface['V1x'].append(0)
	        FenSurface['V1y'].append(sala_length*(j+1)-distPortaParede)
	        FenSurface['V1z'].append(hPorta)
	        FenSurface['V2x'].append(0)
	        FenSurface['V2y'].append(sala_length*(j+1)-distPortaParede)
	        FenSurface['V2z'].append(0)
	        FenSurface['V3x'].append(0)
	        FenSurface['V3y'].append(sala_length*(j+1)-distPortaParede-lPorta)
	        FenSurface['V3z'].append(0)
	        FenSurface['V4x'].append(0)
	        FenSurface['V4y'].append(sala_length*(j+1)-distPortaParede-lPorta)
	        FenSurface['V4z'].append(hPorta)
	                #Porta Leste
	        FenSurface['V1x'].append(corr_width)
	        FenSurface['V1y'].append(sala_length*(j+1)-distPortaParede-lPorta)
	        FenSurface['V1z'].append(hPorta)
	        FenSurface['V2x'].append(corr_width)
	        FenSurface['V2y'].append(sala_length*(j+1)-distPortaParede-lPorta)
	        FenSurface['V2z'].append(0)
	        FenSurface['V3x'].append(corr_width)
	        FenSurface['V3y'].append(sala_length*(j+1)-distPortaParede)
	        FenSurface['V3z'].append(0)
	        FenSurface['V4x'].append(corr_width)
	        FenSurface['V4y'].append(sala_length*(j+1)-distPortaParede)
	        FenSurface['V4z'].append(hPorta)

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

	for i in range(len(listaZonas)):
	    obj = IDF._create_datadict('Zone')
	    obj['Name'] = listaZonas[i]
	    obj['Direction of Relative North'] = 0
	    obj['Multiplier'] = 1
	    obj['X Origin'] = ZonasX[i]
	    obj['Y Origin'] = ZonasY[i]
	    obj['Z Origin'] = ZonasZ[i] 
	    idf.add(obj)


	obj = IDF._create_datadict('ZoneList')
	obj['Name'] = 'Salas'
	for i in range(len(Salas)):
	    obj[i+1] = Salas[i]
	idf.add(obj)

	obj = IDF._create_datadict('Zonelist')
	obj['Name'] = 'Tudo'
	for i in range(len(listaZonas)):
	    obj[i+1] = listaZonas[i]
	idf.add(obj)

	obj = IDF._create_datadict('Zonelist')
	obj['Name'] = 'Corredores'
	for i in range(len(ListaCorredor)):
	    obj[i+1] = ListaCorredor[i]
	idf.add(obj)

	for i in range(len(listaZonas)):
	    obj = IDF._create_datadict('AirflowNetwork:MultiZone:Zone')
	    obj['Zone Name'] = listaZonas[i]
	    obj[5] = 100
	    obj[7] = 300000
	    idf.add(obj)

	for i in range(len(listaJanelas)):
	    obj = IDF._create_datadict('AirflowNetwork:MultiZone:Surface')
	    obj[0] = listaJanelas[i]
	    obj[1] = 'Janela'
	    obj[3] = .5
	    obj[4] = 'Temperature'
	    obj[5] = 'Temp_setpoint'
	    obj[8] = 100
	    obj[10] = 300000
	    obj[11] = 'Sch_Ocupacao'
	    idf.add(obj)
	    
	for i in range(len(listaPortas)):
	    obj = IDF._create_datadict('AirflowNetwork:MultiZone:Surface')
	    obj[0] = listaPortas[i]
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

liPvto=[1,3,5]
liDime=[[8,9.3,16.1,22.9,36.6,47.5,50],[13,18.8,36.4,55.2,89.5,158,200],[1.5,2,3,3,3,4,5],[4,6,14,12,12,16,20]] # [[Prof],[Comp],[Corr],[Sala]]

for pvto in range(len(liPvto)):
	for tipo in range(len(liDime[0])):
		out = main(n_salas_x_pvtos = liDime[3][tipo],n_pvtos = liPvto[pvto],pvto_height = 3,corr_width = liDime[2][tipo],bdg_length = liDime[1][tipo],bdg_width = liDime[0][tipo],input = ('modelo.idf'),output = ('tipo'+str(tipo)+'n_pvtoss'+str(liPvto[pvto])+'.idf'))
		idf = out[0]
		outputname = out[1]
		idf.save(outputname)