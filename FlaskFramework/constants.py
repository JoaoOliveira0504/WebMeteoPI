import numpy as np

boxVianaDoCastelo = (570, 428, 770, 628)
boxLeiria = (574, 902, 774, 1102)
boxAveiro = (603, 687, 803, 887)
boxBeja = (735, 1546, 935, 1746)
boxBraga = (645, 463, 845, 663)
boxBraganca = (953, 401, 1153, 601)
boxCasteloBranco = (817, 886, 1017, 1086)
boxPortalegre = (829, 1012, 1029, 1212)
boxPorto = (611, 562, 811, 762)
boxSantarem = (597, 1026, 797, 1226)
boxCoimbra = (645, 792, 845, 992)
boxEvora = (740, 1183, 940, 1383)
boxFaro = (736, 1546, 936, 1746)
boxGuarda = (859, 712, 1059, 912)
boxLisboa = (513, 1149, 713, 1349)
boxSetubal = (559, 1193, 759, 1393)
boxVilaReal = (770, 527, 970, 727)
boxViseu = (740, 682, 940, 882)

idVianaDoCastelo = 1240610
idLeiria = 1210718
idAveiro = 1210702
idBeja = 1200562
idBraga = 6212124
idBraganca = 1200575
idCasteloBranco = 1200570
idPortalegre = 1200571
idPorto = 1240903
idSantarem = 1210734
idCoimbra = 1210707
idEvora = 1200558
idFaro = 1200554
idGuarda = 1210683
idLisboa = 7240919
idSetubal = 1210770
idVilaReal = 1240566
idViseu = 1240675

station_box_dict = {
    idVianaDoCastelo: boxVianaDoCastelo,
    idLeiria: boxLeiria,
    idAveiro: boxAveiro,
    idBeja: boxBeja,
    idBraga: boxBraga,
    idBraganca: boxBraganca,
    idCasteloBranco: boxCasteloBranco,
    idPortalegre: boxPortalegre,
    idPorto: boxPorto,
    idSantarem: boxSantarem,
    idCoimbra: boxCoimbra,
    idEvora: boxEvora,
    idFaro: boxFaro,
    idGuarda: boxGuarda,
    idLisboa: boxLisboa,
    idSetubal: boxSetubal,
    idVilaReal: boxVilaReal,
    idViseu: boxViseu
}

ids = np.array([1240610, 1210718, 1210702, 1200562, 6212124,
 1200575, 1200570, 1200571, 1240903, 1210734, 1210707, 1200558,
  1200554, 1210683, 7240919, 1210770, 1240566, 1240675])



__all__ = ['boxVianaDoCastelo', 'boxLeiria', 'boxAveiro', 'boxBeja', 'boxBraga', 'boxBraganca', 'boxCasteloBranco', 'boxPortalegre', 'boxPorto', 'boxSantarem', 'boxCoimbra', 'boxEvora', 'boxFaro', 'boxGuarda', 'boxLisboa', 'boxSetubal', 'boxVilaReal', 'boxViseu'] + ['idVianaDoCastelo', 'idLeiria', 'idAveiro', 'idBeja', 'idBraga', 'idBraganca', 'idCasteloBranco', 'idPortalegre', 'idPorto', 'idSantarem', 'idCoimbra', 'idEvora', 'idFaro', 'idGuarda', 'idLisboa', 'idSetubal', 'idVilaReal', 'idViseu'] + ['ids'] + ['station_box_dict']
