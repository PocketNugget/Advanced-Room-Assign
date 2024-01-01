from pathlib import Path

# from tkinter import i*
# Explicit imports to satisfy Flake8
from tkinter import *
import sys
# Arbol
class Nodo:
    def __init__(self, clave, salon, horainicio, horafinal, dia1, dia2):
        self.clave = clave
        self.salon = salon
        self.horainicio = horainicio
        self.horafinal = horafinal
        self.dia1 = dia1
        self.dia2=dia2
        self.left = None
        self.right = None

# Nodo Raiz
raiz = Nodo("Raiz", "Raiz", None, None, None, None)

##### LADO IZQUIERDO SOLO CURSOS EN CN #####
raiz.left= Nodo("LIS1012", "CN-101", 700, 840, 2, 4)

raiz.left.left=Nodo("LIS1012", "CN-101", 1800, 1940, 1, 3)
raiz.left.right=Nodo("LRT3022", "CN-110", 1600, 1740, 1, None)

raiz.left.left.left=Nodo("LRT3022", "CN-112", 800, 940, 3, None)
raiz.left.left.right=Nodo("LRT3022", "CN-112", 1000, 1140, 3, None)

raiz.left.right.left=Nodo("LRT3022", "CN-112", 800, 940, 4, None)
raiz.left.right.right=Nodo("LRT3022", "CN-112", 1000, 1140, 4, None)

raiz.left.left.left.left=Nodo("LRT3022", "CN-112", 1400, 1540, 3, None)
raiz.left.left.left.right=Nodo("LRT3022", "CN-112", 1500, 1640, 4, None)

raiz.left.left.right.left=Nodo("LRT2032", "CN-112", 800, 940, 1, None)
raiz.left.left.right.right=Nodo("LRT2032", "CN-112", 1000, 1140, 1, None)

raiz.left.right.left.left=Nodo("LRT2032", "CN-112", 1000, 1140, 2, None)
raiz.left.right.left.right=Nodo("LRT2032", "CN-112", 1600, 1740, 3, None)

raiz.left.right.right.left=Nodo("LRT2032", "CN-112", 1800, 1940, 3, None)
raiz.left.right.right.right=Nodo("LRT2032", "CN-112", 1800, 1940, 4, None)

raiz.left.left.left.left.left=Nodo("LRT2032", "CN-112", 1800, 1940, 4, None) 
raiz.left.left.left.left.right=Nodo("LRT2032", "CN-112", 1200, 1340, 4, None)

raiz.left.left.left.right.left=Nodo("LBM3032", "CN-113", 1800, 1940, 2, None)
raiz.left.left.left.right.right=Nodo("LBM3032", "CN-113", 1800, 1940, 4, None)

raiz.left.left.right.left.left=Nodo("LMT3021", "CN-113", 1400, 1540, 4, None)
raiz.left.left.right.left.right=Nodo("LMT3032", "CN-113", 800, 1030, 4, None)

raiz.left.left.right.right.left=Nodo("LRT2032", "CN-113", 800, 940, 3, None)
raiz.left.left.right.right.right=Nodo("LRT2032", "CN-113", 1000, 1140, 3, None)

raiz.left.right.left.left.left=Nodo("LRT2052", "CN-113", 1400, 1540, 2, None)
raiz.left.right.left.left.right=Nodo("LRT2052", "CN-113", 1400, 1540, 4, None)

raiz.left.right.left.right.left=Nodo("LRT2052", "CN-113", 1400, 1540, 5, None)
raiz.left.right.left.right.right=Nodo("LRT3032", "CN-113", 1200, 1340, 2, None)

raiz.left.right.right.left.left=Nodo("LRT3032", "CN-113", 1600, 1740, 3, None)
raiz.left.right.right.left.right=Nodo("LRT3032", "CN-113", 1200, 1340, 4, None)

raiz.left.right.right.right.left=Nodo("LRT3032", "CN-115", 1200, 1340, 4, None)
raiz.left.right.right.right.right=Nodo("LIS3132", "CN-115", 1200, 1340, 5, None)

raiz.left.left.left.left.left.left=Nodo("LRT4052", "CN-115", 1200, 1340, 5, None)
raiz.left.left.left.left.left.right=Nodo("LRT4052", "CN-116", 1800, 1940, 3, None)

raiz.left.left.left.left.right.left=Nodo("LRT4052", "CN-116", 1800, 1940, 4, None)
raiz.left.left.left.left.right.right=Nodo("LRT4052", "CN-116", 1600, 1740, 5, None)

raiz.left.left.left.right.left.left=Nodo("LRT4052", "CN-116", 1000, 1100, 6, None)
raiz.left.left.left.right.left.right=Nodo("LRT4052", "CN-116", 800, 940, 6, None)

raiz.left.left.left.right.right.left=Nodo("LRT4052", "CN-122", 1300, 1440, 4, None)
raiz.left.left.left.right.right.right=Nodo("LIS3032", "CN-201", 1300, 1415, 1, 3)

raiz.left.left.right.left.left.left=Nodo("LMT2012", "CN-201", 1300, 1415, 2, 4)
raiz.left.left.right.left.left.right=Nodo("LIS1012", "CN-202", 900, 1040, 1, 3)

raiz.left.left.right.left.right.left=Nodo("LIS1012", "CN-202", 900, 1040, 2, 4)
raiz.left.left.right.left.right.right=Nodo("LIS1012", "CN-202", 1100, 1240, 1, 3)

raiz.left.left.right.right.left.left=Nodo("LIS1012", "CN-202", 1100, 1240, 2, 4)
raiz.left.left.right.right.left.right=Nodo("LIS1012", "CN-202", 1300, 1440, 2, 4)

raiz.left.left.right.right.right.left=Nodo("LMT4032", "CN-218", 1200, 1340, 2, None)
raiz.left.left.right.right.right.right=Nodo("LMT4032", "CN-218", 1200, 1340, 4, None)

raiz.left.right.left.left.left.left=Nodo("LMT4032", "CN-218", 1200, 1340, 5, None)
raiz.left.right.left.left.left.right=Nodo("LMT4032", "CN-218", 1200, 1340, 4, None)

raiz.left.right.left.left.right.left=Nodo("LBM4052", "CN-220", 1900, 2015, 2, 4)          
raiz.left.right.left.left.right.right=Nodo("LIS4052", "CN-220", 1100, 1240, 5, 6)

raiz.left.right.left.right.left.left=Nodo("LMT3022", "CN-221", 1300, 1415, 1, 3)
raiz.left.right.left.right.left.right=Nodo("LRT2042", "CN-235", 1600, 1715, 1, 3)

raiz.left.right.left.right.right.left=Nodo("LRT4062", "CN-235", 1800, 1940, 2, None)
raiz.left.right.left.right.right.right=Nodo("LRT4062", "CN-235", 1800, 1940, 2, None)

raiz.left.right.right.left.left.left=Nodo("LRT4062", "CN-235", 1000, 1140, 5, None)
raiz.left.right.right.left.left.right=Nodo("LRT4062", "CN-235", 1000, 1140, 5, None)

##### LADO DERECHO DEL ARBOL #######
#salones CS
raiz.right = Nodo("LBM4032", "CS-106" , 1600 , 1715 , 2, 4)
raiz.right.left= Nodo("LIS3072","CS-122",1000,1115, 2, 4)

raiz.right = Nodo("LBM4032", "CS-106" , 1600 , 1715 , 2, 4)
raiz.right.left= Nodo("LIS3072","CS-122",1000,1115, 2, 4)

#salones SL
raiz.right.right= Nodo("LBM4082", "SL-307", 1730, 1845, 2, 4)
raiz.right.left.left= Nodo("LIS2022", "SL-307", 1200, 1340,2, None)
raiz.right.left.right= Nodo("LIS4042","SL-202", 1130, 1245, 2, 4)
raiz.right.right.left= Nodo("LIS4092","SL-307", 1730, 1845, 2, 4)
raiz.right.right.right= Nodo("TMT4031", "SL-307", 1730, 1845, 2, 4)

