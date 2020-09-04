from tinydb import TinyDB, Query


db = TinyDB('db.json')

print('Clearing database')

db.truncate()

# Bright Supergiants (Luminositu Class I / Ia)
# Load Blue-Tinted White

db.insert({'type': 'O0 I', 'lum': 2150000, 'mass': 130, 'diameter': 0.218, 'roche limit': 1.528, 'H-': 1101, 'H': 1324, 'H+': 2588, 'Frost Line': -1, 'Limit': 7150})
db.insert({'type': 'O1 I', 'lum': 2020000, 'mass': 125, 'diameter': 0.211, 'roche limit': 1.469, 'H-': 987, 'H': 1188, 'H+': 2322, 'Frost Line': -1, 'Limit': 6875})
db.insert({'type': 'O2 I', 'lum': 1890000, 'mass': 121, 'diameter': 0.207, 'roche limit': 1.422, 'H-': 926, 'H': 1114, 'H+': 2177, 'Frost Line': -1, 'Limit': 6655})
db.insert({'type': 'O3 I', 'lum': 1760000, 'mass': 117, 'diameter': 0.204, 'roche limit': 1.375, 'H-': 826, 'H': 994, 'H+': 1942, 'Frost Line': -1, 'Limit': 6435})
db.insert({'type': 'O4 I', 'lum': 1630000, 'mass': 113, 'diameter': 0.200, 'roche limit': 1.328, 'H-': 736, 'H': 886, 'H+': 1730, 'Frost Line': -1, 'Limit': 6215})
db.insert({'type': 'O5 I', 'lum': 1500000, 'mass': 109, 'diameter': 0.196, 'roche limit': 1.281, 'H-': 654, 'H': 787, 'H+': 1538, 'Frost Line': -1, 'Limit': 5995})
db.insert({'type': 'O6 Ia', 'lum': 1360000, 'mass': 90, 'diameter': 0.186, 'roche limit': 1.058, 'H-': 875, 'H': 1171, 'H+': 2059, 'Frost Line': -1, 'Limit': 4950})
db.insert({'type': 'O7 Ia', 'lum': 1120000, 'mass': 75, 'diameter': 0.200, 'roche limit': 0.882, 'H-': 795, 'H': 1040, 'H+': 1774, 'Frost Line': -1, 'Limit': 4125})
db.insert({'type': 'O8 Ia', 'lum': 913000, 'mass': 65, 'diameter': 0.214, 'roche limit': 0.764, 'H-': 717, 'H': 960, 'H+': 1687, 'Frost Line': -1, 'Limit': 3575})
db.insert({'type': 'O9 Ia', 'lum': 731000, 'mass': 55, 'diameter': 0.228, 'roche limit': 0.647, 'H-': 642, 'H': 859, 'H+': 1510, 'Frost Line': -1, 'Limit': 3025})

# Giant Stars (Luminosity Class III)

# White

db.insert({'type': 'F0 III', 'lum': 53, 'mass': 8, 'diameter': 0.022, 'roche limit': 0, 'H-': 5.47, 'H': 7.11, 'H+': 12.9, 'Frost Line': 35.3, 'Limit': 400})
db.insert({'type': 'F1 III', 'lum': 51, 'mass': 7.4, 'diameter': 0.023, 'roche limit': 0.087, 'H-': 5.36, 'H': 7.2, 'H+': 12.7, 'Frost Line': 34.7, 'Limit': 370})
db.insert({'type': 'F2 III', 'lum': 49, 'mass': 6.8, 'diameter': 0.023, 'roche limit': 0.08, 'H-': 5.26, 'H': 7.05, 'H+': 12.4, 'Frost Line': 34.0, 'Limit': 340})
db.insert({'type': 'F3 III', 'lum': 47, 'mass': 6.2, 'diameter': 0.024, 'roche limit': 0.073, 'H-': 5.15, 'H': 6.89, 'H+': 12.1, 'Frost Line': 33.3, 'Limit': 310})
db.insert({'type': 'F4 III', 'lum': 45, 'mass': 5.6, 'diameter': 0.024, 'roche limit': 0.066, 'H-': 5.04, 'H': 6.76, 'H+': 11.9, 'Frost Line': 32.6, 'Limit': 280})
db.insert({'type': 'F5 III', 'lum': 43, 'mass': 5, 'diameter': 0.025, 'roche limit': 0.056, 'H-': 4.93, 'H': 6.6, 'H+': 11.6, 'Frost Line': 31.8, 'Limit': 250})
db.insert({'type': 'F6 III', 'lum': 44, 'mass': 4.5, 'diameter': 0.026, 'roche limit': 0.053, 'H-': 4.98, 'H': 6.69, 'H+': 11.8, 'Frost Line': 32.2, 'Limit': 225})
db.insert({'type': 'F7 III', 'lum': 46, 'mass': 4, 'diameter': 0.028, 'roche limit': 0.047, 'H-': 5.09, 'H': 6.82, 'H+': 12.0, 'Frost Line': 32.9, 'Limit': 200})
db.insert({'type': 'F8 III', 'lum': 47, 'mass': 3.5, 'diameter': 0.03, 'roche limit': 0.042, 'H-': 5.15, 'H': 6.89, 'H+': 12.1, 'Frost Line': 33.3, 'Limit': 175})
db.insert({'type': 'F9 III', 'lum': 49, 'mass': 3, 'diameter': 0.032, 'roche limit': 0.035, 'H-': 5.26, 'H': 7.05, 'H+': 12.4, 'Frost Line': 34, 'Limit': 150})

# Orange

