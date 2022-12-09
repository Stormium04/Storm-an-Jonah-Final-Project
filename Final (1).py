def hello():
    '''Welcomes the user'''
    print("Authorized user detected, welcome user to the Mobile Suit Database!")

series = ['Mobile Suit Gundam 0079', 'Mobile Suit Gundam: The 8th MS Team', 'Mobile Suit Zeta Gundam', 'Mobile Suit Gundam ZZ', 'Mobile Suit Gundam: Chars Counterattack', 'Mobile Suit Gundam Unicorn', 'Mobile Suit Gundam 00', 'Mobile Suit Gundam Awakening OF the Trailblazer']
    
def list_series():
    '''Lists all Gundam Series.'''
    i = 0
    length = len(series)
    while i < length:
        print(series[i])
        i += 1
def pick_series(string):
    '''Picks selected series'''
    for item in series:
        if string == item:
            print(str(item) + ' has been selected, would you like a list of mobile suits?')
def mobile_suit_open(string):
    '''Picks out which series to view'''
    if string == 'Show me Mobile Suit Gundam 0079':
        print("Sortie confirmed, White Base data transfer complete, sortie register is ready to view.")
    elif string == 'Show me Mobile Suit Gundam: The 8th MS team':
        print ("Sortie confirmed, 08th MS team ready for deployment, team data transfer complete and ready to view.")
    elif string == 'Show me Mobile Suit Zeta Gundam':
        print("Sortie Confirmed, Argama sending data. Data transfer complete, sortie register complete.")
    elif string == 'Show me Mobile Suit Gundam ZZ':
        print("Sortie Confirmed, Argama sending data. Data transfer complete, sortie register complete.")
    elif string == 'Show me Mobile Suit Gundam: Chars Counterattack':
        print("Sortie Confirmed, Ra Cailum sending data, Captain Bright authorized data transfer. Data transfer complete, sortie register recieved.")
    elif string == 'Show me Mobile Suit Gundam 00':
        print("Sortie confirmed, Celestial Being's Sumeragi suggests a data transfer. Confirmed, prepare for data transfer. Trans-Am Units registered, sortie register recieved. ")
    elif string == 'Show me Mobile Suit Gundam 00 Awakening of the Trailblazer':
        print("ELS detected, Emergency Sortie confirmed. Celestial Being sortie register is being recieved. Trans-Am usage is confirmed, sortie register recieved.")
    elif string == 'Show me Mobile Suit Gundam Unicorn':
        print("Naheel Argama Contacted, Calamity unit data recieved, data transfer complete, sortie list received.")
def Gundam79_list(string):
    '''displays list of 0079 mobile suits'''
    if string == 'Zeon':
        print("MS-06F Zaku II, MS-06S Zaku II Commander Type, MS-07B Gouf, MS-09 Dom, MSN-02 Zeong.")
    elif string == 'EFSF':
        print("RGM-79 GM, RX-77-2 Guncannon, RX-78-2 Gundam, RX-75 Guntank.")
def Gundam_8th_ms(string):
    '''shows 8th MS team mobile suits.'''
    if string == 'Zeon':
        print("MS-14A Gelgoog, MS-07B-3 Gouf Custom.")
    elif string == 'EFS':
        print("RX-79[G]EZ-8 Gundam Ez8")
def zeta(string):
    ''' Returns Zeta gundam mobile suits.'''
    if string == 'AEUG':
        print("MSA-003 Nemo, MSA-005 Methuss, MSN-00100 Hyaku Shiki, MSZ-006 Zeta Gundam, RX-178 Gundam MKII")
    elif string == 'Titans':
        print("MRX-009 Psycho Gundam, NRX-044 Asshimar, PMX-000 Messala, PMX-003 The O")
def Zz(string):
    '''Returns ZZ mobile suits.'''
    if string == 'AEUG':
        print("MSZ-010 ZZ Gundam")
    elif string == 'Neo Zeon':
              print("AMA-01X Jamru Fin, AMX-004 Qubely")
def chars_counterattack(string):
    '''Returns Chars Counterattack Mobile suits'''
    if string == 'Londo Bell':
        print("RX-93 v Gundam, RX-93-v2 Hi-v Gundam")
    elif string == 'Neo Zeon':
        print("MSN-04 Sazabi.")
