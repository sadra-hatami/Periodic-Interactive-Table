# Mendeleev Interactive Table | جدول تعاملی مندلیف (تناوبی)
# By Sadra Hatami | صدرا حاتمی

elements_name = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", 
    "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", 
    "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", 
    "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", 
    "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", 
    "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", 
    "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", 
    "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", 
    "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", 
    "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", 
    "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", 
    "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", 
    "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", 
    "Livermorium", "Tennessine", "Oganesson"
]

bar_yoni = [
    1, 0, 1, 2, 3, 4, -3, -2, -1, 0, 1, 2, 3, 4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 3, 2, 2, 2, 2, 1, 2, 3, 4,
    -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1, 2, 3, 4, -3, -2, -1, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, -1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, -1, 0
]

adad_jermi = [
    1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 40, 39, 40, 45, 48, 51, 52, 55,
    56, 59, 58, 59, 63, 65, 69, 71, 74, 75, 79, 81, 84, 85, 87, 88, 89, 90, 91, 93, 94, 95, 97, 98,
    99,101, 103, 105, 106, 107, 109, 110, 112, 113, 115,118, 119, 121, 122, 125, 126, 127, 128,
    131, 132, 133, 137, 138, 139, 140, 141, 144, 145, 150, 152, 153, 157, 158, 159, 162, 164,
    165, 167, 169, 172, 173, 175, 178, 179, 181, 182, 183, 185, 187, 188, 189, 190, 192, 195,
    197, 198, 199, 200, 204, 205, 207, 208, 209, 210, 222, 223, 226, 227, 232, 235, 238, 239,
    240, 241, 244, 243, 247, 251, 252, 257, 258, 259, 262, 267, 270, 271, 270, 277, 276, 281,
    280, 285, 284, 289, 290, 293, 294, 294, 294, 294, 294, 294, 294, 294
]

electron_madar_number = [
    (1), (2), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 8, 1), (2, 8, 2), (2, 8, 3), (2, 8, 4), (2, 8, 5),
    (2, 8, 6), (2, 8, 7), (2, 8, 8), (2, 8, 8, 1), (2, 8, 8, 2), (2, 8, 8, 3), (2, 8, 8, 4), (2, 8, 8, 5), (2, 8, 8, 6), (2, 8, 8, 7),
    (2, 8, 8, 8), (2, 8, 8, 9), (2, 8, 8, 10), (2, 8, 8, 11), (2, 8, 8, 12), (2, 8, 18, 3), (2, 8, 18, 4), (2, 8, 18, 5), (2, 8, 18, 6),
    (2, 8, 18, 7), (2, 8, 18, 8), (2, 8, 18, 8, 1), (2, 8, 18, 8, 2), (2, 8, 18, 9, 2), (2, 8, 18, 10, 2), (2, 8, 18, 11, 2),
    (2, 8, 18, 12, 2), (2, 8, 18, 13, 2), (2, 8, 18, 14, 2), (2, 8, 18, 15, 2), (2, 8, 18, 16, 2), (2, 8, 18, 17, 1),
    (2, 8, 18, 18, 1), (2, 8, 18, 18, 3), (2, 8, 18, 18, 4), (2, 8, 18, 18, 5), (2, 8, 18, 18, 6), (2, 8, 18, 18, 7),
    (2, 8, 18, 18, 8), (2, 8, 18, 18, 8, 1), (2, 8, 18, 18, 8, 2), (2, 8, 18, 18, 9, 2), (2, 8, 18, 18, 10, 2),
    (2, 8, 18, 18, 11, 2), (2, 8, 18, 18, 12, 2), (2, 8, 18, 18, 13, 2), (2, 8, 18, 18, 14, 2),
    (2, 8, 18, 18, 15, 2), (2, 8, 18, 18, 16, 2), (2, 8, 18, 18, 17, 2), (2, 8, 18, 18, 18, 2),
    (2, 8, 18, 18, 19, 2), (2, 8, 18, 18, 20, 2), (2, 8, 18, 18, 21, 2), (2, 8, 18, 18, 22, 2),
    (2, 8, 18, 18, 23, 2), (2, 8, 18, 32, 9, 2), (2, 8, 18, 32, 10, 2), (2, 8, 18, 32, 11, 2),
    (2, 8, 18, 32, 12, 2), (2, 8, 18, 32, 13, 2), (2, 8, 18, 32, 14, 2), (2, 8, 18, 32, 15, 2),
    (2, 8, 18, 32, 16, 1), (2, 8, 18, 32, 18, 1), (2, 8, 18, 32, 18, 3), (2, 8, 18, 32, 18, 4),
    (2, 8, 18, 32, 18, 5), (2, 8, 18, 32, 18, 6), (2, 8, 18, 32, 18, 7), (2, 8, 18, 32, 18, 8),
    (2, 8, 18, 32, 18, 8, 1), (2, 8, 18, 32, 18, 8, 2), (2, 8, 18, 32, 18, 9, 2),
    (2, 8, 18, 32, 18, 10, 2), (2, 8, 18, 32, 18, 11, 2), (2, 8, 18, 32, 18, 12, 2),
    (2, 8, 18, 32, 18, 13, 2), (2, 8, 18, 32, 18, 14, 2), (2, 8, 18, 32, 18, 15, 2),
    (2, 8, 18, 32, 18, 16, 2), (2, 8, 18, 32, 18, 17, 2), (2, 8, 18, 32, 18, 18, 2),
    (2, 8, 18, 32, 18, 19, 2), (2, 8, 18, 32, 18, 20, 2), (2, 8, 18, 32, 18, 21, 2),
    (2, 8, 18, 32, 18, 22, 2), (2, 8, 18, 32, 18, 23, 2), (2, 8, 18, 32, 32, 9, 2),
    (2, 8, 18, 32, 32, 10, 2), (2, 8, 18, 32, 32, 11, 2), (2, 8, 18, 32, 32, 12, 2),
    (2, 8, 18, 32, 32, 13, 2), (2, 8, 18, 32, 32, 14, 2), (2, 8, 18, 32, 32, 15, 2),
    (2, 8, 18, 32, 32, 16, 2), (2, 8, 18, 32, 32, 17, 1), (2, 8, 18, 32, 32, 18, 1),
    (2, 8, 18, 32, 32, 18, 3), (2, 8, 18, 32, 32, 18, 4), (2, 8, 18, 32, 32, 18, 5),
    (2, 8, 18, 32, 32, 18, 6), (2, 8, 18, 32, 32, 18, 7)
]