db.insert({'type': 'K0 III', 'lum': 95, 'mass': 4, 'diameter': 0.075, 'roche limit': 0, 'H-': 7.32, 'H': 9.82, 'H+': 17.3, 'Frost Line': 47.3, 'Limit': 200})
db.insert({'type': 'K1 III', 'lum': 140, 'mass': 4.2, 'diameter': 0.099, 'roche limit': 0, 'H-': 8.88, 'H': 11.9, 'H+': 20.9, 'Frost Line': 57.4, 'Limit': 210})
db.insert({'type': 'K2 III', 'lum': 185, 'mass': 4.4, 'diameter': 0.123, 'roche limit': 0, 'H-': 10.3, 'H': 13.8, 'H+': 24, 'Frost Line': 66, 'Limit': 220})
db.insert({'type': 'K3 III', 'lum': 230, 'mass': 4.6, 'diameter': 0.147, 'roche limit': 0, 'H-': 11.4, 'H': 15.3, 'H+': 26.8, 'Frost Line': 73.6, 'Limit': 230})
db.insert({'type': 'K4 III', 'lum': 275, 'mass': 4.8, 'diameter': 0.172, 'roche limit': 0, 'H-': 12.5, 'H': 16.7, 'H+': 29.3, 'Frost Line': 80.5, 'Limit': 240})
db.insert({'type': 'K5 III', 'lum': 320, 'mass': 5, 'diameter': 0.196, 'roche limit': 0, 'H-': 13.5, 'H': 18.1, 'H+': 31.6, 'Frost Line': 86.8, 'Limit': 250})
db.insert({'type': 'K6 III', 'lum': 350, 'mass': 5.26, 'diameter': 0.215, 'roche limit': 0, 'H-': 14.1, 'H': 18.9, 'H+': 33.1, 'Frost Line': 90.1, 'Limit': 263})
db.insert({'type': 'K7 III', 'lum': 380, 'mass': 5.52, 'diameter': 0.225, 'roche limit': 0, 'H-': 14.7, 'H': 19.7, 'H+': 34.5, 'Frost Line': 94.6, 'Limit': 276})
db.insert({'type': 'K8 III', 'lum': 410, 'mass': 5.78, 'diameter': 0.254, 'roche limit': 0, 'H-': 15.2, 'H': 20.4, 'H+': 35.8, 'Frost Line': 98.2, 'Limit': 289})
db.insert({'type': 'K9 III', 'lum': 440, 'mass': 6.04, 'diameter': 0.274, 'roche limit': 0, 'H-': 15.8, 'H': 21.2, 'H+': 37.1, 'Frost Line': 102, 'Limit': 302})

# Red

db.insert({'type': 'M0 III', 'lum': 470, 'mass': 6.3, 'diameter': 0.293, 'roche limit': 0, 'H-': 16.3, 'H': 21.8, 'H+': 38.3, 'Frost Line': 106, 'Limit': 315})
db.insert({'type': 'M1 III', 'lum': 832, 'mass': 6.52, 'diameter': 0.447, 'roche limit': 0, 'H-': 21.7, 'H': 29.0, 'H+': 50.9, 'Frost Line': 140, 'Limit': 326})
db.insert({'type': 'M2 III', 'lum': 1194, 'mass': 6.74, 'diameter': 0.6, 'roche limit': 0, 'H-': 25.9, 'H': 34.7, 'H+': 61, 'Frost Line': 168, 'Limit': 337})
db.insert({'type': 'M3 III', 'lum': 1556, 'mass': 6.96, 'diameter': 0.754, 'roche limit': 0, 'H-': 29.6, 'H': 39.7, 'H+': 69.7, 'Frost Line': 192, 'Limit': 348})
db.insert({'type': 'M4 III', 'lum': 1918, 'mass': 7.18, 'diameter': 0.907, 'roche limit': 0, 'H-': 32.9, 'H': 44, 'H+': 77.3, 'Frost Line': 213, 'Limit': 359})
db.insert({'type': 'M5 III', 'lum': 2280, 'mass': 7.40, 'diameter': 1.06, 'roche limit': 0, 'H-': 35.9, 'H': 48, 'H+': 84.3, 'Frost Line': 232, 'Limit': 370})
db.insert({'type': 'M6 III', 'lum': 2382, 'mass': 7.85, 'diameter': 1.214, 'roche limit': 0, 'H-': 36.7, 'H': 49.1, 'H+': 86.2, 'Frost Line': 237, 'Limit': 392})
db.insert({'type': 'M7 III', 'lum': 2485, 'mass': 8.3, 'diameter': 1.368, 'roche limit': 0, 'H-': 37.4, 'H': 50.1, 'H+': 88, 'Frost Line': 242, 'Limit': 415})
db.insert({'type': 'M8 III', 'lum': 2587, 'mass': 8.75, 'diameter': 1.521, 'roche limit': 0, 'H-': 38.2, 'H': 51.1, 'H+': 89.8, 'Frost Line': 247, 'Limit': 437})
db.insert({'type': 'M9 III', 'lum': 2690, 'mass': 9.2, 'diameter': 1.675, 'roche limit': 0, 'H-': 39.0, 'H': 52.2, 'H+': 91.6, 'Frost Line': 252, 'Limit': 460})

# Subgiant Stars (Luminosity Class iV)

# Blue-White

db.insert({'type': 'O0 IV', 'lum': 1360000, 'mass': 100, 'diameter': 0.159, 'roche limit': 1.175, 'H-': 835, 'H': 1171, 'H+': 2059, 'Frost Line': -1, 'Limit': 5500})
db.insert({'type': 'O1 IV', 'lum': 1090000, 'mass': 97, 'diameter': 0.145, 'roche limit': 1.140, 'H-': 784, 'H': 1049, 'H+': 1843, 'Frost Line': -1, 'Limit': 4850})
db.insert({'type': 'O2 IV', 'lum': 872000, 'mass': 95, 'diameter': 0.132, 'roche limit': 1.117, 'H-': 701, 'H': 938, 'H+': 1649, 'Frost Line': -1, 'Limit': 4750})
db.insert({'type': 'O3 IV', 'lum': 696000, 'mass': 93, 'diameter': 0.118, 'roche limit': 1.093, 'H-': 626, 'H': 838, 'H+': 1473, 'Frost Line': -1, 'Limit': 4650})
db.insert({'type': 'O4 IV', 'lum': 552000, 'mass': 89, 'diameter': 0.105, 'roche limit': 1.046, 'H-': 558, 'H': 747, 'H+': 1312, 'Frost Line': -1, 'Limit': 4450})
db.insert({'type': 'O5 IV', 'lum': 437000, 'mass': 77, 'diameter': 0.091, 'roche limit': 0.905, 'H-': 496, 'H': 664, 'H+': 1167, 'Frost Line': -1, 'Limit': 3850})
db.insert({'type': 'O6 IV', 'lum': 313000, 'mass': 55, 'diameter': 0.085, 'roche limit': 0.647, 'H-': 420, 'H': 562, 'H+': 988, 'Frost Line': -1, 'Limit': 2750})
db.insert({'type': 'O7 IV', 'lum': 223000, 'mass': 44, 'diameter': 0.079, 'roche limit': 0.517, 'H-': 355, 'H': 475, 'H+': 834, 'Frost Line': -1, 'Limit': 2250})
db.insert({'type': 'O8 IV', 'lum': 157000, 'mass': 34, 'diameter': 0.071, 'roche limit': 0.400, 'H-': 298, 'H': 399, 'H+': 700, 'Frost Line': -1, 'Limit': 1700})
db.insert({'type': 'O9 IV', 'lum': 110000, 'mass': 27, 'diameter': 0.067, 'roche limit': 0.318, 'H-': 249, 'H': 333, 'H+': 585, 'Frost Line': -1, 'Limit': 1350})