def unicorn(string):
    '''Returns the mobile suits in Gundam Unicorn.'''
    if string == 'Vist':
        print("RX-0 Unicorn Gundam, RX-0 [N] Unicorn Gundam 02 Banshee Norn.")
    elif string == 'Sleeves':
        print("MSN-06S Sinanju.")
def Gundam_00(string):
    '''returns 00 mobile suits.'''
    if string == 'Celestial Being':
        print("GN-001 Gundam Exia, GN-0000 00 Gundam/00 Raiser, GN-002 Gundam Dynames, GN-003 Gundam Kyrios, GN-005 Gundam Virtue")
def Quantum(string):
    '''Returns Awakening Of The Trailblazer mobile suits'''
    if string == 'Celestial Being':
        print("GNT-0000 00 Qan[T]")

def RX_78_2():
    '''Displays RX-78-2 Stats.'''
    print("Names: RX-78-2")
    print("Overall Height: 18.5 meters")
    print("Max Weight 60.0 metric tons")
    print("Empty Weight: 43.4 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1380 kw")
    print("Sensor Range: 5700 meters")
    print("Max Acceleration: 0.93 G")
    print("Max Speed: 165 km/h")
    print("Armorments: 60mm Vulcan Gun, Beam Saber, Beam Javelin, BOWA*XBR-M-79-07G Beam Rifle")
    print("BLASH*XHB-L-03/N-STD Hyper Bazooka, RX*M-Sh-008/S-01025 Shield, Super Napalm, Gundam Hammer, Hyper Hammer.")
    print("Special Features: Core Block System, Hardpoints, Learning Computer, Heatproof Field, Magnet Coating, Autopilot.")
    print("Pilot: Amuro Ray")
def GM():
    '''Displays RGM-79 GM stats.'''
    print("Name: RGM-79 GM")
    print("Overall Height: 18.5 meters")
    print("Max Weight: 58.8 metric tons")
    print("Empty Weight: 41.2 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1250 kw")
    print("Sensor Range: 6000 meters")
    print("Max Acceleration: 0.94 G")
    print("Max Speed: 102 km/h")
    print("Armaments: 60mm Vulcan Gun, THI BSjG01 Beam Saber, BR-M-79C-1 Beam Spray Gun, BOWA-XBR-M-79-07G Beam Rifle")
    print("YHI YF-MG1000 100mm Machine Gun, BLASH HB-L-03/N-STD Hyper Bazooka, RGM*S-sh-WF/S-00109 Shield.")
    print("Special Features: Mount Rack, Parachute Pack, Corvette Booster")
    print("Pilots: mass production unit, too many pilots to name.")
def Guncannon():
    '''Displays Guncannon Stats.'''
    print("Name: RX-77-2")
    print("Overall Height: 17.5 meters")
    print("Max Weight: 70.0 metric tons.")
    print("Empty Weight: 51.0 metric tons.")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1380 kw")
    print("Sensor Range: 6000 meters")
    print("Max Acceleration: 0.74 G")
    print("Max Speed: 78 km/h")
    print("Armaments: 60mm Vulcan Gun, 240mm Cannon, Spray Missile Launcher, XBR-M-79a Beam Rifle, YHI YF-MG100 100mm Machine Gun, Hand Grenade.")
    print("Special Features: Core Block System.")
    print("Pilot: Kai Shiden")
def Guntank():
    '''Displays Guntank Stats.'''
    print("Name: RX-75 Guntank")
    print("Overall Height: 15.6 meters")
    print("Max Weight: 80.0 metric tons")
    print("Empty Weight: 56.0 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor.")
    print("Power Output: 878 kw")
    print("Sensor Range: 6000 meters")
    print("Max Acceleration: 1.10 G")
    print("Max Speed: 70 km/h")
    print("Armaments: 120mm Low-Recoil Cannon, 4-tube 40mm Bop Missile Launcher")
    print("Special Features: Core Block System")
    print("Pilot's, Hayato Kobayashi, Ryu Jose")
def Zaku_II():
    '''Displays Zaku II stats.'''
    print("Name: MS-06F Zaku II")
    print("Overall Height: 17.5 meters")
    print("Max Weight: 73.3 metric tons")
    print("Empty Weight: 58.1 metric tons")
    print("Power Output: 951 kw")
    print("Sensor Range: 3200 meters")
    print("Max Acceleration: 0.59 G")
    print("Max Speed: 88 km/h")
    print("Armaments: Shoulder Shield, 120mm Machine Gun, H&L-SB25K/280mmA-P Zaku Bazooka, Heat Hawk Type 5, MIP-B6 Cracker Grenade")
    print("Pilots: Mass Production Unit, too many pilots to name")
