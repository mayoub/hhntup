#!/usr/bin/env python

import math

VARIABLES = {
    'averageIntPerXing': {
        'title': r'$\langle\mu\rangle|_{LB,BCID}$',
        'filename': 'averageIntPerXing',
        'bins': 20,
        'range': (1, 21),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'actualIntPerXing': {
        'title': r'$\langle\mu\rangle|_{LB}(BCID)$',
        'filename': 'actualIntPerXing',
        'bins': 20,
        'range': (1, 21),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'sum_pt': {
        'title': r'$\sum p_T$',
        'filename': 'sum_pt',
        'bins': 20,
        'range': (50000, 450000),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'sum_pt_full': {
        'title': r'$\sum p_T$ (all)',
        'filename': 'sum_pt_full',
        'bins': 20,
        'range': (50000, 450000),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'higgs_pt': {
        'title': r'Higgs $p_T$',
        'filename': 'higgs_pt',
        'bins': 20,
        'range': (0, 200),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'numJets': {
        'title': r'Number of Jets with $p_T>25$ GeV',
        'filename': 'numjets',
        'bins': 7,
        'range': (-.5, 6.5),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'MET': {
        'title': r'$E^{miss}_{T}$',
        'filename': 'MET',
        'bins': 20,
        'range': (0, 100),
        'scale': 1./1000,
        'units': 'GeV',
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'sphericity': {
        'title': r'sphericity',
        'filename': 'sphericity',
        'bins': 20,
        'range': (0, 1),
        'cats': ['VBF', 'BOOSTED']
    },
    'sphericity_full': {
        'title': r'sphericity (all)',
        'filename': 'sphericity_full',
        'bins': 20,
        'range': (0, 1),
        'cats': ['VBF', 'BOOSTED']
    },
    'aplanarity': {
        'title': r'aplanarity',
        'filename': 'aplanarity',
        'bins': 20,
        'range': (0, .15),
        'cats': ['VBF', 'BOOSTED']
    },
    'aplanarity_full': {
        'title': r'aplanarity (all)',
        'filename': 'aplanarity_full',
        'bins': 20,
        'range': (0, .15),
        'cats': ['VBF', 'BOOSTED']
    },
    'MET_centrality': {
        'title': r'$E^{miss}_{T}$ Centrality',
        'filename': 'met_centrality',
        'bins': 20,
        'range': (-math.sqrt(2), math.sqrt(2)),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'mass2_vis_tau1_tau2': {
        'title': r'$M^{vis}_{\tau_{1},\/\tau_{2}}$',
        'filename': 'mass_vis',
        'bins': 20,
        'range': (0, 250),
        'scale': 0.001,
        'units': 'GeV',
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'mass_mmc_tau1_tau2': {
        'title': r'$M^{MMC}_{\tau_{1},\/\tau_{2}}$',
        'filename': 'mass_MMC',
        'bins': 20,
        'range': (0, 250),
        'units': 'GeV',
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'mass_collinear_tau1_tau2': {
        'title': r'$M^{col}_{\tau_{1},\/\tau_{2}}$',
        'filename': 'mass_collinear',
        'bins': 20,
        'range': (0, 250),
        'units': 'GeV',
        'scale': 0.001,
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau1_fourvect.Pt()/1000': {
        'title': r'$p_{T_{\tau_{1}}}$ [GeV]',
        'filename': 'tau1_pt',
        'bins': 20,
        'range': (20, 100),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau2_fourvect.Pt()/1000': {
        'title': r'$p_{T_{\tau_{2}}}$ [GeV]',
        'filename': 'tau2_pt',
        'bins': 20,
        'range': (20, 100),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau1_numTrack': {
        'title': r'$\tau_{1}$ Number of Tracks',
        'filename': 'tau1_numTrack',
        'bins': 6,
        'range': (-.5, 4.5),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau2_numTrack': {
        'title': r'$\tau_{2}$ Number of Tracks',
        'filename': 'tau2_numTrack',
        'bins': 6,
        'range': (-.5, 4.5),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau1_x': {
        'title': r'$\tau_{1_{x}}$',
        'filename': 'tau1_x',
        'bins': 20,
        'range': (-5, 5),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau2_x': {
        'title': r'$\tau_{2_{x}}$',
        'filename': 'tau2_x',
        'bins': 20,
        'range': (-5, 5),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau1_BDTJetScore': {
        'title': r'$\tau_{1}$ BDT Score',
        'filename': 'tau1_BDTJetScore',
        'bins': 20,
        'range': (.5, 1),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau2_BDTJetScore': {
        'title': r'$\tau_{2}$ BDT Score',
        'filename': 'tau2_BDTJetScore',
        'bins': 20,
        'range': (.5, 1),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'cos_theta_tau1_tau2': {
        'title': r'$\cos(\alpha_{\tau_{1},\/\tau_{2}})$',
        'filename': 'cos_theta_tau1_tau2',
        'bins': 20,
        'range': (-1, 1),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'theta_tau1_tau2': {
        'title': r'$\alpha_{\tau_{1},\/\tau_{2}}$',
        'filename': 'theta_tau1_tau2',
        'bins': 20,
        'range': (0, math.pi),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'dR_tau1_tau2': {
        'title': r'$\Delta R_{\tau_{1},\/\tau_{2}}$',
        'filename': 'dr_tau1_tau2',
        'bins': 20,
        'range': (0.7, 3.5),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'dPhi_tau1_tau2': {
        'title': r'$\Delta \phi_{\tau_{1},\/\tau_{2}}$',
        'filename': 'dphi_tau1_tau2',
        'bins': 20,
        'range': (0., math.pi),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    ('tau1_fourvect.Eta()', 'tau2_fourvect.Eta()'): {
        'title': r'$\eta_{\tau_{1,\/2}}$',
        'filename': 'tau_eta',
        'bins': 20,
        'range': (-3, 3),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau1_charge': {
        'title': r'$\tau_1$ Charge',
        'filename': 'tau1_charge',
        'bins': 5,
        'range': (-2.5, 2.5),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau2_charge': {
        'title': r'$\tau_2$ Charge',
        'filename': 'tau2_charge',
        'bins': 5,
        'range': (-2.5, 2.5),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau1_centrality': {
        'title': r'$\tau_1$ Centrality',
        'filename': 'tau1_centrality',
        'bins': 20,
        'range': (0, 1),
        'cats': ['VBF']
    },
    'tau2_centrality': {
        'title': r'$\tau_2$ Centrality',
        'filename': 'tau2_centrality',
        'bins': 20,
        'range': (0, 1),
        'cats': ['VBF']
    },
    'tau1_fourvect.Eta()': {
        'title': r'$\eta_{\tau_{1}}$',
        'filename': 'tau1_eta',
        'bins': 20,
        'range': (-3, 3),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'tau2_fourvect.Eta()': {
        'title': r'$\eta_{\tau_{2}}$',
        'filename': 'tau2_eta',
        'bins': 20,
        'range': (-3, 3),
        'cats': ['VBF', 'GGF', 'BOOSTED']
    },
    'jet1_fourvect.Eta()': {
        'title': r'$\eta_{jet_{1}}$',
        'filename': 'jet1_eta',
        'bins': 20,
        'range': (-5, 5),
        'cats': ['VBF', 'BOOSTED']
    },
    'jet2_fourvect.Eta()': {
        'title': r'$\eta_{jet_{2}}$',
        'filename': 'jet2_eta',
        'bins': 20,
        'range': (-5, 5),
        'cats': ['VBF','BOOSTED']
    },
    'jet1_fourvect.Pt()/1000': {
        'title': r'$p_{T_{jet_{1}}}$ [GeV]',
        'filename': 'jet1_pt',
        'bins': 20,
        'range': (20, 160),
        'cats': ['VBF','BOOSTED']
    },
    'jet2_fourvect.Pt()/1000': {
        'title': r'$p_{T_{jet_{2}}}$ [GeV]',
        'filename': 'jet2_pt',
        'bins': 20,
        'range': (20, 160),
        'cats': ['VBF','BOOSTED']
    }
    'jet1_fourvect_boosted.Eta()': {
        'title': r'boosted $\eta_{jet_{1}}$',
        'filename': 'jet1_eta_boosted',
        'bins': 20,
        'range': (-5, 5),
        'cats': ['VBF']
    },
    'jet2_fourvect_boosted.Eta()': {
        'title': r'boosted $\eta_{jet_{2}}$',
        'filename': 'jet2_eta_boosted',
        'bins': 20,
        'range': (-5, 5),
        'cats': ['VBF']
    },
    ('jet1_fourvect.Eta()', 'jet2_fourvect.Eta()'): {
        'title': r'$\eta_{jet_{1,\/2}}$',
        'filename': 'jet_eta',
        'bins': 20,
        'range': (-5, 5),
        'cats': ['VBF']
    },
    ('jet1_fourvect_boosted.Eta()', 'jet2_fourvect_boosted.Eta()'): {
        'title': r'boosted $\eta_{jet_{1,\/2}}$',
        'filename': 'jet_eta_boosted',
        'bins': 20,
        'range': (-5, 5),
        'cats': ['VBF']
    },
    'dEta_jets': {
        'title': r'$|\Delta\eta_{jet_{1},\/jet_{2}}|$',
        'filename': 'dEta_jets',
        'bins': 20,
        'range': (0, 6),
        'cats': ['VBF']
    },
    'dEta_jets_boosted': {
        'title': r'boosted $|\Delta\eta_{jet_{1},\/jet_{2}}|$',
        'filename': 'dEta_jets_boosted',
        'bins': 20,
        'range': (0, 6),
        'cats': ['VBF']
    },
    'eta_product_jets': {
        'title': r'$\eta_{jet_{1}} \times \/ \eta_{jet_{2}}$',
        'filename': 'eta_product_jets',
        'bins': 20,
        'range': (-10, 10),
        'cats': ['VBF']
    },
    'mass_jet1_jet2': {
        'title': r'$M_{jet_{1},\/jet_{2}}$',
        'filename': 'M_jet1_jet2',
        'bins': 21,
        'range': (0, 600),
        'scale': 1./1000,
        'units': 'GeV',
        'cats': ['VBF']
    },
}


if __name__ == '__main__':

    from utils import *
    from matplotlib import cm
    from categories import CATEGORIES
    from samples import *
    from matplotlib.backends.backend_pdf import PdfPages
    from background_estimation import qcd_ztautau_norm
    from config import plots_dir
    import os

    PLOTS_DIR = plots_dir(__file__)

    # QCD shape region SS or !OS
    shape_region = 'SS'
    control_region = 'SS'
    target_region = 'OS'

    mc_ztautau   = MC_Ztautau()
    mc_others = MC_Others()

    vbf_125 = MC_VBF(mass=125)
    ggf_125 = MC_ggF(mass=125)
    wh_125  =  MC_WH(mass=125)
    zh_125  =  MC_ZH(mass=125)

    data = Data()

    qcd = QCD(data=data, mc=[mc_others, mc_ztautau],
              sample_region=control_region)

    signals = [
        vbf_125,
        ggf_125,
        wh_125,
        zh_125
    ]

    figures = {}

    for category, cat_info in sorted(CATEGORIES.items(), key=lambda item: item[0]):
        if category == 'preselection':
            continue
        figures[category] = {}

        #cuts = Cut('80 < mass_mmc_tau1_tau2 < 110')
        cuts = Cut()

        qcd.scale = 1.
        mc_ztautau.scale = 1.

        # determine normalization of QCD and Ztautau
        # in each category separately
        qcd_scale, ztautau_scale = qcd_ztautau_norm(
            qcd=qcd,
            ztautau=mc_ztautau,
            backgrounds=[mc_others],
            data=data,
            category=category,
            target_region=target_region,
            control_region=control_region)

        print qcd_scale, ztautau_scale

        qcd.scale = qcd_scale
        mc_ztautau.scale = ztautau_scale

        if shape_region != control_region:
            tmp1 = Hist(10, -2, 2)
            tmp2 = tmp1.Clone()

            qcd.draw_into(
                    tmp1,
                    'tau1_BDTJetScore > -100',
                    category, target_region,
                    sample_region=control_region,
                    cuts=cuts)

            qcd.draw_into(
                    tmp2,
                    'tau1_BDTJetScore > -100',
                    category, target_region,
                    sample_region=shape_region,
                    cuts=cuts)

            qcd_scale *= tmp1.Integral() / tmp2.Integral()
            qcd.scale = qcd_scale

        print qcd_scale, ztautau_scale

        for expr, var_info in VARIABLES.items():
            if category.upper() not in var_info['cats']:
                continue
            print expr
            bins = var_info['bins']
            min, max = var_info['range']

            if 'scale' in var_info:
                expr = "%s * %f" % (expr, var_info['scale'])

            other_hist = mc_others.draw(expr,
                                  category, target_region,
                                  bins, min, max,
                                  cuts=cuts)

            qcd_hist = qcd.draw(expr,
                                category, target_region,
                                bins, min, max,
                                sample_region=shape_region,
                                cuts=cuts)

            ztautau_hist = mc_ztautau.draw(expr,
                                           category, target_region,
                                           bins, min, max,
                                           cuts=cuts)
            bkg_hists = [qcd_hist, other_hist, ztautau_hist]

            data_hist = data.draw(expr,
                                  category, target_region,
                                  bins, min, max,
                                  cuts=cuts)

            print "Data events: %d" % sum(data_hist)
            print "Model events: %f" % sum(sum(bkg_hists))
            for hist in bkg_hists:
                print hist.GetTitle(), sum(hist)
            print "Data / Model: %f" % (sum(data_hist) / sum(sum(bkg_hists)))

            fig = draw(data=data_hist, model=bkg_hists,
                       name=var_info['title'],
                       output_name=var_info['filename'],
                       category_name=cat_info['name'],
                       category=category,
                       units=var_info.get('units', None),
                       range=var_info['range'],
                       show_ratio=True,
                       show_qq=False,
                       model_colour_map=None,
                       dir=PLOTS_DIR)
            figures[category][expr] = fig

    import datetime
    now = datetime.datetime.today()
    # put all plots in a multipage pdf
    for category, exprs in figures.items():
        pdf = PdfPages(os.path.join(PLOTS_DIR, 'features_%s.pdf' % category))
        for expr, fig in sorted(exprs.items(), key=lambda x: x[0]):
            pdf.savefig(fig)
        d = pdf.infodict()
        d['Title'] = 'Features'
        d['Author'] = 'Noel Dawe'
        d['Subject'] = 'Higgs tautau hh features'
        d['Keywords'] = 'higgs tau'
        d['CreationDate'] = now
        d['ModDate'] = now
        pdf.close()