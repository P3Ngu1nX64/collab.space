# List of Web Colors (HTML Compatible) in RGB
# Reference: https://en.wikipedia.org/wiki/Web_colors
import colorsys


# Pink Colors:
Pink = (255, 192, 203)
LightPink = (255, 182, 193)
HotPink = (255, 105, 180)
DeepPink = (255, 20, 147)
PaleVioletRed = (219, 112, 147)
MediumVioletRed = (199, 21, 133)
list_pink = {
    "Pink": Pink,
    "LightPink": LightPink,
    "HotPink": HotPink,
    "DeepPink": DeepPink,
    "PaleVioletRed": PaleVioletRed,
    "MediumVioletRed": MediumVioletRed
}

# Red Colors:
LightSalmon = (255, 160, 122)
Salmon = (250, 128, 114)
DarkSalmon = (233, 150, 122)
LightCoral = (240, 128, 128)
IndianRed = (205, 92, 92)
Crimson = (220, 20, 60)
Firebrick = (178, 34, 34)
DarkRed = (139, 0, 0)
Red = (255, 0, 0)
list_red = {
    "LightSalmon": LightSalmon,
    "Salmon": Salmon,
    "DarkSalmon": DarkSalmon,
    "LightCoral": LightCoral,
    "IndianRed": IndianRed,
    "Crimson": Crimson,
    "Firebrick": Firebrick,
    "DarkRed": DarkRed,
    "Red": Red
}

# Orange Colors:
OrangeRed = (255, 69, 0)
Tomato = (255, 99, 71)
Coral = (255, 127, 80)
DarkOrange = (255, 140, 0)
Orange = (255, 165, 0)
list_orange = {
    "OrangeRed": Orange,
    "Tomato": Tomato,
    "Coral": Coral,
    "DarkOrange": DarkOrange,
    "Orange": Orange
}

# Yellow Colors:
Yellow = (255, 255, 0)
LightYellow = (255, 255, 224)
LemonChiffon = (255, 250, 205)
LightGoldenrodYellow = (250, 250, 210)
PapayaWhip = (255, 239, 213)
Moccasin = (255, 228, 181)
PeachPuff = (255, 218, 185)
PaleGoldenrod = (238, 232, 170)
Khaki = (240, 230, 140)
DarkKhaki = (189, 183, 107)
Gold = (255, 215, 0)
list_yellow = {
    "Yellow": Yellow,
    "LightYellow": LightYellow,
    "LemonChiffon": LemonChiffon,
    "LightGoldenrodYellow": LightGoldenrodYellow,
    'PapayaWhip': PapayaWhip,
    "Moccasin": Moccasin,
    "PeachPuff": PeachPuff,
    "PaleGoldenrod": PaleGoldenrod,
    "Khaki": Khaki,
    "DarkKhaki": DarkKhaki,
    "Gold": Gold
}

# Brown Colors:
Cornsilk = (255, 248, 220)
BlanchedAlmond = (255, 235, 205)
Bisque = (255, 228, 196)
NavajoWhite = (255, 222, 173)
Wheat = (245, 222, 179)
Burlywood = (222, 184, 135)
Tan = (210, 180, 140)
RosyBrown = (188, 143, 143)
SandyBrown = (244, 164, 96)
Goldenrod = (218, 165, 32)
DarkGoldenrod = (184, 134, 11)
Peru = (205, 133, 63)
Chocolate = (210, 105, 30)
SaddleBrown = (139, 69, 19)
Sienna = (160, 82, 45)
Brown = (165, 42, 42)
Maroon = (128, 0, 0)
list_brown = {
    "Cornsilk": Cornsilk,
    "BlanchedAlmond": BlanchedAlmond,
    "Bisque": Bisque,
    "NavajoWhite": NavajoWhite,
    "Wheat": Wheat,
    "Burlywood": Burlywood,
    "Tan": Tan,
    "RosyBrown": RosyBrown,
    "SandyBrown": SandyBrown,
    "Goldenrod": Goldenrod,
    "DarkGoldenrod": DarkGoldenrod,
    "Peru": Peru,
    "Chocolate": Chocolate,
    "SaddleBrown": SaddleBrown,
    "Sienna": Sienna,
    "Brown": Brown,
    "Maroon": Maroon,
}