def Chars_Zaku():
    '''Displays Char's Zaku II stats.'''
    print("Name: MS-06S Zaku II Commander Type")
    print("Overall Height: 17.5 meters")
    print("Armaments: Shoulder Shield, ASR-78 MS Anti-Ship Rifle, Type A2 Ms Bazooka, Machine Gun, Heat Hawk")
    print("Pilot: Char Aznable")
    #Not Much Info is known about this Mobile Suit so the stats aren't perfect.
def Gouf():
    '''Displays Gouf stats.'''
    print("Name: MS-07B Gouf")
    print("Overall Height: 18.7 Meters")
    print("Max Weight 75.4 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1034 kw")
    print("Sensor Range: 3600 meters")
    print("Max Accerleration: 0.54 G")
    print("Max Speed: 99 km/h")
    print("Armaments: 5-barrel 75mm Machine Gun, Heat Rod, Shield, Heat Sword Type-βIV, Heat Hawk Type 5, Heat Wire")
    print("Pilot: Ramba Ral")
def dom():
    '''Displays Dom stats.'''
    print("Name: MS-09 Dom")
    print("Overall Height: 18.6")
    print("Max Weight: 81.8 metric tons")
    print("Empty Weight: 62.6 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1269 kw")
    print("Sensor Range: 5400 meters")
    print("Max Acceleration: 0.71 G")
    print("Max Speed 381 km/h")
    print("Armaments: Scattering Beam Cannon, Heat Saber, H&L-GB03K/360mm Giant Bazooka, Heat Hawk, Sturm Faust")
    print("Pilots: Black Tri-Stars")
def Zeong():
    '''Displays Zeong stats'''
    print("Name: MSN-02 Zeong")
    print("Overall Height: 17.3 meters")
    print("Max Weight: 231.9 metric tons")
    print("Empty Weight: 151.2 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 9400 kw")
    print("Sensor Range: 81000 meters")
    print("Max Acceleration: 0.81 G")
    print("Armaments: Wired 5-barrel Mega Particle Cannon, Waist Mega Particle Cannon, Head Mega Paticle Cannon")
    print("Special Equipment: Psycommu System, Detachable Head")
    print("Pilot: Char Aznable")
def Ez8():
    '''Displays Gundam Ez8 Stats'''
    print("Name: RX-79[G]Ez-8 Gundam Ez8")
    print("Overrall Height: 18.0 meters ")
    print("Max Weight: 71.7 metric tons")
    print("Empty Weight: 51.5 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1380 kw")
    print("Sensor Range: 5900 meters")
    print("Max Acceleration: 0.74 G")
    print("Armaments: 35mm Machine Gun, 12.7mm Vulcan Gun, X.B.Sa-G-03 Beam Saber, BLASH XBR-M-79E Beam Rifle, RGM-S-Sh-WF/S-00116-AP-A Shield")
    print("Special Equipment: Container Rack, Parachute Pack, Weapon Container")
    print("Pilot: Shiro Amada")
def Gelgoog():
    '''Displays Gelgoog Stats.'''
    print("Name: MS-14A Gelgoog")
    print("Overall Height: 19.2 meters")
    print("Max Weight: 73.3 metric tons")
    print("Empty Weight: 42.1 metric tons")
    print("Power Output: 1440 kw")
    print("Sensor Range: 6300 meters")
    print("Max Acceleration: 0.84 G")
    print("Max Speed: 180 km/h")
    print("Armaments: Twin Beam Sword, Beam Rifle, M-120A1 120mm Machine Gun, 380mm Giant Bazooka, Large Beam Machine Gun, shield")
    print("Special Equipment: Sand Hose")
    print("Pilots: Mass Produced Mobile suit, too many pilots to name")
def Gouf_Custom():
    '''Displays Gouf Custom Stats'''
    print("Name: MS-07b-3 Gouf Custom")
    print("Overall Height: 18.7 meters")
    print("Max Weight: 77.5 metric tons")
    print("Empty Weight: 58.5 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1034 kw")
    print("Sensor Range: 3600 meters")
    print("Max Acceleration: 0.53 G")
    print("Armaments: Heat Wire, 3-Barrel 35mm Machine Gun, Gatling Shield, 75mm Gatling Gun, Head Sword Type D III, Heat Knuckle")
    print("Special Equipment: Flare Launcher")
    print("Pilot: Norris Packard")