# Blue-White

db.insert({'type': 'B0 IV', 'lum': 81000, 'mass': 20, 'diameter': 0.061, 'roche limit': 0.215, 'H-': 214, 'H': 287, 'H+': 503, 'Frost Line': -1, 'Limit': 1000})
db.insert({'type': 'B1 IV', 'lum': 65200, 'mass': 18, 'diameter': 0.054, 'roche limit': 0.212, 'H-': 192, 'H': 257, 'H+': 451, 'Frost Line': -1, 'Limit': 900})
db.insert({'type': 'B2 IV', 'lum': 49400, 'mass': 16, 'diameter': 0.047, 'roche limit': 0.188, 'H-': 167, 'H': 224, 'H+': 392, 'Frost Line': -1, 'Limit': 800})
db.insert({'type': 'B3 IV', 'lum': 33600, 'mass': 14, 'diameter': 0.039, 'roche limit': 0.165, 'H-': 138, 'H': 185, 'H+': 324, 'Frost Line': -1, 'Limit': 700})
db.insert({'type': 'B4 IV', 'lum': 17800, 'mass': 12, 'diameter': 0.032, 'roche limit': 0.141, 'H-': 101, 'H': 135, 'H+': 236, 'Frost Line': -1, 'Limit': 600})
db.insert({'type': 'B5 IV', 'lum': 2000, 'mass': 10, 'diameter': 0.025, 'roche limit': 0.118, 'H-': 33.6, 'H': 45, 'H+': 79, 'Frost Line': 217, 'Limit': 500})
db.insert({'type': 'B6 IV', 'lum': 1632, 'mass': 9.2, 'diameter': 0.024, 'roche limit': 0.109, 'H-': 30.4, 'H': 40.7, 'H+': 71.3, 'Frost Line': 196, 'Limit': 460})
db.insert({'type': 'B7 IV', 'lum': 1263, 'mass': 8.4, 'diameter': 0.024, 'roche limit': 0.099, 'H-': 26.7, 'H': 35.8, 'H+': 62.8, 'Frost Line': 173, 'Limit': 420})
db.insert({'type': 'B8 IV', 'lum': 894, 'mass': 7.6, 'diameter': 0.0023, 'roche limit': 0.09, 'H-': 22.5, 'H': 30.1, 'H+': 52.8, 'Frost Line': 145, 'Limit': 380})
db.insert({'type': 'B9 IV', 'lum': 525, 'mass': 6.8, 'diameter': 0.0022, 'roche limit': 0.08, 'H-': 17.2, 'H': 23.1, 'H+': 40.5, 'Frost Line': 112, 'Limit': 340})

# Blue-White

db.insert({'type': 'A0 IV', 'lum': 156, 'mass': 6, 'diameter': 0.021, 'roche limit': 0.071, 'H-': 9.38, 'H': 12.6, 'H+': 22.1, 'Frost Line': 60.6, 'Limit': 300})
db.insert({'type': 'A1 IV', 'lum': 133, 'mass': 5.6, 'diameter': 0.020, 'roche limit': 0.066, 'H-': 8.66, 'H': 11.6, 'H+': 20.1, 'Frost Line': 56, 'Limit': 280})
db.insert({'type': 'A2 IV', 'lum': 109, 'mass': 5.2, 'diameter': 0.018, 'roche limit': 0.062, 'H-': 7.84, 'H': 10.5, 'H+': 18.4, 'Frost Line': 50.7, 'Limit': 260})
db.insert({'type': 'A3 IV', 'lum': 84.6, 'mass': 4.8, 'diameter': 0.016, 'roche limit': 0.057, 'H-': 6.91, 'H': 9.26, 'H+': 16.3, 'Frost Line': 44.6, 'Limit': 240})
db.insert({'type': 'A4 IV', 'lum': 60.8, 'mass': 4.4, 'diameter': 0.015, 'roche limit': 0.052, 'H-': 5.86, 'H': 7.85, 'H+': 13.8, 'Frost Line': 37.9, 'Limit': 220})
db.insert({'type': 'A5 IV', 'lum': 37, 'mass': 4.0, 'diameter': 0.013, 'roche limit': 0.047, 'H-': 4.57, 'H': 6.13, 'H+': 10.8, 'Frost Line': 29.5, 'Limit': 200})
db.insert({'type': 'A6 IV', 'lum': 33.4, 'mass': 3.7, 'diameter': 0.013, 'roche limit': 0.044, 'H-': 4.34, 'H': 5.81, 'H+': 10.2, 'Frost Line': 28, 'Limit': 185})
db.insert({'type': 'A7 IV', 'lum': 29.8, 'mass': 3.4, 'diameter': 0.013, 'roche limit': 0.04, 'H-': 4.10, 'H': 5.49, 'H+': 9.64, 'Frost Line': 26.5, 'Limit': 170})
db.insert({'type': 'A8 IV', 'lum': 26.2, 'mass': 3.1, 'diameter': 0.0013, 'roche limit': 0.037, 'H-': 3.85, 'H': 5.15, 'H+': 9.04, 'Frost Line': 24.9, 'Limit': 155})
db.insert({'type': 'A9 IV', 'lum': 22.6, 'mass': 2.8, 'diameter': 0.0013, 'roche limit': 0.033, 'H-': 3.57, 'H': 4.78, 'H+': 8.4, 'Frost Line': 23.1, 'Limit': 140})

# Main Sequence Stars (Luminosity Class V)

# Blue-White