# Green Colors:
DarkOliveGreen = (85, 107, 47)
Olive = (128, 128, 0)
OliveDrab = (107, 142, 35)
YellowGreen = (154, 205, 50)
LimeGreen = (50, 250, 50)
Lime = (0, 255, 0)
LawnGreen = (124, 252, 0)
Chartreuse = (127, 255, 0)
GreenYellow = (173, 255, 47)
SpringGreen = (0, 255, 127)
MediumSpringGreen = (0, 250, 154)
LightGreen = (144, 238, 144)
PaleGreen = (152, 251, 152)
DarkSeaGreen = (143, 188, 143)
MediumAquamarine = (102, 205, 170)
MediumSeaGreen = (60, 179, 113)
SeaGreen = (46, 139, 87)
ForestGreen = (34, 139, 34)
Green = (0, 128, 0)
DarkGreen = (0, 100, 0)
list_green = {
    "DarkOliveGreen": DarkOliveGreen,
    "Olive": Olive,
    "OliveDrab": OliveDrab,
    "YellowGreen": YellowGreen,
    "LimeGreen": LimeGreen,
    "Lime": Lime,
    "LawnGreen": LawnGreen,
    "Chartreuse": Chartreuse,
    "GreenYellow": Green,
    "SpringGreen": SpringGreen,
    "MediumSpringGreen": MediumSeaGreen,
    "LightGreen": LightGreen,
    "PaleGreen": PaleGreen,
    "DarkSeaGreen": DarkSeaGreen,
    "MediumAquamarine": MediumAquamarine,
    "MediumSeaGreen": MediumSeaGreen,
    "SeaGreen": SeaGreen,
    "ForestGreen": ForestGreen,
    "Green": Green,
    "DarkGreen": DarkGreen
}

# Cyan Colors:
Aqua = (0, 255, 255)
Cyan = (0, 255, 255)
LightCyan = (224, 255, 255)
PaleTurquoise = (175, 238, 238)
Aquamarine = (127, 255, 212)
Turquoise = (64, 224, 208)
MediumTurquoise = (72, 209, 204)
DarkTurquoise = (0, 206, 209)
LightSeaGreen = (32, 178, 170)
CadetBlue = (95, 158, 160)
DarkCyan = (0, 139, 139)
Teal = (0, 128, 128)
list_cyan = {
    "Aqua": Aqua,
    "Cyan": Cyan,
    "LightCyan": LightCyan,
    "PaleTurquoise": PaleTurquoise,
    "Aquamarine": Aquamarine,
    "Turquoise": Turquoise,
    "MediumTurquoise": MediumTurquoise,
    "DarkTurquoise": DarkTurquoise,
    "LightSeaGreen": LightSeaGreen,
    "CadetBlue": CadetBlue,
    "DarkCyan": DarkCyan,
    "Teal": Teal
}

# Blue Colors:
LightSteelBlue = (176, 196, 222)
PowderBlue = (176, 224, 230)
LightBlue = (173, 216, 230)
SkyBlue = (135, 206, 235)
LightSkyBlue = (135, 206, 250)
DeepSkyBlue = (0, 191, 255)
DodgerSkyBlue = (30, 144, 255)
DodgerBlue = (100, 149, 237)
CornflowerBlue = (100, 149, 237)
SteelBlue = (70, 130, 180)
RoyalBlue = (65, 105, 225)
Blue = (0, 0, 255)
MediumBlue = (0, 0, 205)
DarkBlue = (0, 0, 139)
Navy = (0, 0, 128)
MidnightBlue = (25, 25, 112)
list_blue = {
    "LightSteelBlue": LightBlue,
    "PowderBlue": PowderBlue,
    "LightBlue": LightBlue,
    "SkyBlue": SkyBlue,
    "LightSkyBlue": LightSkyBlue,
    "DeepSkyBlue": DeepSkyBlue,
    "DodgerSkyBlue": DodgerSkyBlue,
    "DodgerBlue": DodgerBlue,
    "CornflowerBlue": CornflowerBlue,
    "SteelBlue": SteelBlue,
    "RoyalBlue": RoyalBlue,
    "Blue": Blue,
    "MediumBlue": MediumBlue,
    "DarkBlue": DarkBlue,
    "Navy": Navy,
    "MidnightBlue": MidnightBlue
}