def Zeta():
    '''Displays Zeta gundam Stats'''
    print("Name: MSZ-006 Zeta Gundam")
    print("Overall Height: 19.85 meters")
    print("Waverider mode Overall Legnth: 24.32 meters")
    print("Waverider mode Wingspan: 18.61 meters")
    print("Max Weight: 62.3 metric tons")
    print("Empty Weight: 28.7 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 2020 kw")
    print("Sensor Range: 14000 meters")
    print("Max Acceleration: 1.81 G")
    print("Armaments: MU-86G 60mm Vulcan Gun,  Grappling Wire, A.E.BLASH XB-G-35/Du.105 Beam Saber, XBR-M87A2 Beam Rifle, FXA-03M2 Hyper Mega Launcher")
    print("Special Equipment: Bio-Sensor, Waverider Transformation, Sealant Launchers")
    print("Pilot: Kamille Bidan")
    
def Nemo():
    '''Displays Nemo stats.'''
    print("Name: MSA-003 Nemo")
    print("Overall Height: 19.5 meters")
    print("Max Weight: 55.6 metric tons")
    print("Empty Weight: 36.2 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1620 kw")
    print("Sensor Range: 10020 meters")
    print("Max Accerlation: 1.15 g")
    print("Armaments: 60mm Vulcan Gun, Beam Saber, AE/ZIM.C-BAZ-531 300mm Clay Bazooka,BOWA·BR-S-85-C2 Beam Rifle")
    print("Special Equipment: Ballute System.")
    print("Pilots: Mass Production Unit, many pilots")
def Methuss():
    '''Displays Methuss stats.'''
    print("Name: MSA-005 Methuss")
    print("Overall Height: 26.0 meters")
    print("Max Weight: 52.4 metric tons")
    print("Empty Weight: 27.8 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1640 kw")
    print("Sensor Range: 11300 meters")
    print("Max Acceleration: 1.81 G")
    print("Armaments: Arm Beam gun, Beam Saber, BR-M-87 Beam Rifle, Beam Diffusion Missile, Shield, Grenade Launcher")
    print("Special Equipment: Transformation in Mobile Armor form")
    print("Pilot: Fa Yuiry")
    
def Hyaku_Shiki():
    '''Displays Hyaku Shiki stats'''
    print("Name: MSN-00100 Hyaku Shiki")
    print("Overall Height: 21.4 meters")
    print("Max Weight: 54.5 metric tons")
    print("Empty Weight: 31.5 metric tons")
    print("Power Output: 1850 kw")
    print("Sensor Range: 11200 meters")
    print("Max Acceleration: 1.37 G")
    print("Armaments: 60mm Vulcan gun, Beam Saber, BR-M-87 Beam Rifle, FHA-03M1 Mega Bazooka Launcher")
    print("Special Equipment: IDE System, Beam-Resistant Coating, Sealant Launcher, Ballute System")
    print("Pilot: Quattro Bajeena")
def MKII():
    '''Displays Gundam MKII Stats'''
    print("Name: RX-178 Gundam MK-II")
    print("Overall Height: 19.6 meters")
    print("Max Weight: 54.1 metric tons")
    print("Empty Weight: 33.4 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1930 kw")
    print("Sensor Range: 11300 meters")
    print("Max Acceleration 1.50 G")
    print("Armaments: Beam Saber, Beam Rifle, Hyper Bazooka, Shield, Vulcan Pod, Clay Bazooka, Beam Magnum")
    print("Special Equipment: FXA-00 Flying Armor")
    print("Pilots: Kamille Bidan, Quattro Bajeena, Katz Kobayashi")
def psycho():
    '''Displays Psycho Gundam Stats'''
    print("Name: MRX-009 Psycho Gundam")
    print("Overall Height: 40 meters [MS Mode], 30.2 meters[MF mode]")
    print("Overall Width: 32.4 meters [MF mode]")
    print("Max Weight: 388.6 metric tons")
    print("Empty Weight: 214.1 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 33600 kw")
    print("Sensor Range: 10200 meters")
    print("Max Acceleration: 0.50 G[MS mode], 1.72[MF Mode]")
    print("Max Speed: 612.52 km/h[Mach 0.5 MF Mode]")
    print("Armaments: Small Mega Beam Cannon, Diffuse Mega Particle Cannon, Beam Cannon, Shield")
    print("Special Equipment: Anti-Beam Barrier, Psycommu System, Psycho-Control System, Minovsky Craft System, Mobile Suit to Mobile Fortress Transformation")
    print("Pilots: Four Murasame")
