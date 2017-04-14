from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='cement_plant',
                    processed_cargos_and_output_ratios=[('COAL', 2), ('CLAY', 2), ('GRVL', 4)],
                    combined_cargos_boost_prod=True,
                    prod_cargo_types=['BDMT'],
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    map_colour='19',
                    spec_flags='bitmask(IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE)',
                    name='string(STR_IND_CEMENT_PLANT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_ESTATE))',
                    fund_cost_multiplier='203')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].processed_cargos_and_output_ratios=[('PETR', 2), ('CLAY', 2), ('GRVL', 4)]

industry.add_tile(id='cement_plant_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type ='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    type ='empty',
)
spriteset_1 = industry.add_spriteset(
    sprites = [(80, 10, 64, 113, -31, -82)],
)
spriteset_2 = industry.add_spriteset(
    sprites = [(150, 10, 64, 113, -31, -82)],
)
spriteset_3 = industry.add_spriteset(
    sprites = [(220, 10, 64, 113, -31, -82)],
)
spriteset_4 = industry.add_spriteset(
    sprites = [(290, 10, 64, 113, -31, -82)],
)
spriteset_5 = industry.add_spriteset(
    sprites = [(220, 130, 64, 113, -31, -82), (290, 130, 64, 113, -31, -82), (360, 130, 64, 113, -31, -82), (430, 130, 64, 113, -31, -82),
               (500, 130, 64, 113, -31, -82), (570, 130, 64, 113, -31, -82), (640, 130, 64, 113, -31, -82)],
    animation_rate = 1,
)
spriteset_ground_5 = industry.add_spriteset(
    type ='concrete',
    num_sprites_to_autofill = len(spriteset_5.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_5 = industry.add_spriteset(
    type ='empty',
    num_sprites_to_autofill = len(spriteset_5.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_6 = industry.add_spriteset(
    sprites = [(430, 10, 64, 113, -31, -82)],
)
spriteset_7 = industry.add_spriteset(
    sprites = [(500, 10, 64, 113, -31, -82)],
)
spriteset_8 = industry.add_spriteset(
    sprites = [(570, 10, 64, 113, -31, -82)],
)
spriteset_9 = industry.add_spriteset(
    sprites = [(640, 10, 64, 113, -31, -82)],
)
spriteset_10 = industry.add_spriteset(
    sprites = [(710, 10, 64, 113, -31, -82)],
)
spriteset_11 = industry.add_spriteset(
    sprites = [(780, 10, 64, 113, -31, -82)],
)
spriteset_clay_staithe = industry.add_spriteset(
    sprites = [(80, 130, 64, 31, -31, 0)],
)
spriteset_stone_staithe = industry.add_spriteset(
    sprites = [(150, 130, 64, 31, -31, 0)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 0,
    yoffset= 0,
    zoffset= 81,
    animation_frame_offset = 1
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 3,
    yoffset= 0,
    zoffset= 81
)

industry.add_spritelayout(
    id = 'cement_plant_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_5',
    ground_sprite = spriteset_ground_5,
    ground_overlay = spriteset_ground_overlay_5,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_10',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_10],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_11',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_11],
    smoke_sprites = [sprite_smoke_2, sprite_smoke_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_clay_staithe',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_clay_staithe],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'cement_plant_spritelayout_stone_staithe',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_stone_staithe],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'cement_plant_industry_layout_1',
    layout = [(0, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_2'),
              (0, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_3'),
              (1, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_1'),
              (1, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (2, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (3, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (4, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_stone_staithe'),
              (4, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_11'),
              (4, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_8'),
              (4, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_7'),
              (5, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_clay_staithe'),
              (5, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_10'),
              (5, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_9'),
    ]
)
industry.add_industry_layout(
    id = 'cement_plant_industry_layout_2',
    layout = [(0, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_2'),
              (0, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_3'),
              (0, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_1'),
              (1, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (1, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (2, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (2, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (2, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_11'),
              (2, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_8'),
              (2, 4, 'cement_plant_tile_1', 'cement_plant_spritelayout_7'),
              (3, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (3, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (3, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_10'),
              (3, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_9'),
              (3, 4, 'cement_plant_tile_1', 'cement_plant_spritelayout_stone_staithe'),
    ]
)
industry.add_industry_layout(
    id = 'cement_plant_industry_layout_3',
    layout = [(0, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_2'),
              (0, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_3'),
              (0, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (0, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (0, 4, 'cement_plant_tile_1', 'cement_plant_spritelayout_stone_staithe'),
              (0, 5, 'cement_plant_tile_1', 'cement_plant_spritelayout_clay_staithe'),
              (1, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_2'),
              (1, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_3'),
              (1, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (1, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (1, 4, 'cement_plant_tile_1', 'cement_plant_spritelayout_11'),
              (1, 5, 'cement_plant_tile_1', 'cement_plant_spritelayout_8'),
              (1, 6, 'cement_plant_tile_1', 'cement_plant_spritelayout_7'),
              (2, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_1'),
              (2, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_1'),
              (2, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (2, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (2, 4, 'cement_plant_tile_1', 'cement_plant_spritelayout_10'),
              (2, 5, 'cement_plant_tile_1', 'cement_plant_spritelayout_9'),
    ]
)
industry.add_industry_layout(
    id = 'cement_plant_industry_layout_4',
    layout = [(0, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_2'),
              (0, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_3'),
              (0, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_2'),
              (0, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_3'),
              (1, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (1, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (1, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (1, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_1'),
              (2, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (2, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (2, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (3, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (3, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (3, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (4, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_stone_staithe'),
              (4, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_11'),
              (4, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_8'),
              (4, 3, 'cement_plant_tile_1', 'cement_plant_spritelayout_7'),
              (5, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_clay_staithe'),
              (5, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_10'),
              (5, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_9'),
    ]
)
industry.add_industry_layout(
    id = 'cement_plant_industry_layout_5',
    layout = [(0, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_1'),
              (0, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_1'),
              (1, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_2'),
              (1, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_3'),
              (2, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (2, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_6'),
              (3, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (3, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_5'),
              (4, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (4, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_4'),
              (4, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_stone_staithe'),
              (5, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_11'),
              (5, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_8'),
              (5, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_7'),
              (6, 0, 'cement_plant_tile_1', 'cement_plant_spritelayout_10'),
              (6, 1, 'cement_plant_tile_1', 'cement_plant_spritelayout_9'),
              (6, 2, 'cement_plant_tile_1', 'cement_plant_spritelayout_clay_staithe'),
    ]
)