db.insert({'type': 'O0 V', 'lum': 1240000, 'mass': 100, 'diameter': 0.093, 'roche limit': 1.175, 'H-': 835, 'H': 1118, 'H+': 1965, 'Frost Line': -1, 'Limit': 5000})
db.insert({'type': 'O1 V', 'lum': 994000, 'mass': 97.5, 'diameter': 0.089, 'roche limit': 1.146, 'H-': 748, 'H': 1001, 'H+': 1759, 'Frost Line': -1, 'Limit': 4875})
db.insert({'type': 'O2 V', 'lum': 795000, 'mass': 95, 'diameter': 0.083, 'roche limit': 1.117, 'H-': 669, 'H': 875, 'H+': 1492, 'Frost Line': -1, 'Limit': 4750})
db.insert({'type': 'O3 V', 'lum': 634000, 'mass': 92.5, 'diameter': 0.079, 'roche limit': 1.087, 'H-': 597, 'H': 799, 'H+': 1405, 'Frost Line': -1, 'Limit': 4625})
db.insert({'type': 'O4 V', 'lum': 504000, 'mass': 90, 'diameter': 0.075, 'roche limit': 1.058, 'H-': 532, 'H': 713, 'H+': 1253, 'Frost Line': -1, 'Limit': 4500})
db.insert({'type': 'O5 V', 'lum': 398000, 'mass': 60, 'diameter': 0.07, 'roche limit': 0.705, 'H-': 473, 'H': 633, 'H+': 1113, 'Frost Line': -1, 'Limit': 3000})
db.insert({'type': 'O6 V', 'lum': 260000, 'mass': 37, 'diameter': 0.066, 'roche limit': 0.435, 'H-': 382, 'H': 512, 'H+': 900, 'Frost Line': -1, 'Limit': 1850})
db.insert({'type': 'O7 V', 'lum': 154000, 'mass': 30, 'diameter': 0.061, 'roche limit': 0.353, 'H-': 294, 'H': 394, 'H+': 692, 'Frost Line': -1, 'Limit': 1500})
db.insert({'type': 'O8 V', 'lum': 99100, 'mass': 23, 'diameter': 0.056, 'roche limit': 0.271, 'H-': 238, 'H': 316, 'H+': 556, 'Frost Line': -1, 'Limit': 1150})
db.insert({'type': 'O9 V', 'lum': 57600, 'mass': 20, 'diameter': 0.052, 'roche limit': 0.235, 'H-': 180, 'H': 245, 'H+': 424, 'Frost Line': -1, 'Limit': 1000})

# Blue-White

db.insert({'type': 'B0 V', 'lum': 36200, 'mass': 17.5, 'diameter': 0.0047, 'roche limit': 0.206, 'H-': 143, 'H': 192, 'H+': 336, 'Frost Line': -1, 'Limit': 875})
db.insert({'type': 'B1 V', 'lum': 19400, 'mass': 14.2, 'diameter': 0.0042, 'roche limit': 0.167, 'H-': 104, 'H': 140, 'H+': 246, 'Frost Line': 676, 'Limit': 710})
db.insert({'type': 'B2 V', 'lum': 9360, 'mass': 10.9, 'diameter': 0.0035, 'roche limit': 0.129, 'H-': 72, 'H': 97, 'H+': 171, 'Frost Line': 470, 'Limit': 545})
db.insert({'type': 'B3 V', 'lum': 4890, 'mass': 7.6, 'diameter': 0.031, 'roche limit': 0.09, 'H-': 53, 'H': 71, 'H+': 124, 'Frost Line': 340, 'Limit': 380})
db.insert({'type': 'B4 V', 'lum': 2290, 'mass': 6.7, 'diameter': 0.026, 'roche limit': 0.079, 'H-': 36, 'H': 49, 'H+': 85, 'Frost Line': 233, 'Limit': 335})
db.insert({'type': 'B5 V', 'lum': 1160, 'mass': 5.9, 'diameter': 0.021, 'roche limit': 0.07, 'H-': 26, 'H': 35, 'H+': 61, 'Frost Line': 166, 'Limit': 295})
db.insert({'type': 'B6 V', 'lum': 692, 'mass': 5.2, 'diameter': 0.02, 'roche limit': 0.062, 'H-': 20, 'H': 27, 'H+': 47, 'Frost Line': 128, 'Limit': 260})
db.insert({'type': 'B7 V', 'lum': 404, 'mass': 4.5, 'diameter': 0.019, 'roche limit': 0.053, 'H-': 16, 'H': 21, 'H+': 36, 'Frost Line': 97.5, 'Limit': 225})
db.insert({'type': 'B8 V', 'lum': 211, 'mass': 4.1, 'diameter': 0.018, 'roche limit': 0.049, 'H-': 11, 'H': 15, 'H+': 26, 'Frost Line': 70.5, 'Limit': 205})
db.insert({'type': 'B9 V', 'lum': 119, 'mass': 3.8, 'diameter': 0.016, 'roche limit': 0.045, 'H-': 8.2, 'H': 11, 'H+': 20, 'Frost Line': 52.9, 'Limit': 190})

# Blue-White

db.insert({'type': 'A0 V', 'lum': 90, 'mass': 3.5, 'diameter': 0.0149, 'roche limit': 0.0412, 'H-': 7.2, 'H': 9.6, 'H+': 17, 'Frost Line': 46, 'Limit': 175})
db.insert({'type': 'A1 V', 'lum': 75.2, 'mass': 3.22, 'diameter': 0.0136, 'roche limit': 0.0379, 'H-': 6.6, 'H': 8.4, 'H+': 16, 'Frost Line': 42, 'Limit': 161})
db.insert({'type': 'A2 V', 'lum': 60.4, 'mass': 2.94, 'diameter': 0.0123, 'roche limit': 0.0346, 'H-': 5.9, 'H': 7.9, 'H+': 14, 'Frost Line': 37.7, 'Limit': 147})
db.insert({'type': 'A3 V', 'lum': 45.6, 'mass': 2.66, 'diameter': 0.011, 'roche limit': 0.0313, 'H-': 5.1, 'H': 6.9, 'H+': 12, 'Frost Line': 32.8, 'Limit': 133})
db.insert({'type': 'A4 V', 'lum': 30.8, 'mass': 2.38, 'diameter': 0.0097, 'roche limit': 0.028, 'H-': 4.2, 'H': 5.6, 'H+': 9.8, 'Frost Line': 27.0, 'Limit': 119})
db.insert({'type': 'A5 V', 'lum': 16, 'mass': 2.1, 'diameter': 0.0084, 'roche limit': 0.0247, 'H-': 3.1, 'H': 4.1, 'H+': 7.1, 'Frost Line': 19.4, 'Limit': 105})
db.insert({'type': 'A6 V', 'lum': 14.42, 'mass': 2.02, 'diameter': 0.0083, 'roche limit': 0.0238, 'H-': 2.9, 'H': 3.9, 'H+': 6.7, 'Frost Line': 18.5, 'Limit': 101})
db.insert({'type': 'A7 V', 'lum': 12.84, 'mass': 1.94, 'diameter': 0.0082, 'roche limit': 0.0228, 'H-': 2.7, 'H': 3.7, 'H+': 6.4, 'Frost Line': 17.5, 'Limit': 97})
db.insert({'type': 'A8 V', 'lum': 11.26, 'mass': 1.86, 'diameter': 0.0081, 'roche limit': 0.0219, 'H-': 2.6, 'H': 3.5, 'H+': 6.0, 'Frost Line': 16.3, 'Limit': 93})
db.insert({'type': 'A9 V', 'lum': 9.68, 'mass': 1.78, 'diameter': 0.0080, 'roche limit': 0.021, 'H-': 2.4, 'H': 3.2, 'H+': 5.5, 'Frost Line': 15.1, 'Limit': 89})