isotopes_number = [
    (1, "H1"), (2, "He3", "He4"), (2, "Li6", "Li7"), (1, "Be9"),
    (2, "B10", "B11"), (2, "C12", "C13"), (2, "N14", "N15"), 
    (3, "O16", "O17", "O18"), (1, "F19"), (1, "Ne20"), 
    (1, "Na23"), (1, "Mg24"), (2, "Al27", "Al28"), 
    (3, "Si28", "Si29", "Si30"), (2, "P31", "P32"), 
    (3, "S32", "S33", "S34"), (2, "Cl35", "Cl37"), (3, "Ar36", "Ar38", "Ar40"), 
    (2, "K39", "K40"), (1, "Ca40"), (2, "Sc45", "Sc46"), 
    (2, "Ti46", "Ti47"), (2, "V50", "V51"), (2, "Cr52", "Cr53"),
    (3, "Mn55", "Mn56", "Mn57"), (1, "Fe56"), (2, "Co59", "Co60"), 
    (2, "Ni58", "Ni60"), (3, "Cu63", "Cu65", "Cu66"), 
    (3, "Zn64", "Zn66", "Zn68"), (1, "Ga69"), (1, "Ge74"),
    (2, "As75", "As76"), (3, "Se74", "Se76", "Se78"),
    (1, "Br79"), (2, "Kr78", "Kr80"), (2, "Rb85", "Rb87"), 
    (2, "Sr84", "Sr86"), (2, "Y89", "Y90"), (3, "Zr90", "Zr92", "Zr94"),
    (2, "Nb93", "Nb94"), (3, "Mo92", "Mo94", "Mo96"),
    (2, "Tc98", "Tc99"), (3, "Ru98", "Ru100", "Ru102"), 
    (2, "Rh103", "Rh105"), (3, "Pd104", "Pd106", "Pd108"),
    (3, "Ag107", "Ag109", "Ag111"), (2, "Cd106", "Cd108"),
    (2, "In113", "In115"), (2, "Sn112", "Sn114"), 
    (3, "Sb121", "Sb123", "Sb125"), (3, "Te130", "Te132", "Te134"),
    (2, "I127", "I131"), (1, "Xe129"), (2, "Cs133", "Cs134"),
    (2, "Ba138", "Ba140"), (3, "La138", "La139", "La140"),
    (3, "Ce140", "Ce142", "Ce144"), (1, "Pr141"),
    (3, "Nd144", "Nd146", "Nd148"), (2, "Pm145", "Pm146"),
    (2, "Sm144", "Sm147"), (2, "Eu151", "Eu153"),
    (1, "Gd158"), (2, "Tb159", "Tb160"),
    (2, "Dy160", "Dy162"), (2, "Ho165", "Ho167"),
    (1, "Er166"), (2, "Tm169", "Tm170"),
    (2, "Yb168", "Yb170"), (3, "Lu175", "Lu176", "Lu177"),
    (3, "Hf174", "Hf176", "Hf178"), (3, "Ta180", "Ta181", "Ta182"),
    (2, "W182", "W183"), (3, "Re185", "Re187", "Re188"),
    (2, "Os188", "Os190"), (2, "Ir191", "Ir193"),
    (2, "Pt194", "Pt195"), (3, "Au197", "Au198", "Au199"),
    (2, "Hg202", "Hg204"), (2, "Tl203", "Tl205"),
    (2, "Pb206", "Pb207"), (2, "Bi209", "Bi210"),
    (2, "Po208", "Po209"), (1, "At210"),
    (2, "Rn222", "Rn223"), (1, "Fr223"),
    (2, "Ra226", "Ra228"), (1, "Ac227"),
    (3, "Th232", "Th234", "Th235"), (3, "Pa231", "Pa232", "Pa233"),
    (4, "U238", "U239", "U240", "U241"), (4, "Np237", "Np238", "Np239", "Np240"),
    (5, "Pu244", "Pu245", "Pu246", "Pu247", "Pu248"),
    (3, "Am241", "Am242", "Am243"), (3, "Cm242", "Cm243", "Cm244"),
    (2, "Bk247", "Bk248"), (2, "Cf249", "Cf250"),
    (2, "Es252", "Es253"), (2, "Fm257", "Fm258"),
    (2, "Md258", "Md259"), (1, "No259"),
    (2, "Lr262", "Lr263"), (2, "Rf267", "Rf268"),
    (2, "Db270", "Db271"), (2, "Sg271", "Sg272"),
    (2, "Bh270", "Bh271"), (2, "Hs277", "Hs278"),
    (3, "Mt276", "Mt277", "Mt278"), (2, "Ds281", "Ds282"),
    (1, "Rg280"), (1, "Cn285"),
    (2, "Nh284", "Nh285"), (2, "Fl289", "Fl290"),
    (1, "Mc289"), (1, "Lv293"),
    (1, "Ts294"), (1, "Og294")
] 