#salones HU
raiz.right.left.left.left = Nodo("LRT2012", "HU-117", 1130,  1245, 2, 4)
raiz.right.left.left.right = Nodo("LRT3082", "HU-304", 1600, 1740, 1, None)
raiz.right.left.right.left = Nodo("LIS2012", "HU-322", 830,  945, 2, 4)
raiz.right.left.right.right = Nodo("LRT2012", "HU-325",830,  945, 2, 4)
raiz.right.right.left.left = Nodo("LRT2022", "HU-325", 1600, 1740, 2, None)
raiz.right.right.left.right = Nodo("LRT2022", "HU-413",1000, 1140, 1, None)
raiz.right.right.right.left = Nodo("LRT2022", "HU-413",1000, 1140, 2, None)


#salones IA
raiz.right.right.right.right = Nodo("LBM4022", "IA-101", 830, 945, 5, 6)
raiz.right.left.left.left.left = Nodo("LIS4051", "IA-101", 1700, 1930, 6, None)
raiz.right.left.left.left.right = Nodo("LMT4041", "IA-101", 1500, 1730, 6, None)
raiz.right.left.left.right.left = Nodo("LMT4052", "IA-108", 800, 940, 2, 4)
raiz.right.left.left.right.right = Nodo("LIS2032", "IA-109", 1730, 1845, 1, 3)
raiz.right.left.right.left.left = Nodo ("LIS4102", "IA-109", 1600, 1715, 1, 3)
raiz.right.left.right.left.right = Nodo("LMT4042", "IA-109", 830, 945, 5, 6)
raiz.right.left.right.right.left = Nodo("LRT2012", "IA-109", 1000, 1115, 1, 3)
raiz.right.left.right.right.right = Nodo("TMT4011", "IA-109", 830, 945, 5, 6)
raiz.right.right.left.left.left = Nodo("LBM4042", "IA-120", 1000, 1115, 5, 6)
raiz.right.right.left.left.right = Nodo("LIS4032", "IA-120", 830, 945, 5, 6)
raiz.right.right.left.right.left = Nodo("LIS3072", "IA-122", 1130, 1245, 2, 4)
raiz.right.right.left.right.right = Nodo("LMT3022", "IA-122", 1600, 1715, 2, 4)
raiz.right.right.right.left.left = Nodo("LIS1022", "IA-123", 900, 1040, 1, 3)
raiz.right.right.right.left.right = Nodo("LMT4022", "IA-123", 1000, 1140, 5, 6)
raiz.right.right.right.right.left = Nodo("LMT4022", "IA-123", 1600, 1740, 2, 4)
raiz.right.right.right.right.right = Nodo("LIS3032", "IA-205", 1600, 1740, 1, 3)
raiz.right.left.left.left.left.left = Nodo("LIS3042", "IA-205", 1430, 1545, 2, 4)
raiz.right.left.left.left.left.right = Nodo("LRT4042", "IA-205", 830, 945, 2, 4)
raiz.right.left.left.left.right.left = Nodo("LBM3022", "IA-206", 1600, 1715, 1, 3)
raiz.right.left.left.left.right.right = Nodo("LMT4042", "IA-206", 1430, 1545, 1, 3)
raiz.right.left.left.right.left.left = Nodo("LRT3032", "IA-206", 1800, 1940, 2, 4)
raiz.right.left.left.right.left.right = Nodo("LRT3062", "IA-206", 1430, 1545, 1, 3)
raiz.right.left.left.right.right.left = Nodo("LIS4062", "IA-209", 1600, 1740, 2, 4)
raiz.right.left.left.right.right.right = Nodo("LBM4072", "IA-210", 1800, 1940, 1, 3)
raiz.right.left.right.left.left.left = Nodo("LIS2032", "IA-211", 1130, 1245, 2, 4)
raiz.right.left.right.left.left.right = Nodo("LIS2082", "IA-213", 1600, 1715, 1, 3)
raiz.right.left.right.left.right.left = Nodo("LRT4012", "IA-213", 1600, 1715, 2, 4)

#salones LA

raiz.right.left.right.right.left.left = Nodo("LMT3032", "LA-116", 800, 1030, 1, None)
raiz.right.left.right.right.left.right = Nodo("LMT3032", "LA-116", 800, 1030, 2, None)
raiz.right.left.right.right.right.left = Nodo("LMT3032", "LA-116", 800, 1030, 3, None)
raiz.right.left.right.right.right.right = Nodo("LMT3042", "LA-116", 1600, 1740, 1, None)
raiz.right.right.left.left.left.left = Nodo("LMT3042", "LA-116", 1600, 1740, 3, None)
raiz.right.right.left.left.left.right = Nodo("LMT3052", "LA-206", 1600, 1940, 1, 3)
raiz.right.right.left.left.right.left = Nodo("LMT3061", "LA-116", 800, 940, 3, None)
raiz.right.right.left.left.right.right = Nodo("LMT3061", "LA-116", 1200, 1340, 4, None)
raiz.right.right.left.right.left.left = Nodo("LMT3061", "LA-116", 1200, 1340, 2, None)
raiz.right.right.left.right.left.right = Nodo("LMT3061", "LA-116", 1200, 1340, 6, None)
raiz.right.right.left.right.right.left = Nodo("LMT3061", "LA-116", 1400, 1540, 5, None)
raiz.right.right.left.right.right.right = Nodo("LMT3061", "LA-116", 800, 940, 4, None)
raiz.right.right.right.left.left.left = Nodo("LRT2022", "LA-207", 800, 940, 1, 3)
raiz.right.right.right.left.left.right = Nodo("LRT2022", "LA-206", 1400, 1540, 1, 3)
raiz.right.right.right.left.right.left = Nodo("LRT2022", "LA-116", 1600, 1740, 2, 4)
raiz.right.right.right.left.right.right = Nodo("LRT2022", "LA-207", 1500, 1640, 2, 4)
raiz.right.right.right.right.left.left = Nodo("LRT3032", "LA-205", 1800, 1940, 1, 3)
raiz.right.right.right.right.left.right = Nodo("LRT3082", "LA-207", 1200, 1340, 2, 4)
raiz.right.right.right.right.right.left = Nodo("LRT4032", "LA-206", 830, 945, 5, 6)

#salones BI
raiz.right.right.right.right.right.right = Nodo("LIS1012", "BI-106", 900, 1040, 1, 3)
raiz.right.left.left.left.left.left.left = Nodo("LIS1012", "BI-106", 900, 1040, 2, 4)
raiz.right.left.left.left.left.left.right = Nodo("LIS1012", "BI-106", 1100, 1240, 1, 3)
raiz.right.left.left.left.left.right.left = Nodo("LIS1012", "BI-106", 1100, 1240, 2, 4)
raiz.right.left.left.left.left.right.right = Nodo("LIS1022", "BI-106", 1300, 1440, 2, 4)

#salones NE
raiz.right.left.left.left.right.left.left = Nodo("LRT2022", "NE-202", 800, 940, 2, 4)

