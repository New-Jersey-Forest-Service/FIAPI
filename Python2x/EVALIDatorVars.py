# EVALIDatorVars.py


class EVALIDatorVars:
    #default constructor
    def __init__(self):
        #tuple of variable names used in this class
        v = ('nmDict', 'dmDict', 'stateDict')
        #dictionary of numerator/denominator variables
        self.nmDict = {'aslw':'Area of sampled land and water, in acres','afl':'Area of forest land, in acres','atl':'Area of timberland, in acres',\
                       'nltfl':'Number of live tress (at least 1 inch d.b.h./d.r.c.), in trees, on forest land','ngsfl':'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                       'nsdfl':'Number of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land','nlsfl':'Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on forest land',\
                       'nlttl':'Number of live trees (at least 1 inch d.b.h./d.r.c.), in trees, on timberland','ngstl':'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                       'nsdtl':'Number of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland','nlstl':'Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on timberland',\
                       'nvltfl':'Net volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land','nvgsfl':'Net volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                       'nvslpfl':'Net volume of saw-log portion of sawtimber trees, in cubic feet, on forest land','nvstfl':'Net volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                       'gvstfl':'Gross volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land','gvltfl':'Gross volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'svltfl':'Sound volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land','nvsdfl':'Net volume of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'nvlttl':'Net volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','nvgstl':'Net volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'nvslptl': 'Net volume of saw-log portion of sawtimber trees, in cubic feet, on timberland','nvsttl':'Net volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                       'nvsdtl':'Net volume of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','agdwfl':'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                       'dwmbfl':'Dry weight of merchantable bole for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land','dwtlfl':'Dry weight of tops and limbs for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land',\
                       'agdwlsfl':'Aboveground dry weight of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in short tons, on forest land','dwsfl':'Dry weight of stumps for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land',\
                       'bgdwfl':'Belowground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land','agdwfl':'Aboveground dry weight of live trees (woodland species at least 1 inch d.r.c.), in short tons, on forest land',\
                       'agdwbfl':'Aboveground dry weight of bark for live trees (at least 1 inch d.b.h./d.r.c.), in short tons, on forest land','agdwsdfl':'Aboveground dry weight of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in short tons, on forest land',\
                       'aggwfl':'Aboveground green weight of live trees (at least 1 inch d.b.h./d.r.c.), in short tons, on forest land','agdwfl':'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land calculated with retired regional methods',\
                       'agmdwfl':'Aboveground merchantable dry weight of live trees (at least 5 inches d.b.h./d.r.c), in short tons, on forest land calculated with retired regional methods','dwmbtl':'Dry weight of merchantable bole for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland',\
                       'agdwtl':'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','dwtltl':'Dry weight of tops and limbs for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland',\
                       'agdwlstl':'Aboveground dry weight of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in short tons, on timberland','dwstl':'Dry weight of stumps for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland',\
                       'bgdwtl':'Belowground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','agdwtl':'Aboveground dry weight of live trees (woodland species at least 1 inch d.r.c.), in short tons, on timberland',\
                       'agdwtlrrm':'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland calculated with retired regional methods','agmdwtlrrm':'Aboveground merchantable dry weight of live trees (at least 5 inches d.b.h./d.r.c), in short tons, on timberland calculated with retired regional methods',\
                       'agcfl':'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land','bgcfl':'Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                       'agbgcsdfl':'Above and belowground carbon in standing-dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land','agclssbfl':'Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land',\
                       'bgclssbfl':'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land','cscrcwdfl':'Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on forest land',\
                       'clfl':'Carbon in litter, in short tons, on forest land','cosfl':'Carbon in organic soil, in short tons, on forest land','tcfl':'Carbon in organic soil, in short tons, on forest land','agbgcfl':'Above and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                       'fcp1lagfl':'Forest carbon pool 1: live aboveground, in metric tonnes, on forest land','fcp2lbgfl':'Forest carbon pool 2: live belowground, in metric tonnes, on forest land','fcp3dwfl':'Forest carbon pool 3: dead wood, in metric tonnes, on forest land',\
                       'fcp4lfl':'Forest carbon pool 4: litter, in metric tonnes, on forest land','fcp5sofl':'Forest carbon pool 5: soil organic, in metric tonnes, on forest land','fctfl':'Forest carbon total: all 5 pools, in metric tonnes, on forest land',\
                       'agctl':'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','bgctl':'Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                       'agbgcsdtl':'Above and belowground carbon in standing-dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','agclssbtl':'Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland',\
                       'bgclssbtl':'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland','cscrcwdtl':'Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on timberland','cltl':'Carbon in litter, in short tons, on timberland',\
                       'costl':'Carbon in organic soil, in short tons, on timberland','agbgctl':'Above and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','aangfl':'Average annual net growth of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'aanggsfl':'Average annual net growth of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land','aagstfl':'Average annual net growth of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                       'aangtl':'Average annual net growth of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','aanggstl':'Average annual net growth of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'aagsttl':'Average annual net growth of sawtimber trees, in board feet (International 1/4-inch rule), on timberland','aamfl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                       'aamcffl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land','aamgsfl':'Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                       'aamstfl':'Average annual mortality of sawtimber trees, in board feet (International 1/4-inch rule), on forest land','aamtl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                       'aamcftl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','aamgstl':'Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'aamsttl':'Average annual mortality of sawtimber trees, in board feet (International 1/4-inch rule), on timberland','aarfl':'Average annual removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'aargsfl':'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land','aarstfl':'Average annual removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                       'aahrfl':'Average annual harvest removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land','aahrgsfl':'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                       'aahrswfl':'Average annual harvest removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land','aaorfl':'Average annual other removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'aaorgsfl':'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land','aaorstfl':'Average annual other removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                       'aartl':'Average annual removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','aargstl':'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'aarsttl':'Average annual removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland','aahrtl':'Average annual harvest removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                       'aahrgstl':'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland','aahrswtl':'Average annual harvest removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                       'aaortl':'Average annual other removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','aaorgstl':'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'aaorsttl':'Average annual other removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland','tvfwdspfl':'Number of CWD pieces, in pieces, on forest land','ncwdpfl':'Total volume of FWD (small) pieces, in cubic feet, on forest land',\
                       'tvfwdmpfl':'Total volume of FWD (medium) pieces, in cubic feet, on forest land','tvfwdlpfl':'Total volume of FWD (large) pieces, in cubic feet, on forest land','tvfwdaspfl':'Total volume of FWD (all sizes) pieces, in cubic feet, on forest land',\
                       'tvcwdfl':'Total volume of CWD, in cubic feet, on forest land','tvdwmpfl':'Total volume of DWM piles, in cubic feet, on forest land','tvdwmall':'Total volume of DWM (FWD, CWD and piles) in cubic feet, on forest land',\
                       'dwfwdspfl':'Dry weight of FWD (small) pieces, in short tons, on forest land','dwfwdmpfl':'Dry weight of FWD (medium) pieces, in short tons, on forest land','dwfwdlpfl':'Dry weight of FWD (large) pieces, in short tons, on forest land',\
                       'dwfwdaspfl':'Dry weight of FWD (all sizes) pieces, in short tons, on forest land','dwcwdfl':'Dry weight of CWD, in short tons, on forest land','dwdwmpfl':'Dry weight of DWM piles, in short tons, on forest land','tdwdwmallfl':'Total dry weight of DWM (FWD, CWD and piles) in short tons, on forest land',\
                       'cfwdspfl':'Carbon in FWD (small) pieces, in short tons, on forest land','cfwdmpfl':'Carbon in FWD (medium) pieces, in short tons, on forest land','cfwdlpfl':'Carbon in FWD (large) pieces, in short tons, on forest land','cfwdaspfl':'Carbon in FWD (all sizes) pieces, in short tons, on forest land',\
                       'ccwdfl':'Carbon in CWD, in short tons, on forest land','cdwmallfl':'Carbon in DWM piles, in short tons, on forest land','tcdwmall':'Total carbon in DWM (FWD, CWD and piles) in short tons, on forest land','ac-sbirp':'Area change - sampled at both inventories by remeasured plots',\
                       'ac-aflbrp':'Area change - area forest land both measurements from remeasured plots','ac-aflemrp':'Area change - area forest land either measurement from remeasured plots','ac-atlbmrp':'Area change - area timberland both measurements from remeasured plots',\
                       'ac-atlemrp':'Area change - area timberland either measurement from remeasured plots'}
        self.dmDict = {'nodenominator':'No denominator - just produce estimate.','aslw':'Area of sampled land and water, in acres',\
                       'aslw':'Area of sampled land and water, in acres','afl':'Area of forest land, in acres','atl':'Area of timberland, in acres',\
                       'nltfl':'Number of live tress (at least 1 inch d.b.h./d.r.c.), in trees, on forest land','ngsfl':'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                       'nsdfl':'Number of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land','nlsfl':'Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on forest land',\
                       'nlttl':'Number of live trees (at least 1 inch d.b.h./d.r.c.), in trees, on timberland','ngstl':'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                       'nsdtl':'Number of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland','nlstl':'Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on timberland',\
                       'nvltfl':'Net volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land','nvgsfl':'Net volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                       'nvslpfl':'Net volume of saw-log portion of sawtimber trees, in cubic feet, on forest land','nvstfl':'Net volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                       'gvstfl':'Gross volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land','gvltfl':'Gross volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'svltfl':'Sound volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land','nvsdfl':'Net volume of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'nvlttl':'Net volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','nvgstl':'Net volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'nvslptl': 'Net volume of saw-log portion of sawtimber trees, in cubic feet, on timberland','nvsttl':'Net volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                       'nvsdtl':'Net volume of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','agdwfl':'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                       'dwmbfl':'Dry weight of merchantable bole for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land','dwtlfl':'Dry weight of tops and limbs for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land',\
                       'agdwlsfl':'Aboveground dry weight of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in short tons, on forest land','dwsfl':'Dry weight of stumps for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land',\
                       'bgdwfl':'Belowground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land','agdwfl':'Aboveground dry weight of live trees (woodland species at least 1 inch d.r.c.), in short tons, on forest land',\
                       'agdwbfl':'Aboveground dry weight of bark for live trees (at least 1 inch d.b.h./d.r.c.), in short tons, on forest land','agdwsdfl':'Aboveground dry weight of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in short tons, on forest land',\
                       'aggwfl':'Aboveground green weight of live trees (at least 1 inch d.b.h./d.r.c.), in short tons, on forest land','agdwfl':'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land calculated with retired regional methods',\
                       'agmdwfl':'Aboveground merchantable dry weight of live trees (at least 5 inches d.b.h./d.r.c), in short tons, on forest land calculated with retired regional methods','dwmbtl':'Dry weight of merchantable bole for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland',\
                       'agdwtl':'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','dwtltl':'Dry weight of tops and limbs for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland',\
                       'agdwlstl':'Aboveground dry weight of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in short tons, on timberland','dwstl':'Dry weight of stumps for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland',\
                       'bgdwtl':'Belowground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','agdwtl':'Aboveground dry weight of live trees (woodland species at least 1 inch d.r.c.), in short tons, on timberland',\
                       'agdwtlrrm':'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland calculated with retired regional methods','agmdwtlrrm':'Aboveground merchantable dry weight of live trees (at least 5 inches d.b.h./d.r.c), in short tons, on timberland calculated with retired regional methods',\
                       'agcfl':'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land','bgcfl':'Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                       'agbgcsdfl':'Above and belowground carbon in standing-dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land','agclssbfl':'Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land',\
                       'bgclssbfl':'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land','cscrcwdfl':'Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on forest land',\
                       'clfl':'Carbon in litter, in short tons, on forest land','cosfl':'Carbon in organic soil, in short tons, on forest land','tcfl':'Carbon in organic soil, in short tons, on forest land','agbgcfl':'Above and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                       'fcp1lagfl':'Forest carbon pool 1: live aboveground, in metric tonnes, on forest land','fcp2lbgfl':'Forest carbon pool 2: live belowground, in metric tonnes, on forest land','fcp3dwfl':'Forest carbon pool 3: dead wood, in metric tonnes, on forest land',\
                       'fcp4lfl':'Forest carbon pool 4: litter, in metric tonnes, on forest land','fcp5sofl':'Forest carbon pool 5: soil organic, in metric tonnes, on forest land','fctfl':'Forest carbon total: all 5 pools, in metric tonnes, on forest land',\
                       'agctl':'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','bgctl':'Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                       'agbgcsdtl':'Above and belowground carbon in standing-dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','agclssbtl':'Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland',\
                       'bgclssbtl':'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland','cscrcwdtl':'Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on timberland','cltl':'Carbon in litter, in short tons, on timberland',\
                       'costl':'Carbon in organic soil, in short tons, on timberland','agbgctl':'Above and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland','aangfl':'Average annual net growth of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'aanggsfl':'Average annual net growth of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land','aagstfl':'Average annual net growth of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                       'aangtl':'Average annual net growth of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','aanggstl':'Average annual net growth of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'aagsttl':'Average annual net growth of sawtimber trees, in board feet (International 1/4-inch rule), on timberland','aamfl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                       'aamcffl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land','aamgsfl':'Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                       'aamstfl':'Average annual mortality of sawtimber trees, in board feet (International 1/4-inch rule), on forest land','aamtl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                       'aamcftl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','aamgstl':'Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'aamsttl':'Average annual mortality of sawtimber trees, in board feet (International 1/4-inch rule), on timberland','aarfl':'Average annual removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'aargsfl':'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land','aarstfl':'Average annual removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                       'aahrfl':'Average annual harvest removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land','aahrgsfl':'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                       'aahrswfl':'Average annual harvest removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land','aaorfl':'Average annual other removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                       'aaorgsfl':'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land','aaorstfl':'Average annual other removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                       'aartl':'Average annual removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','aargstl':'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'aarsttl':'Average annual removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland','aahrtl':'Average annual harvest removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                       'aahrgstl':'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland','aahrswtl':'Average annual harvest removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                       'aaortl':'Average annual other removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland','aaorgstl':'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                       'aaorsttl':'Average annual other removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland','tvfwdspfl':'Number of CWD pieces, in pieces, on forest land','ncwdpfl':'Total volume of FWD (small) pieces, in cubic feet, on forest land',\
                       'tvfwdmpfl':'Total volume of FWD (medium) pieces, in cubic feet, on forest land','tvfwdlpfl':'Total volume of FWD (large) pieces, in cubic feet, on forest land','tvfwdaspfl':'Total volume of FWD (all sizes) pieces, in cubic feet, on forest land',\
                       'tvcwdfl':'Total volume of CWD, in cubic feet, on forest land','tvdwmpfl':'Total volume of DWM piles, in cubic feet, on forest land','tvdwmall':'Total volume of DWM (FWD, CWD and piles) in cubic feet, on forest land',\
                       'dwfwdspfl':'Dry weight of FWD (small) pieces, in short tons, on forest land','dwfwdmpfl':'Dry weight of FWD (medium) pieces, in short tons, on forest land','dwfwdlpfl':'Dry weight of FWD (large) pieces, in short tons, on forest land',\
                       'dwfwdaspfl':'Dry weight of FWD (all sizes) pieces, in short tons, on forest land','dwcwdfl':'Dry weight of CWD, in short tons, on forest land','dwdwmpfl':'Dry weight of DWM piles, in short tons, on forest land','tdwdwmallfl':'Total dry weight of DWM (FWD, CWD and piles) in short tons, on forest land',\
                       'cfwdspfl':'Carbon in FWD (small) pieces, in short tons, on forest land','cfwdmpfl':'Carbon in FWD (medium) pieces, in short tons, on forest land','cfwdlpfl':'Carbon in FWD (large) pieces, in short tons, on forest land','cfwdaspfl':'Carbon in FWD (all sizes) pieces, in short tons, on forest land',\
                       'ccwdfl':'Carbon in CWD, in short tons, on forest land','cdwmallfl':'Carbon in DWM piles, in short tons, on forest land','tcdwmall':'Total carbon in DWM (FWD, CWD and piles) in short tons, on forest land','ac-sbirp':'Area change - sampled at both inventories by remeasured plots',\
                       'ac-aflbrp':'Area change - area forest land both measurements from remeasured plots','ac-aflemrp':'Area change - area forest land either measurement from remeasured plots','ac-atlbmrp':'Area change - area timberland both measurements from remeasured plots',\
                       'ac-atlemrp':'Area change - area timberland either measurement from remeasured plots'}                       
        #dictionary of FIA state codes
        #includes Puerto Rico (PR) and
        #US Virgin Islands (VI)
        self.stateDict = {'AL':'1','AK':'2','AZ':'3','AR':'5','CA':'6',\
                          'CO':'8','CT':'9','DE':'10','FL':'12','GA':'13',\
                          'ID':'16','IL':'17','IN':'18','IA':'19','KS':'20',\
                          'KY':'21','LA':'22','ME':'23','MD':'24','MA':'24',\
                          'MI':'26','MN':'27','MS':'28','MO':'29','MT':'30',\
                          'NE':'31','NV':'32','NH':'33','NJ':'34','NM':'35',\
                          'NY':'36','NC':'37','ND':'38','OH':'39','OK':'40',\
                          'OR':'41','PA':'42','RI':'44','SC':'45','SD':'46',\
                          'TN':'47','TX':'48','UT':'49','VT':'50','VA':'51',\
                          'WA':'53','WV':'54','WI':'55','WY':'56','PR':'72',\
                          'VI':'78'}
