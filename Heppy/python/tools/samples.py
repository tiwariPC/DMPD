from collections import OrderedDict

sample = {
    'Data' : {
        'order' : 0,
        'files' : ['SingleMuon_Run2015B_PromptReco_v1', 'SingleMuon_Run2015B_17Jul2015_v1', 'SingleElectron_Run2015B_PromptReco_v1', 'SingleElectron_Run2015B_17Jul2015_v1', 'DoubleMuon_Run2015B_PromptReco_v1', 'DoubleMuon_Run2015B_17Jul2015_v1', 'DoubleEG_Run2015B_PromptReco_v1', 'DoubleEG_Run2015B_17Jul2015_v1', 'MET_Run2015B_PromptReco_v1', 'MET_Run2015B_17Jul2015_v1'],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linestyle' : 1,
        'label' : "Data",
        'weight': 1.,
        'plot': True,
    },
    'DYJetsToLL' : {
        'order' : 1,
        'files' : ['DYJetsToLL_M50_amcatnloFXFX_pythia8_v3'],
        #'files' : ['DYJetsToLL_M50_madgraphMLM_pythia8_v1'],
        'fillcolor' : 418,
        'fillstyle' : 1001,
        'linecolor' : 418,
        'linestyle' : 1,
        'label' : "Z(ll) + jets",
        'weight': 1.,
        'plot': True,
    },
    'DYJetsToLL_HT' : {
        'order' : 1,
        'files' : ['DYJetsToLL_M50_HT100to200_madgraphMLM_pythia8_v2', 'DYJetsToLL_M50_HT200to400_madgraphMLM_pythia8_v2', 'DYJetsToLL_M50_HT400to600_madgraphMLM_pythia8_v2', 'DYJetsToLL_M50_HT600toInf_madgraphMLM_pythia8_v2'],
        'fillcolor' : 418,
        'fillstyle' : 1001,
        'linecolor' : 418,
        'linestyle' : 1,
        'label' : "Z(ll) + jets",
        'weight': 1.,
        'plot': True,
    },
    'ZJetsToNuNu_HT' : {
        'order' : 1,
        'files' : ['ZJetsToNuNu_HT100to200_madgraphMLM_pythia8_v1', 'ZJetsToNuNu_HT200to400_madgraphMLM_pythia8_v1', 'ZJetsToNuNu_HT400to600_madgraphMLM_pythia8_v1', 'ZJetsToNuNu_HT600toInf_madgraphMLM_pythia8_v1'],
        'fillcolor' : 856,
        'fillstyle' : 1001,
        'linecolor' : 856,#856
        'linestyle' : 1,
        'label' : "Z(#nu#nu) + jets",
        'weight': 3., #FIXME
        'plot': True,
    },
    'WJetsToLNu' : {
        'order' : 2,
        'files' : ['WJetsToLNu_amcatnloFXFX_pythia8_v1'],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linestyle' : 1,
        'label' : "W(l#nu) + jets",
        'weight': 1.,
        'plot': True,
    },
    'TTbar' : {
        'order' : 3,
        #'files' : ['TT_powheg_pythia8_v2'],
        'files' : ['TTJets_madgraphMLM_pythia8_v2'],
        'fillcolor' : 798,
        'fillstyle' : 1001,
        'linecolor' : 798,
        'linestyle' : 1,
        'label' : "t#bar{t}",#, single t
        'weight': 1.,
        'plot': True,
    },
    'ST' : {
        'order' : 4,
        'files' : ['ST_tW_antitop_5f_inclusiveDecays_powheg_pythia8_v1','ST_t_channel_antitop_4f_leptonDecays_amcatnlo_pythia8_v1','ST_t_channel_top_4f_leptonDecays_amcatnlo_pythia8_v1','ST_s_channel_4f_leptonDecays_amcatnlo_pythia8_v1'],
        'fillcolor' : 801,
        'fillstyle' : 1001,
        'linecolor' : 801,
        'linestyle' : 1,
        'label' : "single t",
        'weight': 1.,
        'plot': True,
    },
    'VV' : {
        'order' : 5,
        'files' : ['ZZ_pythia8_v3','WZ_pythia8_v1','WW_pythia8_v1'],
        'fillcolor' : 602,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linestyle' : 1,
        'label' : "VV",
        'weight': 1.,
        'plot': True,
    },
    'QCD' : {
        'order' : 6,
        'files' : ['QCD_HT_1000to1500_madgraphMLM_pythia8_v2','QCD_HT_1500to2000_madgraphMLM_pythia8_v1','QCD_HT_2000toInf_madgraphMLM_pythia8_v1'],
        'fillcolor' : 920,
        'fillstyle' : 1001,
        'linecolor' : 920,
        'linestyle' : 1,
        'label' : "QCD",
        'weight': 1.,
        'plot': True,
    },
    # Signals 623 625 628 629 633 634 635 636
    'ZZhllbb_M600' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M600_madgraph_v1'],
        'fillcolor' : 623,
        'fillstyle' : 3005,
        'linecolor' : 623,
        'linestyle' : 1,
        'label' : "m_{Z'} = 600 GeV",
        'weight': 1.,
        'plot': False,
    },
    'ZZhllbb_M800' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M800_madgraph_v1'],
        'fillcolor' : 623,
        'fillstyle' : 3005,
        'linecolor' : 623,
        'linestyle' : 1,
        'label' : "m_{Z'} = 800 GeV",
        'weight': 1.,
        'plot': False,
    },
    'ZZhllbb_M1000' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M1000_madgraph_v1'],
        'fillcolor' : 623,
        'fillstyle' : 3005,
        'linecolor' : 623,
        'linestyle' : 1,
        'label' : "m_{Z'} = 1000 GeV",
        'weight': 1.,
        'plot': True,
    },
    'ZZhllbb_M1200' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M1200_madgraph_v1'],
        'fillcolor' : 625,
        'fillstyle' : 3005,
        'linecolor' : 625,
        'linestyle' : 1,
        'label' : "m_{Z'} = 1200 GeV",
        'weight': 1.,
        'plot': False,
    },
    'ZZhllbb_M1400' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M1400_madgraph_v1'],
        'fillcolor' : 625,
        'fillstyle' : 3005,
        'linecolor' : 625,
        'linestyle' : 1,
        'label' : "m_{Z'} = 1400 GeV",
        'weight': 1.,
        'plot': False,
    },
    'ZZhllbb_M1600' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M1600_madgraph_v1'],
        'fillcolor' : 628,
        'fillstyle' : 3005,
        'linecolor' : 628,
        'linestyle' : 1,
        'label' : "m_{Z'} = 1600 GeV",
        'weight': 1.,
        'plot': False,
    },
    'ZZhllbb_M1800' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M1800_madgraph_v1'],
        'fillcolor' : 628,
        'fillstyle' : 3005,
        'linecolor' : 628,
        'linestyle' : 1,
        'label' : "m_{Z'} = 1800 GeV",
        'weight': 1.,
        'plot': False,
    },
    'ZZhllbb_M2000' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M2000_madgraph_v1'],
        'fillcolor' : 628,
        'fillstyle' : 3005,
        'linecolor' : 628,
        'linestyle' : 1,
        'label' : "m_{Z'} = 2000 GeV",
        'weight': 1.,
        'plot': True,
    },
    'ZZhllbb_M2500' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M2500_madgraph_v1'],
        'fillcolor' : 629,
        'fillstyle' : 3005,
        'linecolor' : 629,
        'linestyle' : 1,
        'label' : "m_{Z'} = 2500 GeV",
        'weight': 1.,
        'plot': False,
    },
    'ZZhllbb_M3000' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M3000_madgraph_v1'],
        'fillcolor' : 633,
        'fillstyle' : 3005,
        'linecolor' : 633,
        'linestyle' : 1,
        'label' : "m_{Z'} = 3000 GeV",
        'weight': 1.,
        'plot': True,
    },
    'ZZhllbb_M3500' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M3500_madgraph_v1'],
        'fillcolor' : 634,
        'fillstyle' : 3005,
        'linecolor' : 634,
        'linestyle' : 1,
        'label' : "m_{Z'} = 3500 GeV",
        'weight': 1.,
        'plot': False,
    },
    'ZZhllbb_M4000' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M4000_madgraph_v1'],
        'fillcolor' : 635,
        'fillstyle' : 3005,
        'linecolor' : 635,
        'linestyle' : 1,
        'label' : "m_{Z'} = 4000 GeV",
        'weight': 1.,
        'plot': True,
    },
    'ZZhllbb_M4500' : {
        'order' : 1001,
        'files' : ['ZprimeToZhToZlephbb_narrow_M4500_madgraph_v1'],
        'fillcolor' : 635,
        'fillstyle' : 3005,
        'linecolor' : 635,
        'linestyle' : 1,
        'label' : "m_{Z'} = 4500 GeV",
        'weight': 1.,
        'plot': False,
    },
    
    # Dummy entry for background sum
    'BkgSum' : {
        'order' : 0,
        'files' : [],
        'fillcolor' : 1,
        'fillstyle' : 3003,
        'linecolor' : 1,
        'linestyle' : 1,
        'label' : "MC Stat",
        'weight': 1.,
        'plot': True,
    },
}

