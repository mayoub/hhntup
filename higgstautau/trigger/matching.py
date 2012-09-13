from rootpy.tree.filtering import EventFilter
from atlastools import utils
from atlastools.units import GeV
from atlastools import datasets
from math import *

from . import utils as triggerutils


class TauTriggerMatchIndex(EventFilter):
    """
    Match reco taus to trigger taus. If there are more than two EF taus, take
    the leading two.
    """
    def __init__(self,
                 config,
                 datatype,
                 year,
                 dR=0.2,
                 passthrough=False,
                 **kwargs):

        super(TauTriggerMatchIndex, self).__init__(
                passthrough=passthrough,
                **kwargs)

        if not passthrough:
            self.config = config
            self.dR = dR
            year %= 1000
            self.year = year
            """
            WARNING: possible bias if matching between MC and data differs
            """
            if datatype == datasets.DATA:
                if year == 11:
                    self.passes = self.passes_data11
                elif year == 12:
                    self.passes = self.passes_data12
                else:
                    raise ValueError(
                            "No data trigger matching defined for year %d" %
                            year)
            elif datatype == datasets.MC:
                if year == 11:
                    self.passes = self.passes_mc11
                elif year == 12:
                    self.passes = self.passes_mc12
                else:
                    raise ValueError(
                            "No MC trigger matching defined for year %d" %
                            year)
            else:
                raise ValueError(
                        "No trigger matching defined for datatype %d" %
                        datatype)

    def passes_mc11(self, event):
        """
        Matching performed during trigger emulation with CoEPPTrigTool
        """
        event.taus.select(lambda tau: tau.trigger_match_index > -1)
        return len(event.taus) >= 2

    def passes_data11(self, event):

        if 177986 <= event.RunNumber <= 187815: # Periods B-K
            trigger = 'EF_tau29_medium1_tau20_medium1'
        elif 188902 <= event.RunNumber <= 191933: # Periods L-M
            trigger = 'EF_tau29T_medium1_tau20T_medium1'
        else:
            raise ValueError("No trigger defined for run %i" % event.RunNumber)
        self.match_index(event, trigger)
        event.taus.select(lambda tau: tau.trigger_match_index > -1)
        return len(event.taus) >= 2

    def passes_mc12(self, event):

        self.match_index(event, 'EF_tau29Ti_medium1_tau20Ti_medium1')
        event.taus.select(lambda tau: tau.trigger_match_index > -1)
        return len(event.taus) >= 2

    def passes_data12(self, event):

        self.match_index(event, 'EF_tau29Ti_medium1_tau20Ti_medium1')
        event.taus.select(lambda tau: tau.trigger_match_index > -1)
        return len(event.taus) >= 2

    def match_index(self, event, trigger):
        """
        Use the info stored in the D3PD for 2012:
        trig_EF_tau_EF_tau29Ti_medium1_tau20Ti_medium1
        """
        matched_taus = []
        matches = {}
        # get indices of trigger taus associated with this trigger
        trigger_idx = triggerutils.get_tau_trigger_obj_idx(
            self.config,
            event,
            trigger)
        # trigger_idx can contain 3 indices
        # will need to take the leading two

        taus = list(event.taus)

        # for each EF tau find closest matching reco tau
        for EF_idx in trigger_idx:
            trigger_tau = event.taus_EF.getitem(EF_idx)
            closest_dR = 99999
            closest_tau = None
            for tau in taus:
                dR = utils.dR(
                        trigger_tau.eta, trigger_tau.phi,
                        tau.eta, tau.phi)
                if dR < self.dR and dR < closest_dR:
                    closest_dR = dR
                    closest_tau = tau
            if closest_tau is not None:
                tau.trigger_match_index = EF_idx
                # remove match from future matches (greedy match)
                taus.remove(closest_tau)


class TauTriggerMatchThreshold(EventFilter):
    """
    Match previously matched reco taus to thresholds of the trigger
    """
    def __init__(self,
                 passthrough=False,
                 **kwargs):

        super(TauTriggerMatchThreshold, self).__init__(
                passthrough=passthrough,
                **kwargs)

    def passes(self, event):

        match_threshold(event, (29, 20))
        return True

    def match_threshold(self, event, thresholds):
        """
        thresholds must be in descending order
        """
        assert len(event.taus) == 2

        # assume only matched taus remain in event.taus
        taus = [(tau, event.taus_EF.getitem(tau.trigger_match_index)) for
                tau in event.taus]

        # sort by pT of EF tau
        taus = sorted(taus, key=lambda tau: tau[1].pt, reverse=True)

        # sanity check
        for tau in taus:
            print tau[0].trigger_match_index, tau[1].pt, tau[0].pt
        print "===="
        assert len(thresholds) == len(taus)

        # assign thresholds in descending order
        for i in xrange(len(taus)):
            taus[i][0].trigger_match_thresh = thresholds[i]
            # sanity check
            assert taus[i][1].pt > thresholds[i] * GeV