#### GRAFO DE DISTANCIAS ####
graph = [
            [0,210,125,101,362,377,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [210,0,304,181,725,246,81,56,132,37,5,2,81,66,53,45,61,91,73,28,114,130,100,90,114,149,251,141,143,142,142,163,163,175,207,0,0,0,0,0,0,0,0,0,0,0],
            [125,304,0,217,362,406,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,84,47,35,0,0,0,0,0,0,0,0],
            [101,181,217,0,362,417,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,74,0,0,0,0,0,0,0],
            [362,725,362,362,0,725,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,63,114,0,0,0,0,0],
            [377,246,406,417,725,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,56,96,140,168,96],
            [0,81,0,0,0,0,0,137,107,44,86,81,25,40,53,61,20,10,8,14,27,49,19,9,33,168,170,60,62,61,61,82,82,94,126,0,0,0,0,0,0,0,0,0,0,0],
            [0,56,0,0,0,0,137,0,30,93,51,56,112,97,84,76,5,35,17,39,52,74,44,34,58,193,195,85,87,86,86,107,107,119,151,0,0,0,0,0,0,0,0,0,0,0],
            [0,132,0,0,0,0,107,30,0,63,138,132,82,67,54,46,71,41,59,37,24,2,32,42,18,117,119,9,11,10,10,31,31,43,75,0,0,0,0,0,0,0,0,0,0,0],
            [0,37,0,0,0,0,44,93,63,0,42,37,44,29,16,42,24,54,36,58,71,93,63,53,77,212,214,104,106,105,105,126,126,138,170,0,0,0,0,0,0,0,0,0,0,0],
            [0,5,0,0,0,0,86,51,138,42,0,5,86,71,58,50,56,86,68,90,103,125,95,85,109,244,246,136,138,137,137,158,158,170,202,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,81,56,132,37,5,0,81,66,53,45,60,90,72,94,107,129,99,89,113,248,250,140,142,141,141,162,162,174,206,0,0,0,0,0,0,0,0,0,0,0],
            [0,81,0,0,0,0,25,112,82,44,86,81,0,15,13,8,20,10,8,14,27,49,19,9,33,168,170,60,62,61,61,82,82,94,126,0,0,0,0,0,0,0,0,0,0,0],
            [0,66,0,0,0,0,40,97,67,29,71,66,15,0,13,6,5,25,7,29,42,64,34,24,48,183,185,75,77,76,76,97,97,109,141,0,0,0,0,0,0,0,0,0,0,0],
            [0,53,0,0,0,0,53,84,54,16,58,53,13,13,0,8,8,38,20,42,55,77,47,37,61,196,198,88,90,89,89,110,110,122,154,0,0,0,0,0,0,0,0,0,0,0],
            [0,45,0,0,0,0,61,76,46,42,50,45,8,6,8,0,16,46,28,50,63,85,55,45,69,204,206,96,98,97,97,118,118,130,162,0,0,0,0,0,0,0,0,0,0,0],
            [0,61,0,0,0,0,20,5,71,24,56,60,20,5,8,16,0,30,12,34,47,69,39,29,53,188,190,80,82,81,81,102,102,114,146,0,0,0,0,0,0,0,0,0,0,0],
            [0,91,0,0,0,0,10,35,41,54,86,90,10,25,38,46,30,0,18,4,17,39,9,2,23,158,160,50,52,51,51,72,72,84,116,0,0,0,0,0,0,0,0,0,0,0],
            [0,73,0,0,0,0,8,17,59,36,68,72,8,7,20,28,12,18,0,112,124,145,121,112,41,176,178,68,70,69,69,90,183,195,207,0,0,0,0,0,0,0,0,0,0,0],
            [0,28,0,0,0,0,14,39,37,58,90,94,14,29,42,50,34,4,112,0,12,34,127,118,19,154,223,46,48,47,47,68,189,201,213,0,0,0,0,0,0,0,0,0,0,0],
            [0,114,0,0,0,0,27,52,24,71,103,107,27,42,55,63,47,17,112,12,0,22,139,118,6,141,143,33,35,12,12,55,201,213,225,0,0,0,0,0,0,0,0,0,0,0],
            [0,130,0,0,0,0,49,74,2,93,125,129,49,64,77,85,69,39,145,34,22,0,30,40,16,119,121,11,13,42,42,33,223,235,247,0,0,0,0,0,0,0,0,0,0,0],
            [0,100,0,0,0,0,19,44,32,63,95,99,19,34,47,55,39,9,121,127,139,30,0,10,14,149,151,41,43,52,52,63,193,205,217,0,0,0,0,0,0,0,0,0,0,0],
            [0,90,0,0,0,0,9,34,42,53,85,89,9,24,37,45,29,2,111,117,118,40,10,0,24,159,161,51,53,28,28,73,183,195,207,0,0,0,0,0,0,0,0,0,0,0],
            [0,114,0,0,0,0,33,58,18,77,109,113,33,48,61,69,53,23,41,19,6,16,14,24,0,135,137,27,29,28,28,49,49,61,93,0,0,0,0,0,0,0,0,0,0,0],
            [0,249,0,0,0,0,168,193,117,212,244,248,168,183,196,204,188,158,176,154,141,119,149,159,135,0,2,108,106,107,107,86,86,74,42,0,0,0,0,0,0,0,0,0,0,0],
            [0,251,0,0,0,0,170,195,119,214,246,250,170,185,198,206,190,160,178,223,143,121,151,161,137,2,0,110,108,109,109,88,88,76,44,0,0,0,0,0,0,0,0,0,0,0],
            [0,141,0,0,0,0,60,85,9,104,136,140,60,75,88,96,80,50,68,46,33,11,41,51,27,108,110,0,2,2,2,22,22,34,66,0,0,0,0,0,0,0,0,0,0,0],
            [0,143,0,0,0,0,62,87,11,106,138,142,62,77,90,98,82,52,70,48,35,13,43,53,29,106,108,2,0,2,2,20,20,32,64,0,0,0,0,0,0,0,0,0,0,0],
            [0,142,0,0,0,0,61,86,10,105,137,141,61,76,89,97,81,51,69,47,12,42,52,28,28,107,109,2,2,0,0,21,21,33,65,0,0,0,0,0,0,0,0,0,0,0],
            [0,142,0,0,0,0,61,86,10,105,137,141,61,76,89,97,81,51,69,47,12,42,52,28,28,107,109,2,2,0,0,21,21,33,65,0,0,0,0,0,0,0,0,0,0,0],
            [0,163,0,0,0,0,82,107,31,126,158,162,82,97,110,118,102,72,90,68,55,33,63,73,49,86,88,22,20,21,21,0,0,12,44,0,0,0,0,0,0,0,0,0,0,0],
            [0,163,0,0,0,0,82,107,31,126,158,162,82,97,110,118,102,72,183,189,201,223,193,183,49,86,88,22,20,21,21,0,0,12,24,0,0,0,0,0,0,0,0,0,0,0],
            [0,175,0,0,0,0,94,119,43,138,170,174,94,109,122,130,114,84,195,201,213,235,205,195,61,74,76,34,32,33,33,12,12,0,12,0,0,0,0,0,0,0,0,0,0,0],
            [0,207,0,0,0,0,126,151,75,170,202,206,126,141,154,162,146,116,207,213,225,247,217,207,93,42,44,66,64,65,65,44,24,12,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,84,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,120,80,0,0,0,0,0,0,0,0],
            [0,0,47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,120,0,70,0,0,0,0,0,0,0,0],
            [0,0,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,80,70,0,0,0,0,0,0,0,0,0],
            [0,0,0,74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,63,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67,0,0,0,0,0],
            [0,0,0,0,114,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67,0,0,0,0,0,0],
            [0,0,0,0,0,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,136,94,122,134],
            [0,0,0,0,0,96,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,136,0,118,146,74],
            [0,0,0,0,0,140,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,94,118,0,28,106],
            [0,0,0,0,0,168,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,122,146,28,0,134],
            [0,0,0,0,0,96,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,134,74,106,134,0]
        ]

#### ARREGLO DE NOMBRE DE NODOS ####
node_names = ["PY-000", "IA-000", "NE-000", "BI-000", "SL-000", "HU-000", "IA-101", "IA-108", "IA-109", "IA-120", "IA-122", "IA-123", "IA-205",
        "IA-206", "IA-209", "IA-210", "IA-211", "IA-213", "CN-101", "CN-110", "CN-112", "CN-113", "CN-115", "CN-116", "CN-122", "CN-201", "CN-202",
        "CN-218", "CN-220", "CN-221", "CN-235", "LA-116", "LA-205", "LA-206", "LA-207", "NE-202", "CS-106", "CS-122", "BI-106", "SL-202", "SL-307",
        "HU-117", "HU-304", "HU-322", "HU-325", "HU-413"]

#### FUNCIONES PARA BUSCAR HORARIO ####
def buscar_clase(nodo, clave, resultados):
    if nodo is not None:
        if nodo.clave == clave:
            resultados.append(nodo)
        buscar_clase(nodo.left, clave, resultados)
        buscar_clase(nodo.right, clave, resultados)


mensaje_completo="hola"
def mostrar_resultados(resultados):
    mensajes = []  # Lista para almacenar los mensajes

    if resultados:
        mensajes.append("Opciones encontradas:")
        for i, resultado in enumerate(resultados, start=1):
            mensaje = (f"{i}. Clave: {resultado.clave}, Salón: {resultado.salon}, "
                       f"Día(s): {resultado.dia1}, {resultado.dia2}, "
                       f"Horario: {resultado.horainicio} - {resultado.horafinal}")
            mensajes.append(mensaje)
    else:
        mensajes.append("No se encontraron clases con la clave proporcionada.")

    # Convertir la lista de mensajes a un solo string con saltos de línea (\n)
    mensaje_completo = '\n'.join(mensajes)
    print(mensaje_completo)  # Imprimir el mensaje completo
    possible_classesClicked(mensaje_completo)

def verificar_conflicto(horario, nueva_clase):
    for clase in horario:
        if (nueva_clase.dia1 == clase.dia1 or nueva_clase.dia1 == clase.dia2 or
                nueva_clase.dia2 == clase.dia1 or nueva_clase.dia2 == clase.dia2):
            if (nueva_clase.horainicio >= clase.horainicio and nueva_clase.horainicio < clase.horafinal) or \
               (nueva_clase.horafinal > clase.horainicio and nueva_clase.horafinal <= clase.horafinal):
                return True
    return False

def verificar_conflicto(horario, nueva_clase):
    for clase in horario:
        if (nueva_clase.dia1 == clase.dia1 or nueva_clase.dia1 == clase.dia2 or
                nueva_clase.dia2 == clase.dia1 or nueva_clase.dia2 == clase.dia2):
            if (nueva_clase.horainicio >= clase.horainicio and nueva_clase.horainicio < clase.horafinal) or \
               (nueva_clase.horafinal > clase.horainicio and nueva_clase.horafinal <= clase.horafinal):
                return True
    return False

mensajes_incompletos = []
def reservar_clase(opcion_elegida, resultados, horario):
    mensajes = []  # Lista para almacenar los mensajes completos
  # Lista para almacenar los mensajes incompletos

    if 1 <= opcion_elegida <= len(resultados):
        clase_elegida = resultados[opcion_elegida - 1]
        if not verificar_conflicto(horario, clase_elegida):
            horario.append(clase_elegida)
            info_clase = "Clase: {}, Salón: {}, Horario: {} - {}, Día(s): {}, {} \n".format(
                clase_elegida.clave, clase_elegida.salon, clase_elegida.horainicio,
                clase_elegida.horafinal, clase_elegida.dia1, clase_elegida.dia2)
            mensajes_incompletos.append(info_clase)
            print(info_clase+"hola")
            mensaje = "Reservaste la clase: " + info_clase  # Mensaje para imprimir en consola
            mensajes.append(mensaje)
        else:
            
            mensaje = "No se puede reservar la clase debido a un conflicto de horario."
            mensajes.append(mensaje)
         
            

    else:
      
        mensaje = "Opción no válida. Por favor, elige una opción válida."
        mensajes.append(mensaje)
    # Unir todos los mensajes en un solo string con saltos de línea (\n)
    mensaje_incompleto = '\n'.join(mensajes_incompletos)
    mensaje_completo = '\n'.join(mensajes)

    print(mensaje_completo)  # Imprimir el mensaje completo
    print(mensaje_incompleto)  # Imprimir el mensaje incompleto
    update_output_text(mensaje_completo)
    # Aquí puedes usar la función update_output_text con mensaje_completo si es necesaria
    # update_output_text(mensaje_completo)

#### FUNCIONES PARA DIJKSTRA ####
#Función Dijkstra
def dijkstra(graph, start, node_names):
    # Número de nodos en el grafo
    num_nodes = len(graph)

    # Verificar si el nodo de inicio está en los nombres de nodos
    if start not in node_names:
        print("El nodo de inicio no está en la lista de nombres de nodos.")
        return []

    # Obtener el índice del nodo de inicio
    start_index = node_names.index(start)

    # Inicializar distancias desde el nodo de inicio a todos los demás nodos como infinito
    distances = [float('inf')] * num_nodes
    distances[start_index] = 0

    # Inicializar el conjunto de nodos no visitados
    unvisited = set(range(num_nodes))

    while unvisited:
        # Seleccionar el nodo con la distancia mínima actual
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)

        # Actualizar las distancias de los nodos vecinos si es necesario
        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0:  # Verificar si hay una conexión
                new_distance = distances[current_node] + graph[current_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

def guardar_salon_day(resultados, day):
    option_salon = []
    for nodo in resultados:
        if ((nodo.dia1 == day) or (nodo.dia2 == day)):
            option_salon.append(nodo.salon)
    return option_salon

def imprimir_distancias(start_node_name, node_names, option_salon, min_distances):
    # Inicializar la cadena de impresión
    result_string = "\nDistancias desde el nodo {} a los nodos seleccionados:".format(start_node_name)

    # Iterar sobre los nodos y agregar las líneas a la cadena
    for i, node_name in enumerate(node_names):
        if node_name in option_salon:
            distance = min_distances[i]
            result_string += "\nNodo {}: {}".format(node_name, distance)

    # Imprimir la cadena acumulada
    print(result_string)

#### MODIFICACIONES PARA DIJKSTRA ####
def concatenar_arreglo(arreglo):
    # Usamos el método join para concatenar todos los elementos del arreglo en un string
    resultado = ''.join(map(str, arreglo))
    return resultado

def distancias_nodo_day(graph, start_node_name, node_names, option_salon):
    # Calcular las distancias utilizando el algoritmo de Dijkstra
    min_distances = dijkstra(graph, start_node_name, node_names)

    # Verificar si se obtuvieron distancias válidas
    if min_distances:
        # Inicializar la cadena de impresión
        result_string = "\nDistancias desde el nodo {} a los nodos seleccionados:".format(start_node_name)

        # Iterar sobre los nodos y agregar las líneas a la cadena
        for i, node_name in enumerate(node_names):
            if node_name in option_salon:
                distance = min_distances[i]
                result_string += "\nNodo {}: {}".format(node_name, distance)

        return result_string  # Devolver la cadena generada

# Funcion para aplicar dijkstra
def my_dijkstra(start_nodes, resultados, graph, node_names):
    option_salon = []
    all_result_strings = []  # Almacenar todas las cadenas generadas

    for nodo in resultados:
        option_salon.append(nodo.salon)

    # Guarda las opciones de salones en un arreglo correspondiente a su día
    option_salon_days = [guardar_salon_day(resultados, i) for i in range(1, 7)]

    for i in range(len(start_nodes)):
        if start_nodes[i] is not None:
            result_string = distancias_nodo_day(graph, start_nodes[i], node_names, option_salon_days[i])
            all_result_strings.append(result_string)  # Almacenar la cadena generada

    # Imprimir las distancias desde el nodo PY-000
    result_string = distancias_nodo_day(graph, "PY-000", node_names, option_salon)
    all_result_strings.append(result_string)  # Almacenar la cadena generada

    # Imprimir las cadenas acumuladas
    big_string = concatenar_arreglo(all_result_strings)
    print(big_string)
    update_dijkstra_text(big_string)

# Funcion para guardar el nodo del dia
def node_day(start_nodes, resultados, opcion_elegida):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    clase_elegida = resultados[opcion_elegida - 1]

    for i in range(len(start_nodes)):
        if start_nodes[i] is None and (clase_elegida.dia1 == i + 1 or clase_elegida.dia2 == i + 1):
            start_nodes[i] = clase_elegida.salon
            #print(f"El nodo inicial de {dias_semana[i]} ha sido establecido en {start_nodes[i]}")

    return start_nodes

#### PATH FILE #####
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"your path to the assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def update_output_text(text):
    canvas.itemconfig(output_text, text=text)
    canvas.configure(scrollregion=canvas.bbox("all"))

def update_text_materias(text):
    canvas.itemconfig(textMaterias, text=text)
    canvas.configure(scrollregion=canvas.bbox("all"))

def update_possible_classes(text):
    canvas.itemconfig(possible_classes_out, text=text)
    canvas.configure(scrollregion=canvas.bbox("all"))

def update_dijkstra_text(text):
    canvas.itemconfig(dijkstra_text, text=text)
    canvas.configure(scrollregion=canvas.bbox("all"))

#### DECLARAR VARIABLES INICIALES ####
horario_funcional = []  # Lista para almacenar las clases reservadas en el horario
start_nodes = [None, None, None, None, None, None] # Nodos de inicio de cada dia
opcion_elegida = None
gl_resultados = []

#### BOTONES DE MATERIAS ####
def algorityProgClicked():
    print("\nHola Algoritmos y Programación")
    resultados = []
    global start_nodes

    # Lógica para buscar la clase
    buscar_clase(raiz, "LIS1012", resultados)
    
    # Lógica para mostrar resultados en la segunda pestaña
    mostrar_resultados(resultados)

    #Realiza el Dijkstra para el nodo del día y playita
    my_dijkstra(start_nodes, resultados, graph, node_names)
    
    # El usuario elige una clase
    '''
    if resultados:
        opcion_elegida = int(input("\nElige el número de la clase que deseas reservar: "))
        reservar_clase(opcion_elegida, resultados, horario_funcional)
    else:
        print("Por favor, ingresa una clave válida.")
    '''
    '''
    global opcion_elegida
    print("Opcion global: " + str(opcion_elegida))

    # Lógica para elegir una clase
    if (opcion_elegida != None):
        print("\nEste es un print")

        # Lógica para verificar y reservar clase
        check_option(resultados, opcion_elegida)
        # Lógica para elegir el nodo inicial
        start_nodes = node_day(start_nodes, resultados, opcion_elegida)
    '''
    global gl_resultados
    gl_resultados = resultados

def basesdDatosClicked():
    '''
    resultados = []
    buscar_clase(raiz, "LIS2082", resultados)
    print("hola bases de datos")
    mostrar_resultados(resultados)
    '''
    print("\nHola Bases de Datos")
    # Buscar clase
    resultados = []
    global start_nodes


    buscar_clase(raiz, "LIS2082", resultados)
    
    # Segunda Pestaña
    mostrar_resultados(resultados) # Muestra las clases disponibles conforme a la clave

    #Realiza el Dijkstra para el nodo del día y playita
    my_dijkstra(start_nodes, resultados, graph, node_names)
    '''
    # El usuario elige una clase
    if resultados:
        opcion_elegida = int(input("\nElige el número de la clase que deseas reservar: "))
        reservar_clase(opcion_elegida, resultados, horario_funcional)
    else:
        print("Por favor, ingresa una clave válida.")
    '''
    opcion_elegida = okClicked()
    check_option(resultados, opcion_elegida)
    # Elegir el nodo inicial conforme a la semana y aplicar Dijkstra tomando nodo inicial PY
    start_nodes = node_day(start_nodes, resultados, opcion_elegida)

def teoriadCompClicked():
    resultados = []
    buscar_clase(raiz, "LIS3042", resultados)
    print("hola teoria de la comp")
    mostrar_resultados(resultados)

def pOOClicked():
    resultados = []
    buscar_clase(raiz, "LIS1022", resultados)
    print("hola poo")
    mostrar_resultados(resultados)

#------------materias de circuitos-------------
def circuitElecClicked():
    resultados = []
    buscar_clase(raiz, "LRT2012", resultados)
    print("hola circuitos electricos")
    mostrar_resultados(resultados)

    
def electropClicked():
    
    resultados = []
    buscar_clase(raiz, "LRT4062", resultados)
    print("hola electronica de potencia")
    mostrar_resultados(resultados)

def labdeCircClicked():
    
    resultados = []
    buscar_clase(raiz, "LRT2032", resultados)
    print("hola laboratorio de circuitos electricos")
    mostrar_resultados(resultados)


def labdeElecDigClicked():
    
    resultados = []
    buscar_clase(raiz, "LMT3021", resultados)
    print("hola laboratorio de electronica digital")
    mostrar_resultados(resultados)


def labdeElecIntClicked():
    resultados = []
    buscar_clase(raiz, "LRT2042", resultados)
    print("hola laboratorio de electronica integrada")
    mostrar_resultados(resultados)

def labdeMaqClicked():
    resultados = []
    buscar_clase(raiz, "LMT3042", resultados)
    print("hola laboratorio de maquinas y mecanísmos")
    mostrar_resultados(resultados)

def elecIntClicked():
    resultados = []
    buscar_clase(raiz, "LRT2042", resultados)
    print("hola electronica integrada")
    mostrar_resultados(resultados)


#------------materias de biomédica-------------
def automatIndClicked():
    resultados = []
    buscar_clase(raiz, "LMT4032", resultados)
    print("hola automatizacion industrial")
    mostrar_resultados(resultados)

def disSisBiomedClicked():
    resultados = []
    buscar_clase(raiz, "LBM4072", resultados)
    print("hola diseño de sistemas biomédicos")
    mostrar_resultados(resultados)

def intHumCompClicked():
    resultados = []
    buscar_clase(raiz, "LIS3032", resultados)
    print("hola interacción humano computadora")
    mostrar_resultados(resultados)



def labInstBiomedClicked():
    resultados = []
    buscar_clase(raiz, "LBM3032", resultados)
    print("hola laboratorio de instrumentación biomédica")
    mostrar_resultados(resultados)


def labInstProcSeClicked():
    resultados = []
    buscar_clase(raiz, "LMT3061", resultados)
    print("hola laboratorio de instrumentación y procesamiento de señales")
    mostrar_resultados(resultados)


def labSeInstClicked():
    resultados = []
    buscar_clase(raiz, "LMT3032", resultados)
    print("hola laboratorio de señales e instrumentación")
    mostrar_resultados(resultados)



def ingClinClicked():
    resultados = []
    buscar_clase(raiz, "LBM4052", resultados)
    print("hola ingeniería clínica")
    mostrar_resultados(resultados)


#------------materias de tecnología e Inovación-------------
def comNubDMClicked():
    resultados = []
    buscar_clase(raiz, "LIS4102", resultados)
    print("hola computo en la nube y datos masivos")
    mostrar_resultados(resultados)

def disDigClicked():
    resultados = []
    buscar_clase(raiz, "LRT2022", resultados)
    print("hola diseño digital")
    mostrar_resultados(resultados)

def sisEmbedClicked():
    resultados = []
    buscar_clase(raiz, "LRT3032", resultados)
    print("hola sistemas embebidos")
    mostrar_resultados(resultados)

def visArtifClicked():
    resultados = []
    buscar_clase(raiz, "LIS4042", resultados)
    print("hola vision artificial")
    mostrar_resultados(resultados)

def visRobClicked():
    resultados = []
    buscar_clase(raiz, "LRT4012", resultados)
    print("hola vision en robótica")
    mostrar_resultados(resultados)

def temSelectIClicked():
    resultados = []
    buscar_clase(raiz, "", resultados)
    print("hola temas selectos I")
    mostrar_resultados(resultados)

def temSelectIIClicked():
    resultados = []
    buscar_clase(raiz, "", resultados)
    print("hola temas selectos II")
    mostrar_resultados(resultados)

def temSelectIIIClicked():
    resultados = []
    buscar_clase(raiz, "", resultados)
    print("hola temas selectos III")
    mostrar_resultados(resultados)

def inovTecClicked():
    resultados = []
    buscar_clase(raiz, "LIS3072", resultados)
    print("hola innovación tecnológica")
    mostrar_resultados(resultados)

#------------materias de redes y control-------------
def fundComClicked():
    resultados = []
    buscar_clase(raiz, "LRT3022", resultados)
    print("hola fundamentos de comunicaciones")
    mostrar_resultados(resultados)

def redAutClicked():
    resultados = []
    buscar_clase(raiz, "LMT4052", resultados)
    print("hola redes automotrices")
    mostrar_resultados(resultados)

def segInfClicked():
    resultados = []
    buscar_clase(raiz, "LIS4062", resultados)
    print("hola seguridad informatica")
    mostrar_resultados(resultados)

def sysComClicked():
    resultados = []
    buscar_clase(raiz, "LBM4022", resultados)
    print("hola sistemas de comunicaciones")
    mostrar_resultados(resultados)

def sysContClicked():
    resultados = []
    buscar_clase(raiz, "LRT3082", resultados)
    print("hola sistemas de control")
    mostrar_resultados(resultados)

def sysDistClicked():
    resultados = []
    buscar_clase(raiz, "LIS4052", resultados)
    print("hola sistemas distribuidos")
    mostrar_resultados(resultados)

def redCompClicked():
    resultados = []
    buscar_clase(raiz, "LRT4042", resultados)
    print("hola redes de computadoras")
    mostrar_resultados(resultados)


#botones que no se deben modificar#
def redesyControlClicked():
    print("¡Hola desde el botón 1!")
    hideall()
    placered()


def progyCompClicked():
    print("¡Hola desde el botón 2!")
    hideall()
    placeprog()

def electroyCircClicked():
    print("¡Hola desde el botón 7!")
    hideall()
    placelectronic()


def sisBiomedClicked():
    print("¡Hola desde el botón 6!")
    hideall()
    placebiomed()

def tecInovClicked():
    print("¡Hola desde el botón 5!")
    hideall()
    placetec()

def exitClicked():
    print("¡Hola desde el botón 3!")
    sys.exit()

def misMateriasClicked():
    print("¡Hola desde el botón 4!")
    hideall()
    canvas.itemconfig(rectangle, state='normal')
    canvas.itemconfig(textMaterias, state='normal')
    update_text_materias(mensajes_incompletos)### llamar el array de los resultados
    print(mensajes_incompletos)


# Unir todos los mensajes incompletos en un solo string con saltos de línea (\n)




def possible_classesClicked(mensaje):
    
    update_possible_classes(mensaje)
    hideall()
    place_possible_classes()

  
    

clean = False

def check_option(resultados, opcion_elegida):
    global horario_funcional
    if resultados:
        reservar_clase(opcion_elegida, resultados, horario_funcional)
        
         
    else:
        update_output_text("Por favor, ingresa una clave válida.")
    
    if (clean==True):
        resultados.clear()  # Limpiar la lista de resultados
    
    #start_nodes = node_day(start_nodes, resultados, opcion_elegida)

def okClicked():
    global start_nodes
    global gl_resultados
    local_opcion_elegida = int(cuadro_texto.get("1.0", "end-1c"))
    global opcion_elegida
    
    opcion_elegida = local_opcion_elegida

    hideall()
    canvas.itemconfig(image_1, state='normal')
    print("Opcion local: " + str(local_opcion_elegida))
    print("Opcion: " + str(opcion_elegida))

    # Lógica para elegir una clase
    if (opcion_elegida != None):
        print("\nEste es un print")

        # Lógica para verificar y reservar clase
        check_option(gl_resultados, opcion_elegida)
        # Lógica para elegir el nodo inicial
        start_nodes = node_day(start_nodes, gl_resultados, opcion_elegida)


infostatus = 0

def infoClicked():
    global infostatus
    hideall()
    placeInfo1()
    infostatus = 0  # Establecer el estado inicial o cualquier otro estado que desees

def nextClicked():
    global infostatus
    hideall()

    # Incrementar infostatus y mostrar la siguiente sección de información
    infostatus = (infostatus + 1) % 5

    if infostatus == 0:
        hideall()
        placeInfo1()
    elif infostatus == 1:
        hideall()
        placeInfo2()
    elif infostatus == 2:
        hideall()
        placeInfo3()
    elif infostatus == 3:
        hideall()
        placeInfo4()
    elif infostatus == 4:
        canvas.itemconfig(image_1, state='normal')

def prevClicked():
    global infostatus
    hideall()

    # Decrementar infostatus y mostrar la sección anterior de información
    infostatus = (infostatus - 1) % 5

    if infostatus == 0:
        hideall()
        placeInfo1()
    elif infostatus == 1:
        hideall()
        placeInfo2()
    elif infostatus == 2:
        hideall()
        placeInfo3()
    elif infostatus == 3:
        hideall()
        placeInfo4()
    elif infostatus == 4:
        hideall()
        canvas.itemconfig(image_1, state='normal')








def placeprog():

    teoriadCompBUT.place(x=168.0,y=182.0,width=618.6766357421875,height=39.0)
    basesdDatosBUT.place(x=168.0,y=76.0,width=618.6766357421875,height=39.0)
    algorityProgBUT.place(x=168.32339477539062,y=23.0,width=618.6766357421875,height=39.0)
    pOOBUT.place(x=168.0,y=129.0,width=618.6766357421875,height=39.0)

def placelectronic():
    
    circuitElecBUT.place(x=168.32339477539062,y=23.0,width=618.6766357421875,height=39.0)
    electropBUT.place(x=168.0,y=76.0,width=618.6766357421875,height=39.0)
    labdeCircBUT.place(x=168.0,y=182.0,width=618.6766357421875,height=39.0)
    labdeElecDigBUT.place(x=168.0,y=235.0,width=618.6766357421875,height=39.0)
    labdeElecIntBUT.place(x=168.0,y=288.0,width=618.6766357421875,height=39.0)
    labdeMaqBUT.place(x=168.0,y=341.0,width=618.6766357421875,height=39.0)
    elecIntBUT.place(x=168.0,y=129.0,width=618.6766357421875,height=39.0)

def placebiomed():
    automatIndBUT.place(x=168.32339477539062,y=23.0,width=618.6766357421875,height=39.0)
    automatIndBUT.place(x=168.32339477539062,y=23.0,width=618.6766357421875,height=39.0)
    disSisBiomedBUT.place(x=168.0,y=76.0,width=618.6766357421875,height=39.0)
    intHumCompBUT.place(x=168.0,y=182.0,width=618.6766357421875,height=39.0)
    labInstBiomedBUT.place(x=168.0,y=235.0,width=618.6766357421875,height=39.0)
    labInstProcSeBUT.place(x=168.0,y=288.0,width=618.6766357421875,height=39.0)
    labSeInstBUT.place(x=168.0,y=341.0,width=618.6766357421875,height=39.0)
    labInstBiomedBUT.place(x=168.0,y=235.0,width=618.6766357421875,height=39.0)
    ingClinBUT.place(x=168.0,y=129.0,width=618.6766357421875,height=39.0)

def placetec():
    compNubDMBUT.place(x=168.32339477539062,y=23.0,width=618.6766357421875,height=39.0)
    disDigBUT.place(x=168.0,y=76.0,width=618.6766357421875,height=39.0)
    sisEmbedBUT.place(x=168.0,y=182.0,width=618.6766357421875,height=39.0)
    visArtifBUT.place(x=168.0,y=235.0,width=618.6766357421875,height=39.0)
    visRobBUT.place(x=168.0,y=288.0,width=618.6766357421875,height=39.0)
    temSelectIBUT.place(x=168.0,y=341.0,width=618.6766357421875,height=39.0)
    temSelectIIBUT.place(x=168.0,y=394.0,width=618.6766357421875,height=39.0)
    temSelectIIIBUT.place(x=168.0,y=447.0,width=618.6766357421875,height=39.0)
    inovTecBUT.place(x=168.0,y=129.0,width=618.6766357421875,height=39.0)

def placered():
    fundComBUT.place(x=168.32339477539062,y=23.0,width=618.6766357421875,height=39.0)
    redAutBUT.place(x=168.0,y=76.0,width=618.6766357421875,height=39.0)
    segInfBUT.place(x=168.0,y=182.0,width=618.6766357421875,height=39.0)
    sysComBUT.place(x=168.0,y=235.0,width=618.6766357421875,height=39.0)
    sysContBUT.place(x=168.0,y=288.0,width=618.6766357421875,height=39.0)
    sysDistBUT.place(x=168.0,y=341.0,width=618.6766357421875,height=39.0)
    redCompBUT.place(x=168.0,y=129.0,width=618.6766357421875,height=39.0)
def place_possible_classes():
    okBUT.place(x=448.0,y=519.0,width=55.82414245605469,height=37.9085693359375)
    canvas.itemconfig(possible_classes_out, state='normal')
    canvas.itemconfig(possible_classes_out_box, state='normal')
    canvas.itemconfig(text_canvas_window, state='normal')

def placeInfo1():
    hideall()
    canvas.itemconfig(readme1, state='normal')
    nextBUT.place(x=482.0,y=521.0,width=75.0,height=38.0)

def placeInfo2():
    hideall()
    canvas.itemconfig(readme2, state='normal')
    nextBUT.place(x=482.0,y=521.0,width=75.0,height=38.0)
    prevBUT.place(x=399.0,y=521.0,width=75.0,height=38.0)

def placeInfo3():
    hideall()
    canvas.itemconfig(readme3, state='normal')
    nextBUT.place(x=482.0,y=521.0,width=75.0,height=38.0)
    prevBUT.place(x=399.0,y=521.0,width=75.0,height=38.0)
def placeInfo4():
    hideall()
    canvas.itemconfig(readme4, state='normal')
    nextBUT.place(x=482.0,y=521.0,width=75.0,height=38.0)
    prevBUT.place(x=399.0,y=521.0,width=75.0,height=38.0)



def hideall():
    canvas.itemconfig(image_1, state='hidden')
    canvas.itemconfig(rectangle, state='hidden')
    canvas.itemconfig(textMaterias, state='hidden')
    canvas.itemconfig(possible_classes_out, state='hidden')
    canvas.itemconfig(possible_classes_out_box, state='hidden')
    canvas.itemconfig(text_canvas_window, state='hidden')
    canvas.itemconfig(readme1, state='hidden')
    canvas.itemconfig(readme2, state='hidden')
    canvas.itemconfig(readme3, state='hidden')
    canvas.itemconfig(readme4, state='hidden')
    nextBUT.place_forget()
    prevBUT.place_forget()
    okBUT.place_forget()
    teoriadCompBUT.place_forget()
    basesdDatosBUT.place_forget()
    algorityProgBUT.place_forget()
    pOOBUT.place_forget()
    circuitElecBUT.place_forget()
    electropBUT.place_forget()
    labdeCircBUT.place_forget()
    labdeElecDigBUT.place_forget()
    labdeElecIntBUT.place_forget()
    labdeMaqBUT.place_forget()
    elecIntBUT.place_forget()
    automatIndBUT.place_forget()
    disSisBiomedBUT.place_forget()
    intHumCompBUT.place_forget()
    labInstBiomedBUT.place_forget()
    labInstProcSeBUT.place_forget()
    labSeInstBUT.place_forget()
    ingClinBUT.place_forget()
    compNubDMBUT.place_forget()
    disDigBUT.place_forget()
    sisEmbedBUT.place_forget()
    visArtifBUT.place_forget()
    visRobBUT.place_forget()
    temSelectIBUT.place_forget()
    temSelectIIBUT.place_forget()
    temSelectIIIBUT.place_forget()
    inovTecBUT.place_forget()
    fundComBUT.place_forget()
    redAutBUT.place_forget()
    segInfBUT.place_forget()
    sysComBUT.place_forget()
    sysContBUT.place_forget()
    sysDistBUT.place_forget()
    redCompBUT.place_forget()


window = Tk()

window.geometry("1355x600")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 600,
    width = 1355,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    158.0,
    600.0,
    fill="#000000",
    outline="")