# White

db.insert({'type': 'F0 V', 'lum': 8.1, 'mass': 1.7, 'diameter': 0.0079, 'roche limit': 0.0200, 'H-': 2.2, 'H': 2.9, 'H+': 5.1, 'Frost Line': 13.8, 'Limit': 68})
db.insert({'type': 'F1 V', 'lum': 7.18, 'mass': 1.62, 'diameter': 0.0077, 'roche limit': 0.0191, 'H-': 2.1, 'H': 2.8, 'H+': 4.8, 'Frost Line': 13.0, 'Limit': 65})
db.insert({'type': 'F2 V', 'lum': 6.26, 'mass': 1.54, 'diameter': 0.0074, 'roche limit': 0.0181, 'H-': 1.9, 'H': 2.6, 'H+': 4.5, 'Frost Line': 12.14, 'Limit': 62})
db.insert({'type': 'F3 V', 'lum': 5.34, 'mass': 1.46, 'diameter': 0.0071, 'roche limit': 0.0172, 'H-': 1.8, 'H': 2.4, 'H+': 4.1, 'Frost Line': 11.21, 'Limit': 59})
db.insert({'type': 'F4 V', 'lum': 4.42, 'mass': 1.38, 'diameter': 0.0068, 'roche limit': 0.0163, 'H-': 1.6, 'H': 2.2, 'H+': 3.8, 'Frost Line': 10.2, 'Limit': 56})
db.insert({'type': 'F5 V', 'lum': 3.5, 'mass': 1.3, 'diameter': 0.0066, 'roche limit': 0.0153, 'H-': 1.5, 'H': 2.0, 'H+': 3.3, 'Frost Line': 9.08, 'Limit': 59})
db.insert({'type': 'F6 V', 'lum': 3.042, 'mass': 1.248, 'diameter': 0.0062, 'roche limit': 0.0147, 'H-': 1.4, 'H': 1.9, 'H+': 3.1, 'Frost Line': 8.46, 'Limit': 50})
db.insert({'type': 'F7 V', 'lum': 2.584, 'mass': 1.196, 'diameter': 0.0059, 'roche limit': 0.0141, 'H-': 1.3, 'H': 1.7, 'H+': 3.1, 'Frost Line': 7.80, 'Limit': 48})
db.insert({'type': 'F8 V', 'lum': 2.126, 'mass': 1.144, 'diameter': 0.0055, 'roche limit': 0.0135, 'H-': 1.1, 'H': 1.5, 'H+': 2.6, 'Frost Line': 7.08, 'Limit': 46})
db.insert({'type': 'F9 V', 'lum': 1.668, 'mass': 1.092, 'diameter': 0.0052, 'roche limit': 0.0129, 'H-': 1.0, 'H': 1.4, 'H+': 2.3, 'Frost Line': 6.27, 'Limit': 44})

# Yellow

db.insert({'type': 'G0 V', 'lum': 1.21, 'mass': 1.040, 'diameter': 0.0048, 'roche limit': 0.0123, 'H-': 0.83, 'H': 1.10, 'H+': 1.95, 'Frost Line': 5.34, 'Limit': 52})
db.insert({'type': 'G1 V', 'lum': 1.102, 'mass': 1.020, 'diameter': 0.0048, 'roche limit': 0.0120, 'H-': 0.79, 'H': 1.05, 'H+': 1.86, 'Frost Line': 5.10, 'Limit': 51})
db.insert({'type': 'G2 V', 'lum': 0.994, 'mass': 1, 'diameter': 0.0047, 'roche limit': 0.0118, 'H-': 0.75, 'H': 1, 'H+': 1.76, 'Frost Line': 4.84, 'Limit': 50})
db.insert({'type': 'G3 V', 'lum': 0.886, 'mass': 0.98, 'diameter': 0.0045, 'roche limit': 0.0116, 'H-': 0.71, 'H': 0.95, 'H+': 1.67, 'Frost Line': 4.57, 'Limit': 49})
db.insert({'type': 'G4 V', 'lum': 0.778, 'mass': 0.96, 'diameter': 0.0044, 'roche limit': 0.0113, 'H-': 0.67, 'H': 0.90, 'H+': 1.58, 'Frost Line': 4.28, 'Limit': 48})
db.insert({'type': 'G5 V', 'lum': 0.67, 'mass': 0.94, 'diameter': 0.0043, 'roche limit': 0.0111, 'H-': 0.62, 'H': 0.84, 'H+': 1.45, 'Frost Line': 3.97, 'Limit': 47})
db.insert({'type': 'G6 V', 'lum': 0.62, 'mass': 0.917, 'diameter': 0.0043, 'roche limit': 0.0108, 'H-': 0.59, 'H': 0.79, 'H+': 1.39, 'Frost Line': 3.82, 'Limit': 46})
db.insert({'type': 'G7 V', 'lum': 0.57, 'mass': 0.894, 'diameter': 0.0043, 'roche limit': 0.0106, 'H-': 0.57, 'H': 0.76, 'H+': 1.34, 'Frost Line': 3.67, 'Limit': 45})
db.insert({'type': 'G8 V', 'lum': 0.52, 'mass': 0.871, 'diameter': 0.0043, 'roche limit': 0.0103, 'H-': 0.54, 'H': 0.73, 'H+': 1.28, 'Frost Line': 3.50, 'Limit': 44})
db.insert({'type': 'G9 V', 'lum': 0.47, 'mass': 0.848, 'diameter': 0.0043, 'roche limit': 0.0100, 'H-': 0.52, 'H': 0.7, 'H+': 1.21, 'Frost Line': 3.33, 'Limit': 43})

# Orange

