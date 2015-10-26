
variable = {}

var_template = {
    # Event
    "rho": {
      "title" : "rho",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },
    "nPV": {
      "title" : "number of reconstructed Primary Vertices",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : False,
    },
    "nMuons": {
      "title" : "number of muons",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nElectrons": {
      "title" : "number of electrons",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nTaus": {
      "title" : "number of taus",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nPhotons": {
      "title" : "number of photons",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nJets": {
      "title" : "number of jets",
      "nbins" : 10,
      "min" : -0.5,
      "max" : 9.5,
      "log" : True,
    },
    "nFatJets": {
      "title" : "number of AK8 jets",
      "nbins" : 6,
      "min" : -0.5,
      "max" : 5.5,
      "log" : True,
    },
    "nBJets": {
      "title" : "number of b-jets",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "eventWeight": {
      "title" : "event weight",
      "nbins" : 100,
      "min" : -1,
      "max" : 1,
      "log" : False,
    },
    
    # MET
    "met_pt": {
      "title" : "raw #slash{E}_{T} (GeV)",
      "nbins" : -1,
      "bins" : [200, 300, 400, 500, 700, 1000],
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
#    "met_pt": {
#      "title" : "raw #slash{E}_{T} (GeV)",
#      "nbins" : 20,
#      "min" : 200,
#      "max" : 1200,
#      "log" : True,
#    },
#    "met_pt": {
#      "title" : "raw #slash{E}_{T} (GeV)",
#      "nbins" : 20,
#      "min" : 0,
#      "max" : 400,
#      "log" : True,
#    },
    "met_phi": {
      "title" : "raw #slash{E}_{T} #varphi",
      "nbins" : 50,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
#    "pfmet_pt": {
#      "title" : "#slash{E}_{T} (GeV)",
#      "nbins" : -1,
#      "bins" : [200, 300, 400, 500, 700, 1000],
#      "min" : 200,
#      "max" : 1200,
#      "log" : True,
#    },
    "pfmet_pt": {
      "title" : "type-1 #slash{E}_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 250,
      "log" : True,
    },
    "pfmet_phi": {
      "title" : "type-1 #slash{E}_{T} #varphi",
      "nbins" : 50,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "met_calo_pt": {
      "title" : "calo #slash{E}_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 250,
      "log" : False,
    },
    "met_tk_pt": {
      "title" : "tracker #slash{E}_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 250,
      "log" : False,
    },
    "fakemet_pt": {
      "title" : "fake #slash{E}_{T} (GeV)",
      "nbins" : 40,
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "fakemet_phi": {
      "title" : "fake #slash{E}_{T} #varphi",
      "nbins" : 50,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "UperpScale": {
      "title" : "U_{#perp} (GeV)",
      "nbins" : 50,
      "min" : -200,
      "max" : 200,
      "log" : False,
    },
    
    
    # Jets
    "jet[N]_pt": {
      "title" : "jet [N] p_{T} (GeV)",
      "nbins" : 25,
      "min" : 0,
      "max" : 500,
      "log" : True,
    },
    "jet[N]_eta": {
      "title" : "jet [N] #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : False,
    },
    "jet[N]_phi": {
      "title" : "jet [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "jet[N]_mass": {
      "title" : "jet [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : False,
    },
    "jet[N]_dPhi_met": {
      "title" : "#Delta #varphi  jet[N]-#slash{E}_{T}",
      "nbins" : 30,
      "min" : 0,
      "max" : 3.15,
      "log" : False,
    },
    "jet[N]_dPhi_jet1": {
      "title" : "#Delta #varphi  jet[N]-jet1",
      "nbins" : 30,
      "min" : 0,
      "max" : 3.15,
      "log" : False,
    },
    "jet[N]_CSV": {
      "title" : "jet [N] CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "jet[N]_rCSV": {
      "title" : "jet [N] CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "jet[N]_flavour": {
      "title" : "jet [N] flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "jet[N]_chf": {
      "title" : "jet [N] charged hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "jet[N]_nhf": {
      "title" : "jet [N] neutral hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "jet[N]_phf": {
      "title" : "jet [N] photon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "jet[N]_elf": {
      "title" : "jet [N] electron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "jet[N]_muf": {
      "title" : "jet [N] muon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "jet[N]_chm": {
      "title" : "jet [N] charged multiplicity",
      "nbins" : 20,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },
    "jet[N]_npr": {
      "title" : "jet [N] constituents multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },

    
    # Fatjets
    "fatjet[N]_pt": {
      "title" : "jet [N] p_{T} (GeV)",
      "nbins" : 20,
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "fatjet[N]_eta": {
      "title" : "jet [N] #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : False,
    },
    "fatjet[N]_phi": {
      "title" : "jet [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "fatjet[N]_mass": {
      "title" : "jet [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : False,
    },
    "fatjet[N]_prunedMass": {
      "title" : "pruned mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : False,
    },
    "fatjet[N]_prunedMassCorr": {
      "title" : "corrected pruned mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : False,
    },
    "fatjet[N]_softdropMass": {
      "title" : "soft drop mass (GeV)",
      "nbins" : 20,
      "min" : 0.,
      "max" : 200.,
      "log" : False,
    },
    "fatjet[N]_softdropMassCorr": {
      "title" : "corrected soft drop mass (GeV)",
      "nbins" : 20,
      "min" : 0.,
      "max" : 200.,
      "log" : False,
    },
    "fatjet[N]_trimmedMass": {
      "title" : "trimmed mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : False,
    },
    "fatjet[N]_filteredMass": {
      "title" : "filtered mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : False,
    },
    "fatjet[N]_dR": {
      "title" : "subjets #Delta R",
      "nbins" : 20,
      "min" : 0,
      "max" : 1.,
      "log" : False,
    },
    "fatjet[N]_dPhi_met": {
      "title" : "#Delta #varphi_{jet-#slash{E}_{T}}",
      "nbins" : 50,
      "min" : 0,
      "max" : 3.15,
      "log" : False,
    },
    "fatjet[N]_tau21": {
      "title" : "#tau_{2} / #tau_{1}",
      "nbins" : 25,
      "min" : 0,
      "max" : 1.,
      "log" : False,
    },
    "fatjet[N]_CSV": {
      "title" : "fatjet CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "fatjet[N]_CSV1": {
      "title" : "subjet 1 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "fatjet[N]_CSV2": {
      "title" : "subjet 2 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "fatjet[N]_flavour": {
      "title" : "fatjet flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "fatjet[N]_flavour1": {
      "title" : "subjet 1 flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "fatjet[N]_flavour2": {
      "title" : "subjet 2 flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "fatjet[N]_chf": {
      "title" : "jet [N] charged hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "fatjet[N]_nhf": {
      "title" : "jet [N] neutral hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "fatjet[N]_phf": {
      "title" : "jet [N] photon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "fatjet[N]_elf": {
      "title" : "jet [N] electron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "fatjet[N]_muf": {
      "title" : "jet [N] muon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "fatjet[N]_chm": {
      "title" : "jet [N] charged multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },
    "fatjet[N]_npr": {
      "title" : "jet [N] constituents multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 100,
      "log" : False,
    },
    
    
    # Leptons
    "lepton[N]_pt": {
      "title" : "lepton [N] p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 400,
      "log" : True,
    },
    "lepton[N]_eta": {
      "title" : "lepton [N] #eta",
      "nbins" : 30,
      "min" : -3.,
      "max" : 3.,
      "log" : False,
    },
    "lepton[N]_phi": {
      "title" : "lepton [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "lepton[N]_mass": {
      "title" : "lepton [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : False,
    },
    "lepton[N]_isElectron": {
      "title" : "isElectron",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "lepton[N]_isMuon": {
      "title" : "isMuon",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "lepton[N]_charge": {
      "title" : "lepton [N] charge",
      "nbins" : 3,
      "min" : -1.5,
      "max" : 1.5,
      "log" : False,
    },
    "lepton[N]_ip2d": {
      "title" : "lepton [N] IP_{2D}",
      "nbins" : 50,
      "min" : -0.02,
      "max" : 0.02,
      "log" : True,
    },
    "lepton[N]_ip3d": {
      "title" : "lepton [N] IP_{3D}",
      "nbins" : 50,
      "min" : -0.05,
      "max" : 0.05,
      "log" : True,
    },
    "lepton[N]_relIso03": {
      "title" : "lepton [N] PFIso_{03}",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.20,
      "log" : True,
    },
    "lepton[N]_relIso04": {
      "title" : "lepton [N] PFIso_{04}",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.20,
      "log" : True,
    },
    "lepton[N]_miniIso": {
      "title" : "lepton [N] miniIso",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.1,
      "log" : True,
    },
    "lepton[N]_looseId": {
      "title" : "loose Id",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "lepton[N]_mediumId": {
      "title" : "medium Id",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "lepton[N]_tightId": {
      "title" : "tight Id",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "lepton[N]_highptId": {
      "title" : "high pT Id",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    
    # Candidates
    "Z_pt": {
      "title" : "Z candidate p_{T} (GeV)",
      "nbins" : 10,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "Z_eta": {
      "title" : "Z candidate #eta",
      "nbins" : 30,
      "min" : -3.,
      "max" : 3.,
      "log" : False,
    },
    "Z_phi": {
      "title" : "Z candidate #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "Z_mass": {
      "title" : "m_{Z} (GeV)",
      "nbins" : 60,
      "min" : 70,
      "max" : 110,
      "log" : False,
    },
    "Z_charge": {
      "title" : "Z candidate charge",
      "nbins" : 3,
      "min" : -1.5,
      "max" : 1.5,
      "log" : False,
    },
    "Z_dR": {
      "title" : "#Delta R_{ll}",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "Z_dEta": {
      "title" : "#Delta #eta_{ll}",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "Z_dPhi": {
      "title" : "#Delta #varphi_{ll}",
      "nbins" : 50,
      "min" : -3.14,
      "max" : 3.14,
      "log" : False,
    },
    
    
    # W
    "W_pt": {
      "title" : "W candidate p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 500,
      "log" : True,
    },
    "W_eta": {
      "title" : "W candidate #eta",
      "nbins" : 30,
      "min" : -3.,
      "max" : 3.,
      "log" : False,
    },
    "W_phi": {
      "title" : "W candidate #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "W_tmass": {
      "title" : "W candidate m_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : False,
    },
    "W_charge": {
      "title" : "W candidate charge",
      "nbins" : 3,
      "min" : -1.5,
      "max" : 1.5,
      "log" : False,
    },
    "W_dR": {
      "title" : "#Delta R_{l-#slash{E}_{T}}",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "W_dEta": {
      "title" : "#Delta #eta_{l-#slash{E}_{T}}",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "W_dPhi": {
      "title" : "#Delta #varphi_{l-#slash{E}_{T}}",
      "nbins" : 50,
      "min" : -3.14,
      "max" : 3.14,
      "log" : False,
    },
    "topMass(pt1,eta1,phi1,mass1,csv1,pt2,eta2,phi2,mass2,csv2,pt3,eta3,phi3,mass3,csv3,pt4,eta4,phi4,mass4,csv4)": {
      "title" : "Top mass",
      "nbins" : 100,
      "min" : 0,
      "max" : 250,
      "log" : False,
    },
    
    # X
    "X_pt": {
      "title" : "X candidate p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 500,
      "log" : True,
    },
    "X_eta": {
      "title" : "X candidate #eta",
      "nbins" : 30,
      "min" : -3.,
      "max" : 3.,
      "log" : False,
    },
    "X_phi": {
      "title" : "X candidate #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "X_mass": {
      "title" : "m_{X} (GeV)",
      "nbins" : -1,
      #"bins" : [500, 540, 583, 629, 678, 730, 785, 843, 904, 968, 1035, 1105, 1178, 1254, 1333, 1415, 1500, 1588, 1679, 1773, 1870, 1970, 2073, 2179, 2288, 2400, 2515, 2633, 2754, 2878, 3005, 3135, 3268, 3404, 3543, 3685, 3830, 3978, 4129, 4283, 4440, 4600],
      #"bins" : [500, 583, 678, 785, 904, 1035, 1178, 1333, 1500, 1679, 1870, 2073, 2288, 2515, 2754, 3005, 3268, 3543, 3830, 4129, 4600],
      "bins" : [x*(1+0.1*x)*40+500 for x in range(28)],#[x*(1+0.1*x)*20+500 for x in range(40)], #[x*(1+0.16*x)*50+500 for x in range(20)],
      "min" : 500.,
      "max" : 4500.,
      "log" : True,
    },
    "X_tmass": {
      "title" : "m_{T}^{X} (GeV)",
      "nbins" : -1,
      #"bins" : [500, 540, 583, 629, 678, 730, 785, 843, 904, 968, 1035, 1105, 1178, 1254, 1333, 1415, 1500, 1588, 1679, 1773, 1870, 1970, 2073, 2179, 2288, 2400, 2515, 2633, 2754, 2878, 3005, 3135, 3268, 3404, 3543, 3685, 3830, 3978, 4129, 4283, 4440, 4600],
      #"bins" : [200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1250, 1500, 2000, 2500, 3000, 3500, 4500],
      "bins" : [x*(1+0.30*x)*50+500 for x in range(15)],
      "min" : 500.,
      "max" : 4500.,
      "log" : True,
    },
    "X_cmass": {
      "title" : "collinear m_{X} (GeV)",
      "nbins" : 90,
      "min" : 500.,
      "max" : 5000.,
      "log" : True,
    },
    "X_kmass": {
      "title" : "m_{X} with kinematic fit (GeV)",
      "nbins" : 90,
      "min" : 500.,
      "max" : 5000.,
      "log" : True,
    },
    "X_charge": {
      "title" : "X candidate charge",
      "nbins" : 20,
      "min" : -10,
      "max" : 10,
      "log" : False,
    },
    "X_dR": {
      "title" : "#Delta R_{Z-jet}",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "X_dEta": {
      "title" : "#Delta #eta_{Z-jet}",
      "nbins" : 50,
      "min" : 0,
      "max" : 5,
      "log" : False,
    },
    "X_dPhi": {
      "title" : "#Delta #varphi_{Z-jet}",
      "nbins" : 50,
      "min" : -3.14,
      "max" : 3.14,
      "log" : False,
    },
    
    "transverseMass(fatjet1_pt,fatjet1_phi,met_pt,met_phi)": {
      "title" : "m_{T}^{X} (GeV)",
      "nbins" : -1,
      #"bins" : [500, 540, 583, 629, 678, 730, 785, 843, 904, 968, 1035, 1105, 1178, 1254, 1333, 1415, 1500, 1588, 1679, 1773, 1870, 1970, 2073, 2179, 2288, 2400, 2515, 2633, 2754, 2878, 3005, 3135, 3268, 3404, 3543, 3685, 3830, 3978, 4129, 4283, 4440, 4600],
      #"bins" : [200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1250, 1500, 2000, 2500, 3000, 3500, 4500],
      "bins" : [x*(1+0.5*x)*50+500 for x in range(13)],#[x*(1+0.30*x)*50+500 for x in range(15)],
      "min" : 500.,
      "max" : 4500.,
      "log" : True,
    },
    
    # Dummy
    "0*run": {
      "title" : "",
      "nbins" : 1,
      "min" : -0.5,
      "max" : 0.5,
      "log" : False,
    },
}


for n, v in var_template.iteritems():
    if '[N]' in n:
        for i in range(1, 5):
            ni = n.replace('[N]', "%d" % i)
            variable[ni] = v.copy()
            variable[ni]['title'] = variable[ni]['title'].replace('[N]', "%d" % i)
    else:
        variable[n] = v