redesyControlIMG = PhotoImage(
    file=relative_to_assets("redesycontrol.png"))
redesyControlBUT = Button(
    image=redesyControlIMG,
    borderwidth=0,
    highlightthickness=0,
    command=redesyControlClicked,
    relief="flat"
)
redesyControlBUT.place(
    x=4.0,
    y=309.0,
    width=150.0,
    height=74.82757568359375
)

output_text = canvas.create_text(
    170.0,
    568.0,
    anchor="nw",
    text="^_^",
    fill="#D1F1FA",
    font=("Inter", 15 * -1)
)

progyCompIMG = PhotoImage(
    file=relative_to_assets("progycomp.png"))
progyCompBUT = Button(
    image=progyCompIMG,
    borderwidth=0,
    highlightthickness=0,
    command=progyCompClicked,
    relief="flat"
)
progyCompBUT.place(
    x=4.0,
    y=10.0,
    width=150.0,
    height=74.82757568359375
)

exitIMG = PhotoImage(
    file=relative_to_assets("exit.png"))
exitBUT = Button(
    image=exitIMG,
    borderwidth=0,
    highlightthickness=0,
    command=exitClicked,
    relief="flat"
)
exitBUT.place(
    x=9.0,
    y=559.0,
    width=55.82414245605469,
    height=37.9085693359375
)

