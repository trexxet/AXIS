from cargo import Cargo

cargo = Cargo(
    id="sulphur",
    type_name="string(STR_CARGO_NAME_SULPHUR)",
    unit_name="string(STR_CARGO_NAME_SULPHUR)",
    type_abbreviation="string(STR_CID_SULPHUR)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_LIQUID, CC_COVERED)",
    cargo_label="SULP",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SULPHUR)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=105,
    capacity_multiplier="1",
    icon_indices=(13, 3),
    sprites_complete=True,
)