n_p_e = [
    (0, 1, 1), (1, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), 
    (6, 6, 6), (7, 7, 7), (8, 8, 8), (10, 9, 9), (10, 10, 10), 
    (12, 11, 11), (12, 12, 12), (14, 13, 13), (16, 14, 14), (16, 15, 15), 
    (17, 16, 16), (18, 17, 17), (22, 18, 18), (23, 19, 19), (24, 20, 20), 
    (24, 21, 21), (25, 22, 22), (26, 23, 23), (26, 24, 24), (28, 25, 25), 
    (30, 26, 26), (30, 27, 27), (32, 28, 28), (33, 29, 29), (34, 30, 30), 
    (36, 31, 31), (39, 32, 32), (42, 33, 33), (45, 34, 34), (46, 35, 35), 
    (47, 36, 36), (50, 37, 37), (53, 38, 38), (56, 39, 39), (56, 40, 40), 
    (58, 41, 41), (58, 42, 42), (60, 43, 43), (61, 44, 44), (63, 45, 45), 
    (65, 46, 46), (66, 47, 47), (67, 48, 48), (69, 49, 49), (71, 50, 50), 
    (74, 51, 51), (77, 52, 52), (78, 53, 53), (81, 54, 54), (83, 55, 55), 
    (85, 56, 56), (88, 57, 57), (92, 58, 58), (93, 59, 59), (97, 60, 60), 
    (99, 61, 61), (103, 62, 62), (106, 63, 63), (108, 64, 64), (113, 65, 65), 
    (114, 66, 66), (118, 67, 67), (122, 68, 68), (125, 69, 69), (129, 70, 70), 
    (132, 71, 71), (139, 72, 72), (142, 73, 73), (145, 74, 74), (148, 75, 75), 
    (151, 76, 76), (157, 77, 77), (160, 78, 78), (164, 79, 79), (169, 80, 80), 
    (172, 81, 81), (174, 82, 82), (179, 83, 83), (182, 84, 84), (186, 85, 85), 
    (188, 86, 86), (191, 87, 87), (193, 88, 88), (196, 89, 89), (200, 90, 90), 
    (202, 91, 91), (205, 92, 92), (208, 93, 93), (211, 94, 94), (215, 95, 95), 
    (218, 96, 96), (222, 97, 97), (227, 98, 98), (232, 99, 99), (237, 100, 100), 
    (241, 101, 101), (245, 102, 102), (249, 103, 103), (253, 104, 104), (257, 105, 105), 
    (261, 106, 106), (267, 107, 107), (270, 108, 108), (271, 109, 109), (277, 110, 110), 
    (280, 111, 111), (285, 112, 112), (288, 113, 113), (290, 114, 114), (293, 115, 115), 
    (294, 116, 116), (294, 117, 117), (294, 118, 118)
] 

madar_number = [
    1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4
] 

electron_last_madar = [
    1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 2, 2, 1, 1, 2, 2, 1, 0,
    1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8
] 

group_period = [
    (1, 1), (1, 18), (2, 1), (2, 2), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (3, 1), (3, 2), (3, 13),
    (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
    (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16), (4, 17), (4, 18), (5, 1), (5, 2), (5, 3), (5, 4),
    (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11),(5, 12), (5, 13), (5, 14), (5, 15), (5, 16), (5, 17),
    (5, 18), (6, 1), (6, 2), (6, 3), (6, 3), (6, 3), (6, 3), (6, 3), (6, 3), (6, 3), (6, 3), (6, 3), (6, 3), (6, 3), (6, 3),
    (6, 3), (6, 3), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14),
    (6, 15), (6, 16), (6, 17), (6, 18), (7, 1), (7, 2), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3),
    (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10),
    (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16), (7, 17), (7, 18)
    ] 

state_room = [
    "Gas", "Gas", "Solid", "Solid", "Solid", "Solid", "Gas", "Gas", "Gas", "Gas", "Solid", "Solid", "Solid",
    "Solid", "Solid", "Solid", "Gas", "Gas", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", 
    "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Gas", "Solid", "Solid", 
    "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", 
    "Solid", "Solid", "Solid", "Gas", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", 
    "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", 
    "Solid", "Solid", "Solid", "Solid", "Liquid", "Solid", "Solid", "Solid", "Solid", "Solid", "Gas", "Solid", 
    "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", 
    "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", "Solid", 
    "Solid", "Solid", "Solid", "Solid", "Solid", "Gas", "Gas", 
] 

zob_point = [
    -259.16, -272.2, 180.5, 1287, 2075, 3550, -210.0, -218.79, -219.62, -248.59, 97.79, 650, 660.37,
    1414, 44.2, 115.2, -101.5, -189.34, 63.5, 842, 1541, 1668, 1910, 1907, 1246, 1538, 1495, 1455,
    1084.62, 419.58, 29.76, 938.25, 817, 221, 113.7, -157.36, 39.3, 777, 1526, 1855, 2468, 2623, 2157,
    2334, 1961, 1554.9, 961.93, 321.07, 156.6, 231.93, 630.63, 221, 113.7, -111.8, 28.5, 727, 920, 798,
    937, 1021, 604, 1047, 822, 1313, 1360, 1685, 1470, 1529, 1541, 1097, 1650, 2233, 3017, 3422, 3186,
    3045, 2446, 1768, 1064, -38.83, 156.6, 327.5, 271.4, 254, 302, -61.7, 27, 700, 1050, 1050, 1535, 1132,
    644, 639.5, 1170, 1340, 1030, 1170, 1130, 1527, 1100, 1030, 1627, 2600, 2620, 2630, 2610, 2630, 2620,
    2710, 2660, 2870, 2200, 2330, 1500, 1300, 200, 47]