def Asshimar():
    '''Displays Asshimar Stats'''
    print("Name: NRX-044 Asshimar")
    print("Overall Height: 23.1 meters")
    print("Max Weight: 63.8 metric tons")
    print("Empty Weight: 41.1 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 2010 kw")
    print("Sensor Range: 10200 meters")
    print("Max Acceleration: 1.07 G[MS Mode], 1.48 G[MA Mode]")
    print("Max Speed: 3704.4 km/h [MA Mode]")
    print("Armaments: Large Beam Rifle, BR-87A Beam Rifle, Beam Saber")
    print("Special Equipment: Mobile Armor to Mobile Suit transformation")
    print("Pilots: Mass Production Unit, too many pilots to name")
def Messala():
    '''Displays Messala Stats'''
    print("Name: PMX-000 Messala")
    print("Overall Height: 30.3 meters")
    print("Max Weight: 89.1 metric tons")
    print("Empty Weight: 37.3 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 4900 kw")
    print("Sensor Range: 11300 meters")
    print("Max Acceleration: 1.08 G")
    print("Armaments: Beam Saber, Mega Particle Cannon, 9-tube Missile Pod, Arm Claw, Grenade Launcher, Vulcan Gun")
    print("Special Features: Mobile Suit to Mobile Armor transformation")
    print("Pilots: Paptimus Scirocco, Sarah Zabiarov, Reccoa Londe")
def The_O():
    '''Displays The O stats'''
    print("Name: PMX-003 The-O")
    print("Overall Height: 28.4 meters")
    print("Max Weight: 86.3 metric tons")
    print("Empty Weight: 57.3 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1840 kw")
    print("Sensor Range: 11300 meters")
    print("Max Acceleration: 1.57 G")
    print("Armaments: Beam Rifle, Beam Sword")
    print("Special Equipment: Bio-sensor System, Sub-Arm")
    print("Pilots: Paptimus Scirocco")
def ZZ():
    '''Displays the ZZ's Stats'''
    print("Name: MSZ-010 ZZ Gundam")
    print("Overall Height: 22.11 meters[MS]")
    print("Wingspan: 18.52 meters [G-Fortress]")
    print("Max Weight: 68.4 metric tons")
    print("Empty Weight: 32.7 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 7340 kw")
    print("Sensor Range: 16200 Meters")
    print("Max Acceleration: 1.48 G[MS], 2.46 G[G-Fortress]")
    print("Armaments: 60mm Double Vulcan Gun, Double Beam Rifle, High Mega Cannon, Hyper Beam Saber/Beam Cannon, 21 tube Missile Launcher, Wing Shield")
    print("Special Features: Bio-Sensor, Core Block System, Seperable Transformation Components, Ballute System, MS to G-Fortress transformation")
    print("Pilots: Judau Ashta")
def Jamru():
    '''displays Jamru Fin stats'''
    print("Name: AMA-01X Jamru Fin")
    print("Overall Height: 17.2 meters")
    print("Max Weight: 58.5 metric tons")
    print("Empty Weight: 24.7 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 4750 kw")
    print("Sensor Range: 13400 meters")
    print("Max Acceleration: 1.41 G")
    print("Armaments: Hyper Mega Cannon, 3-tube Small Missile Launcher,Beam Gun/Beam Saber, Bomber Unit")
    print("Special Features: Optional Mega Booster, Optional Nuclear Pulse Engine Booster")
    print("Pilots: Dale, Deune, Danny")
def Qubeley():
    '''Displays Qubeley Stats'''
    print("Name: AMX-004 Qubeley")
    print("Overall Height: 18.9n meters")
    print("Max Weight: 57.2 metric tons")
    print("Empty Weight: 35.2 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 1820 kw")
    print("Sensor Range: 10900 Meters")
    print("Max Acceleration: 1.08 G")
    print("Armaments: Beam Gun/Saber, Funnels")
    print("Special Features: Psycommu System")
    print("Pilots: Haman Karn")
