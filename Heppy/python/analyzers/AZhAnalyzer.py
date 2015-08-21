from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaR2, deltaPhi
import copy
import math
import ROOT
from array import array

class AZhAnalyzer( Analyzer ):
    '''Analyzer for the Z' -> Zh -> (ll/nunu)bb analysis'''

    def beginLoop(self, setup):
        super(AZhAnalyzer, self).beginLoop(setup)
        self.Hist = {}
        
        Z2LLlabels = ["Trigger", "#Lep #geq 2", "Z cand", "Jet p_{T}", "Z p_{T}", "Z mass", "h mass", "b-tag 1", "b-tag 2"]
        Z2NNlabels = ["Trigger", "e/#mu veto", "Jet p_{T}", "#slash{E}_{T}", "#Delta #varphi > 2.5", "h mass", "b-tag 1", "b-tag 2"]
        HEEPlabels = ["isEcalDriven", "#Delta #eta_{in}^{seed}", "#Delta #varphi_{in}", "H/E", "E^{2x5}/E^{5x5}", "Lost Hits", "|d_{xy}|"]
        pTbins = [0., 5., 10., 15., 20., 25., 30., 35., 40., 45., 50., 60., 70., 80., 90., 100., 110., 120., 130., 150., 175., 200., 225., 250., 300., 350., 400., 500., 750., 1000., 1250., 1500., 2000., 2500.]
        dRbins = [0., 0.025, 0.05, 0.075, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.75, 1.0]
        if "outputfile" in setup.services:
            setup.services["outputfile"].file.cd("Counters")
            self.Hist["Z2EECounter"] = ROOT.TH1F("ZtoEECounter", "", len(Z2LLlabels), 0, len(Z2LLlabels))
            self.Hist["Z2MMCounter"] = ROOT.TH1F("ZtoMMCounter", "", len(Z2LLlabels), 0, len(Z2LLlabels))
            self.Hist["Z2NNCounter"] = ROOT.TH1F("ZtoNNCounter", "", len(Z2NNlabels), 0, len(Z2NNlabels))
            for i, l in enumerate(Z2LLlabels):
                self.Hist["Z2EECounter"].GetXaxis().SetBinLabel(i+1, l)
                self.Hist["Z2MMCounter"].GetXaxis().SetBinLabel(i+1, l)
            for i, l in enumerate(Z2NNlabels):
                self.Hist["Z2NNCounter"].GetXaxis().SetBinLabel(i+1, l)
            setup.services["outputfile"].file.cd("..")
            #
            setup.services["outputfile"].file.mkdir("Leptons")
            setup.services["outputfile"].file.cd("Leptons")
            for i, n in enumerate(["Elec1", "Elec2", "Muon1", "Muon2"]):
                self.Hist[n] = ROOT.TH1F(n, ";Lepton p_{T} (GeV);Events", len(pTbins)-1, array('f', pTbins))
            for i, n in enumerate(["ElecZdR", "MuonZdR"]):
                self.Hist[n] = ROOT.TH1F(n, ";gen #Delta R;Events", len(dRbins)-1, array('f', dRbins))
            self.Hist["HEEP_EB"] = ROOT.TH1F("HEEP_EB", ";;Events", len(HEEPlabels), 0, len(HEEPlabels))
            self.Hist["HEEP_EE"] = ROOT.TH1F("HEEP_EE", ";;Events", len(HEEPlabels), 0, len(HEEPlabels))
            for i, l in enumerate(HEEPlabels):
                self.Hist["HEEP_EB"].GetXaxis().SetBinLabel(i+1, l)
                self.Hist["HEEP_EE"].GetXaxis().SetBinLabel(i+1, l)
            self.Hist["HEEP_EE"].GetXaxis().SetBinLabel(5, "#sigma_{i#eta i#eta}")
            setup.services["outputfile"].file.cd("..")
            #
            setup.services["outputfile"].file.mkdir("Eff")
            setup.services["outputfile"].file.cd("Eff")
            for i, n in enumerate(["EffElec1_HEEP", "EffElec2_HEEP", "EffMuon1_HighPt", "EffMuon2_HighPt"]):
                self.Hist[n] = ROOT.TH1F(n, ";Lepton p_{T} (GeV);Efficiency", len(pTbins)-1, array('f', pTbins))
            for i, n in enumerate(["EffElecZdR", "EffElecZdR_Loose", "EffElecZdR_Tight", "EffElecZdR_HEEP", "EffElecZdR_HEEPpfIso", "EffElecZdR_HEEPminiIso", "EffMuonZdR", "EffMuonZdR_Loose_Loose", "EffMuonZdR_HighPt_Loose", "EffMuonZdR_HighPt_HighPt", "EffMuonZdR_Tight_Tight"]):
                self.Hist[n] = ROOT.TH1F(n, ";gen #Delta R;Efficiency", len(dRbins)-1, array('f', dRbins))
            self.Hist["EffHEEP_EB"] = ROOT.TH1F("EffHEEP_EB", ";;Efficiency", len(HEEPlabels), 0, len(HEEPlabels))
            self.Hist["EffHEEP_EE"] = ROOT.TH1F("EffHEEP_EE", ";;Efficiency", len(HEEPlabels), 0, len(HEEPlabels))
            for i, l in enumerate(HEEPlabels):
                self.Hist["EffHEEP_EB"].GetXaxis().SetBinLabel(i+1, l)
                self.Hist["EffHEEP_EE"].GetXaxis().SetBinLabel(i+1, l)
            self.Hist["EffHEEP_EE"].GetXaxis().SetBinLabel(5, "#sigma_{i#eta i#eta}")
            # Set Sumw2
            for n, h in self.Hist.iteritems():
                h.Sumw2()

            
    def endLoop(self, setup):
        self.Hist["EffElec1_HEEP"].Divide(self.Hist["Elec1"])
        self.Hist["EffElec2_HEEP"].Divide(self.Hist["Elec2"])
        self.Hist["EffMuon1_HighPt"].Divide(self.Hist["Muon1"])
        self.Hist["EffMuon2_HighPt"].Divide(self.Hist["Muon2"])
        self.Hist["EffElecZdR_Loose"].Divide(self.Hist["ElecZdR"])
        self.Hist["EffElecZdR_Tight"].Divide(self.Hist["ElecZdR"])
        self.Hist["EffElecZdR_HEEP"].Divide(self.Hist["ElecZdR"])
        self.Hist["EffElecZdR_HEEPpfIso"].Divide(self.Hist["ElecZdR"])
        self.Hist["EffElecZdR_HEEPminiIso"].Divide(self.Hist["ElecZdR"])
        self.Hist["EffMuonZdR"].Divide(self.Hist["MuonZdR"])
        self.Hist["EffMuonZdR_Loose_Loose"].Divide(self.Hist["MuonZdR"])
        self.Hist["EffMuonZdR_HighPt_Loose"].Divide(self.Hist["MuonZdR"])
        self.Hist["EffMuonZdR_HighPt_HighPt"].Divide(self.Hist["MuonZdR"])
        self.Hist["EffMuonZdR_Tight_Tight"].Divide(self.Hist["MuonZdR"])
        self.Hist["EffHEEP_EB"].Divide(self.Hist["HEEP_EB"])
        self.Hist["EffHEEP_EE"].Divide(self.Hist["HEEP_EE"])
        
        
        
    def fillGenPlots(self, event):
        if hasattr(event, "genleps") and len(event.genleps) >= 2:
            i1, i2 = [0, 1] if event.genleps[0].pt() > event.genleps[1].pt() else [1, 0]
            l1, l2 = -1, -1
            genZdR = deltaR(event.genleps[i1].eta(), event.genleps[i1].phi(), event.genleps[i2].eta(), event.genleps[i2].phi())
            # Electrons
            if abs(event.genleps[0].pdgId())==11:
                for i, l in enumerate(event.highptElectrons):
                    if deltaR(l.eta(), l.phi(), event.genleps[i1].eta(), event.genleps[i1].phi())<0.1 and abs(1-l.pt()/event.genleps[i1].pt()) < 0.3: l1 = i
                    elif deltaR(l.eta(), l.phi(), event.genleps[i2].eta(), event.genleps[i2].phi())<0.1 and abs(1-l.pt()/event.genleps[i2].pt()) < 0.3: l2 = i
                self.Hist["Elec1"].Fill(event.genleps[i1].pt())
                self.Hist["Elec2"].Fill(event.genleps[i2].pt())
                self.Hist["ElecZdR"].Fill(genZdR)
                if l1 >= 0 and l2 >= 0:
                    if event.highptElectrons[l1].isHEEP: self.Hist["EffElec1_HEEP"].Fill(event.genleps[i1].pt())
                    if event.highptElectrons[l2].isHEEP: self.Hist["EffElec2_HEEP"].Fill(event.genleps[i2].pt())    
                    # deltaR
                    self.Hist["EffElecZdR"].Fill(genZdR)
                    if event.highptElectrons[l1].electronID('POG_Cuts_ID_PHYS14_25ns_v1_ConvVetoDxyDz_Loose') and event.highptElectrons[l2].electronID('POG_Cuts_ID_PHYS14_25ns_v1_ConvVetoDxyDz_Loose'): self.Hist["EffElecZdR_Loose"].Fill(genZdR)
                    if event.highptElectrons[l1].electronID('POG_Cuts_ID_PHYS14_25ns_v1_ConvVetoDxyDz_Tight') and event.highptElectrons[l2].electronID('POG_Cuts_ID_PHYS14_25ns_v1_ConvVetoDxyDz_Tight'): self.Hist["EffElecZdR_Tight"].Fill(genZdR)
                    if event.highptElectrons[l1].isHEEP and event.highptElectrons[l2].isHEEP: self.Hist["EffElecZdR_HEEP"].Fill(genZdR)
                    if event.highptElectrons[l1].isHEEP and event.highptElectrons[l2].isHEEP and event.highptElectrons[l1].miniRelIso<0.1 and event.highptElectrons[l2].miniRelIso<0.1: self.Hist["EffElecZdR_HEEPminiIso"].Fill(genZdR)
                    if event.highptElectrons[l1].isHEEP and event.highptElectrons[l2].isHEEP and event.highptElectrons[l1].relIso03<0.15 and event.highptElectrons[l2].relIso03<0.15: self.Hist["EffElecZdR_HEEPpfIso"].Fill(genZdR)
                    
                
            # Muons
            if abs(event.genleps[0].pdgId())==13:
                for i, l in enumerate(event.highptMuons):
                    if deltaR(l.eta(), l.phi(), event.genleps[i1].eta(), event.genleps[i1].phi())<0.1 and abs(1-l.pt()/event.genleps[i1].pt()) < 0.3: l1 = i
                    elif deltaR(l.eta(), l.phi(), event.genleps[i2].eta(), event.genleps[i2].phi())<0.1 and abs(1-l.pt()/event.genleps[i2].pt()) < 0.3: l2 = i
                self.Hist["Muon1"].Fill(event.genleps[i1].pt())
                self.Hist["Muon2"].Fill(event.genleps[i2].pt())
                self.Hist["MuonZdR"].Fill(genZdR)
                if l1 >= 0 and l2 >= 0:
                    if event.highptMuons[l1].muonID("POG_ID_HighPt"): self.Hist["EffMuon1_HighPt"].Fill(event.genleps[i1].pt())
                    if event.highptMuons[l2].muonID("POG_ID_HighPt"): self.Hist["EffMuon2_HighPt"].Fill(event.genleps[i2].pt())
                    # deltaR
                    self.Hist["EffMuonZdR"].Fill(genZdR)
                    if event.highptMuons[l1].muonID("POG_ID_Loose") and event.highptMuons[l2].muonID("POG_ID_Loose"): self.Hist["EffMuonZdR_Loose_Loose"].Fill(genZdR)
                    if event.highptMuons[l1].muonID("POG_ID_HighPt") or event.highptMuons[l2].muonID("POG_ID_HighPt"): self.Hist["EffMuonZdR_HighPt_Loose"].Fill(genZdR)
                    if event.highptMuons[l1].muonID("POG_ID_HighPt") and event.highptMuons[l2].muonID("POG_ID_HighPt"): self.Hist["EffMuonZdR_HighPt_HighPt"].Fill(genZdR)
                    if event.highptMuons[l1].muonID("POG_ID_Tight") and event.highptMuons[l2].muonID("POG_ID_Tight"): self.Hist["EffMuonZdR_Tight_Tight"].Fill(genZdR)

    
    
    def addFakeMet(self, event, particles):
        # Copy regular met
        event.fakemet = copy.deepcopy(event.met)
        px, py = event.met.px(), event.met.py()
        for i, p in enumerate(particles):
            if not p:
                continue
            else:
                px += p.px()
                py += p.py()
        
        event.fakemet.setP4(ROOT.reco.Particle.LorentzVector(px, py, 0, math.hypot(px, py)))
        return True
    
    def isHEEP(self, e):
        e.isHEEP = False
        if not e.pt() > 35.: return False
        
        if e.superCluster().isNonnull() and e.superCluster().seed().isNonnull():
            dEtaInSeed = e.deltaEtaSuperClusterTrackAtVtx() - e.superCluster().eta() + e.superCluster().seed().eta()
        else:
            dEtaInSeed = 1.e99
        
        if hasattr(e.gsfTrack(),"trackerExpectedHitsInner"):
		        nMissingHits = e.gsfTrack().trackerExpectedHitsInner().numberOfLostHits()
        else:
		        nMissingHits = e.gsfTrack().hitPattern().numberOfHits(ROOT.reco.HitPattern.MISSING_INNER_HITS)
        
        if abs(e.superCluster().eta()) < 1.4442:
            for i in range(self.Hist["HEEP_EB"].GetNbinsX()): self.Hist["HEEP_EB"].AddBinContent(i+1)
            if not e.ecalDriven(): return False
            self.Hist["EffHEEP_EB"].AddBinContent(1)
            if not abs(dEtaInSeed) < 0.004: return False
            self.Hist["EffHEEP_EB"].AddBinContent(2)
            if not abs(e.deltaPhiSuperClusterTrackAtVtx()) < 0.06: return False
            self.Hist["EffHEEP_EB"].AddBinContent(3)
            if not e.hadronicOverEm() < 1./e.energy() + 0.05: return False
            self.Hist["EffHEEP_EB"].AddBinContent(4)
            if not (e.e2x5Max()/e.e5x5() > 0.94 or e.e1x5()/e.e5x5() > 0.83): return False
            self.Hist["EffHEEP_EB"].AddBinContent(5)
            if not nMissingHits <= 1: return False
            self.Hist["EffHEEP_EB"].AddBinContent(6)
            if not abs(e.dxy()) < 0.02: return False
            self.Hist["EffHEEP_EB"].AddBinContent(7)
        elif abs(e.superCluster().eta()) > 1.566 and abs(e.superCluster().eta()) < 2.5:
            for i in range(self.Hist["HEEP_EE"].GetNbinsX()): self.Hist["HEEP_EE"].AddBinContent(i+1)
            if not e.ecalDriven(): return False
            self.Hist["EffHEEP_EE"].AddBinContent(1)
            if not abs(dEtaInSeed) < 0.006: return False
            self.Hist["EffHEEP_EE"].AddBinContent(2)
            if not abs(e.deltaPhiSuperClusterTrackAtVtx()) < 0.06: return False
            self.Hist["EffHEEP_EE"].AddBinContent(3)
            if not e.hadronicOverEm() < 5./e.energy() + 0.05: return False
            self.Hist["EffHEEP_EE"].AddBinContent(4)
            if not e.sigmaIetaIeta() < 0.03: return False
            self.Hist["EffHEEP_EE"].AddBinContent(5)
            if not nMissingHits <= 1: return False
            self.Hist["EffHEEP_EE"].AddBinContent(6)
            if not abs(e.dxy()) < 0.05: return False
            self.Hist["EffHEEP_EE"].AddBinContent(7)
        else:
            return False

        e.isHEEP = True
        return True
    
    
    def process(self, event):
        event.isAZh = False
        event.isZ2EE = False
        event.isZ2MM = False
        event.isZ2NN = False
         # All
        self.Hist["Z2EECounter"].AddBinContent(0)
        self.Hist["Z2MMCounter"].AddBinContent(0)
        self.Hist["Z2NNCounter"].AddBinContent(0)
        
         # Trigger
        if event.HLT_BIT_HLT_Ele105_CaloIdVT_GsfTrkIdT_v: self.Hist["Z2EECounter"].AddBinContent(1)
        if event.HLT_BIT_HLT_Mu45_eta2p1_v: self.Hist["Z2MMCounter"].AddBinContent(1)
        if event.HLT_BIT_HLT_PFMET170_NoiseCleaned_v: self.Hist["Z2NNCounter"].AddBinContent(1)
        
        #########################
        #    Part 1: Leptons    #
        #########################
        
        # Separate inclusive lepton collections
        event.highptElectrons = [x for x in event.inclusiveLeptons if x.isElectron() and x.electronID('POG_Cuts_ID_PHYS14_25ns_v1_ConvVetoDxyDz_Loose')] # and self.isHEEP(x) and x.miniRelIso<0.1
        event.highptMuons = [x for x in event.inclusiveLeptons if x.isMuon() and x.muonID("POG_ID_Loose")] #x.isTrackerMuon() and x.miniRelIso<0.1
        event.highptLeptons = []
        event.highptElectrons.sort(key = lambda l : l.pt(), reverse = True)
        event.highptMuons.sort(key = lambda l : l.pt(), reverse = True)
        #
        for i, e in enumerate(event.highptElectrons): self.isHEEP(e)
        #for i, m in enumerate(event.highptMuons): print m.pt(), m.tunePMuonBestTrack().pt()
        
        self.fillGenPlots(event)
        
        # Categorization
        if len(event.highptElectrons) >= 2 and event.highptElectrons[0].pt() > self.cfg_ana.elec1pt and event.highptElectrons[1].pt() > self.cfg_ana.elec2pt:
            event.isZ2EE = True
        elif len(event.highptMuons) >= 2 and event.highptMuons[0].pt() > self.cfg_ana.muon1pt and event.highptMuons[1].pt() > self.cfg_ana.muon2pt:
            event.isZ2MM = True
        elif len(event.selectedMuons) + len(event.selectedElectrons) == 0:
            event.isZ2NN = True
        else:
            return True
        
        event.isZ2LL = event.isZ2EE or event.isZ2MM
        
         # Lep > 2 / Veto
        if event.isZ2EE: self.Hist["Z2EECounter"].AddBinContent(2)
        if event.isZ2MM: self.Hist["Z2MMCounter"].AddBinContent(2)
        if event.isZ2NN: self.Hist["Z2NNCounter"].AddBinContent(2)
        
        # Build Z candidate
        if event.isZ2EE and event.highptElectrons[0].charge() != event.highptElectrons[1].charge():
            event.highptLeptons = event.highptElectrons
        elif event.isZ2MM and event.highptMuons[0].charge() != event.highptMuons[1].charge():
            event.highptLeptons = event.highptMuons
        elif event.isZ2NN:
            event.highptLeptons = []
        else:
            return True
        
        # Z candidate
        if event.isZ2LL:
            event.Z = event.highptLeptons[0].p4() + event.highptLeptons[1].p4()
            event.Z.charge = event.highptLeptons[0].charge() + event.highptLeptons[1].charge()
            event.Z.deltaR = deltaR(event.highptLeptons[0].eta(), event.highptLeptons[0].phi(), event.highptLeptons[1].eta(), event.highptLeptons[1].phi())
            event.Z.deltaEta = abs(event.highptLeptons[0].eta() - event.highptLeptons[1].eta())
            event.Z.deltaPhi = deltaPhi(event.highptLeptons[0].phi(), event.highptLeptons[1].phi())
        else:
            event.Z = ROOT.reco.Particle.LorentzVector(0, 0, 0, 0)
        
        if event.isZ2LL and event.Z.mass() < 50.:
            return True
        
        # Z cand
        if event.isZ2EE: self.Hist["Z2EECounter"].AddBinContent(3)
        if event.isZ2MM: self.Hist["Z2MMCounter"].AddBinContent(3)
        
        
        #FIXME
        event.A = ROOT.reco.Particle.LorentzVector(0, 0, 0, 0)
        event.fakemet = ROOT.reco.Particle.LorentzVector(0, 0, 0, 0)
        event.isAZh = True
        
        #########################
        #    Part 2: Jets       #
        #########################
        