misMateriasIMG = PhotoImage(
    file=relative_to_assets("mismaterias.png"))
misMateriasBUT = Button(
    image=misMateriasIMG,
    borderwidth=0,
    highlightthickness=0,
    command=misMateriasClicked,
    relief="flat"
)
misMateriasBUT.place(
    x=4.0,
    y=438.0,
    width=150.0,
    height=74.82757568359375
)

tecInovIMG = PhotoImage(
    file=relative_to_assets("tecinov.png"))
tecInovBUT = Button(
    image=tecInovIMG,
    borderwidth=0,
    highlightthickness=0,
    command=tecInovClicked,
    relief="flat"
)
tecInovBUT.place(
    x=4.0,
    y=234.0,
    width=150.0,
    height=74.82758331298828
)

sisBiomedIMG = PhotoImage(
    file=relative_to_assets("sisbiomed.png"))
sisBiomedBUT = Button(
    image=sisBiomedIMG,
    borderwidth=0,
    highlightthickness=0,
    command=sisBiomedClicked,
    relief="flat"
)
sisBiomedBUT.place(
    x=4.0,
    y=159.0,
    width=150.0,
    height=74.82758331298828
)

electroyCircIMG = PhotoImage(
    file=relative_to_assets("electroycirc.png"))
electroyCircBUT = Button(
    image=electroyCircIMG,
    borderwidth=0,
    highlightthickness=0,
    command=electroyCircClicked,
    relief="flat"
)
electroyCircBUT.place(
    x=4.0,
    y=85.0,
    width=150.0,
    height=74.82758331298828
)

