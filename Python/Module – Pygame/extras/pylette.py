# A color palette made for pygame. May be used elsewhere too.
# Based on Wikipedia's list of colors (by shade)
# All colors of every shade arranged by brightness, then least saturation (hsv).

# This project is currently paused due to RGB vs sRGB namespace issues.
# pylette_web has taken its place.

import colorsys as cs

# Shades of Black
shades_black = {  # May be removed.
    'midnight_blue': midnight_blue,
    'dim_gray': dim_gray,
}
dim_gray = (105, 105, 105)
ebony = (85, 93, 80)
taupe = (72, 60, 50)
davys_gray = (85, 85, 85)  # Also Davy's Gray
charcoal = (54, 69, 79)
outer_space = (65, 74, 76)
cafe_noire = (75, 54, 33)
black_bean = (61, 12, 2)
black_olive = (59, 60, 54)
onyx = (53, 56, 57)
jet = (52, 52, 52)  # Also Jet Black
black_leather = (37, 53, 41)  # Also Black Leather Jacket
raisin_black = (36, 33, 36)
charleston_green = (35, 43, 43)
eerie_black = (27, 27, 27)
licorice = (26, 17, 16)
black = (0, 0, 0)

# Shades of Blue
shades_blue = {
    'periwinkle': periwinkle,
    'ice_blue': ice_blue,
    'neon_blue': neon_blue,
    'blue': blue,
    'ultramarine': ultramarine,
    'uranian_blue': uranian_blue,
    'florescent_blue': florescent_blue,
    'baby_blue': baby_blue,
    'argentinian_blue': argentinian_blue,
    'bleu_de_france': bleu_de_france,
    'powder_blue': powder_blue,
    'light_blue': light_blue,
    'ruddy_blue': ruddy_blue,
    'savoy_blue': savoy_blue,
    'medium_blue': medium_blue,
    'blue_ncs': blue_ncs,
    'spanish_blue': spanish_blue,
    'munsell_blue': munsell_blue,
    'pantone_blue': pantone_blue,
    'liberty': liberty,
    'egyptian_blue': egyptian_blue,
    'morning_blue': morning_blue,
    'polynesian_blue': polynesian_blue,
    'picotee_blue': picotee_blue,
    'duck_blue': duck_blue,
    'dark_blue': dark_blue,
    'teal_blue': teal_blue,
    'resolution_blue': resolution_blue,
    'teal': teal,
    'navy_blue': navy_blue,
    'midnight_blue': midnight_blue,
    'sapphire': sapphire,
    'delft_blue': delft_blue,
    'penn_blue': penn_blue,
    'space_cadet': space_cadet
}
periwinkle = (204, 204, 255)
ice_blue = (153, 255, 255)
neon_blue = (77, 77, 255)
crayola_blue = (31, 117, 254)
blue = (0, 0, 255)
ultramarine = (64, 0, 255)
uranian_blue = (175, 216, 245)
florescent_blue = (21, 244, 238)
baby_blue = (137, 207, 240)
argentinian_blue = (108, 180, 238)
bleu_de_france = (49, 140, 231)
powder_blue = (176, 224, 230)
light_blue = (173, 216, 230)
ruddy_blue = (118, 171, 223)  # From the beak of a ruddy duck
savoy_blue = (75, 97, 209)  # Also Italian Blue
medium_blue = (0, 0, 205)
blue_ncs = (0, 135, 189)  # Also Psychological Primary Blue
spanish_blue = (0, 112, 184)  # Also known as the spanish "azul"
munsell_blue = (0, 147, 175)
pantone_blue = (0, 24, 168)
liberty = (84, 90, 167)
egyptian_blue = (16, 52, 166)
morning_blue = (141, 163, 153)
polynesian_blue = (34, 76, 152)
picotee_blue = (146, 39, 135)  # From the picotee flower
duck_blue = (0, 119, 145)
dark_blue = (0, 0, 139)
teal_blue = (54, 117, 136)
resolution_blue = (0, 35, 135)
teal = (0, 128, 128)  # From the neck coloring of a duck named the common teal.
navy_blue = (0, 0, 128)
midnight_blue = (25, 25, 112)
independence = (76, 81, 109)
sapphire = (8, 37, 103)
delft_blue = (31, 48, 94)
penn_blue = (1, 31, 91)  # Also Penn University Blue
space_cadet = (30, 41, 82)


oxford_blue = (0, 33, 71)
bistre = (61, 43, 31)
eigengrau = (22, 22, 29)  # Meaning Intrinsic Gray (German)

# Shades of Brown
shades_brown = {
    'beige': beige,
    'buff': buff,
    'desert_sand': desert_sand,
    'cocoa_brown': cocoa_brown,
    'khaki': khaki,
    'red_brown': red_brown,
    'beaver': beaver,
    'chestnut': chestnut,
    'burnt_umber': burnt_umber,
    'chocolate': chocolate,
    'dark_brown': dark_brown
}
beige = (245, 245, 220)
buff = (240, 220, 130)  # From the color of buffed leather
desert_sand = (237, 201, 175)
cocoa_brown = (210, 105, 30)
khaki = (195, 176, 145)
red_brown = (165, 42, 42)
beaver = (159, 129, 112)
chestnut = (149, 69, 53)
burnt_umber = (138, 51, 36)
chocolate = (123, 63, 0)
dark_brown = (92, 64, 50)


# Brightness of color: μ = (R + G + B) / 3
def brightness(colors, mode='a'):
    r, g, b = colors  # unpacking tuple
    if mode.casefold() in ['a', 'arith', 'arithmetic', 'arithmetic mean']:
        return round((r + g + b) / 3, 1)
    elif mode.casefold() in ['g', 'geo', 'geometric', 'geometric mean']:
        return round((r * g * b) ** (1 / 3), 1)


for key, value in shades_brown.items():
    r, g, b = value
    r /= 255
    g /= 255
    b /= 255
    h, s, v = cs.rgb_to_hsv(r, g, b)
    print(key, value,  ":", round(v, 3), round(s, 3))