josh_point =[-252.87, -268.93, 1342, 2469, 4000, 4827, -195.8, -182.96, -188.11, -246.08, 883, 1090, 2519, 2900, 280,
             444.6, -34.04, -185.0, 759, 1655, 2830, 3287, 3400, 2671, 2061, 2862, 2927, 2913, 2562, 907, 2204, 2833, 613,
             685, 332, -157.37, 688, 1382, 3337, 4409, 4742, 4639, 4768, 4130, 3968, 3370, 1961, 765, 2072, 2602, 903, 988,
             444.6, -108.1, 671, 1640, 2123, 1064, 935, 1021, 3000, 1070, 1094, 2310, 3420, 2560, 2400, 3000, 1490, 1600, 3400,
             4602, 5731, 5828, 5900, 5027, 4446, 4446, 2856, 356.58, 1470, 1749, 1564, 962, 337, -61.7, 677, 1413, 1050, 1081,
             1570, 4131, 4130, 639.5, 1063, 1340, 1007, 963, 1133, 1527, 1100, 1030, 1627, 2600, 2620, 2630, 2610, 2630, 2620,
             2710, 2660, 2870, 2200, 2330, 1500, 1300, 200, 47]

chegali = [0.08988, 0.1786, 0.534, 1.848, 2.46, 2.267, 0.0012506, 0.001429, 0.001696, 0.0008999, 0.968, 1.738,
           2.7, 2.33, 1.82, 2.07, 0.003214, 0.003733, 0.87, 1.55, 2.99, 4.54, 6.11, 7.19, 7.43, 7.87, 8.9, 8.9, 8.96, 7.14,
           5.91, 5.32, 5.73, 7.74, 3.12, 0.003733, 1.53, 2.64, 3.75, 6.51, 8.57, 10.22, 11.72, 12.37, 12.41, 12.02, 10.49,
           8.65, 11.87, 7.31, 6.73, 6.24, 4.93, 0.00375, 1.87, 5.58, 6.15, 6.77, 6.77, 7.01, 8.3, 7.52, 5.24, 7.9, 8.23, 8.55,
           8.8, 8.8, 8.88, 6.9, 9.79, 13.31, 16.65, 19.25, 21.02, 22.59, 22.59, 21.45, 19.32, 13.53, 11.85, 11.34, 9.74, 9.2,
           7.2, 5e-07, 0.87, 5.5, 10.07, 11.72, 15.37, 18.95, 20.25, 19.86, 13.68, 13.69, 15.7, 15.99, 9.18, 15.0, 12.99, 13.0,
           12.03, 17.28, 18.88, 18.96, 17.9, 18.9, 18.69, 19.0, 16.9, 14.3, 13.2, 14.0, 14.8, 13.0, 10.0, 0.5]

sh_atomic = [53, 31, 167, 112, 87, 70, 65, 60, 50, 38, 186, 160, 143, 118, 110, 104, 99, 88, 227, 197, 184, 175, 171, 139,
             127, 126, 125, 124, 128, 139, 135, 125, 118, 116, 114, 88, 262, 212, 180, 175, 164, 139, 139, 127, 126, 139, 144,
             143, 143, 140, 138, 140, 133, 216, 262, 193, 186, 182, 175, 169, 165, 162, 159, 152, 147, 143, 142, 141, 139, 139,
             174, 156, 145, 139, 137, 137, 136, 135, 144, 151, 156, 175, 156, 140, 202, 0, 270, 221, 225, 220, 215, 209, 206, 200,
             197, 197, 196, 196, 196, 196, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195, 195]

element_type = ['Nonmetal', 'Noble Gas', 'Metal', 'Metal', 'Metalloid', 'Nonmetal', 'Nonmetal', 'Nonmetal', 'Nonmetal', 'Noble Gas',
                'Metal', 'Metal', 'Metal', 'Metalloid', 'Nonmetal', 'Nonmetal', 'Nonmetal', 'Noble Gas', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal',
                'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metalloid', 'Metalloid', 'Nonmetal', 'Nonmetal', 'Noble Gas',
                'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metalloid',
                'Metalloid', 'Nonmetal', 'Noble Gas', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal',
                'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Liquid Metal',
                'Metal', 'Metal', 'Metal', 'Metalloid', 'Nonmetal', 'Noble Gas', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal',
                'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal',
                'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal', 'Metal']