db.insert({'type': 'K0 V', 'lum': 0.420, 'mass': 0.825, 'diameter': 0.0043, 'roche limit': 0.0097, 'H-': 0.49, 'H': 0.66, 'H+': 1.15, 'Frost Line': 3.15, 'Limit': 42})
db.insert({'type': 'K1 V', 'lum': 0.352, 'mass': 0.774, 'diameter': 0.0039, 'roche limit': 0.0091, 'H-': 0.45, 'H': 0.6, 'H+': 1.05, 'Frost Line': 2.88, 'Limit': 39})
db.insert({'type': 'K2 V', 'lum': 0.284, 'mass': 0.723, 'diameter': 0.0036, 'roche limit': 0.0085, 'H-': 0.4, 'H': 0.54, 'H+': 0.95, 'Frost Line': 2.59, 'Limit': 36})
db.insert({'type': 'K3 V', 'lum': 0.216, 'mass': 0.672, 'diameter': 0.0033, 'roche limit': 0.0079, 'H-': 0.36, 'H': 0.47, 'H+': 0.82, 'Frost Line': 2.26, 'Limit': 34})
db.insert({'type': 'K4 V', 'lum': 0.148, 'mass': 0.621, 'diameter': 0.003, 'roche limit': 0.0073, 'H-': 0.29, 'H': 0.39, 'H+': 0.68, 'Frost Line': 1.87, 'Limit': 31})
db.insert({'type': 'K5 V', 'lum': 0.08, 'mass': 0.57, 'diameter': 0.0027, 'roche limit': 0.0069, 'H-': 0.21, 'H': 0.29, 'H+': 0.5, 'Frost Line': 1.38, 'Limit': 29})
db.insert({'type': 'K6 V', 'lum': 0.072, 'mass': 0.558, 'diameter': 0.0027, 'roche limit': 0.0066, 'H-': 0.20, 'H': 0.27, 'H+': 0.48, 'Frost Line': 1.31, 'Limit': 28})
db.insert({'type': 'K7 V', 'lum': 0.064, 'mass': 0.537, 'diameter': 0.0026, 'roche limit': 0.0063, 'H-': 0.19, 'H': 0.26, 'H+': 0.45, 'Frost Line': 1.23, 'Limit': 27})
db.insert({'type': 'K8 V', 'lum': 0.056, 'mass': 0.522, 'diameter': 0.0026, 'roche limit': 0.0062, 'H-': 0.18, 'H': 0.24, 'H+': 0.42, 'Frost Line': 1.15, 'Limit': 26})
db.insert({'type': 'K9 V', 'lum': 0.048, 'mass': 0.506, 'diameter': 0.0026, 'roche limit': 0.0060, 'H-': 0.17, 'H': 0.23, 'H+': 0.39, 'Frost Line': 1.07, 'Limit': 25})

# Red

db.insert({'type': 'M0 V', 'lum': 0.040, 'mass': 0.489, 'diameter': 0.0058, 'roche limit': 0.0058, 'H-': 0.15, 'H': 0.21, 'H+': 0.36, 'Frost Line': 0.97, 'Limit': 24})
db.insert({'type': 'M1 V', 'lum': 0.034, 'mass': 0.458, 'diameter': 0.0054, 'roche limit': 0.0054, 'H-': 0.14, 'H': 0.18, 'H+': 0.32, 'Frost Line': 0.895, 'Limit': 23})
db.insert({'type': 'M2 V', 'lum': 0.027, 'mass': 0.426, 'diameter': 0.0051, 'roche limit': 0.0051, 'H-': 0.13, 'H': 0.15, 'H+': 0.28, 'Frost Line': 0.797, 'Limit': 21})
db.insert({'type': 'M3 V', 'lum': 0.021, 'mass': 0.395, 'diameter': 0.0047, 'roche limit': 0.0047, 'H-': 0.11, 'H': 0.13, 'H+': 0.24, 'Frost Line': 0.703, 'Limit': 19})
db.insert({'type': 'M4 V', 'lum': 0.012, 'mass': 0.363, 'diameter': 0.0043, 'roche limit': 0.0043, 'H-': 0.09, 'H': 0.11, 'H+': 0.20, 'Frost Line': 0.532, 'Limit': 16})
db.insert({'type': 'M5 V', 'lum': 0.007, 'mass': 0.331, 'diameter': 0.0039, 'roche limit': 0.0039, 'H-': 0.07, 'H': 0.09, 'H+': 0.16, 'Frost Line': 0.406, 'Limit': 15})
db.insert({'type': 'M6 V', 'lum': 0.006, 'mass': 0.302, 'diameter': 0.0036, 'roche limit': 0.0036, 'H-': 0.05, 'H': 0.07, 'H+': 0.12, 'Frost Line': 0.376, 'Limit': 14})
db.insert({'type': 'M7 V', 'lum': 0.004, 'mass': 0.273, 'diameter': 0.0032, 'roche limit': 0.0032, 'H-': 0.04, 'H': 0.05, 'H+': 0.09, 'Frost Line': 0.307, 'Limit': 13})
db.insert({'type': 'M8 V', 'lum': 0.003, 'mass': 0.244, 'diameter': 0.0029, 'roche limit': 0.0029, 'H-': 0.03, 'H': 0.04, 'H+': 0.07, 'Frost Line': 0.266, 'Limit': 12})
db.insert({'type': 'M9 V', 'lum': 0.001, 'mass': 0.215, 'diameter': 0.0026, 'roche limit': 0.0026, 'H-': 0.02, 'H': 0.03, 'H+': 0.06, 'Frost Line': 0.154, 'Limit': 11})

# Subdwarf Stars (Luminosity Class VI)

# White

db.insert({'type': 'F5 VI', 'lum': 0.977, 'mass': 0.8, 'diameter': 0.0053, 'roche limit': 0.0094, 'H-': 0.75, 'H': 1, 'H+': 1.75, 'Frost Line': 4.8, 'Limit': 40})
db.insert({'type': 'F6 VI', 'lum': 0.846, 'mass': 0.76, 'diameter': 0.0052, 'roche limit': 0.009, 'H-': 0.69, 'H': 0.03, 'H+': 1.63, 'Frost Line': 4.46, 'Limit': 38})
db.insert({'type': 'F7 VI', 'lum': 0.715, 'mass': 0.72, 'diameter': 0.0051, 'roche limit': 0.0085, 'H-': 0.64, 'H': 0.86, 'H+': 1.5, 'Frost Line': 4.11, 'Limit': 36})
db.insert({'type': 'F8 VI', 'lum': 0.584, 'mass': 0.68, 'diameter': 0.005, 'roche limit': 0.008, 'H-': 0.58, 'H': 0.78, 'H+': 1.35, 'Frost Line': 3.71, 'Limit': 34})
db.insert({'type': 'F9 VI', 'lum': 0.453, 'mass': 0.64, 'diameter': 0.0049, 'roche limit': 0.0076, 'H-': 0.51, 'H': 0.68, 'H+': 1.19, 'Frost Line': 3.27, 'Limit': 32})

# Yellow