#        print "###########", "Muon" if event.isZ2MM else "ELE"
#        for i, j in enumerate(event.highptLeptons): print i, j.pt(), j.eta(), j.phi(), j.isMuon()
#        for i, j in enumerate(event.cleanJetsAK8): print i, j.pt(), j.eta(), j.phi()
        
        #FIXME
#        if len(event.cleanJetsAK8) < 1:
#            event.cleanJetsAK8.append( ROOT.pat.Jet() )
        
        if len(event.cleanJetsAK8) < 1 or event.cleanJetsAK8[0].pt() < self.cfg_ana.fatjet_pt:
            return True
        if event.isZ2EE: self.Hist["Z2EECounter"].AddBinContent(4)
        if event.isZ2MM: self.Hist["Z2MMCounter"].AddBinContent(4)
        if event.isZ2NN: self.Hist["Z2NNCounter"].AddBinContent(3)
        
        
        #########################
        #   Part 3: Candidates  #
        #########################
        
        # h candidate with pseudo-kin fit
        kH = event.cleanJetsAK8[0].p4()
        k = 125.0/event.cleanJetsAK8[0].mass() if event.cleanJetsAK8[0].mass() > 0 else 0. #.userFloat("ak8PFJetsCHSSoftDropMass")
        kH = ROOT.reco.Particle.LorentzVector(event.cleanJetsAK8[0].px()*k, event.cleanJetsAK8[0].py()*k, event.cleanJetsAK8[0].pz()*k, event.cleanJetsAK8[0].energy()*k)
        
        # A/Z' candidate
        if event.isZ2LL:
            event.A = event.Z + event.cleanJetsAK8[0].p4()
            event.A.mT = event.A.mass()
            event.A.mC = event.A.mass()
            event.A.mK = (event.Z + kH).mass()
            event.A.deltaR = deltaR(event.Z.eta(), event.Z.phi(), event.cleanJetsAK8[0].eta(), event.cleanJetsAK8[0].phi())
            event.A.deltaEta = abs(event.Z.eta() - event.cleanJetsAK8[0].eta())
            event.A.deltaPhi = deltaPhi(event.Z.phi(), event.cleanJetsAK8[0].phi())
        elif len(event.highptLeptons) == 1:
            event.A = event.highptLeptons[0].p4() + event.met.p4() + event.cleanJetsAK8[0].p4()
            pz = 0.
            a = 80.4**2 - event.highptLeptons[0].mass()**2 + 2.*event.highptLeptons[0].px()*event.met.px() + 2.*event.highptLeptons[0].py()*event.met.py()
            A = 4*( event.highptLeptons[0].energy()**2 - event.highptLeptons[0].pz()**2 )
            B = -4*a*event.highptLeptons[0].pz()
            C = 4*event.highptLeptons[0].energy()**2 * (event.met.px()**2  + event.met.py()**2) - a**2
            D = B**2 - 4*A*C
            if D>0:
                pz = min((-B+math.sqrt(D))/(2*A), (-B-math.sqrt(D))/(2*A))
            else:
                pz = -B/(2*A)
            kmet = event.met.p4()
            kmet.SetPz(pz)
            event.A.mT = (event.highptLeptons[0].p4() + kmet + event.cleanJetsAK8[0].p4()).mass()
            cmet = event.met.p4()
            cmet.SetPz(event.highptLeptons[0].pz())
            event.A.mC = (event.highptLeptons[0].p4() + cmet + event.cleanJetsAK8[0].p4()).mass()
            event.A.mK = (event.highptLeptons[0].p4() + kmet + kH).mass()
        else:
            event.A = event.met.p4() + event.cleanJetsAK8[0].p4()
            event.A.mT = math.sqrt( 2.*event.cleanJetsAK8[0].energy()*event.met.pt()*(1.-math.cos( deltaPhi(event.cleanJetsAK8[0].phi(), event.met.phi()) )) )
            cmet = event.met.p4()
            cmet.SetPz( -event.cleanJetsAK8[0].pz() )
            event.A.mC = (cmet + event.cleanJetsAK8[0].p4()).mass()
            event.A.mK = math.sqrt( 2.*kH.energy()*event.met.pt()*(1.-math.cos( deltaPhi(kH.phi(), event.met.phi()) )) )
        
        if event.isZ2LL:
            self.addFakeMet(event, [event.highptLeptons[0], event.highptLeptons[1]])
        else:
            self.addFakeMet(event, [])
        
        if (event.isZ2LL and event.Z.pt() < self.cfg_ana.Z_pt) or (event.isZ2NN and event.met.pt() < self.cfg_ana.met_pt):
            return True
        
        
        # Fill tree
        event.isAZh = True
        
        # ---------- Estimate cuts ----------