algorityProgIMG = PhotoImage(
    file=relative_to_assets("algorityprog.png"))
algorityProgBUT = Button(
    image=algorityProgIMG,
    borderwidth=0,
    highlightthickness=0,
    command=algorityProgClicked,
    relief="flat"
)

basesdDatosIMG = PhotoImage(
    file=relative_to_assets("basesddatos.png"))
basesdDatosBUT = Button(
    image=basesdDatosIMG,
    borderwidth=0,
    highlightthickness=0,
    command=basesdDatosClicked,
    relief="flat"
)

teoriadCompIMG = PhotoImage(
    file=relative_to_assets("teoriadcomp.png"))
teoriadCompBUT = Button(
    image=teoriadCompIMG,
    borderwidth=0,
    highlightthickness=0,
    command=teoriadCompClicked,
    relief="flat"
)



pOOIMG = PhotoImage(
    file=relative_to_assets("pooimg.png"))
pOOBUT = Button(
    image=pOOIMG,
    borderwidth=0,
    highlightthickness=0,
    command=pOOClicked,
    relief="flat"
)

circuitElecIMG = PhotoImage(
    file=relative_to_assets("circuitelect.png"))
circuitElecBUT = Button(
    image=circuitElecIMG,
    borderwidth=0,
    highlightthickness=0,
    command=circuitElecClicked,
    relief="flat"
)

