import json

with open 'C:/Users/LabEEE_1-2/Desktop/epJSON/pre-analise_6600.json' as file:
    idf = json.loads(file)

print(idf['AirflowNetwork:MultiZone:Surface'][0])

for obj in idf["AirflowNetwork:MultiZone:Surface"]:
    del obj['idf_order']

print(idf['AirflowNetwork:MultiZone:Surface'][0])

new_idf = json.dumps(idf)

'''
  "AirflowNetwork:MultiZone:Surface": {
        "AirflowNetwork:MultiZone:Surface 1": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 165,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window-3_zn_0",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.240707397461
        },
        "AirflowNetwork:MultiZone:Surface 2": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 166,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window-1_zn_1",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.240707397461
        },
        "AirflowNetwork:MultiZone:Surface 3": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 167,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window-2_zn_1",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.240707397461
        },
        "AirflowNetwork:MultiZone:Surface 4": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 168,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window-3_zn_2",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.240707397461
        },
        "AirflowNetwork:MultiZone:Surface 5": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 169,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window-1_zn_3",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.366555786133
        },
        "AirflowNetwork:MultiZone:Surface 6": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 170,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window-0_zn_4",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.240707397461
        },
        "AirflowNetwork:MultiZone:Surface 7": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 171,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window-3_zn_4",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.240707397461
        },
        "AirflowNetwork:MultiZone:Surface 8": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 172,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Janela",
            "surface_name": "window-0_zn_5",
            "ventilation_control_mode": "Temperature",
            "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 0.240707397461
        },
        "AirflowNetwork:MultiZone:Surface 9": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 173,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Porta",
            "surface_name": "door_zn_0",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 1.0
        },
        "AirflowNetwork:MultiZone:Surface 10": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 174,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Porta",
            "surface_name": "door_zn_1",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 1.0
        },
        "AirflowNetwork:MultiZone:Surface 11": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 175,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Porta",
            "surface_name": "door_zn_2",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 1.0
        },
        "AirflowNetwork:MultiZone:Surface 12": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 176,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Porta",
            "surface_name": "door_zn_3",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 1.0
        },
        "AirflowNetwork:MultiZone:Surface 13": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 177,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Porta",
            "surface_name": "door_zn_4",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 1.0
        },
        "AirflowNetwork:MultiZone:Surface 14": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12,
            "idf_order": 178,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "leakage_component_name": "Porta",
            "surface_name": "door_zn_5",
            "ventilation_control_mode": "NoVent",
            "venting_availability_schedule_name": "Sch_Ocupacao",
            "window_door_opening_factor_or_crack_factor": 1.0
        }
    },
    "AirflowNetwork:MultiZone:Zone": {
        "AirflowNetwork:MultiZone:Zone 1": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 158,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "zone_name": "zone_0"
        },
        "AirflowNetwork:MultiZone:Zone 2": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 159,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "zone_name": "zone_1"
        },
        "AirflowNetwork:MultiZone:Zone 3": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 160,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "zone_name": "zone_2"
        },
        "AirflowNetwork:MultiZone:Zone 4": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 161,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "zone_name": "zone_3"
        },
        "AirflowNetwork:MultiZone:Zone 5": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 162,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "zone_name": "zone_4"
        },
        "AirflowNetwork:MultiZone:Zone 6": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 163,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "zone_name": "zone_5"
        },
        "AirflowNetwork:MultiZone:Zone 7": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 164,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "zone_name": "corridor_0"
        }
    },

    "Building": {
        "pre-analise_6600": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 4,
            "loads_convergence_tolerance_value": 0.04,
            "maximum_number_of_warmup_days": 25,
            "north_axis": 82.0,
            "solar_distribution": "FullInteriorAndExterior",
            "temperature_convergence_tolerance_value": 0.4,
            "terrain": "City"
        }
    },

    "BuildingSurface:Detailed": {
        "ceil_corr_0": {
            "construction_name": "Exterior Roof",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 93,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "corridor_0"
        },
        "ceiling_zn_0": {
            "construction_name": "Exterior Roof",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 57,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_0"
        },
        "ceiling_zn_1": {
            "construction_name": "Exterior Roof",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 63,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_1"
        },
        "ceiling_zn_2": {
            "construction_name": "Exterior Roof",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 69,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_2"
        },
        "ceiling_zn_3": {
            "construction_name": "Exterior Roof",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 75,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_3"
        },
        "ceiling_zn_4": {
            "construction_name": "Exterior Roof",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 81,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_4"
        },
        "ceiling_zn_5": {
            "construction_name": "Exterior Roof",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 87,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_5"
        },
        "floor_corr_0": {
            "construction_name": "Exterior Floor",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 92,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
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
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        },
        "floor_zn_0": {
            "construction_name": "Exterior Floor",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 56,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
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
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_0"
        },
        "floor_zn_1": {
            "construction_name": "Exterior Floor",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 62,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
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
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_1"
        },
        "floor_zn_2": {
            "construction_name": "Exterior Floor",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 68,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
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
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_2"
        },
        "floor_zn_3": {
            "construction_name": "Exterior Floor",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 74,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
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
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_3"
        },
        "floor_zn_4": {
            "construction_name": "Exterior Floor",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 80,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
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
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_4"
        },
        "floor_zn_5": {
            "construction_name": "Exterior Floor",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 86,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
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
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_5"
        },
        "wall-0_corr_0": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 94,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Adiabatic",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        },
        "wall-0_zn_0": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 58,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-2_zn_2",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_0"
        },
        "wall-0_zn_1": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 64,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-2_zn_3",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_1"
        },
        "wall-0_zn_2": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 70,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-2_zn_4",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_2"
        },
        "wall-0_zn_3": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 76,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-2_zn_5",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_3"
        },
        "wall-0_zn_4": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 82,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_4"
        },
        "wall-0_zn_5": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 88,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_5"
        },
        "wall-1_zn_0": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 59,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-corr_zn_0",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_0"
        },
        "wall-1_zn_1": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 65,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_1"
        },
        "wall-1_zn_2": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 71,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-corr_zn_2",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_2"
        },
        "wall-1_zn_3": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 77,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_3"
        },
        "wall-1_zn_4": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 83,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-corr_zn_4",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_4"
        },
        "wall-1_zn_5": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 89,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_5"
        },
        "wall-2_corr_0": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 95,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Adiabatic",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        },
        "wall-2_zn_0": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 60,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_0"
        },
        "wall-2_zn_1": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 66,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_1"
        },
        "wall-2_zn_2": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 72,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-0_zn_0",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_2"
        },
        "wall-2_zn_3": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 78,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-0_zn_1",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_3"
        },
        "wall-2_zn_4": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 84,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-0_zn_2",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_4"
        },
        "wall-2_zn_5": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 90,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-0_zn_3",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 4.03350325015,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_5"
        },
        "wall-3_zn_0": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 61,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
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
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_0"
        },
        "wall-3_zn_1": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 67,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-corr_zn_1",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
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
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_1"
        },
        "wall-3_zn_2": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 73,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
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
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_2"
        },
        "wall-3_zn_3": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 79,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-corr_zn_3",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
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
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_3"
        },
        "wall-3_zn_4": {
            "construction_name": "Exterior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 85,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
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
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "WindExposed",
            "zone_name": "zone_4"
        },
        "wall-3_zn_5": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 91,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-corr_zn_5",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
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
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "zone_5"
        },
        "wall-corr_zn_0": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 96,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-1_zn_0",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
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
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        },
        "wall-corr_zn_1": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 97,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-3_zn_1",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        },
        "wall-corr_zn_2": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 98,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-1_zn_2",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 8.27178156142,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 8.27178156142,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        },
        "wall-corr_zn_3": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 99,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-3_zn_3",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 4.13589078071,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 8.27178156142,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 8.27178156142,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        },
        "wall-corr_zn_4": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 100,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-1_zn_4",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 8.27178156142,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 8.27178156142,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        },
        "wall-corr_zn_5": {
            "construction_name": "Interior Wall",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 101,
            "number_of_vertices": 4.0,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "wall-3_zn_5",
            "sun_exposure": "NoSun",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 8.27178156142,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 8.27178156142,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 2.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                }
            ],
            "wind_exposure": "NoWind",
            "zone_name": "corridor_0"
        }
    },


        "glass_construction_zone_0": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "idf_order": 49,
            "outside_layer": "glass_material_zone_0"
        },
        "glass_construction_zone_1": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "idf_order": 50,
            "outside_layer": "glass_material_zone_1"
        },
        "glass_construction_zone_2": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "idf_order": 51,
            "outside_layer": "glass_material_zone_2"
        },
        "glass_construction_zone_3": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "idf_order": 52,
            "outside_layer": "glass_material_zone_3"
        },
        "glass_construction_zone_4": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "idf_order": 53,
            "outside_layer": "glass_material_zone_4"
        },
        "glass_construction_zone_5": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "idf_order": 54,
            "outside_layer": "glass_material_zone_5"
        }
        
        "equip_zone_0": {
            "design_level_calculation_method": "Watts/Area",
            "end_use_subcategory": "General",
            "fraction_latent": 0.0,
            "fraction_lost": 0.0,
            "fraction_radiant": 0.5,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 137,
            "schedule_name": "Sch_Equip_Computador",
            "watts_per_zone_floor_area": 3.63317358398,
            "zone_or_zonelist_name": "zone_0"
        },
        "equip_zone_1": {
            "design_level_calculation_method": "Watts/Area",
            "end_use_subcategory": "General",
            "fraction_latent": 0.0,
            "fraction_lost": 0.0,
            "fraction_radiant": 0.5,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 138,
            "schedule_name": "Sch_Equip_Computador",
            "watts_per_zone_floor_area": 3.63317358398,
            "zone_or_zonelist_name": "zone_1"
        },
        "equip_zone_2": {
            "design_level_calculation_method": "Watts/Area",
            "end_use_subcategory": "General",
            "fraction_latent": 0.0,
            "fraction_lost": 0.0,
            "fraction_radiant": 0.5,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 139,
            "schedule_name": "Sch_Equip_Computador",
            "watts_per_zone_floor_area": 3.63317358398,
            "zone_or_zonelist_name": "zone_2"
        },
        "equip_zone_3": {
            "design_level_calculation_method": "Watts/Area",
            "end_use_subcategory": "General",
            "fraction_latent": 0.0,
            "fraction_lost": 0.0,
            "fraction_radiant": 0.5,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 140,
            "schedule_name": "Sch_Equip_Computador",
            "watts_per_zone_floor_area": 2.11566381836,
            "zone_or_zonelist_name": "zone_3"
        },
        "equip_zone_4": {
            "design_level_calculation_method": "Watts/Area",
            "end_use_subcategory": "General",
            "fraction_latent": 0.0,
            "fraction_lost": 0.0,
            "fraction_radiant": 0.5,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 141,
            "schedule_name": "Sch_Equip_Computador",
            "watts_per_zone_floor_area": 3.63317358398,
            "zone_or_zonelist_name": "zone_4"
        },
        "equip_zone_5": {
            "design_level_calculation_method": "Watts/Area",
            "end_use_subcategory": "General",
            "fraction_latent": 0.0,
            "fraction_lost": 0.0,
            "fraction_radiant": 0.5,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 142,
            "schedule_name": "Sch_Equip_Computador",
            "watts_per_zone_floor_area": 2.11566381836,
            "zone_or_zonelist_name": "zone_5"
        },

    "FenestrationSurface:Detailed": {
        "door-corr_zn_0": {
            "building_surface_name": "wall-corr_zn_0",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 116,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door_zn_0",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 3.63589078071,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 3.63589078071,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 2.73589078071,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 2.73589078071,
            "vertex_4_z_coordinate": 2.1
        },
        "door-corr_zn_1": {
            "building_surface_name": "wall-corr_zn_1",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 117,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door_zn_1",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 2.0,
            "vertex_1_y_coordinate": 2.73589078071,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 2.0,
            "vertex_2_y_coordinate": 2.73589078071,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 2.0,
            "vertex_3_y_coordinate": 3.63589078071,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 2.0,
            "vertex_4_y_coordinate": 3.63589078071,
            "vertex_4_z_coordinate": 2.1
        },
        "door-corr_zn_2": {
            "building_surface_name": "wall-corr_zn_2",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 118,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door_zn_2",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 7.77178156142,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 7.77178156142,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 6.87178156142,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 6.87178156142,
            "vertex_4_z_coordinate": 2.1
        },
        "door-corr_zn_3": {
            "building_surface_name": "wall-corr_zn_3",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 119,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door_zn_3",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 2.0,
            "vertex_1_y_coordinate": 6.87178156142,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 2.0,
            "vertex_2_y_coordinate": 6.87178156142,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 2.0,
            "vertex_3_y_coordinate": 7.77178156142,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 2.0,
            "vertex_4_y_coordinate": 7.77178156142,
            "vertex_4_z_coordinate": 2.1
        },
        "door-corr_zn_4": {
            "building_surface_name": "wall-corr_zn_4",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 120,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door_zn_4",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 11.9076723421,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 11.9076723421,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 11.0076723421,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 11.0076723421,
            "vertex_4_z_coordinate": 2.1
        },
        "door-corr_zn_5": {
            "building_surface_name": "wall-corr_zn_5",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 121,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door_zn_5",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 2.0,
            "vertex_1_y_coordinate": 11.0076723421,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 2.0,
            "vertex_2_y_coordinate": 11.0076723421,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 2.0,
            "vertex_3_y_coordinate": 11.9076723421,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 2.0,
            "vertex_4_y_coordinate": 11.9076723421,
            "vertex_4_z_coordinate": 2.1
        },
        "door_zn_0": {
            "building_surface_name": "wall-1_zn_0",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 103,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door-corr_zn_0",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 4.03350325015,
            "vertex_1_y_coordinate": 2.73589078071,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 4.03350325015,
            "vertex_2_y_coordinate": 2.73589078071,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 4.03350325015,
            "vertex_3_y_coordinate": 3.63589078071,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 4.03350325015,
            "vertex_4_y_coordinate": 3.63589078071,
            "vertex_4_z_coordinate": 2.1
        },
        "door_zn_1": {
            "building_surface_name": "wall-3_zn_1",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 106,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door-corr_zn_1",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 3.63589078071,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 3.63589078071,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 2.73589078071,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 2.73589078071,
            "vertex_4_z_coordinate": 2.1
        },
        "door_zn_2": {
            "building_surface_name": "wall-1_zn_2",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 108,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door-corr_zn_2",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 4.03350325015,
            "vertex_1_y_coordinate": 2.73589078071,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 4.03350325015,
            "vertex_2_y_coordinate": 2.73589078071,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 4.03350325015,
            "vertex_3_y_coordinate": 3.63589078071,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 4.03350325015,
            "vertex_4_y_coordinate": 3.63589078071,
            "vertex_4_z_coordinate": 2.1
        },
        "door_zn_3": {
            "building_surface_name": "wall-3_zn_3",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 110,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door-corr_zn_3",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 3.63589078071,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 3.63589078071,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 2.73589078071,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 2.73589078071,
            "vertex_4_z_coordinate": 2.1
        },
        "door_zn_4": {
            "building_surface_name": "wall-1_zn_4",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 113,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door-corr_zn_4",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 4.03350325015,
            "vertex_1_y_coordinate": 2.73589078071,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 4.03350325015,
            "vertex_2_y_coordinate": 2.73589078071,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 4.03350325015,
            "vertex_3_y_coordinate": 3.63589078071,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 4.03350325015,
            "vertex_4_y_coordinate": 3.63589078071,
            "vertex_4_z_coordinate": 2.1
        },
        "door_zn_5": {
            "building_surface_name": "wall-3_zn_5",
            "construction_name": "Interior Door",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 115,
            "number_of_vertices": 4.0,
            "outside_boundary_condition_object": "door-corr_zn_5",
            "surface_type": "Door",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 3.63589078071,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 3.63589078071,
            "vertex_2_z_coordinate": 0.0,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 2.73589078071,
            "vertex_3_z_coordinate": 0.0,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 2.73589078071,
            "vertex_4_z_coordinate": 2.1
        },
        "window-0_zn_4": {
            "building_surface_name": "wall-0_zn_4",
            "construction_name": "glass_construction_zone_4",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 111,
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 4.0294697469,
            "vertex_1_y_coordinate": 4.13589078071,
            "vertex_1_z_coordinate": 1.52779364079,
            "vertex_2_x_coordinate": 4.0294697469,
            "vertex_2_y_coordinate": 4.13589078071,
            "vertex_2_z_coordinate": 0.971669249833,
            "vertex_3_x_coordinate": 0.00403350325015,
            "vertex_3_y_coordinate": 4.13589078071,
            "vertex_3_z_coordinate": 0.971669249833,
            "vertex_4_x_coordinate": 0.00403350325015,
            "vertex_4_y_coordinate": 4.13589078071,
            "vertex_4_z_coordinate": 1.52779364079
        },
        "window-0_zn_5": {
            "building_surface_name": "wall-0_zn_5",
            "construction_name": "glass_construction_zone_5",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 114,
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 4.0294697469,
            "vertex_1_y_coordinate": 4.13589078071,
            "vertex_1_z_coordinate": 1.62079123467,
            "vertex_2_x_coordinate": 4.0294697469,
            "vertex_2_y_coordinate": 4.13589078071,
            "vertex_2_z_coordinate": 0.878671655953,
            "vertex_3_x_coordinate": 0.00403350325015,
            "vertex_3_y_coordinate": 4.13589078071,
            "vertex_3_z_coordinate": 0.878671655953,
            "vertex_4_x_coordinate": 0.00403350325015,
            "vertex_4_y_coordinate": 4.13589078071,
            "vertex_4_z_coordinate": 1.62079123467
        },
        "window-1_zn_1": {
            "building_surface_name": "wall-1_zn_1",
            "construction_name": "glass_construction_zone_1",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 104,
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 4.03350325015,
            "vertex_1_y_coordinate": 0.00413589078071,
            "vertex_1_z_coordinate": 1.62079123467,
            "vertex_2_x_coordinate": 4.03350325015,
            "vertex_2_y_coordinate": 0.00413589078071,
            "vertex_2_z_coordinate": 0.878671655953,
            "vertex_3_x_coordinate": 4.03350325015,
            "vertex_3_y_coordinate": 4.13175488993,
            "vertex_3_z_coordinate": 0.878671655953,
            "vertex_4_x_coordinate": 4.03350325015,
            "vertex_4_y_coordinate": 4.13175488993,
            "vertex_4_z_coordinate": 1.62079123467
        },
        "window-1_zn_3": {
            "building_surface_name": "wall-1_zn_3",
            "construction_name": "glass_construction_zone_3",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 109,
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 4.03350325015,
            "vertex_1_y_coordinate": 0.00413589078071,
            "vertex_1_z_coordinate": 1.52779364079,
            "vertex_2_x_coordinate": 4.03350325015,
            "vertex_2_y_coordinate": 0.00413589078071,
            "vertex_2_z_coordinate": 0.971669249833,
            "vertex_3_x_coordinate": 4.03350325015,
            "vertex_3_y_coordinate": 4.13175488993,
            "vertex_3_z_coordinate": 0.971669249833,
            "vertex_4_x_coordinate": 4.03350325015,
            "vertex_4_y_coordinate": 4.13175488993,
            "vertex_4_z_coordinate": 1.52779364079
        },
        "window-2_zn_1": {
            "building_surface_name": "wall-2_zn_1",
            "construction_name": "glass_construction_zone_1",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 105,
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 0.00403350325015,
            "vertex_1_y_coordinate": 0.0,
            "vertex_1_z_coordinate": 1.62079123467,
            "vertex_2_x_coordinate": 0.00403350325015,
            "vertex_2_y_coordinate": 0.0,
            "vertex_2_z_coordinate": 0.878671655953,
            "vertex_3_x_coordinate": 4.0294697469,
            "vertex_3_y_coordinate": 0.0,
            "vertex_3_z_coordinate": 0.878671655953,
            "vertex_4_x_coordinate": 4.0294697469,
            "vertex_4_y_coordinate": 0.0,
            "vertex_4_z_coordinate": 1.62079123467
        },
        "window-3_zn_0": {
            "building_surface_name": "wall-3_zn_0",
            "construction_name": "glass_construction_zone_0",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 102,
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 4.13175488993,
            "vertex_1_z_coordinate": 1.52779364079,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 4.13175488993,
            "vertex_2_z_coordinate": 0.971669249833,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 0.00413589078071,
            "vertex_3_z_coordinate": 0.971669249833,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 0.00413589078071,
            "vertex_4_z_coordinate": 1.52779364079
        },
        "window-3_zn_2": {
            "building_surface_name": "wall-3_zn_2",
            "construction_name": "glass_construction_zone_2",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 107,
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 4.13175488993,
            "vertex_1_z_coordinate": 1.52779364079,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 4.13175488993,
            "vertex_2_z_coordinate": 0.971669249833,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 0.00413589078071,
            "vertex_3_z_coordinate": 0.971669249833,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 0.00413589078071,
            "vertex_4_z_coordinate": 1.52779364079
        },
        "window-3_zn_4": {
            "building_surface_name": "wall-3_zn_4",
            "construction_name": "glass_construction_zone_4",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22,
            "idf_order": 112,
            "number_of_vertices": 4.0,
            "surface_type": "Window",
            "vertex_1_x_coordinate": 0.0,
            "vertex_1_y_coordinate": 4.13175488993,
            "vertex_1_z_coordinate": 1.52779364079,
            "vertex_2_x_coordinate": 0.0,
            "vertex_2_y_coordinate": 4.13175488993,
            "vertex_2_z_coordinate": 0.971669249833,
            "vertex_3_x_coordinate": 0.0,
            "vertex_3_y_coordinate": 0.00413589078071,
            "vertex_3_z_coordinate": 0.971669249833,
            "vertex_4_x_coordinate": 0.0,
            "vertex_4_y_coordinate": 0.00413589078071,
            "vertex_4_z_coordinate": 1.52779364079
        }
    },

    "Lights": {
        "lights_zone_0": {
            "design_level_calculation_method": "Watts/Area",
            "fraction_radiant": 0.72,
            "fraction_replaceable": 1.0,
            "fraction_visible": 0.18,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 149,
            "return_air_fraction": 0.0,
            "schedule_name": "Sch_Iluminacao",
            "watts_per_zone_floor_area": 5.81824951172,
            "zone_or_zonelist_name": "zone_0"
        },
        "lights_zone_1": {
            "design_level_calculation_method": "Watts/Area",
            "fraction_radiant": 0.72,
            "fraction_replaceable": 1.0,
            "fraction_visible": 0.18,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 150,
            "return_air_fraction": 0.0,
            "schedule_name": "Sch_Iluminacao",
            "watts_per_zone_floor_area": 5.81824951172,
            "zone_or_zonelist_name": "zone_1"
        },
        "lights_zone_2": {
            "design_level_calculation_method": "Watts/Area",
            "fraction_radiant": 0.72,
            "fraction_replaceable": 1.0,
            "fraction_visible": 0.18,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 151,
            "return_air_fraction": 0.0,
            "schedule_name": "Sch_Iluminacao",
            "watts_per_zone_floor_area": 5.81824951172,
            "zone_or_zonelist_name": "zone_2"
        },
        "lights_zone_3": {
            "design_level_calculation_method": "Watts/Area",
            "fraction_radiant": 0.72,
            "fraction_replaceable": 1.0,
            "fraction_visible": 0.18,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 152,
            "return_air_fraction": 0.0,
            "schedule_name": "Sch_Iluminacao",
            "watts_per_zone_floor_area": 3.38807373047,
            "zone_or_zonelist_name": "zone_3"
        },
        "lights_zone_4": {
            "design_level_calculation_method": "Watts/Area",
            "fraction_radiant": 0.72,
            "fraction_replaceable": 1.0,
            "fraction_visible": 0.18,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 153,
            "return_air_fraction": 0.0,
            "schedule_name": "Sch_Iluminacao",
            "watts_per_zone_floor_area": 5.81824951172,
            "zone_or_zonelist_name": "zone_4"
        },
        "lights_zone_5": {
            "design_level_calculation_method": "Watts/Area",
            "fraction_radiant": 0.72,
            "fraction_replaceable": 1.0,
            "fraction_visible": 0.18,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 11,
            "idf_order": 154,
            "return_air_fraction": 0.0,
            "schedule_name": "Sch_Iluminacao",
            "watts_per_zone_floor_area": 3.38807373047,
            "zone_or_zonelist_name": "zone_5"
        }
    },

        "ArgamassaReboco(25mm)": {
            "conductivity": 0.204948913908,
            "density": 2000.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "idf_order": 24,
            "roughness": "Rough",
            "solar_absorptance": 0.40478515625,
            "specific_heat": 1000.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.025,
            "visible_absorptance": 0.40478515625
        },
        "Ceram Tij 8 fur circ (10 cm)": {
            "conductivity": 0.160394802189,
            "density": 1103.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "idf_order": 26,
            "roughness": "Rough",
            "specific_heat": 920.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.033
        },

        "TelhaCeramica": {
            "conductivity": 1.05,
            "density": 2000.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "idf_order": 25,
            "roughness": "Rough",
            "solar_absorptance": 0.40478515625,
            "specific_heat": 920.0,
            "thermal_absorptance": 0.9,
            "thickness": 0.01,
            "visible_absorptance": 0.40478515625
        },

        "CavidadeBloco:CamaradeAr(20-50mm)": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 2,
            "idf_order": 31,
            "thermal_resistance": 0.897784707862
        },

    "People": {
        "people_zone_0": {
            "activity_level_schedule_name": "Sch_Atividade",
            "fraction_radiant": 0.3,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 10,
            "idf_order": 143,
            "number_of_people_calculation_method": "People/Area",
            "number_of_people_schedule_name": "Sch_Ocupacao",
            "people_per_zone_floor_area": 0.254135392253,
            "sensible_heat_fraction": "Autocalculate",
            "zone_or_zonelist_name": "zone_0"
        },
        "people_zone_1": {
            "activity_level_schedule_name": "Sch_Atividade",
            "fraction_radiant": 0.3,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 10,
            "idf_order": 144,
            "number_of_people_calculation_method": "People/Area",
            "number_of_people_schedule_name": "Sch_Ocupacao",
            "people_per_zone_floor_area": 0.254135392253,
            "sensible_heat_fraction": "Autocalculate",
            "zone_or_zonelist_name": "zone_1"
        },
        "people_zone_2": {
            "activity_level_schedule_name": "Sch_Atividade",
            "fraction_radiant": 0.3,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 10,
            "idf_order": 145,
            "number_of_people_calculation_method": "People/Area",
            "number_of_people_schedule_name": "Sch_Ocupacao",
            "people_per_zone_floor_area": 0.254135392253,
            "sensible_heat_fraction": "Autocalculate",
            "zone_or_zonelist_name": "zone_2"
        },
        "people_zone_3": {
            "activity_level_schedule_name": "Sch_Atividade",
            "fraction_radiant": 0.3,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 10,
            "idf_order": 146,
            "number_of_people_calculation_method": "People/Area",
            "number_of_people_schedule_name": "Sch_Ocupacao",
            "people_per_zone_floor_area": 0.147987714301,
            "sensible_heat_fraction": "Autocalculate",
            "zone_or_zonelist_name": "zone_3"
        },
        "people_zone_4": {
            "activity_level_schedule_name": "Sch_Atividade",
            "fraction_radiant": 0.3,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 10,
            "idf_order": 147,
            "number_of_people_calculation_method": "People/Area",
            "number_of_people_schedule_name": "Sch_Ocupacao",
            "people_per_zone_floor_area": 0.254135392253,
            "sensible_heat_fraction": "Autocalculate",
            "zone_or_zonelist_name": "zone_4"
        },
        "people_zone_5": {
            "activity_level_schedule_name": "Sch_Atividade",
            "fraction_radiant": 0.3,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 10,
            "idf_order": 148,
            "number_of_people_calculation_method": "People/Area",
            "number_of_people_schedule_name": "Sch_Ocupacao",
            "people_per_zone_floor_area": 0.147987714301,
            "sensible_heat_fraction": "Autocalculate",
            "zone_or_zonelist_name": "zone_5"
        }
    },
    "Shading:Building:Detailed": {
        "shading-0_0": {
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 15,
            "idf_order": 132,
            "number_of_vertices": 4.0,
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 12.7743715609,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 10.0670065003,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 10.0670065003,
                    "vertex_y_coordinate": 12.7743715609,
                    "vertex_z_coordinate": 2.49946289062
                }
            ]
        },
        "shading-1_0": {
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 15,
            "idf_order": 133,
            "number_of_vertices": 4.0,
            "vertices": [
                {
                    "vertex_x_coordinate": 10.4337057191,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 10.0670065003,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 10.0670065003,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 10.4337057191,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                }
            ]
        },
        "shading-2_0": {
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 15,
            "idf_order": 134,
            "number_of_vertices": 4.0,
            "vertices": [
                {
                    "vertex_x_coordinate": 10.0670065003,
                    "vertex_y_coordinate": -0.36669921875,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 10.0670065003,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": -0.36669921875,
                    "vertex_z_coordinate": 2.49946289062
                }
            ]
        },
        "shading-3_0": {
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 15,
            "idf_order": 135,
            "number_of_vertices": 4.0,
            "vertices": [
                {
                    "vertex_x_coordinate": -0.36669921875,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                },
                {
                    "vertex_x_coordinate": -0.36669921875,
                    "vertex_y_coordinate": 12.4076723421,
                    "vertex_z_coordinate": 2.49946289062
                }
            ]
        }
    },
    "Site:GroundTemperature:BuildingSurface":
    
        "glass_material_zone_0": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 3,
            "idf_order": 33,
            "solar_heat_gain_coefficient": 0.684505615234,
            "u_factor": 5.7
        },
        "glass_material_zone_1": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 3,
            "idf_order": 34,
            "solar_heat_gain_coefficient": 0.684505615234,
            "u_factor": 5.7
        },
        "glass_material_zone_2": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 3,
            "idf_order": 35,
            "solar_heat_gain_coefficient": 0.684505615234,
            "u_factor": 5.7
        },
        "glass_material_zone_3": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 3,
            "idf_order": 36,
            "solar_heat_gain_coefficient": 0.684505615234,
            "u_factor": 5.7
        },
        "glass_material_zone_4": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 3,
            "idf_order": 37,
            "solar_heat_gain_coefficient": 0.829041748047,
            "u_factor": 5.7
        },
        "glass_material_zone_5": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 3,
            "idf_order": 38,
            "solar_heat_gain_coefficient": 0.829041748047,
            "u_factor": 5.7
        }
    },
    "Zone": {
        "corridor_0": {
            "direction_of_relative_north": 0.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "idf_order": 128,
            "multiplier": 1,
            "x_origin": 4.03350325015,
            "y_origin": 0.0,
            "z_origin": 0.0
        },
        "zone_0": {
            "direction_of_relative_north": 0.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "idf_order": 122,
            "multiplier": 1,
            "x_origin": 0.0,
            "y_origin": 0.0,
            "z_origin": 0.0
        },
        "zone_1": {
            "direction_of_relative_north": 0.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "idf_order": 123,
            "multiplier": 1,
            "x_origin": 6.03350325015,
            "y_origin": 0.0,
            "z_origin": 0.0
        },
        "zone_2": {
            "direction_of_relative_north": 0.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "idf_order": 124,
            "multiplier": 1,
            "x_origin": 0.0,
            "y_origin": 4.13589078071,
            "z_origin": 0.0
        },
        "zone_3": {
            "direction_of_relative_north": 0.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "idf_order": 125,
            "multiplier": 1,
            "x_origin": 6.03350325015,
            "y_origin": 4.13589078071,
            "z_origin": 0.0
        },
        "zone_4": {
            "direction_of_relative_north": 0.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "idf_order": 126,
            "multiplier": 1,
            "x_origin": 0.0,
            "y_origin": 8.27178156142,
            "z_origin": 0.0
        },
        "zone_5": {
            "direction_of_relative_north": 0.0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 7,
            "idf_order": 127,
            "multiplier": 1,
            "x_origin": 6.03350325015,
            "y_origin": 8.27178156142,
            "z_origin": 0.0
        }
    },
    "ZoneList": {
        "All": {
            "idf_max_extensible_fields": 7,
            "idf_max_fields": 8,
            "idf_order": 130,
            "zones": [
                {
                    "zone_name": "zone_0"
                },
                {
                    "zone_name": "zone_1"
                },
                {
                    "zone_name": "zone_2"
                },
                {
                    "zone_name": "zone_3"
                },
                {
                    "zone_name": "zone_4"
                },
                {
                    "zone_name": "zone_5"
                },
                {
                    "zone_name": "corridor_0"
                }
            ]
        },
        "Corridors": {
            "idf_max_extensible_fields": 1,
            "idf_max_fields": 2,
            "idf_order": 131,
            "zones": [
                {
                    "zone_name": "corridor_0"
                }
            ]
        },
        "Offices": {
            "idf_max_extensible_fields": 6,
            "idf_max_fields": 7,
            "idf_order": 129,
            "zones": [
                {
                    "zone_name": "zone_0"
                },
                {
                    "zone_name": "zone_1"
                },
                {
                    "zone_name": "zone_2"
                },
                {
                    "zone_name": "zone_3"
                },
                {
                    "zone_name": "zone_4"
                },
                {
                    "zone_name": "zone_5"
                }
            ]
        }
    }
'''