def Nu_Gundam():
    '''Displays v (Nu) Gundam Stats'''
    print("Name: RX-93 v Gundam")
    print("Overall Height: 23.0 meters")
    print("Max Weight: 63.0 metric tons")
    print("Empty Weight: 27.9 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 2980 kw")
    print("Sensor Range: 21300 meters")
    print("Max Acceleration: 1.55 G")
    print("Armaments: 60mm Vulcan Gun, Beam Saber, Spare Beam Saber, Beam Rifle, New Hyper Bazooka, Fin Funnels, Shield, Beam Machine Gun")
    print("Special Features: Birdlime Launchers, Dummy Launchers, Psycho-Frame Cockpit")
    print("Pilots: Amuro Ray")
def Hi_Nu():
    '''Displays Hi v(nu) Gundam Stats'''
    print("Name: RX-93-v2 Hi-v Gundam")
    print("Overall Height: 20.0 meters")
    print("Empty Weight: 27.9 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Armaments: 60mm Vulcan Gun, Machine Gun/Beam Gatling Gun, Beam Saber, Fin Funnels, Beam Rifle, New Hyper Bazooka, Shield")
    print("Special Features: Propellent/Thuster Unit, Psycho-Frame")
    print("Pilots: Amuro Ray")
#Not much info of this suit is known as it is a hypothetical alternate to the Nu gundam in an alternate version of the movie.
def Sazabi():
    '''Displays the Sazabi's Stats'''
    print("Name: MSN-04 Sazabi")
    print("Overall Height: 25.6 meters")
    print("Max Weight: 71.2 metric tons")
    print("Empty Weight: 30.5 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 3960 kw")
    print("Sensor Range: 22600 meters")
    print("Max Acceleration: 1.87 G")
    print("Armaments: Beam Saber, Funnels, Scattering Mega Particle Cannon, Beam Shot Rifle, Shield, Beam tomahawk")
    print("Special Features: External Propellent tanks, Psychoframe Cockpit, Psycommu System")
    print("Pilots: Char Aznable")
def Unicorn():
    '''Displays The Unicorn's Stats.'''
    print("Name: RX-0 Unicorn Gundam")
    print("Overall Height: 19.7 meters[Unicorn Mode], 21.7 meters[Destroy Mode]")
    print("Max Weight: 42.7 metric tons")
    print("Empty Weight: 23.7 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 3480 kw [Unmeasurable in Destroy Mode]")
    print("Sensor Range: 22000 meters [Unmeasurable in Destroy Mode]")
    print("Armaments: 60mm Vulcan Gun, Beam Saber, Beam Tonfa, Beam Magnum, Hyper Bazooka, Shield, Beam Gatling Gun, Armed Armor DE")
    print("Special Equipment: La+ Program, Intention Automatic System, NT-D System, Destroy Unchained, Luminous Crystal Body")
    print("Pilots: Banagher Links")
def Banshee():
    '''Displays Banshee Norns stats'''
    print("Name: RX-0 [N] Unicorn Gundam 02 Banshee")
    print("Overall Height: 19.7 meters[Unicorn Mode], 21.7 meters[Destroy Mode]")
    print("Max Weight: 48.8 metric tons")
    print("Empty Weight: 27.3 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 4520 kw [Unmeasurable in Destroy Mode]")
    print("Sensor Range: 68600 meters [Unmeasurble in Destroy Mode]")
    print("Armaments: 60mm Vulcan Gun, Beam Magnum, Revolving Launcher, Beam Jutte, BOP Missile, MGaAP, Micro Hide Bomb, Beam Saber, Beam Tonfa, Armed Armor DE")
    print("Special Features: NT-D, Armed Armor XC")
    print("Pilots: Riddhe Marcenas")
def Sinanju():
    '''Displays Sinanju Stats'''
    print("Name: MSN-06S Sinanju")
    print("Overall Height: 22.6 meters")
    print("Max Weight: 56.9 metric tons")
    print("Empty Weight: 25.2 metric tons")
    print("Power Source: Minovsky Ultracompact Fusion Reactor")
    print("Power Output: 3240 kw")
    print("Sensor Range: 23600 meters")
    print("Max Acceeration: 2.26 G")
    print("Armaments: 60mm Vulcan Gun, Beam Saber, Beam Rifle, Shield, Beam Axe, Rocket Bazooka")
    print("special Features: External Propellant Tanks, Psycho-Frame Cockpit, Intention Automatic System")
    print("Pilots: Full Frontal")