electropIMG = PhotoImage(
    file=relative_to_assets("electrop.png"))
electropBUT = Button(
    image=electropIMG,
    borderwidth=0,
    highlightthickness=0,
    command=electropClicked,
    relief="flat"
)


labdeCircIMG = PhotoImage(
    file=relative_to_assets("labdecirc.png"))
labdeCircBUT = Button(
    image=labdeCircIMG,
    borderwidth=0,
    highlightthickness=0,
    command=labdeCircClicked,
    relief="flat"
)


labdeElecDigIMG = PhotoImage(
    file=relative_to_assets("labdeelecdig.png"))
labdeElecDigBUT = Button(
    image=labdeElecDigIMG,
    borderwidth=0,
    highlightthickness=0,
    command=labdeElecDigClicked,
    relief="flat"
)


labdeElecIntIMG = PhotoImage(
    file=relative_to_assets("labdeelecint.png"))
labdeElecIntBUT = Button(
    image=labdeElecIntIMG,
    borderwidth=0,
    highlightthickness=0,
    command=labdeElecIntClicked,
    relief="flat"
)


labdeMaqIMG = PhotoImage(
    file=relative_to_assets("labdemaq.png"))
labdeMaqBUT = Button(
    image=labdeMaqIMG,
    borderwidth=0,
    highlightthickness=0,
    command=labdeMaqClicked,
    relief="flat"
)


elecIntIMG = PhotoImage(
    file=relative_to_assets("elecint.png"))
elecIntBUT = Button(
    image=elecIntIMG,
    borderwidth=0,
    highlightthickness=0,
    command=elecIntClicked,
    relief="flat"
)
automatIndIMG = PhotoImage(
    file=relative_to_assets("automatind.png"))
automatIndBUT = Button(
    image=automatIndIMG,
    borderwidth=0,
    highlightthickness=0,
    command=automatIndClicked,
    relief="flat"
)


disSisBiomedIMG = PhotoImage(
    file=relative_to_assets("dissisbiomed.png"))
disSisBiomedBUT = Button(
    image=disSisBiomedIMG,
    borderwidth=0,
    highlightthickness=0,
    command=disSisBiomedClicked,
    relief="flat"
)


intHumCompIMG = PhotoImage(
    file=relative_to_assets("inthumcomp.png"))
intHumCompBUT = Button(
    image=intHumCompIMG,
    borderwidth=0,
    highlightthickness=0,
    command=intHumCompClicked,
    relief="flat"
)


labInstBiomedIMG = PhotoImage(
    file=relative_to_assets("labinstbiomed.png"))
labInstBiomedBUT = Button(
    image=labInstBiomedIMG,
    borderwidth=0,
    highlightthickness=0,
    command=labInstBiomedClicked,
    relief="flat"
)