discoverers = ['Henry Cavendish', 'Pierre Janssen', 'Johann August Arfvedson', 'Friedrich Wöhler', 'Joseph Gay-Lussac', '-',
               'Daniel Rutherford', 'Carl Wilhelm Scheele and Joseph Priestley', 'Henri Moissan', 'William Ramsay', 'Humphry Davy',
               'Joseph Black', 'Hans Christian Ørsted', 'Jöns Jacob Berzelius', 'Hennig Brand', '-', 'Carl Wilhelm Scheele', 'William Ramsay',
               'Humphry Davy', 'Humphry Davy', 'Lars Fredrik Nilson', 'William Gregor', 'Andrés Manuel del Río', 'Louis Nicolas Vauquelin',
               'Johann Gottlieb Gahn', '-', 'George Brandt', 'Axel Fredrik Cronstedt', '-', 'Andreas Sigismund Marggraf', 'Paul-Émile Lecoq de Boisbaudran',
               'Clemens Winkler', 'Albertus Magnus', 'Jöns Jacob Berzelius', 'Antoine Jérôme Balard', 'William Ramsay', 'Robert Bunsen and Gustav Kirchhoff',
               'William Cruickshank', 'Johan Gadolin', 'Martin Heinrich Klaproth', 'Charles Hatchett', 'Carl Wilhelm Scheele', 'Carl Auer von Welsbach',
               'Karl Ernst Claus', 'William Hyde Wollaston', 'William Hyde Wollaston', '-', 'Friedrich Strohmeyer', 'Ferdinand Reich and Theodor Richter', '-', '-',
               'Franz Joseph Müller von Reichenstein', 'Bernard Courtois', 'William Ramsay and Morris Travers', 'Robert Bunsen and Gustav Kirchhoff',
               'Carl Wilhelm Scheele', 'Carl Gustaf Mosander', 'Martin Heinrich Klaproth', 'Carl Auer von Welsbach', 'Carl Auer von Welsbach', '-',
               'Paul-Émile Lecoq de Boisbaudran', 'Eugène-Anatole Demarçay', 'Jean Charles Galissard de Marignac', 'Carl Auer von Welsbach',
               'Paul-Émile Lecoq de Boisbaudran', 'Carl Gustaf Mosander', 'Carl Gustaf Mosander', 'Per Teodor Cleve', 'Jean Charles Galissard de Marignac',
               'Carl Auer von Welsbach', 'Dirk Coster and George de Hevesy', 'Martin Heinrich Klaproth', 'Juan José Galisteo',
               'Walter Noddack, Ida Tacke, and Otto Berg', 'Smithson Tennant', 'Smithson Tennant', 'Antonio de Ulloa', '-', '-', 'William Crookes', '-', '-',
               'Marie Curie and Pierre Curie', 'Dale R. Corson, Kenneth Ross MacKenzie, and Emilio Segrè', 'Friedrich Dorn', 'Marguerite Perey',
               'Marie Curie and Pierre Curie', 'Friedrich Oskar Giesel', 'Jöns Jacob Berzelius', 'Otto Hahn and Lise Meitner', 'Martin Heinrich Klaproth',
               'Glenn T. Seaborg and Arthur C. Wahl', 'Glenn T. Seaborg, Ralph A. James, and Albert Ghiorso', 'Glenn T. Seaborg, Ralph A. James, and Albert Ghiorso',
               'Glenn T. Seaborg, Ralph A. James, and Albert Ghiorso', 'Albert Ghiorso, Glenn T. Seaborg, and Gregory R. Choppin',
               'Albert Ghiorso, Glenn T. Seaborg, and Almon E. Larsh', 'Albert Ghiorso, Glenn T. Seaborg, and Albert M. Katz',
               'Albert Ghiorso, Glenn T. Seaborg, and Ronald L. Perlman', 'Albert Ghiorso, Glenn T. Seaborg, and Bernard Ghiorso',
               'Albert Ghiorso, Glenn T. Seaborg, and John R. T. Lawrence', 'Albert Ghiorso, Glenn T. Seaborg, and Torbjörn Sikkeland',
               'Georgy N. Flerov and team', 'Joint Institute for Nuclear Research (JINR)', 'Albert Ghiorso, Glenn T. Seaborg, and team',
               'Gottfried Münzenberg and team', 'Peter Armbruster, Gottfried Münzenberg, and team', 'Peter Armbruster, Gottfried Münzenberg, and team',
               'Peter Armbruster, Gottfried Münzenberg, and team', 'Peter Armbruster, Gottfried Münzenberg, and team',
               'Peter Armbruster, Gottfried Münzenberg, and team', 'Joint Institute for Nuclear Research (JINR)', 'Joint Institute for Nuclear Research (JINR)',
               'Joint Institute for Nuclear Research (JINR)', 'Joint Institute for Nuclear Research (JINR)', 'Joint Institute for Nuclear Research (JINR)',
               'Joint Institute for Nuclear Research (JINR)']

discovery_locations = ['England', 'France', 'Sweden', 'Germany', 'France', '-', 'Scotland', 'Sweden', 'France', 'England', 'England', 'Scotland',
                       'Denmark', 'Sweden', 'Germany', '-', 'Sweden', 'England', 'England', 'England', 'Sweden', 'England', 'Mexico', 'France', 'Sweden', '-',
                       'Sweden', 'Sweden', '-', 'Germany', 'France', 'Germany', 'Germany', 'Sweden', 'France', 'England', 'Germany', 'Scotland', 'Finland',
                       'Germany', 'England', 'Sweden', 'Italy', 'Russia', 'England', 'England', '-', 'Germany', 'Germany', '-', '-', 'Romania', 'France', 'England',
                       'Germany', 'Sweden', 'Sweden', 'Germany', 'Austria', 'Austria', '-', 'France', 'France', 'Switzerland', 'Sweden', 'France', 'Sweden',
                       'Sweden', 'Sweden', 'Switzerland', 'Austria', 'Denmark', 'Sweden', 'Spain', 'Germany', 'England', 'England', 'Peru', '-', '-', 'England', '-', '-',
                       'Poland', 'USA', 'Germany', 'France', 'Poland', 'Germany', 'Sweden', 'Germany', 'Germany', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA',
                       'USA', 'USA', 'USA', 'USA', 'Russia', 'Russia', 'USA', 'Germany', 'Germany', 'Germany', 'Germany', 'Germany', 'Germany', 'Japan', 'Russia',
                       'Russia', 'Russia', 'Russia', 'Russia']


yonesh_energy = [1312, 2372, 520, 899, 800, 1086, 1402, 1314, 1681, 2080, 496, 738, 577, 787, 1012, 999, 1251, 1520, 419, 589, 633, 658,
                 650, 652, 760, 762, 759, 736, 745, 906, 579, 762, 947, 941, 1000, 1350, 402, 549, 631, 660, 658, 687, 702, 715, 719, 735, 815, 731,
                 558, 708, 707, 903, 1008, 1260, 390, 503, 498, 540, 527, 533, 579, 588, 579, 600, 565, 570, 573, 581, 570, 603, 523, 658, 587, 770,
                 760, 740, 780, 840, 899, 1007, 589, 715, 703, 730, 1030, 1030, 380, 509, 580, 568, 590, 590, 588, 595, 580, 602, 586, 594, 588, 579,
                 585, 587, 588, 560, 640, 730, 740, 650, 800, 700, 760, 680, 790, 800, 720, 650, 600, 950]