def Exia():
    '''Displays Gundam Exia Stats'''
    print("Name: GN-001 Gundam Exia")
    print("Overall Height: 18.3 meters")
    print("Empty Weight: 57.2 metric tons")
    print("Power Source: GN Drive")
    print("Armaments: GN Sword, GN Beam Saber, GN Beam Dagger, GN Long Blade & GN Short Blade, GN Vulcan, Proto GN Sword")
    print("Special Features: Over Boost Mode, Optical Camouflage, Trans-am System, Veda-linked Operating System")
    print("Pilots: Setsuna F. Seiei")
def Kyrios():
    '''Displays Gundam Kyrios Stats'''
    print("Name: GN-003 Gundam Kyrios")
    print("Head Height: 18.9 meters")
    print("Empty Weight: 54.8 metric tons")
    print("Power Source: GN Drive")
    print("Armaments: GN Beam Submachine Gun, GN Shield, GN Beeam Saber, GN Vulcan, GN Hand Missile Unit, Tail Unit, Tail Booster")
    print("Special Features: GN Field, Optical Camouflage, Trans-Am System, Veda-linked Operating System")
    print("Pilots: Allelujah Haptism")
def Raiser():
    '''Displays 00 + 00 Raiser stats'''
    print("Name: GN-0000+GNR-010 00 Raiser")
    print("Overall Height: 18.3 meters")
    print("Empty Weight: 75.1 metric tons")
    print("Power Source: 2x GN Drives")
    print("Armaments: GN Sword II, GN Sword III, GN Beam Machine Gun, GN Beam Saber, GN Shield, GN Vulcan")
    print("Special Features: Twin Drive System, Raiser System, GN Field, Trans-Am System, Trans-Am Burst System, Trans-Am Raiser")
    print("Pilots: Setsuna F. Seiei, Saji Crossroad")
def Dynames():
    '''Displays Gundam Dynames Stats'''
    print("Name: GN-002 Gundam Dynames")
    print("Overall Height: 18.2 meters")
    print("Empty Weight: 59.1 metric tons")
    print("Power Source: GN Drive")
    print("Armaments: GN Sniper Rifle, GN Missile, GN Beam Saber, GN Shield, GN Full Shield, GN Beam Pistol, Super Substratospheric Altittude Gun")
    print("Special Features: Sniper Mode, Dock for Haro, Optical Camouflage, Trans-Am System, Veda-linked Operating Sytem")
    print("Pilots: Lockon Stratos")
def Virtue():
    '''Displays Gundam Virtue stats'''
    print("Name: GN-005 Gundam Virtue")
    print("Overall Height: 18.4 meters")
    print("Empty Weight: 55.7 metric tons")
    print("Power Source: GN Drive")
    print("Armaments: GN Bazooka, GN Bazooka Burst Mode, GN Beam Saber, GN Cannon")
    print("Special Features: GN Field, Optical Camouflage, Trans-Am System, Transformation to GN-004 Nadleeh, Veda-linked operating system")
    print("Pilots: Tieria Erde")
def Qant():
    '''Displays 00 Qan[T] Stats'''
    print("Name: GNT-0000 00 Qan[T]")
    print("Overall Height: 18.3 meters")
    print("Empty Weight: 63.5 metric tons")
    print("Power Source: 2 x GN Drive")
    print("Armaments: GN Sword V, GN Sword Bit, GN Shield")
    print("Special Features: Bit Control System, GN Field, Miniature Veda Terminal, Quantum Brainwave Control System, Twin Drive System, Quantum System, Quantum Teleportation System, Trans-am System, Veda-linked Operating System")
    print("Pilots: Setsuna F. Seiei")
    

class Suit():
    '''Classes a custom Mobile Suit'''

    def __init__(self, name, height, weight, power, armaments, features, pilots):
        '''Create's your own stats'''
        self.name = name
        self.height = height
        self.weight = weight
        self.power = power
        self.armaments = armaments
        self.features = features
        self.pilots = pilots
    def __str__(self):
        '''Turns stats into a string'''
        string = 'Name: ' + self.name + ' \nHeight: ' + self.height + '\nWeight: ' + self.power + '\nArmaments: ' + self.armaments + '\nFeatures: ' + self.features + '\nPilots: ' + self.pilots
        return string




    
    

    


    
