from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaR2, deltaPhi
import copy
import math
import ROOT
import sys

class SyncAnalyzer( Analyzer ):
    '''Sync plot'''
    
    def beginLoop(self,setup):
        super(SyncAnalyzer,self).beginLoop(setup)
        if "outputfile" in setup.services:
            setup.services["outputfile"].file.cd()
            setup.services["outputfile"].file.mkdir("Sync")
            setup.services["outputfile"].file.cd("Sync")
            
            SRLabels = ["All events", "Jet pT > 110", "dPhi(j1,j2)<2.5", "MET > 200", "Jets < 3", "Lepton veto", "Tau veto", "Photon veto"]
            ZCRLabels = ["Trigger", "#Jets > 1", "Jet cuts", "Lep #geq 2", "Lep1 cuts", "Lep2 cuts", "Z cand", "MEt cut"]
            WCRLabels = ["Trigger", "#Jets > 1", "Jet cuts", "Lep #geq 2", "Lep1 cuts", "Lep2 cuts", "Z cand", "MEt cut"]
            
            self.SR = ROOT.TH1F("SR", "Signal Region", 8, 0, 8)
            self.ZCR = ROOT.TH1F("ZCR", "Z Control Region", 8, 0, 8)
            self.WCR = ROOT.TH1F("WCR", "W Control Region", 8, 0, 8)
            
            for i, l in enumerate(SRLabels): self.SRCounter.GetXaxis().SetBinLabel(i+1, l)
            for i, l in enumerate(ZCRLabels): self.ZCRCounter.GetXaxis().SetBinLabel(i+1, l)
            for i, l in enumerate(WCRLabels): self.WCRCounter.GetXaxis().SetBinLabel(i+1, l)
            
    def syncSR(self, event):
    
        self.Sync.Fill(0)
        if len(event.cleanJets) >= 1 and event.cleanJets[0].pt()>110. and event.cleanJets[0].chargedHadronEnergyFraction()>0.2 and event.cleanJets[0].neutralHadronEnergyFraction()<0.7 and event.cleanJets[0].neutralEmEnergyFraction()<0.7:
            self.Sync.Fill(1)                               
            if len(event.cleanJets) < 2 or ( abs(deltaPhi(event.cleanJets[0].phi(), event.cleanJets[1].phi())) < 2.5 and event.cleanJets[1].neutralHadronEnergyFraction()<0.7 and event.cleanJets[1].neutralEmEnergyFraction()<0.9 ):
                self.Sync.Fill(2)
                if event.met.pt()>200.:
                    self.Sync.Fill(3)
                    if len(event.cleanJets)<3:
                        self.Sync.Fill(4)
                        if len(event.inclusiveLeptons) == 0:
                            self.Sync.Fill(5)
                            if len(event.selectedTaus) == 0:
                                self.Sync.Fill(6)
                                if len(event.selectedPhotons) == 0:
                                    self.Sync.Fill(7)
                                    
                                    #print "%d:%d:%d" % ( event.input.eventAuxiliary().id().run(), event.input.eventAuxiliary().id().luminosityBlock(), event.input.eventAuxiliary().id().event() )
    
    
    def syncZCR(self, event):
    
    
    
    def process(self, event):
        if event.isSR:
            self.syncSR(event)
        elif event.isZCR:
            self.syncZCR(event)
        else event.isWCR:
            self.syncWCR(event)
        
        
        
        
        
        
                                
        
        return True
    