kashf = [1766, 1895, 1817, 1798, 1808, 1869, 1772, 1774, 1886, 1898, 1807, 1755, 1825, 1824, 1669, 1777, 1810, 1898, 1861, 1808, 1879,
         1791, 1801, 1797, 1774, 1780, 1735, 1751, 1797, 1746, 1875, 1886, 1974, 1820, 1826, 1898, 1869, 1808, 1794, 1789, 1801, 1790, 1937,
         1940, 1944, 1803, 1735, 1824, 1863, 1817, 1800, 1782, 1811, 1940, 1860, 1774, 1949, 1945, 1945, 1946, 1945, 1953, 1947, 1955, 1953,
         1950, 1952, 1923, 1953, 1960, 1949, 1923, 1866, 1926, 1925, 1939, 1931, 1803, 1797, 1869, 1861, 2077, 204, 1941, 1940, 1900, 1939,
         1944, 1949, 1944, 1940, 1944, 1940, 1944, 1944, 1944, 1949, 1950, 1952, 1953, 1955, 1958, 1961, 1964, 1965, 1976, 1981, 1984, 1982,
         1984, 2000, 2000, 2003, 2004, 2010, 2012, 2016, 2015]

name_2 = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", 
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", 
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", 
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", 
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", 
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", 
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", 
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", 
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", 
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", 
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", 
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

jerm = ["1,008", "4,003", "6,94", "9,01", "10,80", "12,01","14,01", "16,00", "19,00", "20,18", "22,99", "24,31", "26,98", "28,09", "30,97",
        "32,07", "35,45", "39,95", "39,10", "40,08", "44,96", "47,87", "50,94", "52,00", "54,94", "55,85", "58,93", "58,69", "63,55", "65,39",
        "69,72", "72,64", "74,92", "78,96", "79,90", "83,80", "85,47", "87,62", "88,91", "91,22", "92,91", "95,94", "---", "101,1", "102,90",
        "106,40", "107,90","112,40", "114,80", "118,70", "121,80", "127,60", "126,90", "131,30", "132,9", "137,3", "175,00", "178,5",
        "180,90", "183,80", "186,20", "190,20", "192,20", "195,1", "197,00", "200,60", "204,30", "207,20", "209,00", "[209]", "[210]",
        "[222]", "[223]", "[226]", "[262]", "[267]", "[268]", "[271]", "[272]", "[277]", "[276]", "[281]", "[280]", "[277]", "[284]", "[289]",
        "[288]", "[293]", "[296]", "[294]", "138,90", "140,10", "140,90", "142,20", "[145]", "150,40", "152,00", "157,30", "158,90", "162,50",
        "164,90", "167,30", "168,90", "173,00", "[227]", "232,00", "231,00", "238,00", "[237]", "[244]", "[243]", "[247]", "[247]", "[251]", "[252]",
        "[257]", "[258]", "[259]"]

names = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
         "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
         "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
         "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
         "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
         "Sb", "Te", "I", "Xe", "Cs", "Ba", "Lu", "Hf", "Ta", "W",
         "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At",
         "Rn", "Fr", "Ra", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt",
         "Ds", "Rg", "Cn", "Nh", "Fi", "Mc", "Lv", "Ts", "Og", "La",
         "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho",
         "Er", "Tm", "Yb", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
         "Bk", "Cf", "Es", "Fm", "Md", "No"]

main_coor = []

ss = [-450, -400, -350, -300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300, 350, 400]
cc = [-350, -300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300]
coors = [-450, 400, -450, -400, 150, 200, 250, 300, 350, 400, -450, -400, 150, 200, 250, 300, 350, 400]

for i in range(4):
    for ii in ss:
        coors.append(ii)
    
for i in range(2):
    for ii in cc:
        coors.append(ii)

colors = ["red", "red", "red", "red", "blue", "blue", "blue", "blue", "blue", "blue", "red", "red", "blue", "blue", "blue", "blue", "blue",
          "blue", "red", "red", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "blue", "blue",
          "blue", "blue", "blue", "blue", "red", "red", "green", "green", "green", "green", "green", "green", "green", "green", "green",
          "green", "blue", "blue", "blue", "blue", "blue", "blue","red", "red", "green", "green", "green", "green", "green", "green", "green",
          "green", "green", "green", "blue", "blue", "blue", "blue", "blue", "blue","red", "red", "green", "green", "green", "green", "green",
          "green", "green", "green", "green", "green", "blue", "blue", "blue", "blue", "blue", "blue"]
for i in range(28):
    colors.append("yellow")
    
'''

colors = ['red', 'red', 'red', 'red', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'red', 'red',
          'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'red', 'red', 'yellow', 'yellow', 'yellow',
          'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'cyan', 'cyan', 'cyan',
          'cyan', 'cyan', 'cyan', 'red', 'red', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow',
          'yellow', 'yellow', 'yellow', 'yellow', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'red', 'red',
          'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow',
          'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'red', 'red', 'yellow', 'yellow', 'yellow', 'yellow',
          'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan',
          'cyan', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
          'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
          'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
          'magenta', 'magenta']
'''

numbers = []
for i in range(1, 57, 1):
    numbers.append(i)
    
for i in range(71, 89, 1):
    numbers.append(i)
    
for i in range(103, 119, 1):
    numbers.append(i)
    
