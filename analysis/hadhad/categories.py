from rootpy.tree import Cut
from higgstautau.hadhad import categories

ID_MEDIUM = Cut('tau1_JetBDTSigMedium==1 && tau2_JetBDTSigMedium==1')
# low cut fixes mass, high cut removes QCD
DR_FIX = Cut('1.0 < dR_tau1_tau2 < 3.2')
MASS_FIX = Cut('mass_mmc_tau1_tau2 > 70')
MAX_NJET = Cut('numJets <= 3')
COMMON_CUTS = Cut('MET > 20000') & ID_MEDIUM & DR_FIX & MASS_FIX & MAX_NJET

CATEGORIES = {
    'vbf': {
        'name': r'$\tau_{had}\tau_{had}$: VBF Category',
        'code': categories.CATEGORY_VBF,
        'cuts': COMMON_CUTS, #& Cut('mass_jet1_jet2 > 100000'),
        'fitbins': 5,
        'shape_region': '!OS',
        'control_region': 'SS',
        'target_region': 'OS',
        'features': [
            'dEta_jets',
            #'dEta_jets_boosted',
            'eta_product_jets',
            #'eta_product_jets_boosted',
            'mass_jet1_jet2',
            'sphericity',
            #'aplanarity',
            'tau1_centrality',
            'tau2_centrality',
            #'sphericity_boosted',
            #'aplanarity_boosted',
            #'tau1_centrality_boosted',
            #'tau2_centrality_boosted',
            #'cos_theta_tau1_tau2',
            'dR_tau1_tau2',
            #'tau1_BDTJetScore',
            #'tau2_BDTJetScore',
            'tau1_x',
            'tau2_x',
            'MET_centrality',
            #'higgs_pt',
            #'sum_pt'
        ]
    },
    'boosted': {
        'name': r'$\tau_{had}\tau_{had}$: Boosted Category',
        'code': categories.CATEGORY_BOOSTED,
        'cuts': COMMON_CUTS,
        'fitbins': 8,
        'shape_region': 'SS',
        'control_region': 'SS',
        'target_region': 'OS',
        'features': [
            'sphericity',
            #'aplanarity',
            #'cos_theta_tau1_tau2',
            'dR_tau1_tau2',
            'tau1_BDTJetScore',
            'tau2_BDTJetScore',
            'tau1_x',
            'tau2_x',
            'MET_centrality',
            #'sum_pt',
            #'higgs_pt'
        ]
    },
    'ggf': {
            'name': r'$\tau_{had}\tau_{had}$: Non-Boosted Category',
        'code': categories.CATEGORY_GGF,
        'cuts': COMMON_CUTS,
        'fitbins': 10,
        'shape_region': 'SS',
        'control_region': 'SS',
        'target_region': 'OS',
        'features': [
            #'cos_theta_tau1_tau2',
            'dR_tau1_tau2',
            'tau1_BDTJetScore',
            'tau2_BDTJetScore',
            'tau1_x',
            'tau2_x',
            'MET_centrality'
        ]
    },
    'preselection': {
        'name': r'$\tau_{had}\tau_{had}$: At Preselection',
        'code': None,
        'cuts': COMMON_CUTS,
        'fitbins': 10,
        'shape_region': 'SS',
        'control_region': 'SS',
        'target_region': 'OS',
    }
}