#samplegroups = {

    ##'QCD' : {
        ##'order' : 1,
        ##'files' : ['QCD_HT100To250','QCD_HT250To500','QCD_HT500To1000','QCD_HT1000ToInf'],
        ###'files' : ['QCD_HT500To1000','QCD_HT1000ToInf'],
        ##'color' : 920,#9909,
        ##'lcolor': 921,#9909,
        ##'label' : 'QCD',
        ##'weight': 1.,
        ##},

    #'singleT' : {
        #'order' : 2,
        #'files' : ['TToLeptons_schannel','TbarToLeptons_schannel','TToLeptons_tchannel','TbarToLeptons_tchannel','T_tWchannel','Tbar_tWchannel'],
        #'color' : 9908,
        #'lcolor': 9918,
        #'label' : 'single t',
        #'weight': 1.,
        #},

    #'TT' : {
        #'order' : 3,
        #'files' : ['TTJets'],
        #'color' : 9903,
        #'lcolor': 9913,
        #'label' : 't#bar{t}',
        #'weight': 1.,
        #},

    #'Gamma' : {
        #'order' : 4,
        #'files' : ['GJets_HT100to200','GJets_HT200to400','GJets_HT400to600','GJets_HT600toInf'],
        #'color' : 9904,
        #'lcolor': 9914,
        #'label' : '#gamma + jets',
        #'weight': 1.,
        #},

    #'Zmumu' : {
        #'order' : 5,
        #'files' : ['DYJetsToLL_M50_HT100to200','DYJetsToLL_M50_HT200to400','DYJetsToLL_M50_HT400to600','DYJetsToLL_M50_HT600toInf'],
        #'color' : 9905,
        #'lcolor': 9915,
        #'label' : 'Z#rightarrow#mu#mu + jets',
        #'weight': 1.,
        #},

    #'Wmunu' : {
        #'order' : 6,
        #'files' : ['WJetsToLNu_HT100to200','WJetsToLNu_HT200to400','WJetsToLNu_HT400to600','WJetsToLNu_HT600toInf'],
        #'color' : 9901,
        #'lcolor': 9911,
        #'label' : 'W#rightarrow#mu#nu + jets',
        #'weight': 1.,
        #},

    #'Znunu' : {
        #'order' : 7,
        #'files' : ['ZJetsToNuNu_HT100to200','ZJetsToNuNu_HT200to400','ZJetsToNuNu_HT400to600','ZJetsToNuNu_HT600toInf'],
        #'color' : 9906,
        #'lcolor': 9916,
        #'label' : 'Z#rightarrow#nu#nu + jets',
        #'weight': 1.,
        #},

    #'signal_DMM1AV' : {
        #'order' : 9,
        #'files' : ['DM_Monojet_M1_AV'],
        #'color' : 0,
        #'lcolor': 9957,
        #'label' : 'DM M1 AV [#sigma=1pb]',
        #'weight': 1.,
        #},

    #'signal_DMM10AV' : {
        #'order' : 10,
        #'files' : ['DM_Monojet_M10_AV'],
        #'color' : 0,
        #'lcolor': 9956,
        #'label' : 'DM M10 AV [#sigma=1pb]',
        #'weight': 1.,
        #},
    
    #'signal_DMM10V' : {
        #'order' : 11,
        #'files' : ['DM_Monojet_M10_V'],
        #'color' : 0,
        #'lcolor': 9955,
        #'label' : 'DM M10 V [#sigma=1pb]',
        #'weight': 1.,
        #},
    
    #'signal_DMM100AV' : {
        #'order' : 12,
        #'files' : ['DM_Monojet_M100_AV'],
        #'color' : 0,
        #'lcolor': 9954,
        #'label' : 'DM M100 AV [#sigma=1pb]',
        #'weight': 1.,
        #},
        
    #'signal_DMM100V' : {
        #'order' : 13,
        #'files' : ['DM_Monojet_M100_V'],
        #'color' : 0,
        #'lcolor': 9953,
        #'label' : 'DM M100 V [#sigma=1pb]',
        #'weight': 1.,
        #},
    
    #'signal_DMM1000AV' : {
        #'order' : 14,
        #'files' : ['DM_Monojet_M1000_AV'],
        #'color' : 0,
        #'lcolor': 9952,
        #'label' : 'DM M1000 AV [#sigma=1pb]',
        #'weight': 1.,
        #},
    
    #'signal_DMM1000V' : {
        #'order' : 15,
        #'files' : ['DM_Monojet_M1000_V'],
        #'color' : 0,
        #'lcolor': 9951,
        #'label' : 'DM M1000 V [#sigma=1pb]',
        #'weight': 1.,
        #},

    #'signal_ZnunuHbb' : {
        #'order' : 16,
        #'files' : ['ZH_HToBB_ZToNuNu'],
        #'color' : 60,
        #'lcolor': 60,
        #'label' : 'Z#rightarrow#nu#nu + H#rightarrowbb [#sigma=1pb]',
        #'weight': 1.,
        #},

    #'signal_DMMonoB' : {
        #'order' : 17,
        #'files' : ['DM_MonoB'],
        #'color' : 70,
        #'lcolor': 70,
        #'label' : 'DM-b/bb [#sigma=1pb]',
        #'weight': 1.,
        #},

    #'signal_DMMonoVbb' : {
        #'order' : 18,
        #'files' : ['DM_MonoVbb'],
        #'color' : 80,
        #'lcolor': 80,
        #'label' : 'DM-Z(bb) [#sigma=1pb]',
        #'weight': 1.,
        #},

    #'signal_DMMonoH' : {
        #'order' : 19,
        #'files' : ['DM_MonoH'],
        #'color' : 90,
        #'lcolor': 90,
        #'label' : 'DM-H(bb) [#sigma=1pb]',
        #'weight': 1.,
        #},