for i in range(57, 71, 1):
    numbers.append(i)

for i in range(89, 103, 1):
    numbers.append(i)

number_1 = 0

from turtle import Screen, Turtle, RawTurtle, TurtleScreen, ScrolledCanvas
from tkinter import *
from tkinter import ttk

def open_on(x, y):
    global number_1
    check.goto(x, y)
    for i, j, name in main_coor:
        if check.distance(i, j) <= 20:
            for i in name_2:
                if name == i:
                    number_1 = int(name_2.index(i)) + 1
                    break
            open_sh(name, number_1)
    
def open_sh(name, nm):
    def el(n, p, e):
        top = Toplevel(t)
        top.geometry("250x120")
        top.resizable(False, False)
        l1 = Label(top, text = 'Neutron: "{}"'.format(n), font = ("Arial", 16, "normal"))
        l2 = Label(top, text = 'Proton: "{}"'.format(p), font = ("Arial", 16, "normal"))
        l3 = Label(top, text = 'Electron: "{}"'.format(e), font = ("Arial", 16, "normal"))

        l1.grid(row = 0, column = 0, sticky = "w")
        l2.grid(row = 1, column = 0, sticky = "w", pady = 10)
        l3.grid(row = 2, column = 0, sticky = "w")

        ttk.Button(top, text = "Exit", command = top.destroy).grid(row = 2, column = 3, padx = 30)
       
    def draw_ar(tu, madar, elc):
        elct = [elc, "m"]
        tu.width(3)
        tu.shape("circle")
        tu.shapesize(0.8)
        tu.color("black", "magenta")
        tu.stamp()
        tu.color("black")
        tu.penup()
        cors = []
        yc = -20

        for i in range(madar):
            tu.sety(yc)
            tu.pendown()
            tu.circle(-yc)
            tu.penup()
            cors.append(-yc)
            yc -= 20

        tu.home()
        tu.shapesize(0.5)

        if madar >= 1:
            tu.color("black", "cyan")

            try:
                asl = elct[0][0]
                
            except:
                asl = elct[0]

            electron = 360 / asl
            for i in range(asl):
                tu.fd(cors[0])
                tu.stamp()
                tu.goto(0, 0)
                tu.rt(electron)

        if madar >= 2:
            tu.seth(90)
            asl = elct[0][1]
            electron = 360 / asl
            for i in range(asl):
                tu.fd(cors[1])
                tu.stamp()
                tu.goto(0, 0)
                tu.rt(electron)

        if madar >= 3:
            tu.seth(90)
            asl = elct[0][2]
            electron = 360 / asl
            for i in range(asl):
                tu.fd(cors[2])
                tu.stamp()
                tu.goto(0, 0)
                tu.rt(electron)

        if madar >= 4:
            tu.seth(90)
            asl = elct[0][3]
            electron = 360 / asl
            for i in range(asl):
                tu.fd(cors[3])
                tu.stamp()
                tu.goto(0, 0)
                tu.rt(electron)

        if madar >= 5:
            tu.seth(90)
            asl = elct[0][4]
            electron = 360 / asl
            for i in range(asl):
                tu.fd(cors[4])
                tu.stamp()
                tu.goto(0, 0)
                tu.rt(electron)

        if madar >= 6:
            tu.seth(90)
            asl = elct[0][5]
            electron = 360 / asl
            for i in range(asl):
                tu.fd(cors[5])
                tu.stamp()
                tu.goto(0, 0)
                tu.rt(electron)

        if madar >= 7:
            tu.seth(90)
            asl = elct[0][6]
            electron = 360 / asl
            for i in range(asl):
                tu.fd(cors[6])
                tu.stamp()
                tu.goto(0, 0)
                tu.rt(electron)
        
        tu.ht()
        
    t = Tk()
    t.geometry("950x600")
    t.resizable(False, False)
    
    frame = Frame(t)
    frame.grid(row = 0, column = 0)
    
    label_1 = Label(frame, text = 'Element Name: "{}"'.format(elements_name[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_2 = Label(frame, text = 'Element.[A]: "{}"'.format(adad_jermi[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_3 = Label(frame, text = 'Element.[Z]: "{}"'.format(nm), fg = "black", font = ("Arial", 16, "normal"))
    label_4 = Label(frame, text = 'Element.[Q]: "{}"'.format(bar_yoni[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_5 = Label(frame, text = 'Subatomic Particles:', fg = "black", font = ("Arial", 16, "normal"))
    button_1 = ttk.Button(frame, text = "Look", command = lambda main = n_p_e[nm - 1]: el(main[0], main[1], main[2]))
    label_6 = Label(frame, text = 'Number Of Isotopes: "{}"'.format(isotopes_number[nm - 1]), fg = "black", font = ("Arial", 14, "normal"))
    label_7 = Label(frame, text = 'Valence Number: "{}"'.format((group_period[nm - 1])[0]), fg = "black", font = ("Arial", 16, "normal"))
    label_8 = Label(frame, text = 'Valence electrons:"{}"'.format(electron_last_madar[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_9 = Label(frame, text = 'Group Number: "{}"'.format((group_period[nm - 1])[1]), fg = "black", font = ("Arial", 16, "normal"))
    label_10 = Label(frame, text = 'Period Number: "{}"'.format((group_period[nm - 1])[0]), fg = "black", font = ("Arial", 16, "normal"))
    label_11 = Label(frame, text = 'Phase At Room Temprature: "{}"'.format(state_room[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_12 = Label(frame, text = 'Melting Piont: "{}C`"'.format(zob_point[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_13 = Label(frame, text = 'Boiling Piont: "{}C`"'.format(josh_point[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_14 = Label(frame, text = 'Density: "{} g/cm~3"'.format(chegali[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_15 = Label(frame, text = 'Atomic Radius: "{} pm"'.format(sh_atomic[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_16 = Label(frame, text = 'Element Type: "{}"'.format(element_type[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_17 = Label(frame, text = 'Ionization Energy: "{} kj/mol"'.format(yonesh_energy[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_18 = Label(frame, text = 'Discovery Year: "{}"'.format(kashf[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))
    label_19 = Label(frame, text = 'Discoverer Name: "{}"'.format(discoverers[nm - 1]), fg = "black", font = ("Arial", 13, "normal"))
    label_20 = Label(frame, text = 'Discovery Location: "{}"'.format(discovery_locations[nm - 1]), fg = "black", font = ("Arial", 16, "normal"))


    label_1.grid(row = 0, column = 0, pady = 0, sticky = "w")
    label_2.grid(row = 1, column = 0, pady = 5, sticky = "w")
    label_3.grid(row = 2, column = 0, pady = 0, sticky = "w")
    label_4.grid(row = 3, column = 0, pady = 5, sticky = "w")
    label_5.grid(row = 4, column = 0, pady = 0, sticky = "w")
    button_1.grid(row = 4, padx = 210, pady = 5, sticky = "w")
    label_6.grid(row = 6, column = 0, pady = 0, sticky = "w")
    label_7.grid(row = 7, column = 0, pady = 5, sticky = "w")
    label_8.grid(row = 8, column = 0, pady = 0, sticky = "w")
    label_9.grid(row = 9, column = 0, pady = 5, sticky = "w")
    label_10.grid(row = 10, column = 0, pady = 0, sticky = "w")
    label_11.grid(row = 11, column = 0, pady = 5, sticky = "w")
    label_12.grid(row = 12, column = 0, pady = 0, sticky = "w")
    label_13.grid(row = 13, column = 0, pady = 5, sticky = "w")
    label_14.grid(row = 14, column = 0, pady = 0, sticky = "w")
    label_15.grid(row = 15, column = 0, pady = 5, sticky = "w")
    label_16.grid(row = 16, column = 0, pady = 0, sticky = "w")
    label_17.grid(row = 0, column = 3, padx = 10, sticky = "w")
    label_18.grid(row = 1, column = 3, padx = 10, sticky = "w")
    label_19.grid(row = 5, column = 0, pady = 5, sticky = "w")
    label_20.grid(row = 2, column = 3, padx = 10, sticky = "w")

    canvas = ScrolledCanvas(t, width = 300, height = 300)
    canvas.grid(row = 0, column = 0, columnspan = 5, padx = 400, sticky = "s")

    screenn = TurtleScreen(canvas)
    screenn.tracer(False)
    tu = RawTurtle(screenn)
    tu.speed(0)
    tu.home()

    draw_ar(tu, (group_period[nm - 1])[0], electron_madar_number[nm - 1])

    ttk.Button(t, text = "Exit", command = t.destroy).grid(row = 16, column = 5, padx = 220)


screen = Screen()
screen.setup(0, 0)
screen.tracer(0)

def draw(x, y, text, text2, text3, col, hum):
    main_coor.append((x, y, str(text)))
    hum.penup()
    hum.goto(x - 25,  y + 25)
    hum.pendown()
    hum.begin_fill()
    hum.color("black", col)
    hum.width(2)
    for i in range(4):
        hum.fd(50)
        hum.rt(90)
    hum.end_fill()
    hum.penup()
    hum.color("black")
    
    if text == "Mg" or text == "Sg" or text == "Rg" or text == "Hg" or text == "Og":
        hum.goto(x, y - 9)
        hum.write("{}".format(text), align = "center", font = ("Arial", 10, "normal"))
        hum.sety(hum.ycor() - 14)
        hum.write("{}".format(text2), align = "center", font = ("Arial", 8, "normal"))
        hum.sety(hum.ycor() + 30)
        hum.write("{}".format(text3), align = "center", font = ("Arial", 9, "normal"))
        
    else:
        hum.goto(x, y - 11)
        hum.write("{}".format(text), align = "center", font = ("Arial", 11, "normal"))
        hum.sety(hum.ycor() - 12)
        hum.write("{}".format(text2), align = "center", font = ("Arial", 8, "normal"))
        hum.sety(hum.ycor() + 30)
        hum.write("{}".format(text3), align = "center", font = ("Arial", 9, "normal"))
    

tr = Turtle()
tr.speed(0)
tr.penup()
tr.ht()

check = tr.clone()

vary = 0
H = 200

for i in range(118):
    draw(coors[vary], H, names[vary], jerm[vary], numbers[vary], colors[vary], tr)
    if names[vary] == "He" or names[vary] == "Ne" or names[vary] == "Ar" or names[vary] == "Kr" or names[vary] == "Xe" or names[vary] == "Rn" or  names[vary] == "Yb":
        H -= 50
    if names[vary] == "Og":
        H -= 100
    vary += 1

tr.goto(-510, 190)
for i in range(7):
    tr.write(str(i + 1), font = ("Arial", 16, "normal"))
    tr.sety(tr.ycor() - 50)

group_n = [(-450, 240), (-398, 185), (-350, 85), (-300, 85), (-250, 85), (-200, 85), (-150, 85),
           (-100, 85), (-50, 85), (0, 85), (50, 85), (100, 85), (150, 185), (200, 185), (250, 185),
           (300, 185), (350, 185), (400, 235)]

for i in group_n:
    tr.goto(i)
    tr.write(str(group_n.index(i) + 1), font = ("Arial", 16, "normal"), align = "center")

screen.title("=> Mendeleev Table :")

screen.onscreenclick(open_on)

screen.tracer(1)
screen.setup(1.0, 1.0)
screen.mainloop()