labInstProcSeIMG = PhotoImage(
    file=relative_to_assets("labinstprocseimg.png"))
labInstProcSeBUT = Button(
    image=labInstProcSeIMG,
    borderwidth=0,
    highlightthickness=0,
    command=labInstProcSeClicked,
    relief="flat"
)


labSeInstIMG = PhotoImage(
    file=relative_to_assets("labseinst.png"))
labSeInstBUT = Button(
    image=labSeInstIMG,
    borderwidth=0,
    highlightthickness=0,
    command=labSeInstClicked,
    relief="flat"
)


ingClinIMG = PhotoImage(
    file=relative_to_assets("ingclin.png"))
ingClinBUT = Button(
    image=ingClinIMG,
    borderwidth=0,
    highlightthickness=0,
    command=ingClinClicked,
    relief="flat"
)
compNubDMIMG = PhotoImage(
    file=relative_to_assets("compnubdm.png"))
compNubDMBUT = Button(
    image=compNubDMIMG,
    borderwidth=0,
    highlightthickness=0,
    command=comNubDMClicked,
    relief="flat"
)


disDigIMG = PhotoImage(
    file=relative_to_assets("disdig.png"))
disDigBUT = Button(
    image=disDigIMG,
    borderwidth=0,
    highlightthickness=0,
    command=disDigClicked,
    relief="flat"
)


sisEmbedIMG = PhotoImage(
    file=relative_to_assets("sisembed.png"))
sisEmbedBUT = Button(
    image=sisEmbedIMG,
    borderwidth=0,
    highlightthickness=0,
    command=sisEmbedClicked,
    relief="flat"
)


visArtifIMG = PhotoImage(
    file=relative_to_assets("visartif.png"))
visArtifBUT = Button(
    image=visArtifIMG,
    borderwidth=0,
    highlightthickness=0,
    command=visArtifClicked,
    relief="flat"
)


visRobIMG = PhotoImage(
    file=relative_to_assets("visrob.png"))
visRobBUT = Button(
    image=visRobIMG,
    borderwidth=0,
    highlightthickness=0,
    command=visRobClicked,
    relief="flat"
)


temSelectIIMG = PhotoImage(
    file=relative_to_assets("temselecti.png"))
temSelectIBUT = Button(
    image=temSelectIIMG,
    borderwidth=0,
    highlightthickness=0,
    command=temSelectIClicked,
    relief="flat"
)


temSelectIIIMG = PhotoImage(
    file=relative_to_assets("temselectii.png"))
temSelectIIBUT = Button(
    image=temSelectIIIMG,
    borderwidth=0,
    highlightthickness=0,
    command=temSelectIIClicked,
    relief="flat"
)


temSelectIIIIMG = PhotoImage(
    file=relative_to_assets("temselectiii.png"))
temSelectIIIBUT = Button(
    image=temSelectIIIIMG,
    borderwidth=0,
    highlightthickness=0,
    command=temSelectIIIClicked,
    relief="flat"
)


inovTecIMG = PhotoImage(
    file=relative_to_assets("inovtec.png"))
inovTecBUT = Button(
    image=inovTecIMG,
    borderwidth=0,
    highlightthickness=0,
    command=inovTecClicked,
    relief="flat"
)

fundComIMG = PhotoImage(
    file=relative_to_assets("fundcom.png"))
fundComBUT = Button(
    image=fundComIMG,
    borderwidth=0,
    highlightthickness=0,
    command=fundComClicked,
    relief="flat"
)


redAutIMG = PhotoImage(
    file=relative_to_assets("redaut.png"))
redAutBUT = Button(
    image=redAutIMG,
    borderwidth=0,
    highlightthickness=0,
    command=redAutClicked,
    relief="flat"
)


segInfIMG = PhotoImage(
    file=relative_to_assets("seginf.png"))
segInfBUT = Button(
    image=segInfIMG,
    borderwidth=0,
    highlightthickness=0,
    command=segInfClicked,
    relief="flat"
)


sysComIMG = PhotoImage(
    file=relative_to_assets("syscom.png"))
sysComBUT = Button(
    image=sysComIMG,
    borderwidth=0,
    highlightthickness=0,
    command=sysComClicked,
    relief="flat"
)


sysCont = PhotoImage(
    file=relative_to_assets("syscont.png"))
sysContBUT = Button(
    image=sysCont,
    borderwidth=0,
    highlightthickness=0,
    command=sysContClicked,
    relief="flat"
)


sysDistIMG = PhotoImage(
    file=relative_to_assets("sysdist.png"))
sysDistBUT = Button(
    image=sysDistIMG,
    borderwidth=0,
    highlightthickness=0,
    command=sysDistClicked,
    relief="flat"
)


redCompIMG = PhotoImage(
    file=relative_to_assets("redcomp.png"))
redCompBUT = Button(
    image=redCompIMG,
    borderwidth=0,
    highlightthickness=0,
    command=redCompClicked,
    relief="flat"
)

rectangle = canvas.create_rectangle(
    168.0,
    23.0,
    787.0,
    475.0,
    fill="#D1F1FA",
    outline=""
)

textMaterias = canvas.create_text(
    186.0,
    34.0,
    anchor="nw",
    text="Aqui se colocan tus materias\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-",
    fill="#000000",
    font=("Ubuntu Medium", 18 * -1)
)




image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    483.0,
    271.0,
    image=image_image_1
)

possible_classes_out_box=canvas.create_rectangle(
    172.0,
    15.0,
    783.0,
    452.0,
    fill="#D0F1FA",
    outline="")



possible_classes_out = canvas.create_text(
    194.0,
    26.0,
    anchor="nw",
    text="-1\n-2\n-3",
    fill="#000000",
    font=("arial", 18 * -1)
)


cuadro_texto = Text(window, height=int(35 / 18), width=int(152 / 13),font=("Arial", 25))
text_canvas_window = canvas.create_window((400, 470), anchor="nw", window=cuadro_texto)


okIMG = PhotoImage(
    file=relative_to_assets("ok.png"))
okBUT = Button(
    image=okIMG,
    borderwidth=0,
    highlightthickness=0,
    command=okClicked,
    relief="flat"
)

prevIMG = PhotoImage(
    file=relative_to_assets("button_4.png"))
prevBUT = Button(
    image=prevIMG,
    borderwidth=0,
    highlightthickness=0,
    command=prevClicked,
    relief="flat"
)


nextIMG = PhotoImage(
    file=relative_to_assets("button_5.png"))
nextBUT = Button(
    image=nextIMG,
    borderwidth=0,
    highlightthickness=0,
    command=nextClicked,
    relief="flat"
)


infoIMG = PhotoImage(
    file=relative_to_assets("info.png"))
infoBUT = Button(
    image=infoIMG,
    borderwidth=0,
    highlightthickness=0,
    command=infoClicked,
    relief="flat"
)
infoBUT.place(
    x=118.0,
    y=562.0,
    width=36.0,
    height=36.0
)

readme1IMG = PhotoImage(
    file=relative_to_assets("readme1.png"))
readme1= canvas.create_image(
    477.0,
    261.0,
    image=readme1IMG
)

readme2IMG = PhotoImage(
    file=relative_to_assets("readme2.png"))
readme2= canvas.create_image(
    477.0,
    261.0,
    image=readme2IMG
)
readme3IMG = PhotoImage(
    file=relative_to_assets("readme3.png"))
readme3= canvas.create_image(
    477.0,
    261.0,
    image=readme3IMG
)

readme4IMG = PhotoImage(
    file=relative_to_assets("readme4.png"))
readme4= canvas.create_image(
    477.0,
    261.0,
    image=readme4IMG
)


rectangleDIJKSTRA=canvas.create_rectangle(
    807.0,
    48.0,
    1337.0,
    559.0,
    fill="#D0F1FA",
    outline="")

dijkstra_text=canvas.create_text(
    828.0,
    59.0,
    anchor="nw",
    text="Hola! este es tu estatus actual con Dijkstra",
    fill="#000000",
    font=("Inter", 18 * -1)
)

dijkstraIMG = PhotoImage(
    file=relative_to_assets("DIJKSTRA.png"))
dijkstra1 = canvas.create_image(
    1076.0,
    25.0,
    image=dijkstraIMG
)


hideall()
canvas.itemconfig(image_1, state='normal')
window.resizable(False, False)
window.mainloop()