#}

samplegroups = {

    'QCD' : {
        'order' : 1,
        #'files' : ['QCD_HT100To250','QCD_HT250To500','QCD_HT500To1000','QCD_HT1000ToInf'],
        #'files' : ['QCD_HT500To1000','QCD_HT1000ToInf'],
        'files' : ['QCD_HT1000ToInf'],
        'color' : 920,#9909,
        'lcolor': 921,#9909,
        'label' : 'QCD',
        'weight': 1.,
        'region': ['SR','ZCR','WCR','GCR'],
        },

    'Top' : {
        'order' : 2,
        'files' : ['Top'],
        'color' : 9903,
        'lcolor': 9913,
        'label' : 't',
        'weight': 1.,
        'region': ['SR','ZCR','WCR','GCR'],
        },

    'Gamma' : {
        'order' : 4,
        'files' : ['GJets'],
        'color' : 9904,
        'lcolor': 9914,
        'label' : '#gamma + jets',
        'weight': 1.,
        'region': ['SR','ZCR','WCR','GCR'],
        },

    'Zmumu' : {
        'order' : 5,
        'files' : ['DYJetsToLL'],
        'color' : 9905,
        'lcolor': 9915,
        'label' : 'Z#rightarrow#mu#mu + jets',
        'weight': 1.,
        'region': ['SR','ZCR','WCR','GCR'],        
        },

    'Wmunu' : {
        'order' : 6,
        'files' : ['WJetsToLNu'],
        'color' : 9901,
        'lcolor': 9911,
        'label' : 'W#rightarrow#mu#nu + jets',
        'weight': 1.,
        'region': ['SR','ZCR','WCR','GCR'],        
        },

    'Znunu' : {
        'order' : 7,
        'files' : ['ZJetsToNuNu'],
        'color' : 9906,
        'lcolor': 9916,
        'label' : 'Z#rightarrow#nu#nu + jets',
        'weight': 1.,
        'region': ['SR','ZCR','WCR','GCR'],        
        },

    #'signal_DMM1AV' : {
        #'order' : 9,
        #'files' : ['DM_Monojet_M1_AV'],
        #'color' : 0,
        #'lcolor': 9957,
        #'label' : 'DM M1 AV [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},

    #'signal_DMM10AV' : {
        #'order' : 10,
        #'files' : ['DM_Monojet_M10_AV'],
        #'color' : 0,
        #'lcolor': 9956,
        #'label' : 'DM M10 AV [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},
    
    #'signal_DMM10V' : {
        #'order' : 11,
        #'files' : ['DM_Monojet_M10_V'],
        #'color' : 0,
        #'lcolor': 9955,
        #'label' : 'DM M10 V [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},
    
    'signal_DMM100AV' : {
        'order' : 12,
        'files' : ['DM_Monojet_M100_AV'],
        'color' : 0,
        'lcolor': 9954,
        'label' : 'DM M100 AV [#sigma=1pb]',
        'weight': 1.,
        'region': ['SR'],        
        },
        
    #'signal_DMM100V' : {
        #'order' : 13,
        #'files' : ['DM_Monojet_M100_V'],
        #'color' : 0,
        #'lcolor': 9953,
        #'label' : 'DM M100 V [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},
    
    #'signal_DMM1000AV' : {
        #'order' : 14,
        #'files' : ['DM_Monojet_M1000_AV'],
        #'color' : 0,
        #'lcolor': 9952,
        #'label' : 'DM M1000 AV [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},
    
    #'signal_DMM1000V' : {
        #'order' : 15,
        #'files' : ['DM_Monojet_M1000_V'],
        #'color' : 0,
        #'lcolor': 9951,
        #'label' : 'DM M1000 V [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},

    #'signal_ZnunuHbb' : {
        #'order' : 16,
        #'files' : ['ZH_HToBB_ZToNuNu'],
        #'color' : 60,
        #'lcolor': 60,
        #'label' : 'Z#rightarrow#nu#nu + H#rightarrowbb [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},

    #'signal_DMMonoB' : {
    #    'order' : 17,
    #    'files' : ['DM_MonoB'],
    #    'color' : 0,
    #    'lcolor': 9950,
    #    'label' : 'DM+bb [#sigma=1pb]',
    #    'weight': 1.,
    #    'region': ['SR'],        
    #    },

    #'signal_DMMonoVbb' : {
        #'order' : 18,
        #'files' : ['DM_MonoVbb'],
        #'color' : 80,
        #'lcolor': 80,
        #'label' : 'DM-Z(bb) [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},

    #'signal_DMMonoH' : {
        #'order' : 19,
        #'files' : ['DM_MonoH'],
        #'color' : 90,
        #'lcolor': 90,
        #'label' : 'DM-H(bb) [#sigma=1pb]',
        #'weight': 1.,
        #'region': ['SR'],        
        #},

}
    
samplegroups = OrderedDict(sorted(samplegroups.iteritems(), key=lambda x: x[1]['order']))