#        if len(event.cleanJetsAK8) <= 1 or event.cleanJetsAK8[0].pt() < self.cfg_ana.fatjet_pt: #FIXME
#            event.cleanJetsAK8.pop()
#            return True
#        if event.isZ2EE: self.Hist["Z2EECounter"].AddBinContent(4)
#        if event.isZ2MM: self.Hist["Z2MMCounter"].AddBinContent(4)
#        if event.isZ2NN: self.Hist["Z2NNCounter"].AddBinContent(3)
        
        if event.isZ2LL: 
            if event.Z.pt() > 200:
                self.Hist["Z2EECounter"].AddBinContent(5) if event.isZ2EE else self.Hist["Z2MMCounter"].AddBinContent(5)
                if event.Z.mass() > 75 and event.Z.mass() < 105:
                    self.Hist["Z2EECounter"].AddBinContent(6) if event.isZ2EE else self.Hist["Z2MMCounter"].AddBinContent(6)
                    if event.cleanJetsAK8[0].userFloat("ak8PFJetsCHSSoftDropMass") > 90 and event.cleanJetsAK8[0].userFloat("ak8PFJetsCHSSoftDropMass") < 150:
                        self.Hist["Z2EECounter"].AddBinContent(7) if event.isZ2EE else self.Hist["Z2MMCounter"].AddBinContent(7)
                        if event.cleanJetsAK8[0].subjets('SoftDrop')[0].bDiscriminator('pfCombinedInclusiveSecondaryVertexV2BJetTags') > 0.605:
                            self.Hist["Z2EECounter"].AddBinContent(8) if event.isZ2EE else self.Hist["Z2MMCounter"].AddBinContent(8)
                            if event.cleanJetsAK8[0].subjets('SoftDrop')[1].bDiscriminator('pfCombinedInclusiveSecondaryVertexV2BJetTags') > 0.605: 
                                self.Hist["Z2EECounter"].AddBinContent(9) if event.isZ2EE else self.Hist["Z2MMCounter"].AddBinContent(9)
        if event.isZ2NN: 
            if event.met.pt() > 200:
                self.Hist["Z2NNCounter"].AddBinContent(4)
                if event.cleanJetsAK8[0].deltaPhi_met>2.5:
                    if event.cleanJetsAK8[0].userFloat("ak8PFJetsCHSSoftDropMass") > 90 and event.cleanJetsAK8[0].userFloat("ak8PFJetsCHSSoftDropMass") < 150:
                        self.Hist["Z2NNCounter"].AddBinContent(5)
                        if event.cleanJetsAK8[0].subjets('SoftDrop')[0].bDiscriminator('pfCombinedInclusiveSecondaryVertexV2BJetTags') > 0.605:
                            self.Hist["Z2NNCounter"].AddBinContent(6)
                            if event.cleanJetsAK8[0].subjets('SoftDrop')[1].bDiscriminator('pfCombinedInclusiveSecondaryVertexV2BJetTags') > 0.605: 
                                self.Hist["Z2NNCounter"].AddBinContent(7)
        return True