db.insert({'type': 'G0 VI', 'lum': 0.322, 'mass': 0.6, 'diameter': 0.0048, 'roche limit': 0.0071, 'H-': 0.43, 'H': 0.57, 'H+': 1, 'Frost Line': 2.76, 'Limit': 30})
db.insert({'type': 'G1 VI', 'lum': 0.295, 'mass': 0.586, 'diameter': 0.0043, 'roche limit': 0.0069, 'H-': 0.41, 'H': 0.55, 'H+': 0.96, 'Frost Line': 2.64, 'Limit': 29})
db.insert({'type': 'G2 VI', 'lum': 0.268, 'mass': 0.571, 'diameter': 0.0039, 'roche limit': 0.0068, 'H-': 0.39, 'H': 0.52, 'H+': 0.91, 'Frost Line': 2.52, 'Limit': 29})
db.insert({'type': 'G3 VI', 'lum': 0.24, 'mass': 0.557, 'diameter': 0.0035, 'roche limit': 0.0066, 'H-': 0.37, 'H': 0.5, 'H+': 0.87, 'Frost Line': 2.38, 'Limit': 28})
db.insert({'type': 'G4 VI', 'lum': 0.213, 'mass': 0.542, 'diameter': 0.003, 'roche limit': 0.0064, 'H-': 0.35, 'H': 0.47, 'H+': 0.82, 'Frost Line': 2.24, 'Limit': 27})
db.insert({'type': 'G5 VI', 'lum': 0.186, 'mass': 0.528, 'diameter': 0.0026, 'roche limit': 0.0062, 'H-': 0.33, 'H': 0.44, 'H+': 0.76, 'Frost Line': 2.1, 'Limit': 26})
db.insert({'type': 'G6 VI', 'lum': 0.172, 'mass': 0.508, 'diameter': 0.0025, 'roche limit': 0.006, 'H-': 0.31, 'H': 0.42, 'H+': 0.73, 'Frost Line': 2.02, 'Limit': 25})
db.insert({'type': 'G7 VI', 'lum': 0.158, 'mass': 0.489, 'diameter': 0.0023, 'roche limit': 0.0058, 'H-': 0.3, 'H': 0.4, 'H+': 0.7, 'Frost Line': 1.93, 'Limit': 24})
db.insert({'type': 'G8 VI', 'lum': 0.145, 'mass': 0.469, 'diameter': 0.0022, 'roche limit': 0.0056, 'H-': 0.29, 'H': 0.39, 'H+': 0.67, 'Frost Line': 1.85, 'Limit': 23})
db.insert({'type': 'G9 VI', 'lum': 0.131, 'mass': 0.45, 'diameter': 0.0021, 'roche limit': 0.0053, 'H-': 0.27, 'H': 0.37, 'H+': 0.64, 'Frost Line': 1.76, 'Limit': 22})


# Dwarf Stars

db.insert({'type': 'D0', 'lum': 0.046, 'mass': 1.4, 'diameter': 0.0017, 'roche limit': 0.0165, 'H-': 0.161, 'H': 0.216, 'H+': 0.379, 'Frost Line': 1.042, 'Limit': 70})
db.insert({'type': 'D1', 'lum': 0.0265, 'mass': 1.1, 'diameter': 0.0016, 'roche limit': 0.013, 'H-': 0.122, 'H': 0.164, 'H+': 0.287, 'Frost Line': 0.789, 'Limit': 55})
db.insert({'type': 'D2', 'lum': 0.0165, 'mass': 0.986, 'diameter': 0.0015, 'roche limit': 0.0116, 'H-': 0.096, 'H': 0.129, 'H+': 0.227, 'Frost Line': 0.623, 'Limit': 50})
db.insert({'type': 'D3', 'lum': 0.006, 'mass': 0.872, 'diameter': 0.0014, 'roche limit': 0.0103, 'H-': 0.058, 'H': 0.078, 'H+': 0.137, 'Frost Line': 0.376, 'Limit': 44})
db.insert({'type': 'D4', 'lum': 0.0018, 'mass': 0.758, 'diameter': 0.0013, 'roche limit': 0.009, 'H-': 0.032, 'H': 0.042, 'H+': 0.071, 'Frost Line': 0.206, 'Limit': 38})
db.insert({'type': 'D5', 'lum': 0.0007, 'mass': 0.643, 'diameter': 0.0012, 'roche limit': 0.0076, 'H-': 0.02, 'H': 0.027, 'H+': 0.047, 'Frost Line': 0.129, 'Limit': 33})
db.insert({'type': 'D6', 'lum': 0.0005, 'mass': 0.529, 'diameter': 0.0011, 'roche limit': 0.0063, 'H-': 0.017, 'H': 0.023, 'H+': 0.039, 'Frost Line': 0.109, 'Limit': 27})
db.insert({'type': 'D7', 'lum': 0.0004, 'mass': 0.42, 'diameter': 0.0009, 'roche limit': 0.05, 'H-': 0.015, 'H': 0.02, 'H+': 0.035, 'Frost Line': 0.097, 'Limit': 21})
db.insert({'type': 'D8', 'lum': 0.0003, 'mass': 0.3, 'diameter': 0.0007, 'roche limit': 0.0036, 'H-': 0.013, 'H': 0.019, 'H+': 0.029, 'Frost Line': 0.084, 'Limit': 15})
db.insert({'type': 'D9', 'lum': 0.0002, 'mass': 0.15, 'diameter': 0.0006, 'roche limit': 0.0018, 'H-': 0.011, 'H': 0.015, 'H+': 0.024, 'Frost Line': 0.069, 'Limit': 7.5})

# Brown Dwarf Stars

# L-Class Brown Dwarf Stars

