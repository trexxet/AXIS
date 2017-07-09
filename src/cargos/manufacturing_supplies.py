from cargo import Cargo

cargo = Cargo(id = 'manufacturing_supplies',
              type_name = 'string(STR_CARGO_NAME_MANUFACTURING_SUPPLIES)',
              unit_name = 'string(STR_CARGO_NAME_MANUFACTURING_SUPPLIES)',
              type_abbreviation = 'string(STR_CID_MANUFACTURING_SUPPLIES)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '0.65',
              cargo_payment_list_colour = '145',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_EXPRESS, CC_PIECE_GOODS)',
              cargo_label = 'MNSP',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '84',
              items_of_cargo = 'string(STR_CARGO_UNIT_MNSP)',
              penalty_lowerbound = '8',
              single_penalty_length = '60',
              price_factor = '134.506702423',
              capacity_multiplier = '1',
              icon_indices = (7, 1))
