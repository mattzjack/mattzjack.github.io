__author__ = 'mk'


from random import randint

praenomina_masculine = "\
Agrippa, Appius, Aulus, \
Caeso, \
Decimus, \
Faustus, \
Gaius, Gnaeus, \
Hostus, \
Lucius, \
Mamercus, Manius, Marcus, Mettius, \
Nonus, Numerius, \
Octavius, Opiter, \
Paullus, Postumus, Proculus, Publius, \
Quintus, \
Septimus, Sertor, Servius, Sextus, Spurius, Statius, \
Tiberius, Titus, Tullus, \
Vibius, Volesus, Vopiscus\
"
praenomina_feminine = "\
Appia, Aula, \
Caesula, \
Decima, \
Fausta, \
Gaia, Gnaea, \
Hosta, \
Lucia, \
Maio, Mamerca, Mania, Marcia, Maxima, Mettia, Mino, \
Nona, Numeria, \
Octavia, \
Paulla, Postuma, Prima, Procula, Publia, \
Quarta, Quinta, \
Secunda, Septima, Servia, Sexta, Spuria, Statia, \
Tertia, Titia, Tiberia, Tulla, \
Vibia, Volusa, Vopisca,\
"
nomina = "\
Aburius\n\
Accius\n\
Accoleius\n\
Acilius\n\
Aebutius\n\
Aedinius\n\
Aelius\n\
Aemilius\n\
Albanius\n\
Albatius\n\
Amatius\n\
Annius\n\
Antistius\n\
Antius\n\
Antonius\n\
Appuleius\n\
Aquillius\n\
Armenius\n\
Arrius\n\
Arsinius\n\
Artorius\n\
Asinius\n\
Ateius\n\
Atius\n\
Atilius\n\
Atrius\n\
Atronius\n\
Attius\n\
Aufidius\n\
Aurelius\n\
Aurius\n\
Ausonius\n\
Avidius\n\
Avitus\n\
Axius\n\
Babudius\n\
Baebius\n\
Balventius\n\
Bantius\n\
Barbatius\n\
Barrius\n\
Betilienus\n\
Betucius\n\
Blandius\n\
Blossius\n\
Bruccius\n\
Bruttius\n\
Bucculeius\n\
Burrienus\n\
Caecilius\n\
Caecina\n\
Caecius\n\
Caedicius\n\
Caelius\n\
Caeparius\n\
Caepasius\n\
Caerellius\n\
Caesennius\n\
Caesetius\n\
Caesius\n\
Caesonius\n\
Caesulenus\n\
Caetronius\n\
Calavius\n\
Calidius\n\
Calpurnius\n\
Calventius\n\
Calvisius\n\
Camilius\n\
Camillius\n\
Camelius\n\
Canidius\n\
Caninius\n\
Canius\n\
Cantilius\n\
Cantius\n\
Canuleius\n\
Canutius\n\
Caprenius\n\
Carius\n\
Caristanius\n\
Carvilius\n\
Cassius\n\
Ceionius\n\
Cicereius\n\
Cilnius\n\
Cincius\n\
Cispius\n\
Claudius\n\
Clodius\n\
Cloelius\n\
Clovius\n\
Cluilius\n\
Cluntius\n\
Cocceius\n\
Coiedius\n\
Cominius\n\
Consentius\n\
Considius\n\
Coruncanius\n\
Cordius\n\
Cornelius\n\
Cosconius\n\
Curius\n\
Curtius\n\
Decumius\n\
Desticius\n\
Dexsius\n\
Didius\n\
Dillius\n\
Domitius\n\
Dossenius\n\
Duccius\n\
Duronius\n\
Egnatius\n\
Epidius\n\
Equitius\n\
Fabius\n\
Fadius\n\
Faenius\n\
Falerius\n\
Favonius\n\
Festinius\n\
Flavius\n\
Flavinius\n\
Flavonius\n\
Floridius\n\
Florius\n\
Floronius\n\
Fufius\n\
Fulcinius\n\
Fulvius\n\
Fundanus\n\
Furius\n\
Gabinius\n\
Galerius\n\
Gavius\n\
Geganius\n\
Gellius\n\
Granius\n\
Gratius\n\
Gratidius\n\
Helvetius\n\
Helvius\n\
Herennius\n\
Herminius\n\
Hirtius\n\
Horatius\n\
Hortensius\n\
Hosidius\n\
Hostilius\n\
Icilius\n\
Insteius\n\
Julius\n\
Junius\n\
Juventius\n\
Laberius\n\
Labienus\n\
Laelius\n\
Laetorius\n\
Lafrenius\n\
Lampronius\n\
Lartius\n\
Liburnius\n\
Licinius\n\
Livius\n\
Lollius\n\
Longinius\n\
Loreius\n\
Lucceius\n\
Lucilius\n\
Lucius\n\
Lucretius\n\
Lusius\n\
Lutatius\n\
Macrinius\n\
Maecilius\n\
Maelius\n\
Mallius\n\
Mamilius\n\
Manlius\n\
Manilius\n\
Marcius\n\
Marius\n\
Matius\n\
Maximius\n\
Memmius\n\
Menenius\n\
Messienus\n\
Metilius\n\
Milonius\n\
Minicius\n\
Minucius\n\
Modius\n\
Mucius\n\
Munatius\n\
Munius\n\
Murrius\n\
Naevius\n\
Nasennius\n\
Nemetorius\n\
Nepius\n\
Nigidius\n\
Nigilius\n\
Ninnius\n\
Nipius\n\
Norbanus\n\
Novius\n\
Numerius\n\
Octavius\n\
Olcinius\n\
Oppius\n\
Opsius\n\
Oranius\n\
Otacilius\n\
Palpellius\n\
Papinius\n\
Papirius\n\
Papius\n\
Pedius\n\
Peltrasius\n\
Pescennius\n\
Petellius\n\
Petilius\n\
Petillius\n\
Petronius\n\
Pinarius\n\
Piscius\n\
Pisentius\n\
Placidius\n\
Plautius\n\
Plinius\n\
Plotius\n\
Pollius\n\
Pompeius\n\
Pompilius\n\
Pomponius\n\
Pomptinus\n\
Pontidius\n\
Pontius\n\
Popidius\n\
Portius\n\
Postumius\n\
Potitius\n\
Paesentius\n\
Publicius\n\
Pullo\n\
Pupius\n\
Quinctilius\n\
Quinctius\n\
Quirinius\n\
Rabirius\n\
Rufius\n\
Rufrius\n\
Rusonius\n\
Rutilius\n\
Sabucius\n\
Sallustius\n\
Salonius\n\
Salvius\n\
Scribonius\n\
Secundinius\n\
Secundius\n\
Seius\n\
Sempronius\n\
Sennius\n\
Sentius\n\
Septimius\n\
Sepunius\n\
Sepurcius\n\
Sergius\n\
Sertorius\n\
Servilius\n\
Sestius\n\
Sextilius\n\
Sextius\n\
Sidonius\n\
Silius\n\
Sittius\n\
Socellius\n\
Sornatius\n\
Spurius\n\
Statius\n\
Statilius\n\
Stertinius\n\
Suedius\n\
Sulpicius\n\
Tadius\n\
Talmudius\n\
Tanicius\n\
Tertinius\n\
Tettidius\n\
Tettienus\n\
Tettius\n\
Titiedius\n\
Titius\n\
Titinius\n\
Trebatius\n\
Trebellius\n\
Treblanus\n\
Tremellius\n\
Tuccius\n\
Tullius\n\
Turullius\n\
Ulpius\n\
Umbrenius\n\
Umbrius\n\
Ummidius\n\
Urgulanius\n\
Uulius\n\
Vagennius\n\
Vagionius\n\
Vagnius\n\
Valerius\n\
Varius\n\
Vassenius\n\
Vatinius\n\
Vedius\n\
Velius\n\
Veranius\n\
Verecundius\n\
Vergilius\n\
Verginius\n\
Vesnius\n\
Vesuvius\n\
Veturius\n\
Vibenius\n\
Vibidius\n\
Vibius\n\
Victricius\n\
Viducius\n\
Vinicius\n\
Vipsanius\n\
Vipstanus\n\
Viridius\n\
Virius\n\
Visellius\n\
Vitellius\n\
Vitruvius\n\
Vivianus\n\
Volaginius\n\
Volcatius\n\
Volumnius\n\
Volusenna\n\
Volusenus\n\
Volusius\n\
Vorenius\n\
"
cognomina = "\
Abercius, Abito, Acacius, Acaunus, Achaicus, Acilianus, Adauctus, Adepphius, Adjutor, Adranos, Adventus, Aeacus, Aebutus, Aemilianus, Aetius, Afer, Agaptus, Agatopus, Agelastus, Agorix, Agricola, Agrippa, Agustalis, Ahala, Ahenobarbus, Albanus, Albinius, Albinus, Albucius, Alethius, Allectus, Aloysius, Aluredes, Alypius, Amandus, Amantius, Ambrosius, Amor, Amphion, Anatolius, Ancus, Andronicus, Angelus, Antius, Anullinus, Apelles, Apellinus, Aper, Apollonarius, Aponius, Aquila, Aquilius, Aquillius, Aratus, Arcadius, Arcavius, Archarius, Arius, Armiger, Arminus, Arpagius, Arrianus, Arruntius, Aruns, Arvina, Asellio, Asina, Asprenas, Asprenus, Assanius, Audaios, Audens, Augendus, Augurnus, Augurius, Augustalis, Augustanus, Augustus, Auila, Aurelianus, Aurelius, Ausonius, Auspex, Auxentius, Auxientius, Auxilius, Avienus, Avitus, \
Balbillus, Balbus, Balduinus, Bambalio, Bamballio, Banquerius, Barbatus, Baro, Bassus, Bato, Belenus, Belisarius, Bellator, Belletor, Bellicus, Bellus, Bestia, Betto, Bibaculus, Bibulus, Bitucus, Blandus, Bodenius, Bolanus, Bonifatius, Bonosus, Bonus, Bradua, Britannicus, Brocchus, Bromidus, Bruccius, Brucetus, Bruscius, Brutus, Bubo, Buccio, Bulla, Burcanius, Burrus, Buteo, \
Caecilianus, Caecina, Caecus, Caelistis, Caelestius, Caelianus, Caelinus, Caepio, Caerellius, Caesar, Calacicus, Calatinus, Caldus, Calenus, Calerus, Caletus, Caligula, Callisunus, Calogerus, Calpornius, Calpurnianus, Calpurnis, Calvinus, Calvus, Camerius, Camillus, Campanus, Candidianus, Candidus, Candidius, Canio, Canisius, Cantaber, Capito, Capiton, Caprarius, Caracturus, Carantus, Carbo, Carinus, Carius, Carnifex, Carus, Casca, Cassianus, Castinus, Castorius, Castus, Catianus, Catilina, Cato, Catonius, Catullus, Catulus, Catus, Cecilianus, Celatus, Celer, Celsus, Cenaeus, Cencius, Censorinus, Censorius, Centumalus, Cerialis, Cerinthus, Cerularius, Cervianus, Cervidus, Cethegus, Chlorus, Christianus, Cicero, Cico, Cimber, Cinna, Cinnianus, Cita, Cittinus, Civilis, Clarus, Classicianus, Claudianus, Clemens, Clement, Clodian, Clodianus, Cogitatus, Colias, Collatinus, Columbanus, Columella, Comes, Comitianus, Comitinus, Commidius, Commidus, Commius, Commodus, Concessus, Congrio, Constans, Constantius, Corbulo, Cordus, Cornix, Cornutus, Corvinus, Corvus, Cosmas, Cotentinus, Cotta, Crassus, Cremutius, Crescentius, Cresces, Crispian, Crispin, Crispus, Crito, Crotilo, Cucuphas, Culleolus, Cumanus, Cunobarrus, Cupitas, Curio, Cyprianus, Cyprias, Cyricus, \
Dacien, Dalmatius, Dama, Damasippus, Damasus, Damian, Dannicus, Dardanius, Dardanus, Decentius, Decianus, Decmitius, Decmus, Dexion, Dexippus, Didicus, Dignus, Dio, Diocletianus, Diocourides, Disertus, Docilinus, Docilus, Dolabella, Dominicus, Domitianus, Donatianus, Donatus, Donicus, Dorotheus, Draco, Drusillus, Drusus (associated with Gens Claudia), Dubitatius, Dulcitius, Durio, Durus, Duvianus, \
Eborius, Eburnus, Ecdicius, Eclectus, Egbuttius, Egnatius, Elerius, Eliphas, Elpidius, Elvorix, Emeritus, Encratis, Ennecus, Ennius, Ennodius, Eonus, Epidianus, Epimachus, Epolonius, Erasinus, Esdras, Eudomius, Eudoxius, Eugenius, Eugenus, Eulogius, Eumenius, Eunapius, Euphemius, Eustacius, Eutherius, Evodius, Excingus, Exsupereus, Exuperantius, Exupertus, \
Fabianus, Fabillus, Facilis, Fadus, Fagus, Falco, Falconius, Falx, Famia, Familiaris, Fastidius, Farus, Faustillus, Faustinianus, Faustinius, Faustus, Faventinus, Felicissimus, Felissimus, Felix, Ferentinus, Ferreolius, Festus, Fidelis, Figulus, Fimbria, Fimus, Firminus, Firmus, Flaccus, Flamma, Flavian, Flavianus, Flavillus, Flavinus, Florens, Florentius, Florianus, Florus, Forianus, Fortunatus, Fraucus, Fredisius, Frigidian, Frontalis, Frontinus, Fronto, Fructosis, Frugi, Frugius, Frumentius, Fullofaudes, Fulvianus, Furius, Fuscinus, Fuscus, \
Gaianus, Gaius, Gala, Galarius, Galenus, Galerus, Gallio, Gallus, Galvisius, Garilianus, Gaurus, Gavros, Gavrus, Gelasius, Gellius, Gemellus, Geminianus, Generidus, Genesius, Genialis, Gennadius, Gerardus, Germanus, Germanicus, Gessius, Geta, Getha, Glabrio, Glaucia, Globulus, Gluvias, Glycia, Gordian Gordianus, Gordio, Gorgonius, Gracchus, Gracilis, Gratian, Gratidianus, Grattus, Gregorius, Grumio, Gualterus, Gryllus, \
Habitus, Hadrianus, Hardalio, Haterius, Helvius, Herculius, Herenus, Herma, Hermina, Hesychius, Hiberus, Hilario, Hilaris, Hilarius, Hirpinius, Hirrus, Homullus, Honoratus, Horatius, Hortensis, Hortensius, Hortensus, Hosidius, Humilus, Hybrida, \
Iacomus, Igennus, Ignatius, Indaletius, Indus, Ingenuus, Ingenvinus, Iocundus, Iovinus, Irenaeus, Isatis, Isauricus, Italicus, Ivmarus, Ianuarius, Iavolenus, Iovinianus, Iovinus, Iovius, Iuba, Iulian, Iulianus, Iuncinus, Iuncus, Iunianus, Iustianus, Iustinianus, Iustinus, Iustus, Iuvenlis, \
Labienus, Lactantius, Laeca, Laenas, Laetinianus, Laevinus, Larcius, Lartius, Lateranus, Latinius, Laurentius, Leddicus, Lentullus, Lentulus, Leon, Leontius, Lepidus, Lepontus, Leptis, Libanius, Liberalis, Libo, Licinianus, Licinius, Ligur, Ligustinus, Limetanus, Linus, Litorius, Littera, Litumaris, Livianus, Livigenus, Longinus, Lovernianus, Lovernius, Lucan, Lucanus, Lucianus, Lucius, Luccius, Lucceius, Lucilianus, Lucretius, Luctacus, Lucullus, Lunaris, Luonercus, Lupercus, Lupicinus, Lupinus, Lupis, Lurco, Lurio, Lutherius, Lutorius, \
Maccalus, Macrinus, Macro, Macrobius, Mactator, Maecenus, Maecius, Magnentius, Magnus, Magunnus, Maius, Major, Majus, Malchus, Mallus, Maltinus, Mancinus, Manlius, Mansuetus, Marcallas, Marcellinus, Marcellus, Marcialis, Marcipor, Margarita, Marinianus, Marinus, Maritialis, Maritimus, Marius, Maro, Marsallas, Marsicus, Marsus, Marsyas, Martial, Martialis, Martianus, Martinus, Martius, Martyrius, Marullinus, Marullus, Maternus, Matho, Mauricius, Maursus, Maximian, Maximianus, Maximinius, Maximinus, Maximus, Medullinus, Megellus, Melissus, Melitus, Mellitus, Melus, Meminius, Memmius, Memor, Mercator, Mercurialis, Mercurinus, Merula, Messala, Messor, Metellus, Metilius, Metunus, Micianus, Mico, Micon, Milonius, Minervalis, Minianus, Minicianus, Moderatus, Molacus, Momus, Montanus, Montaus, Mordanticus, Mucianus, Muco, Muncius, Murena, Mus, Musa, Musicus, Mutilus, Mutius, \
Nabor, Naevius, Narcissus, Narses, Nasica, Naso, Natalinus, Natalis, Naucratius, Nazarius, Nectaridus, Nelius, Nemesianus, Nemnogenus, Neneus, Nennius, Nepos, Nero, Nertomarus, Nerva, Nicasius, Nicetius, Nigellus, Niger, Nigidius, Nigrinus, Niraemius, Nolus, Nonius, Noster, Novation, Novellius, Numerianus, Numonis, \
Oceanus, Octavian, Octavianus, Octobrianus, Olennius, Olympicus, Opilio, Opimius, Opis, Optatus, Ordius, Orientalis, Orientius, Orissus, Orosius, Osterianus, Otho, Ovidus, \
Pacatianus, Pachomius, Pacuvianus, Paenula, Paetinus, Paetus, Palicamus, Pamphilius, Panaetius, Pansa, Pantensus, Pantera, Panthera, Papinian, Papus, Paratus, Parnesius, Pascentius, Pastor, Paterculus, Paternus, Patiens, Patricius, Paulinus, Paullus, Pavo, Pelagius, Pennus, Peregrinus, Perennis, Perpenna, Perperna, Pertacus, Pertinax, Petasius, Petreius, Petronax, Petrus, Philippus, Photius, Pictor, Pilatus, Pilus, Piso, Pius, Placidus, Planta, Plautis, Plautius, Plautus, Pleminius, Pollienus, Pollio, Polus, Polybius, Pompolussa, Pomponius, Poplicola, Porcus, Porphyrius, Postumianus, Postumus, Potitus, Praetextus, Prilidianus, Primanus, Primulus, Primus, Prisca, Priscian, Priscillian, Priscillianus, Priscus, Probus, Processus, Proceus, Proculus, Procyon, Profuterius, Propertius, Protacius, Protus, Proxsimus, Publianus, Publicola, Publicus, Pudens, Pudentius, Pulcher, Pulcherius, Pullus, Pusinnus, Pustula, \
Quartinus, Quarto, Quatruus, Quentin, Quietus, Quintilianus, Quintilius, Quintillius, Quintillus, Quiriac, Quiricus, Quirinalis, \
Ramio, Ramirus, Ravilla, Reburrus, Receptus, Rectus, Regillus, Reginus, Regulus, Remigius, Remus, Renatus, Respectus, Restitutus, Rex, Rhesus, Ripanus, Rogatus, Rogelius, Romanus, Romulianus, Romulus, Roscius, Rufinianus, Rufinus, Rufrius, Rufus, Rullus, Ruricius, Ruso, Rusticus, Rutilianus, \
Sabellius, Sabinianus, Sabinus, Sacerdos, Saenus, Salinator, Salonianus, Saloninus, Salonius, Salvian, Salvianus, Sanctus, Sandilianus, Sanga, Sarimarcus, Sarrius, Saturninus, Saunio, Scaevola, Scapula, Scaro, Scato, Scaurus, Schlerus, Scipio, Scribonianus, Scrofa, Sebastianus, Secundas, Segestes, Sejanus, Sellic, Seneca, Senecianus, Senecio, Senilis, Senna, Senopianus, Sentius, Septimianus, Septimus, Seronatus, Serranus, Servanus, Servatius, Seuso, Severlinus, Severus, Sevso, Siculus, Sidonius, Sigilis, Silanus, Silius, Silo, Silus, Silvanus, Similis, Simo, Simplex, Simplicianus, Siricus, Sisenna, Sisinnius, Sita, Sollemnis, Sorex, Sorio, Sosius, Sotericus, Soulinus, Sparticus, Spendius, Speratus, Statius, Stichus, Strabo, Sudrenus, Suilius, Sulinus, Sulla, Super, Superbus, Superstes, Sura, Surinus, Surius, Surus, Sylla, Sylvian, Sylvius, Symmachus, Symphorian, Sympronian, Synistor, Synnodus, \
Tacitus, Taenaris, Tancinus, Tanicus, Tarsicius, Tatianus, Taurinus, Telesinus, Terenteianus, Tertullian, Tertulus, Tetricus, Tetullianus, Thrasea, Thurinus, Tiberillus, Tiberinus, Tibullus, Tiburs, Titianus, Titillus, Torquatus, Traianus, Trailus, Tranio, Tranquillus, Trebonianus, Tremerus, Tremorinus, Trenico, Trenus, Triarius, Trifer, Triferus, Trimalchio, Trogus, Trupo, Tuccianus, Tuditanus, Turibius, Turpilianus, Turpilinus, Tuticanus, Tutor, Tyranus, \
Ulpianus, Urbicus, Ursinus, Ursus, Uticensis, \
Vala, Valens, Valentinian, Valentinus, Valerianus, Valgus (Gens Quintia), Varialus, Varro, Varus, Vatia, Vedrix, Venantius, Venator, Ventor, Venustinius, Vepgenus, Verecundus, Verinus, Verres, Verrucosus, Verullus, Verus, Vespasianus, Vespillo, Vestinus, Vetranio, Vettonianus, Vetus, Viator, Vibennis, Vibius, Victor, Victoricus, Victorinus, Victricius, Vincentius, Vindex, Vinicianus, Viridio, Virilis, Vitalinus, Vitalis, Vitulus, Vitus, Vocula, Volusianus, Vopiscus, Vulso, \
Zeno, Zosimus, \
"

gender = ''

praenomina_masculine = praenomina_masculine.split(', ')
praenomina_feminine = praenomina_feminine.split(', ')
prae_m = praenomina_masculine[randint(0, len(praenomina_masculine) - 1)]
prae_f = praenomina_feminine[randint(0, len(praenomina_feminine) - 1)]

nomina = nomina.splitlines()
nom = nomina[randint(0, len(nomina) - 1)]

cognomina = cognomina.split(', ')
cog = cognomina[randint(0, len(cognomina) - 1)]

def get_gender():
    global gender
    gender = input("Your sex?\na. female;\nb. male;\n(input 'a' or 'b' or perish (or rot).)\n")

get_gender()
print("Your Latin full name is:")
chance = randint(0, 999)
if chance == 0:
    print("##### ##### #####\nCongrats! You win the one a thousandth chance!")
else:
    if gender == 'b':
        print(prae_m + ' ' + nom + ' ' + cog)
    elif gender == 'a':
        print(prae_f + ' ' + nom + ' ' + cog)
    else:
        print("Now die in inferno.")
