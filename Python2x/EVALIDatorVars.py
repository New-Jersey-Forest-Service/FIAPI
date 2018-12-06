# EVALIDatorVars.py
# V 2.1
# NJ Forest Service, 09/2018
# Python 2.7

class EVALIDatorVars:
  '''

  Class that holds dictionaries for EVALIDator variables

  nmDict holds the numerator variables 
  dmDict holds the denominator variables 
  stateDict holds the state variables (includes Puerto Rico & Virgin Islands)
  rowDict holds the row variables 
  colDict holds the column variables

  '''

  def __init__(self):
      v = ('nmDict', 'dmDict', 'stateDict', 'rowDict', 'colDict')

      self.nmDict = {'areafl':'Area of forest land, in acres', 'areatl':'Area of timberland, in acres',\
                     'acasbirp':'Area change annual - sampled at both inventories by remeasured plots', 'acaaflbrp':'Area change annual - area forest land both measurements from remeasured plots',\
                     'acaaflerp':'Area change annual - area forest land either measurement from remeasured plots', 'aslw':'Area of sampled land and water, in acres',\
                     'acaatlbrp':'Area change annual - area timberland both measurements from remeasured plots', 'acabirp':'Area change - sampled at both inventories by remeasured plots',\
                     'acflerp':'Area change - area forest land either measurements from remeasured plots', 'acaatlerp':'Area change annual - area timberland either measurement from remeasured plots',\
                     'acflbrp':'Area change - area forest land both measurements from remeasured plots',\
                     'actlerp':'Area change - area timberland either measurements from remeasured plots', 'actlbrp':'Area change - area timberland both measurements from remeasured plots',\
                     'acrp':'Area change - sampled at both inventories by remeasured plots','aac':'Annual area change',\
                     'aacrp':'Area change annual - sampled at both inventories by remeasured plots', 'tv':'Tree volume',\
                     'nbvgscffl':'Net merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'nsvstcffl':'Net sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'ssvstcffl':'Sound sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'nsvstbffl':'Net sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'gsvstbffl':'Gross sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'gmbvcffl':'Gross merchantable bole volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'smbvcffl':'Sound merchantable bole volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'nmbvcffl':'Net merchantable bole volume of standing dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'nstbffl':'Net sawlog volume of sawtimber trees, in board feet (Doyle rule), on forest land', 'tdw':'Tree dry weight',\
                     'agbmltdstfl':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on forest land',\
                     'mbboltdstfl':'Merchantable bole biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on forest land',\
                     'tlbmltdstfl':'Top and limb biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on forest land',\
                     'abbmlsdstfl':'Aboveground biomass of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in dry short tons, on forest land',\
                     'sbmltdstfl':'Stump biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on forest land',\
                     'bgbmltdstfl':'Belowground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on forest land',\
                     'agbmltwldstfl':'Aboveground biomass of live trees (woodland species at least 1 inch d.r.c.), in dry short tons, on forest land',\
                     'bbmltdstfl':'Bark biomass of live trees (at least 1 inch d.b.h./d.r.c.), in dry short tons, on forest land',\
                     'agbmsdtdstfl':'Aboveground biomass of standing dead trees (at least 5 inches d.b.h./d.r.c.), in dry short tons, on forest land',\
                     'agbmltdstflrrm':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on forest land calculated with retired regional methods',\
                     'mbbbmltdstflrrm':'Merchantable bole biomass of live trees (at least 5 inches d.b.h./d.r.c), in dry short tons, on forest land calculated with retired regional methods',\
                     'sbmstdstfl':'Sawlog biomass of sawtimber trees, in dry short tons, on forest land', 'tgw':'Tree green weight',\
                     'agbmltgstfl':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in green short tons, on forest land',\
                     'mbbmltgstfl':'Merchantable bole biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on forest land',\
                     'tlbmltgstfl':'Top and limb biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on forest land',\
                     'agbmlsgstfl':'Aboveground biomass of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in green short tons, on forest land',\
                     'sbmlfgstfl':'Stump biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on forest land',\
                     'agbmltwlgstfl':'Aboveground biomass of live trees (woodland species at least 1 inch d.r.c.), in green short tons, on forest land',\
                     'sbmstgstfl':'Sawlog biomass of sawtimber trees, in green short tons, on forest land',\
                     'agbmltgstflrrm':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in green short tons, on forest land calculated with retired regional methods',\
                     'mbbmltgstflrrm':'Merchantable bole biomass of live trees (at least 5 inches d.b.h./d.r.c), in green short tons, on forest land calculated with retired regional methods',\
                     'bbmltgstfl':'Bark biomass of live trees (at least 1 inch d.b.h./d.r.c.), in green short tons, on forest land', 'tc':'Tree carbon',\
                     'agcltstfl':'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                     'bgcltstfl':'Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                     'agbgcltstfl':'Aboveground and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land', 'tn':'Tree number',\
                     'nltfl':'Number of live trees (at least 1 inch d.b.h./d.r.c.), in trees, on forest land',\
                     'ngsfl':'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'nsdfl':'Number of standing dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'nlsfl':'Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on forest land', 'dwmv':'Down woody material volume',\
                     'tvsfwdcffl':'Total volume of FWD (small) pieces, in cubic feet, on forest land',\
                     'tvmfwdcffl':'Total volume of FWD (medium) pieces, in cubic feet, on forest land',\
                     'tvlfwdcffl':'Total volume of FWD (large) pieces, in cubic feet, on forest land',\
                     'tvfwdcffl':'Total volume of FWD (all sizes) pieces, in cubic feet, on forest land',\
                     'tvcwdcffl':'Total volume of CWD, in cubic feet, on forest land',\
                     'tvdwmcffl':'Total volume of DWM piles, in cubic feet, on forest land',\
                     'tvdwmfwdcwdcffl':'Total volume of DWM (FWD, CWD and piles) in cubic feet, on forest land', 'dwmdw':'Down woody material dry weight',\
                     'wsfwddstfl':'Weight of FWD (small) pieces, in dry short tons, on forest land',\
                     'wmfwddstfl':'Weight of FWD (medium) pieces, in dry short tons, on forest land',\
                     'wlfwddstfl':'Weight of FWD (large) pieces, in dry short tons, on forest land',\
                     'wfwddstfl':'Weight of FWD (all sizes) pieces, in dry short tons, on forest land',\
                     'wcwddstfl':'Weight of CWD, in dry short tons, on forest land',\
                     'wdwmdstfl':'Weight of DWM piles, in dry short tons, on forest land',\
                     'twdwmfwdcwddstfl':'Total weight of DWM (FWD, CWD and piles) in dry short tons, on forest land', 'dwmc':'Down woody material carbon',\
                     'csfwddstfl':'Carbon in FWD (small) pieces, in short tons, on forest land',\
                     'cmfwddstfl':'Carbon in FWD (medium) pieces, in short tons, on forest land',\
                     'clfwddstfl':'Carbon in FWD (large) pieces, in short tons, on forest land',\
                     'cfwddstfl':'Carbon in FWD (all sizes) pieces, in short tons, on forest land',\
                     'ccwddstfl':'Carbon in CWD, in short tons, on forest land',\
                     'cdwmdstfl':'Carbon in DWM piles, in short tons, on forest land',\
                     'tcdwmfwdcwddstfl':'Total carbon in DWM (FWD, CWD and piles) in short tons, on forest land', 'dwmn':'Down woody material number',\
                     'ncwdppfl':'Number of CWD pieces, in pieces, on forest land', 'c':'Carbon',\
                     'agbgcsdstfl':'Aboveground and belowground carbon in standing dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                     'agclssbstfl':'Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land',\
                     'bgclssbstfl':'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land',\
                     'cscrcwdstfl':'Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on forest land',\
                     'clstfl':'Carbon in litter, in short tons, on forest land',\
                     'cosstfl':'Carbon in organic soil, in short tons, on forest land',\
                     'tcstfl':'Total carbon, in short tons, on forest land',\
                     'fcpool1fl':'Forest carbon pool 1: live aboveground, in metric tonnes, on forest land',\
                     'fcpool2fl':'Forest carbon pool 2: live belowground, in metric tonnes, on forest land',\
                     'fcpool3fl':'Forest carbon pool 3: dead wood, in metric tonnes, on forest land',\
                     'fcpool4fl':'Forest carbon pool 4: litter, in metric tonnes, on forest land',\
                     'fcpool5fl;':'Forest carbon pool 5: soil organic, in metric tonnes, on forest land',\
                     'allfcpoolsfl':'Forest carbon total: all 5 pools, in metric tonnes, on forest land', 'angv':'Annual net growth volume',\
                     'aangmbvcffl':'Average annual net growth of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aangmbvgscffl':'Average annual net growth of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aangsvstbffl':'Average annual net growth of sawlog volume of sawtimber trees, in board feet (Doyle rule), on forest land',\
                     'aangsvstbffl':'Average annual net growth of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aangsvstcffl':'Average annual net growth of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aangmbvasstcffl':'Average annual net growth of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aangmbvstcffl':'Average annual net growth of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'arv':'Annual removals volume',\
                     'aarmbvcffl':'Average annual removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aarmbvgscffl':'Average annual removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aarsvstbffl':'Average annual removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aarsvstcffl':'Average annual removals of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aarmbvasstcffl':'Average annual removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aarmbvstcffl':'Average annual removals of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'arn':'Annual removals number',\
                     'aarfl':'Average annual removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'aargsfl':'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'aarstfl':'Average annual removals of sawtimber trees, in trees, on forest land', 'ahrv':'Annual harvest removals volume',\
                     'aahrmbvcffl':'Average annual harvest removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aahrmbvgscffl':'Average annual harvest removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aahrsvstbffl':'Average annual harvest removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aahrsvstcffl':'Average annual harvest removals of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aahrmbvasstcgfl':'Average annual harvest removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aahrmbvstcffl':'Average annual harvest removals of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'ancv':'Annual net change volume',\
                     'aancmbvcffl':'Average annual net change of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aancmbvgscffl':'Average annual net change of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aancsvstbffl':'Average annual net change of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aancsvstcffl':'Average annual net change of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aancmbvasstcffl':'Average annual net change of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aancmbvstcffl':'Average annual net change of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'ahrn':'Annual harvest removals number',\
                     'aahrfl':'Average annual harvest removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'aahrgsfl':'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'aahrstfl':'Average annual harvest removals of sawtimber trees, in trees, on forest land', 'aorv':'Annual other removals volume',\
                     'aaormbvcffl':'Average annual other removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aaormbvgscffl':'Average annual other removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aaorsvstbffl':'Average annual other removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aaorsvstcffl':'Average annual other removals of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aaormbvasstcffl':'Average annual other removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aaormbvstcffl':'Average annual other removals of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'aorn':'Annual other removals number',\
                     'aaorfl':'Average annual other removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'aaorgsfl':'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'aaorstfl':'Average annual other removals of sawtimber trees, in trees, on forest land', 'amv':'Annual mortality volume',\
                     'aammbvgscffl':'Average annual mortality of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aamsvstbffl':'Average annual mortality of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aamsvstcffl':'Average annual mortality of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aammbvasstcffl':'Average annual mortality of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aammbvstcffl':'Average annual mortality of merchantable bole volume of sawtimber trees, in cubic feet, on forest land',\
                     'aammbvcffl':'Average annual mortality of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land', 'aamn':'Annual mortality number',\
                     'aamfl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'aamgsfl':'Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'aamstfl':'Average annual mortality of sawtimber trees, in trees, on forest land', 'aggv':'Annual gross growth volume',\
                     'aaggmbvcffl':'Average annual gross growth of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aaggmbvgscffl':'Average annual gross growth of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aaggsvstbffl':'Average annual gross growth of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aaggsvstcffl':'Average annual gross growth of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aaggmbvasstcffl':'Average annual gross growth of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aagsmbvstcffl':'Average annual gross growth of merchantable bole volume of sawtimber trees, in cubic feet, on forest land',\
                     'nbvgscftl':'Net merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'nsvstcftl':'Net sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'ssvstcftl':'Sound sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'nsvstbftl':'Net sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'gsvstbftl':'Gross sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'gmbvcftl':'Gross merchantable bole volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'smbvcftl':'Sound merchantable bole volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'nmbvcftl':'Net merchantable bole volume of standing dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'nstbftl':'Net sawlog volume of sawtimber trees, in board feet (Doyle rule), on timberland',\
                     'agbmltdsttl':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on timberland',\
                     'mbboltdsttl':'Merchantable bole biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on timberland',\
                     'tlbmltdsttl':'Top and limb biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on timberland',\
                     'abbmlsdsttl':'Aboveground biomass of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in dry short tons, on timberland',\
                     'sbmltdsttl':'Stump biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on timberland',\
                     'bgbmltdsttl':'Belowground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on timberland',\
                     'agbmltwldsttl':'Aboveground biomass of live trees (woodland species at least 1 inch d.r.c.), in dry short tons, on timberland',\
                     'bbmltdsttl':'Bark biomass of live trees (at least 1 inch d.b.h./d.r.c.), in dry short tons, on timberland',\
                     'agbmsdtdsttl':'Aboveground biomass of standing dead trees (at least 5 inches d.b.h./d.r.c.), in dry short tons, on timberland',\
                     'agbmltdsttlrrm':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on forest land calculated with retired regional methods',\
                     'mbbbmltdsttlrrm':'Merchantable bole biomass of live trees (at least 5 inches d.b.h./d.r.c), in dry short tons, on forest land calculated with retired regional methods',\
                     'sbmstdsttl':'Sawlog biomass of sawtimber trees, in dry short tons, on timberland', 'agbmltgsttl':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in green short tons, on timberland',\
                     'mbbmltgsttl':'Merchantable bole biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on timberland',\
                     'tlbmltgsttl':'Top and limb biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on timberland',\
                     'agbmlsgsttl':'Aboveground biomass of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in green short tons, on timberland',\
                     'sbmlfgsttl':'Stump biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on timberland',\
                     'agbmltwlgsttl':'Aboveground biomass of live trees (woodland species at least 1 inch d.r.c.), in green short tons, on timberland',\
                     'sbmstgsttl':'Sawlog biomass of sawtimber trees, in green short tons, on timberland',\
                     'agbmltgsttlrrm':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in green short tons, on forest land calculated with retired regional methods',\
                     'mbbmltgsttlrrm':'Merchantable bole biomass of live trees (at least 5 inches d.b.h./d.r.c), in green short tons, on forest land calculated with retired regional methods',\
                     'bbmltgsttl':'Bark biomass of live trees (at least 1 inch d.b.h./d.r.c.), in green short tons, on timberland',\
                     'agcltsttl':'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                     'bgcltsttl':'Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                     'agbgcltsttl':'Aboveground and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                     'nlttl':'Number of live trees (at least 1 inch d.b.h./d.r.c.), in trees, on timberland',\
                     'ngstl':'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'nsdtl':'Number of standing dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'nlstl':'Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on timberland', 'tvsfwdcftl':'Total volume of FWD (small) pieces, in cubic feet, on timberland',\
                     'tvmfwdcftl':'Total volume of FWD (medium) pieces, in cubic feet, on timberland',\
                     'tvlfwdcftl':'Total volume of FWD (large) pieces, in cubic feet, on timberland',\
                     'tvfwdcftl':'Total volume of FWD (all sizes) pieces, in cubic feet, on timberland',\
                     'tvcwdcftl':'Total volume of CWD, in cubic feet, on timberland',\
                     'tvdwmcftl':'Total volume of DWM piles, in cubic feet, on timberland',\
                     'tvdwmfwdcwdcftl':'Total volume of DWM (FWD, CWD and piles) in cubic feet, on timberland', 'wsfwddsttl':'Weight of FWD (small) pieces, in dry short tons, on timberland',\
                     'wmfwddsttl':'Weight of FWD (medium) pieces, in dry short tons, on timberland',\
                     'wlfwddsttl':'Weight of FWD (large) pieces, in dry short tons, on timberland',\
                     'wfwddsttl':'Weight of FWD (all sizes) pieces, in dry short tons, on timberland',\
                     'wcwddsttl':'Weight of CWD, in dry short tons, on timberland',\
                     'wdwmdsttl':'Weight of DWM piles, in dry short tons, on timberland',\
                     'twdwmfwdcwddsttl':'Total weight of DWM (FWD, CWD and piles) in dry short tons, on timberland', 'csfwddsttl':'Carbon in FWD (small) pieces, in short tons, on timberland',\
                     'cmfwddsttl':'Carbon in FWD (medium) pieces, in short tons, on timberland',\
                     'clfwddsttl':'Carbon in FWD (large) pieces, in short tons, on timberland',\
                     'cfwddsttl':'Carbon in FWD (all sizes) pieces, in short tons, on timberland',\
                     'ccwddsttl':'Carbon in CWD, in short tons, on timberland',\
                     'cdwmdsttl':'Carbon in DWM piles, in short tons, on timberland',\
                     'tcdwmfwdcwddsttl':'Total carbon in DWM (FWD, CWD and piles) in short tons, on timberland', 'ncwdpptl':'Number of CWD pieces, in pieces, on timberland',\
                     'agbgcsdsttl':'Aboveground and belowground carbon in standing dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                     'agclssbsttl':'Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland',\
                     'bgclssbsttl':'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland',\
                     'cscrcwdsttl':'Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on timberland',\
                     'clsttl':'Carbon in litter, in short tons, on timberland',\
                     'cossttl':'Carbon in organic soil, in short tons, on timberland',\
                     'tcsttl':'Total carbon, in short tons, on timberland',\
                     'fcpool1tl':'Forest carbon pool 1: live aboveground, in metric tonnes, on timberland',\
                     'fcpool2tl':'Forest carbon pool 2: live belowground, in metric tonnes, on timberland',\
                     'fcpool3tl':'Forest carbon pool 3: dead wood, in metric tonnes, on timberland',\
                     'fcpool4tl':'Forest carbon pool 4: litter, in metric tonnes, on timberland',\
                     'fcpool5tl;':'Forest carbon pool 5: soil organic, in metric tonnes, on timberland',\
                     'allfcpoolstl':'Forest carbon total: all 5 pools, in metric tonnes, on timberland',\
                     'aangmbvcftl':'Average annual net growth of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aangmbvgscftl':'Average annual net growth of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aangsvstbftl':'Average annual net growth of sawlog volume of sawtimber trees, in board feet (Doyle rule), on timberland',\
                     'aangsvstbftl':'Average annual net growth of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aangsvstcftl':'Average annual net growth of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aangmbvasstcftl':'Average annual net growth of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aangmbvstcftl':'Average annual net growth of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aarmbvcftl':'Average annual removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aarmbvgscftl':'Average annual removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aarsvstbftl':'Average annual removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aarsvstcftl':'Average annual removals of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aarmbvasstcftl':'Average annual removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aarmbvstcftl':'Average annual removals of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aartl':'Average annual removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'aargstl':'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'aarsttl':'Average annual removals of sawtimber trees, in trees, on timberland',\
                     'aahrmbvcftl':'Average annual harvest removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aahrmbvgscftl':'Average annual harvest removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aahrsvstbftl':'Average annual harvest removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aahrsvstcftl':'Average annual harvest removals of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aahrmbvasstcgtl':'Average annual harvest removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aahrmbvstcftl':'Average annual harvest removals of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aancmbvcftl':'Average annual net change of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aancmbvgscftl':'Average annual net change of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aancsvstbftl':'Average annual net change of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aancsvstcftl':'Average annual net change of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aancmbvasstcftl':'Average annual net change of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aancmbvstcftl':'Average annual net change of merchantable bole volume of sawtimber trees, in cubic feet, on timberland', \
                     'aahrtl':'Average annual harvest removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'aahrgstl':'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'aahrsttl':'Average annual harvest removals of sawtimber trees, in trees, on timberland',\
                     'aaormbvcftl':'Average annual other removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aaormbvgscftl':'Average annual other removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aaorsvstbftl':'Average annual other removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aaorsvstcftl':'Average annual other removals of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aaormbvasstcftl':'Average annual other removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aaormbvstcftl':'Average annual other removals of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aaortl':'Average annual other removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'aaorgstl':'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'aaorsttl':'Average annual other removals of sawtimber trees, in trees, on timberland',\
                     'aammbvgscftl':'Average annual mortality of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aamsvstbftl':'Average annual mortality of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aamsvstcftl':'Average annual mortality of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aammbvasstcftl':'Average annual mortality of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aammbvstcftl':'Average annual mortality of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aammbvcftl':'Average annual mortality of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aamtl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'aamgstl':'Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'aamsttl':'Average annual mortality of sawtimber trees, in trees, on timberland',\
                     'aaggmbvcftl':'Average annual gross growth of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aaggmbvgscftl':'Average annual gross growth of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aaggsvstbftl':'Average annual gross growth of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aaggsvstcftl':'Average annual gross growth of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aaggmbvasstcftl':'Average annual gross growth of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aagsmbvstcftl':'Average annual gross growth of merchantable bole volume of sawtimber trees, in cubic feet, on timberland'}


      self.dmDict = {'nodenominator':'No denominator - just produce estimates', 'areafl':'Area of forest land, in acres', 'areatl':'Area of timberland, in acres',\
                     'aslw':'Area of sampled land and water, in acres', 'acrp':'Area change - sampled at both inventories by remeasured plots',\
                     'aacrp':'Area change annual - sampled at both inventories by remeasured plots', 'tv':'Tree volume',\
                     'nbvgscffl':'Net merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'nsvstcffl':'Net sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'ssvstcffl':'Sound sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'nsvstbffl':'Net sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'gsvstbffl':'Gross sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'gmbvcffl':'Gross merchantable bole volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'smbvcffl':'Sound merchantable bole volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'nmbvcffl':'Net merchantable bole volume of standing dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'nstbffl':'Net sawlog volume of sawtimber trees, in board feet (Doyle rule), on forest land', 'tdw':'Tree dry weight',\
                     'agbmltdstfl':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on forest land',\
                     'mbboltdstfl':'Merchantable bole biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on forest land',\
                     'tlbmltdstfl':'Top and limb biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on forest land',\
                     'abbmlsdstfl':'Aboveground biomass of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in dry short tons, on forest land',\
                     'sbmltdstfl':'Stump biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on forest land',\
                     'bgbmltdstfl':'Belowground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on forest land',\
                     'agbmltwldstfl':'Aboveground biomass of live trees (woodland species at least 1 inch d.r.c.), in dry short tons, on forest land',\
                     'bbmltdstfl':'Bark biomass of live trees (at least 1 inch d.b.h./d.r.c.), in dry short tons, on forest land',\
                     'agbmsdtdstfl':'Aboveground biomass of standing dead trees (at least 5 inches d.b.h./d.r.c.), in dry short tons, on forest land',\
                     'agbmltdstflrrm':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on forest land calculated with retired regional methods',\
                     'mbbbmltdstflrrm':'Merchantable bole biomass of live trees (at least 5 inches d.b.h./d.r.c), in dry short tons, on forest land calculated with retired regional methods',\
                     'sbmstdstfl':'Sawlog biomass of sawtimber trees, in dry short tons, on forest land', 'tgw':'Tree green weight',\
                     'agbmltgstfl':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in green short tons, on forest land',\
                     'mbbmltgstfl':'Merchantable bole biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on forest land',\
                     'tlbmltgstfl':'Top and limb biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on forest land',\
                     'agbmlsgstfl':'Aboveground biomass of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in green short tons, on forest land',\
                     'sbmlfgstfl':'Stump biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on forest land',\
                     'agbmltwlgstfl':'Aboveground biomass of live trees (woodland species at least 1 inch d.r.c.), in green short tons, on forest land',\
                     'sbmstgstfl':'Sawlog biomass of sawtimber trees, in green short tons, on forest land',\
                     'agbmltgstflrrm':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in green short tons, on forest land calculated with retired regional methods',\
                     'mbbmltgstflrrm':'Merchantable bole biomass of live trees (at least 5 inches d.b.h./d.r.c), in green short tons, on forest land calculated with retired regional methods',\
                     'bbmltgstfl':'Bark biomass of live trees (at least 1 inch d.b.h./d.r.c.), in green short tons, on forest land', 'tc':'Tree carbon',\
                     'agcltstfl':'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                     'bgcltstfl':'Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                     'agbgcltstfl':'Aboveground and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land', 'tn':'Tree number',\
                     'nltfl':'Number of live trees (at least 1 inch d.b.h./d.r.c.), in trees, on forest land',\
                     'ngsfl':'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'nsdfl':'Number of standing dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'nlsfl':'Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on forest land', 'dwmv':'Down woody material volume',\
                     'tvsfwdcffl':'Total volume of FWD (small) pieces, in cubic feet, on forest land',\
                     'tvmfwdcffl':'Total volume of FWD (medium) pieces, in cubic feet, on forest land',\
                     'tvlfwdcffl':'Total volume of FWD (large) pieces, in cubic feet, on forest land',\
                     'tvfwdcffl':'Total volume of FWD (all sizes) pieces, in cubic feet, on forest land',\
                     'tvcwdcffl':'Total volume of CWD, in cubic feet, on forest land',\
                     'tvdwmcffl':'Total volume of DWM piles, in cubic feet, on forest land',\
                     'tvdwmfwdcwdcffl':'Total volume of DWM (FWD, CWD and piles) in cubic feet, on forest land', 'dwmdw':'Down woody material dry weight',\
                     'wsfwddstfl':'Weight of FWD (small) pieces, in dry short tons, on forest land',\
                     'wmfwddstfl':'Weight of FWD (medium) pieces, in dry short tons, on forest land',\
                     'wlfwddstfl':'Weight of FWD (large) pieces, in dry short tons, on forest land',\
                     'wfwddstfl':'Weight of FWD (all sizes) pieces, in dry short tons, on forest land',\
                     'wcwddstfl':'Weight of CWD, in dry short tons, on forest land',\
                     'wdwmdstfl':'Weight of DWM piles, in dry short tons, on forest land',\
                     'twdwmfwdcwddstfl':'Total weight of DWM (FWD, CWD and piles) in dry short tons, on forest land', 'dwmc':'Down woody material carbon',\
                     'csfwddstfl':'Carbon in FWD (small) pieces, in short tons, on forest land',\
                     'cmfwddstfl':'Carbon in FWD (medium) pieces, in short tons, on forest land',\
                     'clfwddstfl':'Carbon in FWD (large) pieces, in short tons, on forest land',\
                     'cfwddstfl':'Carbon in FWD (all sizes) pieces, in short tons, on forest land',\
                     'ccwddstfl':'Carbon in CWD, in short tons, on forest land',\
                     'cdwmdstfl':'Carbon in DWM piles, in short tons, on forest land',\
                     'tcdwmfwdcwddstfl':'Total carbon in DWM (FWD, CWD and piles) in short tons, on forest land', 'dwmn':'Down woody material number',\
                     'ncwdppfl':'Number of CWD pieces, in pieces, on forest land', 'c':'Carbon',\
                     'agbgcsdstfl':'Aboveground and belowground carbon in standing dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land',\
                     'agclssbstfl':'Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land',\
                     'bgclssbstfl':'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land',\
                     'cscrcwdstfl':'Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on forest land',\
                     'clstfl':'Carbon in litter, in short tons, on forest land',\
                     'cosstfl':'Carbon in organic soil, in short tons, on forest land',\
                     'tcstfl':'Total carbon, in short tons, on forest land',\
                     'fcpool1fl':'Forest carbon pool 1: live aboveground, in metric tonnes, on forest land',\
                     'fcpool2fl':'Forest carbon pool 2: live belowground, in metric tonnes, on forest land',\
                     'fcpool3fl':'Forest carbon pool 3: dead wood, in metric tonnes, on forest land',\
                     'fcpool4fl':'Forest carbon pool 4: litter, in metric tonnes, on forest land',\
                     'fcpool5fl;':'Forest carbon pool 5: soil organic, in metric tonnes, on forest land',\
                     'allfcpoolsfl':'Forest carbon total: all 5 pools, in metric tonnes, on forest land', 'angv':'Annual net growth volume',\
                     'aangmbvcffl':'Average annual net growth of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aangmbvgscffl':'Average annual net growth of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aangsvstbffl':'Average annual net growth of sawlog volume of sawtimber trees, in board feet (Doyle rule), on forest land',\
                     'aangsvstbffl':'Average annual net growth of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aangsvstcffl':'Average annual net growth of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aangmbvasstcffl':'Average annual net growth of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aangmbvstcffl':'Average annual net growth of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'arv':'Annual removals volume',\
                     'aarmbvcffl':'Average annual removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aarmbvgscffl':'Average annual removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aarsvstbffl':'Average annual removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aarsvstcffl':'Average annual removals of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aarmbvasstcffl':'Average annual removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aarmbvstcffl':'Average annual removals of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'arn':'Annual removals number',\
                     'aarfl':'Average annual removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'aargsfl':'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'aarstfl':'Average annual removals of sawtimber trees, in trees, on forest land', 'ahrv':'Annual harvest removals volume',\
                     'aahrmbvcffl':'Average annual harvest removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aahrmbvgscffl':'Average annual harvest removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aahrsvstbffl':'Average annual harvest removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aahrsvstcffl':'Average annual harvest removals of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aahrmbvasstcgfl':'Average annual harvest removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aahrmbvstcffl':'Average annual harvest removals of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'ancv':'Annual net change volume',\
                     'aancmbvcffl':'Average annual net change of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aancmbvgscffl':'Average annual net change of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aancsvstbffl':'Average annual net change of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aancsvstcffl':'Average annual net change of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aancmbvasstcffl':'Average annual net change of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aancmbvstcffl':'Average annual net change of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'ahrn':'Annual harvest removals number',\
                     'aahrfl':'Average annual harvest removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'aahrgsfl':'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'aahrstfl':'Average annual harvest removals of sawtimber trees, in trees, on forest land', 'aorv':'Annual other removals volume',\
                     'aaormbvcffl':'Average annual other removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aaormbvgscffl':'Average annual other removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aaorsvstbffl':'Average annual other removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aaorsvstcffl':'Average annual other removals of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aaormbvasstcffl':'Average annual other removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aaormbvstcffl':'Average annual other removals of merchantable bole volume of sawtimber trees, in cubic feet, on forest land', 'aorn':'Annual other removals number',\
                     'aaorfl':'Average annual other removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'aaorgsfl':'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'aaorstfl':'Average annual other removals of sawtimber trees, in trees, on forest land', 'amv':'Annual mortality volume',\
                     'aammbvgscffl':'Average annual mortality of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aamsvstbffl':'Average annual mortality of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aamsvstcffl':'Average annual mortality of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aammbvasstcffl':'Average annual mortality of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aammbvstcffl':'Average annual mortality of merchantable bole volume of sawtimber trees, in cubic feet, on forest land',\
                     'aammbvcffl':'Average annual mortality of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land', 'aamn':'Annual mortality number',\
                     'aamfl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land',\
                     'aamgsfl':'Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land',\
                     'aamstfl':'Average annual mortality of sawtimber trees, in trees, on forest land', 'aggv':'Annual gross growth volume',\
                     'aaggmbvcffl':'Average annual gross growth of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land',\
                     'aaggmbvgscffl':'Average annual gross growth of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land',\
                     'aaggsvstbffl':'Average annual gross growth of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land',\
                     'aaggsvstcffl':'Average annual gross growth of sawlog volume of sawtimber trees, in cubic feet, on forest land',\
                     'aaggmbvasstcffl':'Average annual gross growth of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on forest land',\
                     'aagsmbvstcffl':'Average annual gross growth of merchantable bole volume of sawtimber trees, in cubic feet, on forest land',\
                     'nbvgscftl':'Net merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'nsvstcftl':'Net sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'ssvstcftl':'Sound sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'nsvstbftl':'Net sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'gsvstbftl':'Gross sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'gmbvcftl':'Gross merchantable bole volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'smbvcftl':'Sound merchantable bole volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'nmbvcftl':'Net merchantable bole volume of standing dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'nstbftl':'Net sawlog volume of sawtimber trees, in board feet (Doyle rule), on timberland',\
                     'agbmltdsttl':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on timberland',\
                     'mbboltdsttl':'Merchantable bole biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on timberland',\
                     'tlbmltdsttl':'Top and limb biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on timberland',\
                     'abbmlsdsttl':'Aboveground biomass of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in dry short tons, on timberland',\
                     'sbmltdsttl':'Stump biomass of live trees (timber species at least 5 inches d.b.h.), in dry short tons, on timberland',\
                     'bgbmltdsttl':'Belowground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on timberland',\
                     'agbmltwldsttl':'Aboveground biomass of live trees (woodland species at least 1 inch d.r.c.), in dry short tons, on timberland',\
                     'bbmltdsttl':'Bark biomass of live trees (at least 1 inch d.b.h./d.r.c.), in dry short tons, on timberland',\
                     'agbmsdtdsttl':'Aboveground biomass of standing dead trees (at least 5 inches d.b.h./d.r.c.), in dry short tons, on timberland',\
                     'agbmltdsttlrrm':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in dry short tons, on forest land calculated with retired regional methods',\
                     'mbbbmltdsttlrrm':'Merchantable bole biomass of live trees (at least 5 inches d.b.h./d.r.c), in dry short tons, on forest land calculated with retired regional methods',\
                     'sbmstdsttl':'Sawlog biomass of sawtimber trees, in dry short tons, on timberland', 'agbmltgsttl':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in green short tons, on timberland',\
                     'mbbmltgsttl':'Merchantable bole biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on timberland',\
                     'tlbmltgsttl':'Top and limb biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on timberland',\
                     'agbmlsgsttl':'Aboveground biomass of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in green short tons, on timberland',\
                     'sbmlfgsttl':'Stump biomass of live trees (timber species at least 5 inches d.b.h.), in green short tons, on timberland',\
                     'agbmltwlgsttl':'Aboveground biomass of live trees (woodland species at least 1 inch d.r.c.), in green short tons, on timberland',\
                     'sbmstgsttl':'Sawlog biomass of sawtimber trees, in green short tons, on timberland',\
                     'agbmltgsttlrrm':'Aboveground biomass of live trees (at least 1 inch d.b.h./d.r.c), in green short tons, on forest land calculated with retired regional methods',\
                     'mbbmltgsttlrrm':'Merchantable bole biomass of live trees (at least 5 inches d.b.h./d.r.c), in green short tons, on forest land calculated with retired regional methods',\
                     'bbmltgsttl':'Bark biomass of live trees (at least 1 inch d.b.h./d.r.c.), in green short tons, on timberland',\
                     'agcltsttl':'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                     'bgcltsttl':'Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                     'agbgcltsttl':'Aboveground and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                     'nlttl':'Number of live trees (at least 1 inch d.b.h./d.r.c.), in trees, on timberland',\
                     'ngstl':'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'nsdtl':'Number of standing dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'nlstl':'Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on timberland', 'tvsfwdcftl':'Total volume of FWD (small) pieces, in cubic feet, on timberland',\
                     'tvmfwdcftl':'Total volume of FWD (medium) pieces, in cubic feet, on timberland',\
                     'tvlfwdcftl':'Total volume of FWD (large) pieces, in cubic feet, on timberland',\
                     'tvfwdcftl':'Total volume of FWD (all sizes) pieces, in cubic feet, on timberland',\
                     'tvcwdcftl':'Total volume of CWD, in cubic feet, on timberland',\
                     'tvdwmcftl':'Total volume of DWM piles, in cubic feet, on timberland',\
                     'tvdwmfwdcwdcftl':'Total volume of DWM (FWD, CWD and piles) in cubic feet, on timberland', 'wsfwddsttl':'Weight of FWD (small) pieces, in dry short tons, on timberland',\
                     'wmfwddsttl':'Weight of FWD (medium) pieces, in dry short tons, on timberland',\
                     'wlfwddsttl':'Weight of FWD (large) pieces, in dry short tons, on timberland',\
                     'wfwddsttl':'Weight of FWD (all sizes) pieces, in dry short tons, on timberland',\
                     'wcwddsttl':'Weight of CWD, in dry short tons, on timberland',\
                     'wdwmdsttl':'Weight of DWM piles, in dry short tons, on timberland',\
                     'twdwmfwdcwddsttl':'Total weight of DWM (FWD, CWD and piles) in dry short tons, on timberland', 'csfwddsttl':'Carbon in FWD (small) pieces, in short tons, on timberland',\
                     'cmfwddsttl':'Carbon in FWD (medium) pieces, in short tons, on timberland',\
                     'clfwddsttl':'Carbon in FWD (large) pieces, in short tons, on timberland',\
                     'cfwddsttl':'Carbon in FWD (all sizes) pieces, in short tons, on timberland',\
                     'ccwddsttl':'Carbon in CWD, in short tons, on timberland',\
                     'cdwmdsttl':'Carbon in DWM piles, in short tons, on timberland',\
                     'tcdwmfwdcwddsttl':'Total carbon in DWM (FWD, CWD and piles) in short tons, on timberland', 'ncwdpptl':'Number of CWD pieces, in pieces, on timberland',\
                     'agbgcsdsttl':'Aboveground and belowground carbon in standing dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland',\
                     'agclssbsttl':'Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland',\
                     'bgclssbsttl':'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland',\
                     'cscrcwdsttl':'Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on timberland',\
                     'clsttl':'Carbon in litter, in short tons, on timberland',\
                     'cossttl':'Carbon in organic soil, in short tons, on timberland',\
                     'tcsttl':'Total carbon, in short tons, on timberland',\
                     'fcpool1tl':'Forest carbon pool 1: live aboveground, in metric tonnes, on timberland',\
                     'fcpool2tl':'Forest carbon pool 2: live belowground, in metric tonnes, on timberland',\
                     'fcpool3tl':'Forest carbon pool 3: dead wood, in metric tonnes, on timberland',\
                     'fcpool4tl':'Forest carbon pool 4: litter, in metric tonnes, on timberland',\
                     'fcpool5tl;':'Forest carbon pool 5: soil organic, in metric tonnes, on timberland',\
                     'allfcpoolstl':'Forest carbon total: all 5 pools, in metric tonnes, on timberland',\
                     'aangmbvcftl':'Average annual net growth of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aangmbvgscftl':'Average annual net growth of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aangsvstbftl':'Average annual net growth of sawlog volume of sawtimber trees, in board feet (Doyle rule), on timberland',\
                     'aangsvstbftl':'Average annual net growth of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aangsvstcftl':'Average annual net growth of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aangmbvasstcftl':'Average annual net growth of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aangmbvstcftl':'Average annual net growth of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aarmbvcftl':'Average annual removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aarmbvgscftl':'Average annual removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aarsvstbftl':'Average annual removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aarsvstcftl':'Average annual removals of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aarmbvasstcftl':'Average annual removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aarmbvstcftl':'Average annual removals of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aartl':'Average annual removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'aargstl':'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'aarsttl':'Average annual removals of sawtimber trees, in trees, on timberland',\
                     'aahrmbvcftl':'Average annual harvest removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aahrmbvgscftl':'Average annual harvest removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aahrsvstbftl':'Average annual harvest removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aahrsvstcftl':'Average annual harvest removals of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aahrmbvasstcgtl':'Average annual harvest removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aahrmbvstcftl':'Average annual harvest removals of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aancmbvcftl':'Average annual net change of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aancmbvgscftl':'Average annual net change of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aancsvstbftl':'Average annual net change of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aancsvstcftl':'Average annual net change of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aancmbvasstcftl':'Average annual net change of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aancmbvstcftl':'Average annual net change of merchantable bole volume of sawtimber trees, in cubic feet, on timberland', \
                     'aahrtl':'Average annual harvest removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'aahrgstl':'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'aahrsttl':'Average annual harvest removals of sawtimber trees, in trees, on timberland',\
                     'aaormbvcftl':'Average annual other removals of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aaormbvgscftl':'Average annual other removals of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aaorsvstbftl':'Average annual other removals of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aaorsvstcftl':'Average annual other removals of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aaormbvasstcftl':'Average annual other removals of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aaormbvstcftl':'Average annual other removals of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aaortl':'Average annual other removals of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'aaorgstl':'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'aaorsttl':'Average annual other removals of sawtimber trees, in trees, on timberland',\
                     'aammbvgscftl':'Average annual mortality of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aamsvstbftl':'Average annual mortality of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aamsvstcftl':'Average annual mortality of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aammbvasstcftl':'Average annual mortality of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aammbvstcftl':'Average annual mortality of merchantable bole volume of sawtimber trees, in cubic feet, on timberland',\
                     'aammbvcftl':'Average annual mortality of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aamtl':'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland',\
                     'aamgstl':'Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland',\
                     'aamsttl':'Average annual mortality of sawtimber trees, in trees, on timberland',\
                     'aaggmbvcftl':'Average annual gross growth of merchantable bole volume of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland',\
                     'aaggmbvgscftl':'Average annual gross growth of merchantable bole volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland',\
                     'aaggsvstbftl':'Average annual gross growth of sawlog volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland',\
                     'aaggsvstcftl':'Average annual gross growth of sawlog volume of sawtimber trees, in cubic feet, on timberland',\
                     'aaggmbvasstcftl':'Average annual gross growth of merchantable bole volume above the sawlog of sawtimber trees, in cubic feet, on timberland',\
                     'aagsmbvstcftl':'Average annual gross growth of merchantable bole volume of sawtimber trees, in cubic feet, on timberland'}

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

      self.rowDict = {'ta' : 'Trend analysis - StateInventories for rows...no pages','als' : 'All live stocking', 'ararc' : 'AppalachianRegionARC','ars' : 'Artificial regen species', 'aspect' : 'Aspect', 'baal' : 'Basal area all live', 'cn' : 'Condition number',\
                      'cp' : 'Condition proportion', 'cd' : 'Congressional District', 'ccan' : 'County code and name', 'cg' : 'CountyGroup', 'dtr' : 'Distance to road', 'dist1' : 'Disturbance 1', 'dist2' : 'Disturbance 2', 'dist3' : 'Disturbance 3',\
                      'ema' : 'EMAPHEX', 'es' : 'Ecoregion section', 'esb' : 'Ecoregion subsection', 'elevation' : 'Elevation', 'fsr' : 'Forest Service Region', 'ftm' : 'Forest Type MnDNR', 'ft' : 'Forest Type', 'ftfc' : 'Forest type field call', 'ftg' : 'Forest type group',\
                      'ftga' : 'Forest type group abbr', 'gss' : 'Growing-stock stocking', 'huc8' : 'Hydrological Unit Code 8', 'isn' : 'Inventory subcycle number', 'iy' : 'Inventory year', 'lum' : 'Land Use - Major', 'lc' : 'Land class', 'lu' : 'Land use',\
                      'mr' : 'Major region', 'nfs' : 'NFS Region ALP', 'nf' : 'National Forests', 'nfa' : 'National Forests: ALP', 'oc' : 'Ownership class', 'og' : 'Ownership group', 'ogm' : 'Ownership group - Major', 'ofs' : 'Ownership with all FS classes',\
                      'pc' : 'Physiographic class', 'pnc' : 'Present nonforest code remeasurement plots', 'pd' : 'Primary disturbance', 'rpa' : 'RPA Subregion State', 'rss' : 'Reserved status class', 'si' : 'Site index', 'spc' : 'Site productivity class',\
                      'slope' : 'Slope', 'sffsr' : 'SoForFuturesSubReg', 'sa10' : 'Stand age 10 yr classes', 'sa100' : 'Stand age 20 yr classes (0 to 100+)', 'sa500' : 'Stand age 20 yr classes (0 to 500+)', 'sa5' : 'Stand age 5 yr classes',\
                      'so' : 'Stand origin', 'sos' : 'Stand origin species', 'st1' : 'Stand treatment 1', 'st2' : 'Stand treatment 2', 'ssc' : 'Stand-size class', 'ss' : 'Stand-size(field call)', 'sc' : 'State code', 'uc' : 'Unit code'}

      self.colDict = {'als' : 'All live stocking', 'ararc' : 'AppalachianRegionARC', 'aspect' : 'Aspect', 'baal' : 'Basal area all live', 'cn' : 'Condition number',\
                      'cp' : 'Condition proportion', 'dtr' : 'Distance to road', 'dist1' : 'Disturbance 1', 'dist2' : 'Disturbance 2', 'dist3' : 'Disturbance 3',\
                      'elevation' : 'Elevation', 'fsr' : 'Forest Service Region', 'ftm' : 'Forest Type MnDNR',\
                      'ftga' : 'Forest type group abbr', 'gss' : 'Growing-stock stocking', 'isn' : 'Inventory subcycle number', 'iy' : 'Inventory year', 'lum' : 'Land Use - Major', 'lc' : 'Land class', 'lu' : 'Land use',\
                      'mr' : 'Major region', 'nfs' : 'NFS Region ALP', 'nf' : 'National Forests', 'oc' : 'Ownership class', 'og' : 'Ownership group', 'ogm' : 'Ownership group - Major', 'ofs' : 'Ownership with all FS classes',\
                      'pc' : 'Physiographic class', 'pnc' : 'Present nonforest code remeasurement plots', 'pd' : 'Primary disturbance', 'rpa' : 'RPA Subregion State', 'rss' : 'Reserved status class', 'si' : 'Site index', 'spc' : 'Site productivity class',\
                      'slope' : 'Slope', 'sa10' : 'Stand age 10 yr classes', 'sa100' : 'Stand age 20 yr classes (0 to 100+)', 'sa500' : 'Stand age 20 yr classes (0 to 500+)', 'sa5' : 'Stand age 5 yr classes',\
                      'so' : 'Stand origin', 'st1' : 'Stand treatment 1', 'st2' : 'Stand treatment 2', 'ssc' : 'Stand-size class', 'ss' : 'Stand-size(field call)'}
