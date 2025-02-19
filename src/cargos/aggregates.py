from cargo import Cargo

cargo = Cargo(
    id="aggregates",
    type_name="string(STR_CARGO_NAME_AGGREGATES)",
    unit_name="string(STR_CARGO_NAME_AGGREGATES)",
    type_abbreviation="string(STR_CID_AGGREGATES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK)",
    cargo_label="GRVL",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_AGGREGATES)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=91,
    capacity_multiplier="1",
    icon_indices=(5, 1),
    sprites_complete=True,
)