db.insert({'type': 'L0', 'lum': 0.00063, 'mass': 0.083, 'diameter': 0.00053, 'roche limit': 0.00098, 'H-': 0.019, 'H': 0.026, 'H+': 0.044, 'Frost Line': 0.122, 'Limit': 4.2})
db.insert({'type': 'L1', 'lum': 0.0005, 'mass': 0.0807, 'diameter': 0.00053, 'roche limit': 0.00095, 'H-': 0.017, 'H': 0.023, 'H+': 0.039, 'Frost Line': 0.109, 'Limit': 4.1})
db.insert({'type': 'L2', 'lum': 0.00037, 'mass': 0.0784, 'diameter': 0.00052, 'roche limit': 0.00093, 'H-': 0.014, 'H': 0.019, 'H+': 0.034, 'Frost Line': 0.094, 'Limit':4.0})
db.insert({'type': 'L3', 'lum': 0.00024, 'mass': 0.0761, 'diameter': 0.00051, 'roche limit': 0.0009, 'H-': 0.012, 'H': 0.016, 'H+': 0.027, 'Frost Line': 0.076, 'Limit': 3.9})
db.insert({'type': 'L4', 'lum': 0.00011, 'mass': 0.0738, 'diameter': 0.00050, 'roche limit': 0.00087, 'H-': 0.008, 'H': 0.011, 'H+': 0.019, 'Frost Line': 0.051, 'Limit': 3.7})
db.insert({'type': 'L5', 'lum': 0.000095, 'mass': 0.0715, 'diameter': 0.00050, 'roche limit': 0.00085, 'H-': 0.007, 'H': 0.01, 'H+': 0.017, 'Frost Line': 0.048, 'Limit': 3.6})
db.insert({'type': 'L6', 'lum': 0.00008, 'mass': 0.0692, 'diameter': 0.00049, 'roche limit': 0.00082, 'H-': 0.007, 'H': 0.01, 'H+': 0.016, 'Frost Line': 0.044, 'Limit': 3.5})
db.insert({'type': 'L7', 'lum': 0.000065, 'mass': 0.0669, 'diameter': 0.00048, 'roche limit': 0.00079, 'H-': 0.006, 'H': 0.008, 'H+': 0.014, 'Frost Line': 0.04, 'Limit': 3.4})
db.insert({'type': 'L8', 'lum': 0.00005, 'mass': 0.0646, 'diameter': 0.00048, 'roche limit': 0.00076, 'H-': 0.005, 'H': 0.007, 'H+': 0.012, 'Frost Line': 0.035, 'Limit': 3.3})
db.insert({'type': 'L9', 'lum': 0.000035, 'mass': 0.0623, 'diameter': 0.00047, 'roche limit': 0.00074, 'H-': 0.004, 'H': 0.006, 'H+': 0.01, 'Frost Line': 0.029, 'Limit': 3.2})

# T-Class Methane Dwarfs

db.insert({'type': 'T0', 'lum': 0.000020, 'mass': 0.06, 'diameter': 0.00071, 'roche limit': 0.00071, 'H-': 0.003, 'H': 0.005, 'H+': 0.008, 'Frost Line': 0.021, 'Limit': 3.0})
db.insert({'type': 'T1', 'lum': 0.000015, 'mass': 0.0057, 'diameter': 0.00067, 'roche limit': 0.00067, 'H-': 0.003, 'H': 0.004, 'H+': 0.007, 'Frost Line': 0.018, 'Limit': 2.9})
db.insert({'type': 'T2', 'lum': 0.000009, 'mass': 0.054, 'diameter': 0.00064, 'roche limit': 0.00064, 'H-': 0.002, 'H': 0.003, 'H+': 0.005, 'Frost Line': 0.015, 'Limit':2.7})
db.insert({'type': 'T3', 'lum': 0.000006, 'mass': 0.0524, 'diameter': 0.00062, 'roche limit': 0.00062, 'H-': 0.002, 'H': 0.003, 'H+': 0.004, 'Frost Line': 0.012, 'Limit': 2.6})
db.insert({'type': 'T4', 'lum': 0.000004, 'mass': 0.0498, 'diameter': 0.00059, 'roche limit': 0.00059, 'H-': 0.001, 'H': 0.002, 'H+': 0.004, 'Frost Line': 0.010, 'Limit': 2.5})
db.insert({'type': 'T5', 'lum': 0.000003, 'mass': 0.0472, 'diameter': 0.00056, 'roche limit': 0.00056, 'H-': 0.001, 'H': 0.002, 'H+': 0.003, 'Frost Line': 0.009, 'Limit': 2.4})
db.insert({'type': 'T6', 'lum': 0.000002, 'mass': 0.0446, 'diameter': 0.00053, 'roche limit': 0.00053, 'H-': 0.001, 'H': 0.001, 'H+': 0.003, 'Frost Line': 0.007, 'Limit': 2.3})
db.insert({'type': 'T7', 'lum': 0.000001, 'mass': 0.042, 'diameter': 0.00050, 'roche limit': 0.0004, 'H-': 0.001, 'H': 0.001, 'H+': 0.002, 'Frost Line': 0.005, 'Limit': 2.1})
db.insert({'type': 'T8', 'lum': 0, 'mass': 0.0395, 'diameter': 0.00047, 'roche limit': 0.00047, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.002, 'Limit': 2.0})
db.insert({'type': 'T9', 'lum': 0, 'mass': 0.0372, 'diameter': 0.00044, 'roche limit': 0.00044, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.001, 'Limit': 1.9})

# T-Class Ultra-Cool Dwarfs

db.insert({'type': 'Y0', 'lum': 0, 'mass': 0.035, 'diameter': 0.00039, 'roche limit': 0.00043, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00079, 'Limit': 1.7})
db.insert({'type': 'Y1', 'lum': 0, 'mass': 0.033, 'diameter': 0.00038, 'roche limit': 0.00042, 'H-': 0., 'H': 0, 'H+': 0, 'Frost Line': 0.00078, 'Limit': 1.6})
db.insert({'type': 'Y2', 'lum': 0, 'mass': 0.031, 'diameter': 0.00037, 'roche limit': 0.00041, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00076, 'Limit': 1.5})
db.insert({'type': 'Y3', 'lum': 0, 'mass': 0.029, 'diameter': 0.000637, 'roche limit': 0.00040, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00074, 'Limit': 1.4})
db.insert({'type': 'Y4', 'lum': 0, 'mass': 0.027, 'diameter': 0.00036, 'roche limit': 0.00040, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00072, 'Limit': 1.3})
db.insert({'type': 'Y5', 'lum': 0, 'mass': 0.025, 'diameter': 0.00035, 'roche limit': 0.00039, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00071, 'Limit': 1.2})
db.insert({'type': 'Y6', 'lum': 0, 'mass': 0.02, 'diameter': 0.00034, 'roche limit': 0.00038,'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.0007, 'Limit': 1.0})
db.insert({'type': 'Y7', 'lum': 0, 'mass': 0.0175, 'diameter': 0.00034, 'roche limit': 0.00038, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00068, 'Limit': 0.9})
db.insert({'type': 'Y8', 'lum': 0, 'mass': 0.0150, 'diameter': 0.00033, 'roche limit': 0.00037, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00067, 'Limit': 0.8})
db.insert({'type': 'Y9', 'lum': 0, 'mass': 0.0125, 'diameter': 0.00032, 'roche limit': 0.00036, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00065, 'Limit': 0.7})

print('Loaded ' + str(len(db)) + ' items.')