# Purple, Violet, and Magenta Colors:
Lavender = (230, 230, 250)
Thistle = (216, 191, 216)
Plum = (221, 160, 221)
Violet = (238, 130, 238)
Orchid = (218, 112, 214)
Fuchsia = (255, 0, 255)
Magenta = (255, 0, 255)
MediumOrchid = (186, 85, 211)
MediumPurple = (147, 112, 219)
BlueViolet = (138, 43, 226)
DarkViolet = (148, 0, 211)
DarkOrchid = (153, 50, 204)
DarkMagenta = (139, 0, 139)
Purple = (128, 0, 128)
Indigo = (75, 0, 130)
DarkSlateBlue = (72, 61, 139)
SlateBlue = (106, 90, 205)
MediumSlateBlue = ()
list_purple = {  # Also Magenta and Violet
    "Lavender": Lavender,
    "Thistle": Thistle,
    "Plum": Plum,
    "Violet": Violet,
    "Orchid": Orchid,
    "Fuchsia": Fuchsia,
    "Magenta": Magenta,
    "MediumOrchid": MediumOrchid,
    "MediumPurple": MediumPurple,
    "BlueViolet": BlueViolet,
    "DarkViolet": DarkViolet,
    "DarkOrchid": DarkOrchid,
    "DarkMagenta": DarkMagenta,
    "Purple": Purple,
    "Indigo": Indigo,
    "DarkSlateBlue": DarkSlateBlue,
    "SlateBlue": SlateBlue,
    "MediumSlateBlue": MediumSlateBlue,
}

# White Colors:
White = (255, 255, 255)
Snow = (255, 250, 250)
Honeydew = (240, 255, 240)
MintCream = (245, 255, 250)
Azure = (240, 248, 255)
AliceBlue = (240, 248, 255)
GhostWhite = (248, 248, 255)
WhiteSmoke = (245, 245, 245)
Seashell = (255, 235, 238)
Beige = (245, 245, 220)
OldLace = (253, 245, 230)
FloralWhite = (255, 250, 240)
Ivory = (255, 255, 240)
AntiqueWhite = (250, 235, 215)
Linen = (250, 240, 230)
LavenderBlush = (255, 240, 245)
MistyRose = (255, 228, 225)
list_white = {
    "White": White,
    "Snow": Snow,
    "Honeydew": Honeydew,
    "MintCream": MintCream,
    "Azure": Azure,
    "AliceBlue": AliceBlue,
    "GhostWhite": GhostWhite,
    "WhiteSmoke": WhiteSmoke,
    "Seashell": Seashell,
    "Beige": Beige,
    "OldLace": OldLace,
    "FloralWhite": FloralWhite,
    "Ivory": Ivory,
    "AntiqueWhite": AntiqueWhite,
    "Linen": Linen,
    "LavenderBlush": LavenderBlush,
    "MistyRose": MistyRose

}

# Gray and Black Colors:
Gainsboro = (220, 220, 220)
LightGray = (211, 211, 211)
Silver = (192, 192, 192)
DarkGray = (169, 169, 169)
Gray = (128, 128, 128)
DimGray = (105, 105, 105)
LightSlateGray = (119, 136, 153)
SlateGray = (112, 128, 144)
DarkSlateGray = (47, 79, 79)
Black = (0, 0, 0)
list_gray = {  # Also Black
    "Gainsboro": Gainsboro,
    "LightGray": LightGray,
    "Silver": Silver,
    "DarkGray": DarkGray,
    "Gray": Gray,
    "DimGray": DimGray,
    "LightSlateGray": LightSlateGray,
    "SlateGray": SlateGray,
    "DarkSlateGray": DarkSlateGray,
    "Black": Black
}

list_colors = {}
list_colors.update(list_pink, list_red, list_yellow, list_brown, list_green, list_cyan, list_blue, list_purple, list_white, list_gray)
