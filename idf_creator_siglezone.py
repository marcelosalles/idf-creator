# The names given to the surfaces go from 0 to 3, being 0 up, 1 right,
# 2 down, 3 left. 

import json

# WALL_TYPE = 'concrete_eps'  # define the way wall is built

def main(zone_area=10, zone_ratio=1, zone_height=3, absorptance=.5,
    shading=1, azimuth=0, bldg_ratio=1, corr_width=2, wall_u=2.5,
    wall_ct=100, floor_height=0, room_type='0_window', ground=0,  # corr_vent=1, 
    roof=0, thermal_loads=20, people=.1, glass_fs=.87, wwr=.33,
    open_fac=.5, input="seed_single.json", output='output.idf'):
    
    print(output)

    # Making sure numbers are not srings ----------

    zone_area = float(zone_area)
    zone_ratio = float(zone_ratio)
    zone_height = float(zone_height)
    absorptance = float(absorptance)
    shading = float(shading)
    azimuth = float(azimuth)
    bldg_ratio = float(bldg_ratio)
    corr_width = float(corr_width)
    wall_u = float(wall_u)
    wall_ct = float(wall_ct)
    floor_height = float(floor_height)
    thermal_loads = float(thermal_loads)
    glass_fs = float(glass_fs)
    wwr = float(wwr)
    open_fac = float(open_fac)

    # editing thermal load

    electric = float(thermal_loads)
    people = float(people)
    lights = 10.50  # DPI nivel A RTQ-R - Escritório Planta livre

    # Defining U
    
    #if WALL_TYPE == 'standard':
    R_mat = (1-.17*wall_u)/wall_u
    c_plaster = .025/(.085227272727273 * R_mat)
    c_brick = .066/(.2875 * R_mat)
    R_air = (.62727273 * R_mat)

    #elif WALL_TYPE == 'concrete_eps':
    
    c_concrete = 1.75  # condutivity
    e_concrete = (wall_ct*1000)/(1000*2200)  # specific heat and density
    R_concrete = e_concrete/c_concrete
    R_eps = (1-(.17+R_concrete)*wall_u)/wall_u
    esp = True
    if R_eps < 0.001:
        esp = False
        c_concrete = (wall_u*e_concrete)/(1-.17*wall_u)
        print('conductivity concrete: ', c_concrete)
        print('wall_u: ', wall_u, '\n', 'wall_ct: ', wall_ct)
        
    # Defining dependent variables ----------

    zone_x = (zone_area/zone_ratio)**(1/2)
    zone_y = (zone_area /zone_x)
    window_x1 = zone_x*.001
    window_x2 = zone_x*.999
    window_y1 = zone_y*.001
    window_y2 = zone_y*.999

    window_z1 = zone_height*(1-wwr)*.5
    window_z2 = window_z1+(zone_height*wwr)

    door_width = .9
    dist_door_wall = .1
    door_height = 2.1

    # START BUILDING OBJECTS
    idf = dict()

    ##### Building
    idf["Building"] = {
        output[:-7]: {
            "loads_convergence_tolerance_value": 0.04,
            "maximum_number_of_warmup_days": 25,
            "north_axis": azimuth,
            "solar_distribution": "FullInteriorAndExterior",
            "temperature_convergence_tolerance_value": 0.4,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "terrain": "City"
        }
    }

    ##### ZONES

    idf["Zone"] = {
        "corridor": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "direction_of_relative_north": 0.0,
            "multiplier": 1,
            "x_origin": 0,
            "y_origin": 0,
            "z_origin": floor_height
        },
        "office": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "direction_of_relative_north": 0.0,
            "multiplier": 1,
            "x_origin": 0,
            "y_origin": corr_width,
            "z_origin": floor_height
        }
    }

    ##### Building Surface
    idf["BuildingSurface:Detailed"] = {

        # Ceiling
        "ceiling_corridor": {
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "corridor"
        },

        "ceiling_office": {
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "office"
        },

        # Floor
        "floor_corridor": {
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "zone_name": "corridor"
        },

        "floor_office": {
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "zone_name": "office"
        },

        # Walls: 0 = up, 1 = right, 2 = down, 3 = left
        "wall-0_corridor": {
            "surface_type": "Wall",
            "construction_name": "Interior Wall",
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-2_office",
            "sun_exposure": "NoSun",
            "wind_exposure": "NoWind",
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "corridor"
        },
        "wall-1_corridor": {
            "surface_type": "Wall",
            "construction_name": "Exterior Wall",
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "wind_exposure": "WindExposed",
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "corridor"
        },
        "wall-2_corridor": {
            "surface_type": "Wall",
            "construction_name": "Exterior Wall",
            "outside_boundary_condition": "Adiabatic",
            "sun_exposure": "NoSun",
            "wind_exposure": "NoWind",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "corridor"
        },
        "wall-3_corridor": {
            "surface_type": "Wall",
            "construction_name": "Exterior Wall",
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "wind_exposure": "WindExposed",
            "vertices": [
                {
                    "vertex_x_coordinate": 0,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0,
                    "vertex_y_coordinate": corr_width,
                    "vertex_z_coordinate": 0
                },
                {
                    "vertex_x_coordinate": 0,
                    "vertex_y_coordinate": 0,
                    "vertex_z_coordinate": 0
                },
                {
                    "vertex_x_coordinate": 0,
                    "vertex_y_coordinate": 0,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "corridor"
        },

        "wall-0_office": {
            "surface_type": "Wall",
            "construction_name": "Exterior Wall",
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "wind_exposure": "WindExposed",
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "office"
        },
        "wall-1_office": {
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "office"
        },
        "wall-2_office": {
            "surface_type": "Wall",
            "construction_name": "Interior Wall",
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-0_corridor",
            "sun_exposure": "NoSun",
            "wind_exposure": "NoWind",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "office"
        },
        "wall-3_office": {
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                }
            ],
            "zone_name": "office"
        }
    }

    # Top Condition
    if roof == 0:
        ceiling_bound = {
            "construction_name": "Interior Ceiling",
            "outside_boundary_condition": "Adiabatic",
            "sun_exposure": "NoSun",
            "surface_type": "Ceiling",
            "wind_exposure": "NoWind"
        }

    else:
        ceiling_bound = {
            "construction_name": "Exterior Roof",
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "wind_exposure": "WindExposed"
        }

    idf["BuildingSurface:Detailed"]["ceiling_corridor"].update(ceiling_bound)
    idf["BuildingSurface:Detailed"]["ceiling_office"].update(ceiling_bound)

    # Bottom condition
    if ground == 0:
        ground_bound = {
            "construction_name": "Interior Floor",
            "outside_boundary_condition": "Adiabatic",
            "sun_exposure": "NoSun",
            "wind_exposure": "NoWind"
        }

    else:
        ground_bound = {
            "construction_name": "Exterior Floor",
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "wind_exposure": "NoWind"
        }

    idf["BuildingSurface:Detailed"]["floor_corridor"].update(ground_bound)
    idf["BuildingSurface:Detailed"]["floor_office"].update(ground_bound)

    # Wall exposition condition
    exposed_wall = {
        "construction_name": "Exterior Wall",
        "outside_boundary_condition": "Outdoors",
        "sun_exposure": "SunExposed",
        "wind_exposure": "WindExposed"
    }
    interior_wall = {
        "construction_name": "Interior Wall",
        "outside_boundary_condition": "Adiabatic",
        "sun_exposure": "NoSun",
        "wind_exposure": "NoWind"
    }

    if room_type == '0_window':
        idf["BuildingSurface:Detailed"]["wall-1_office"].update(interior_wall)
        idf["BuildingSurface:Detailed"]["wall-3_office"].update(interior_wall)

    elif room_type == '1_window' or room_type == '1_wall':
        idf["BuildingSurface:Detailed"]["wall-1_office"].update(exposed_wall)
        idf["BuildingSurface:Detailed"]["wall-3_office"].update(interior_wall)

    elif room_type == '3_window' or room_type == '3_wall':
        idf["BuildingSurface:Detailed"]["wall-1_office"].update(interior_wall)
        idf["BuildingSurface:Detailed"]["wall-3_office"].update(exposed_wall)

    # Add some needed information

    needed_info = {
        "idf_max_extensible_fields": 12,
        "idf_max_fields": 22,
        "number_of_vertices": 4.0
    }

    for obj in idf["BuildingSurface:Detailed"]:
        idf["BuildingSurface:Detailed"][obj].update(needed_info)

    #### FENESTRATION

    idf["FenestrationSurface:Detailed"] = {
        "door_corridor": {
            "building_surface_name": "wall-0_corridor",
            "construction_name": "Interior Door",
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door_office",
            "surface_type": "Door",
            "vertex_1_x_coordinate": dist_door_wall+door_width,
            "vertex_1_y_coordinate": corr_width,
            "vertex_1_z_coordinate": door_height,
            "vertex_2_x_coordinate": dist_door_wall+door_width,
            "vertex_2_y_coordinate": corr_width,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": dist_door_wall,
            "vertex_3_y_coordinate": corr_width,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": dist_door_wall,
            "vertex_4_y_coordinate": corr_width,
            "vertex_4_z_coordinate": door_height
        },
        "door_office": {
            "building_surface_name": "wall-2_office",
            "construction_name": "Interior Door",
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door_corridor",
            "surface_type": "Door",
            "vertex_1_x_coordinate": dist_door_wall,
            "vertex_1_y_coordinate": 0,
            "vertex_1_z_coordinate": door_height,
            "vertex_2_x_coordinate": dist_door_wall,
            "vertex_2_y_coordinate": 0,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": dist_door_wall+door_width,
            "vertex_3_y_coordinate": 0,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": dist_door_wall+door_width,
            "vertex_4_y_coordinate": 0,
            "vertex_4_z_coordinate": door_height
        },

        "window_1_corridor": {
            "building_surface_name": "wall-1_corridor",
            "construction_name": "Exterior Window",
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": zone_x,
            "vertex_1_y_coordinate": .5,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": zone_x,
            "vertex_2_y_coordinate": .5,
            "vertex_2_z_coordinate": 1.1,
            "vertex_3_x_coordinate": zone_x,
            "vertex_3_y_coordinate": 1.5,
            "vertex_3_z_coordinate": 1.1,
            "vertex_4_x_coordinate": zone_x,
            "vertex_4_y_coordinate": 1.5,
            "vertex_4_z_coordinate": 2.1
        },
        "window_3_corridor": {
            "building_surface_name": "wall-3_corridor",
            "construction_name": "Exterior Window",
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 0,
            "vertex_1_y_coordinate": 1.5,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 0,
            "vertex_2_y_coordinate": 1.5,
            "vertex_2_z_coordinate": 1.1,
            "vertex_3_x_coordinate": 0,
            "vertex_3_y_coordinate": .5,
            "vertex_3_z_coordinate": 1.1,
            "vertex_4_x_coordinate": 0,
            "vertex_4_y_coordinate": .5,
            "vertex_4_z_coordinate": 2.1
        },

        "window_0_office": {
            "building_surface_name": "wall-0_office",
            "construction_name": "glass_construction_office",
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": window_x2,
            "vertex_1_y_coordinate": zone_y,
            "vertex_1_z_coordinate": window_z2,
            "vertex_2_x_coordinate": window_x2,
            "vertex_2_y_coordinate": zone_y,
            "vertex_2_z_coordinate": window_z1,
            "vertex_3_x_coordinate": window_x1,
            "vertex_3_y_coordinate": zone_y,
            "vertex_3_z_coordinate": window_z1,
            "vertex_4_x_coordinate": window_x1,
            "vertex_4_y_coordinate": zone_y,
            "vertex_4_z_coordinate": window_z2
        }
    }

    if room_type == '1_window':
        idf["FenestrationSurface:Detailed"].update({
            "window_side_office": {
                "building_surface_name": "wall-1_office",
                "construction_name": "glass_construction_office",
                "number_of_vertices": 4.0,
                "surface_type": "Window",
                "vertex_1_x_coordinate": zone_x,
                "vertex_1_y_coordinate": window_y1,
                "vertex_1_z_coordinate": window_z2,
                "vertex_2_x_coordinate": zone_x,
                "vertex_2_y_coordinate": window_y1,
                "vertex_2_z_coordinate": window_z1,
                "vertex_3_x_coordinate": zone_x,
                "vertex_3_y_coordinate": window_y2,
                "vertex_3_z_coordinate": window_z1,
                "vertex_4_x_coordinate": zone_x,
                "vertex_4_y_coordinate": window_y2,
                "vertex_4_z_coordinate": window_z2
            }
        })

    elif room_type == '3_window':
        idf["FenestrationSurface:Detailed"].update({
            "window_side_office": {
                "building_surface_name": "wall-3_office",
                "construction_name": "glass_construction_office",
                "number_of_vertices": 4.0,
                "surface_type": "Window",
                "vertex_1_x_coordinate": 0,
                "vertex_1_y_coordinate": window_y2,
                "vertex_1_z_coordinate": window_z2,
                "vertex_2_x_coordinate": 0,
                "vertex_2_y_coordinate": window_y2,
                "vertex_2_z_coordinate": window_z1,
                "vertex_3_x_coordinate": 0,
                "vertex_3_y_coordinate": window_y1,
                "vertex_3_z_coordinate": window_z1,
                "vertex_4_x_coordinate": 0,
                "vertex_4_y_coordinate": window_y1,
                "vertex_4_z_coordinate": window_z2
            }
        })
    
    for obj in idf['FenestrationSurface:Detailed']:
        idf['FenestrationSurface:Detailed'][obj].update({
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22
        })

    #### THERMAL LOADS

    idf["ElectricEquipment"] = {
        "equip_office": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "design_level_calculation_method": "Watts/Area",
            "end_use_subcategory": "General",
            "fraction_latent": 0.0,
            "fraction_lost": 0.0,
            "fraction_radiant": 0.5,
            "schedule_name": "Sch_Equip_Computador",
            "watts_per_zone_floor_area": electric,
            "zone_or_zonelist_name": "office"
        },
        "equip_corredor": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "design_level_calculation_method": "Watts/Area",
            "end_use_subcategory": "General",
            "fraction_latent": 0.0,
            "fraction_lost": 0.0,
            "fraction_radiant": 0.5,
            "schedule_name": "Sch_Equip_Computador",
            "watts_per_zone_floor_area": 0.0,
            "zone_or_zonelist_name": "corridor"
        }
    }

    idf["Lights"] = {
        "lights_office": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "design_level_calculation_method": "Watts/Area",
            "fraction_radiant": 0.72,
            "fraction_replaceable": 1.0,
            "fraction_visible": 0.18,
            "return_air_fraction": 0.0,
            "schedule_name": "Sch_Iluminacao",
            "watts_per_zone_floor_area": lights,
            "zone_or_zonelist_name": "office"
        }
    }

    idf["People"] = {
        "people_office": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 10,
            "activity_level_schedule_name": "Sch_Atividade",
            "fraction_radiant": 0.3,
            "number_of_people_calculation_method": "People/Area",
            "number_of_people_schedule_name": "Sch_Ocupacao",
            "people_per_zone_floor_area": people,
            "sensible_heat_fraction": "Autocalculate",
            "zone_or_zonelist_name": "office"
        }
    }

    #### MATERIALS

    idf["Material"] = {
        "ArgamassaReboco(25mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "conductivity": c_plaster,
            "density": 2000.0,
            "roughness": "Rough",
            "solar_absorptance": absorptance,
            "specific_heat": 1000.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.025,
            "visible_absorptance": 0.7
        },
        "Ceram Tij 8 fur circ (10 cm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "conductivity": c_brick,
            "density": 1103.0,
            "roughness": "Rough",
            "specific_heat": 920.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.033
        },
        "ForroGesso(30mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "conductivity": 0.35,
            "density": 750.0,
            "roughness": "Rough",
            "solar_absorptance": 0.2,
            "specific_heat": 840.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.02,
            "visible_absorptance": 0.2
        },
        "ForroMadeira(15mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "conductivity": 0.15,
            "density": 600.0,
            "roughness": "Rough",
            "solar_absorptance": 0.4,
            "specific_heat": 1340.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.015,
            "visible_absorptance": 0.4
        },
        "LajeMacicaConcreto(100mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "conductivity": 1.75,
            "density": 2200.0,
            "roughness": "Rough",
            "solar_absorptance": 0.7,
            "specific_heat": 1000.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.1,
            "visible_absorptance": 0.7
        },
        "concrete": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "conductivity": c_concrete,
            "density": 2200.0,
            "roughness": "Rough",
            "solar_absorptance": 0.7,
            "specific_heat": 1000.0,
            "thermal_absorptance": 0.9,
            "thickness": e_concrete,
            "visible_absorptance": 0.7
        },
        "PisoCeramico(10mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "conductivity": 0.9,
            "density": 1600.0,
            "roughness": "Rough",
            "solar_absorptance": 0.6,
            "specific_heat": 920.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.01,
            "visible_absorptance": 0.6
        },
        "PortaMadeira(30mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "conductivity": 0.15,
            "density": 614.0,
            "roughness": "Rough",
            "solar_absorptance": 0.9,
            "specific_heat": 2300.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.03,
            "visible_absorptance": 0.9
        },
        "TelhaCeramica": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "conductivity": 1.05,
            "density": 2000.0,
            "roughness": "Rough",
            "solar_absorptance": 0.7,
            "specific_heat": 920.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.01,
            "visible_absorptance": 0.7
        }
    }
    
    if esp:
        idf['Material:NoMass'] = {
            'EPS': {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 6,
                'roughness': 'Smooth',
                'thermal_resistance': R_eps,
                'thermal_absorptance': .9,
                'solar_absorptance': absorptance,
                'visible_absorptance': .7
            }
        }

    idf["Material:AirGap"] = {
        "Atico:CamaradeAr(>50mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "thermal_resistance": 0.21
        },
        "CavidadeBloco:CamaradeAr(20-50mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "thermal_resistance": R_air
        }
    }

    idf["WindowMaterial:SimpleGlazingSystem"] = {
        "Clear 3mm": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 3,
            "solar_heat_gain_coefficient": 0.8,
            "u_factor": 5.7
        },
        "glass_material_office": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 3,
            "solar_heat_gain_coefficient": glass_fs,
            "u_factor": 5.7
        }
    }

    #### AFN OBJECTS

    # AFN Simulation Control
    idf["AirflowNetwork:SimulationControl"] = {
        "Ventilacao": {
            "absolute_airflow_convergence_tolerance": 0.0001,
            "airflownetwork_control": "MultizoneWithoutDistribution",
            "azimuth_angle_of_long_axis_of_building": 0.0,
            "building_type": "HighRise",
            "convergence_acceleration_limit": -0.5,
            "height_selection_for_local_wind_pressure_calculation": "OpeningHeight",
            "initialization_type": "ZeroNodePressures",
            "maximum_number_of_iterations": 500,
            "ratio_of_building_width_along_short_axis_to_width_along_long_axis": bldg_ratio,  # ver isso!!!
            "relative_airflow_convergence_tolerance": 0.01,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "wind_pressure_coefficient_type": "SurfaceAverageCalculation"
        }
    }

    # AFN Zone
    idf["AirflowNetwork:MultiZone:Zone"] = {
        "AirflowNetwork:MultiZone:Zone 1": {
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "zone_name": "office"
        },
        "AirflowNetwork:MultiZone:Zone 2": {
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "zone_name": "corridor"
        }
    }

    # AFN Surface
    idf["AirflowNetwork:MultiZone:Surface"] = {
        "AirflowNetwork:MultiZone:Surface 1": {
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window_0_office",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": open_fac
        },
        "AirflowNetwork:MultiZone:Surface 2": {
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window_1_corridor",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.5
        },
        "AirflowNetwork:MultiZone:Surface 3": {
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window_3_corridor",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.5
        },
        "AirflowNetwork:MultiZone:Surface 4": {
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Porta",
            "surface_name": "door_corridor",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 1.0
        }
    }

    if room_type == '3_window' or room_type == '1_window':

        idf["AirflowNetwork:MultiZone:Surface"]["AirflowNetwork:MultiZone:Surface 5"] = {
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window_side_office",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": open_fac
        }
    
    for obj in idf["AirflowNetwork:MultiZone:Surface"]:
        
        idf["AirflowNetwork:MultiZone:Surface"][obj].update({
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12
        })
        
    with open('seed_single.json', 'r') as file:
        seed = json.loads(file.read())
    
    idf.update(seed)
    
    with open(output, 'w') as file:
        file.write(json.dumps(idf))

''' 
main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=90, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=150, floor_height=15, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single_U-conc-eps.json", output='teste_U-conc-eps.epJSON')

  
# Generate cases
main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=90, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=15, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn33-00.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=180, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=15, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn33-90.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=270, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=18, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn38-00.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=90, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=18, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn39-00.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=180, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=18, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn39-90.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=270, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=21, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn44-00.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=90, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=21, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn45-00.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=180, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=21, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn45-90.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=270, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=24, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn50-00.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=0, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=24, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn50-90.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=90, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=24, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn51-00.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=180, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=24, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn51-90.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=180, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=27, room_type='0_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn57-90.epJSON')

# condicoes de janela diferentes
main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=180, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=21, room_type='1_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn45-90_1.epJSON')

main(zone_area=40, zone_ratio=.625, zone_height=3, absorptance=.7, shading=0, azimuth=180, bldg_ratio=1,
    corr_width=2, wall_u=2.35, wall_ct=100, floor_height=21, room_type='3_window', ground=0,
    roof=0, thermal_loads=70, glass_fs=.87, wwr=.15, open_fac=1, input="seed_single.json", output='zn45-90_3.epJSON')
'''
