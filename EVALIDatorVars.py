#EVALIDatorVars.py


class EVALIDatorVars:
    #default constructor
    def __init__(self):
        #tuple of variable names used in this class
        v = ('nmDict', 'dmDict', 'stateDict')
        #dictionary of numerator/denominator variables
        self.nmDict = {'Area of sampled land and water, in acres':'aslw','Area of forest land, in acres':'afl','Area of timberland, in acres':'atl',\
                       'Number of live tress (at least 1 inch d.b.h./d.r.c.), in trees, on forest land':'nltfl','Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land''ngsfl',\
                       'Number of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land':'nsdfl','Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on forest land':'nlsfl',\
                       'Number of live trees (at least 1 inch d.b.h./d.r.c.), in trees, on timberland':'nlttl','Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on timberland':'ngstl',\
                       'Number of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland':'nsdtl','Number of live seedlings (less than 1 inch d.b.h./d.r.c.), in seedlings, on timberland':'nlstl',\
                       'Net volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'nvltfl','Net volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land':'nvgsfl',\
                       'Net volume of saw-log portion of sawtimber trees, in cubic feet, on forest land':'nvslpfl','Net volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land':'nvstfl',\
                       'Gross volume of sawtimber trees, in board feet (International 1/4-inch rule), on forest land':'gvstfl','Gross volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'gvltfl',\
                       'Sound volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'svltfl','Net volume of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'nvsdfl',\
                       'Net volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland':'nvlttl','Net volume of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland':'nvgstl',\
                       'Net volume of saw-log portion of sawtimber trees, in cubic feet, on timberland':'nvslptl','Net volume of sawtimber trees, in board feet (International 1/4-inch rule), on timberland':'nvsttl',\
                       'Net volume of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland':'nvsdtl','Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land':'agdwfl',\
                       'Dry weight of merchantable bole for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land':'dwmbfl','Dry weight of tops and limbs for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land':'dwtlfl',\
                       'Aboveground dry weight of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in short tons, on forest land':'agdwlsfl','Dry weight of stumps for live trees (timber species at least 5 inches d.b.h.), in short tons, on forest land':'dwsfl',\
                       'Belowground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land':'bgdwfl','Aboveground dry weight of live trees (woodland species at least 1 inch d.r.c.), in short tons, on forest land':'agdwfl',\
                       'Aboveground dry weight of bark for live trees (at least 1 inch d.b.h./d.r.c.), in short tons, on forest land':'agdwbfl','Aboveground dry weight of standing-dead trees (at least 5 inches d.b.h./d.r.c.), in short tons, on forest land':'agdwsdfl',\
                       'Aboveground green weight of live trees (at least 1 inch d.b.h./d.r.c.), in short tons, on forest land':'aggwfl','Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land calculated with retired regional methods':'agdwfl',\
                       'Aboveground merchantable dry weight of live trees (at least 5 inches d.b.h./d.r.c), in short tons, on forest land calculated with retired regional methods':'agmdwfl','Dry weight of merchantable bole for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland':'dwmbtl',\
                       'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland':'agdwtl','Dry weight of tops and limbs for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland':'dwtltl',\
                       'Aboveground dry weight of live saplings (timber species at least 1 and less than 5 inches d.b.h.), in short tons, on timberland':'agdwlstl','Dry weight of stumps for live trees (timber species at least 5 inches d.b.h.), in short tons, on timberland':'dwstl',\
                       'Belowground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland':'bgdwtl','Aboveground dry weight of live trees (woodland species at least 1 inch d.r.c.), in short tons, on timberland':'agdwtl',\
                       'Aboveground dry weight of live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland calculated with retired regional methods':'agdwtlrrm','Aboveground merchantable dry weight of live trees (at least 5 inches d.b.h./d.r.c), in short tons, on timberland calculated with retired regional methods':'agmdwtlrrm',\
                       'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land':'agcfl','Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land':'bgcfl',\
                       'Above and belowground carbon in standing-dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land':'agbgcsdfl','Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land':'agclssbfl',\
                       'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on forest land':'bgclssbfl','Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on forest land':'cscrcwdfl',\
                       'Carbon in litter, in short tons, on forest land':'clfl','Carbon in organic soil, in short tons, on forest land':'cosfl','Total carbon, in short tons, on forest land':'tcfl','Above and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on forest land':'agbgcfl',\
                       'Forest carbon pool 1: live aboveground, in metric tonnes, on forest land':'fcp1lagfl','Forest carbon pool 2: live belowground, in metric tonnes, on forest land':'fcp2lbgfl','Forest carbon pool 3: dead wood, in metric tonnes, on forest land':'fcp3dwfl',\
                       'Forest carbon pool 4: litter, in metric tonnes, on forest land':'fcp4lfl','Forest carbon pool 5: soil organic, in metric tonnes, on forest land':'fcp5sofl','Forest carbon total: all 5 pools, in metric tonnes, on forest land':'fctfl',\
                       'Aboveground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland':'agctl','Belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland':'bgctl',\
                       'Above and belowground carbon in standing-dead trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland':'agbgcsdtl','Aboveground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland':'agclssbtl',\
                       'Belowground carbon in live seedlings, shrubs, and bushes, in short tons, on timberland':'bgclssbtl','Carbon in stumps, coarse roots, and coarse woody debris, in short tons, on timberland':'cscrcwdtl','Carbon in litter, in short tons, on timberland':'cltl',\
                       'Carbon in organic soil, in short tons, on timberland':'costl','Above and belowground carbon in live trees (at least 1 inch d.b.h./d.r.c), in short tons, on timberland':'agbgctl','Average annual net growth of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'aangfl',\
                       'Average annual net growth of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land':'aanggsfl','Average annual net growth of sawtimber trees, in board feet (International 1/4-inch rule), on forest land':'aagstfl',\
                       'Average annual net growth of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland':'aangtl','Average annual net growth of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland':'aanggstl',\
                       'Average annual net growth of sawtimber trees, in board feet (International 1/4-inch rule), on timberland':'aagsttl','Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on forest land':'aamfl',\
                       'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'aamcffl','Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land':'aamgsfl',\
                       'Average annual mortality of sawtimber trees, in board feet (International 1/4-inch rule), on forest land':'aamstfl','Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in trees, on timberland':'aamtl',\
                       'Average annual mortality of trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland':'aamcftl','Average annual mortality of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland':'aamgstl',\
                       'Average annual mortality of sawtimber trees, in board feet (International 1/4-inch rule), on timberland':'aamsttl','Average annual removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'aarfl',\
                       'Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land':'aargsfl','Average annual removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land':'aarstfl',\
                       'Average annual harvest removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'aahrfl','Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land':'aahrgsfl',\
                       'Average annual harvest removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land':'aahrswfl','Average annual other removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land':'aaorfl',\
                       'Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on forest land':'aaorgsfl','Average annual other removals of sawtimber trees, in board feet (International 1/4-inch rule), on forest land':'aaorstfl',\
                       'Average annual removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland':'aartl','Average annual removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland':'aargstl',\
                       'Average annual removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland':'aarsttl','Average annual harvest removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland':'aahrtl',\
                       'Average annual harvest removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland':'aahrgstl','Average annual harvest removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland':'aahrswtl',\
                       'Average annual other removals of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on timberland':'aaortl','Average annual other removals of growing-stock trees (at least 5 inches d.b.h.), in cubic feet, on timberland':'aaorgstl',\
                       'Average annual other removals of sawtimber trees, in board feet (International 1/4-inch rule), on timberland':'aaorsttl','Number of CWD pieces, in pieces, on forest land':'ncwdpfl','Total volume of FWD (small) pieces, in cubic feet, on forest land':'tvfwdspfl',\
                       'Total volume of FWD (medium) pieces, in cubic feet, on forest land':'tvfwdmpfl','Total volume of FWD (large) pieces, in cubic feet, on forest land':'tvfwdlpfl','Total volume of FWD (all sizes) pieces, in cubic feet, on forest land':'tvfwdaspfl',\
                       'Total volume of CWD, in cubic feet, on forest land':'tvcwdfl','Total volume of DWM piles, in cubic feet, on forest land':'tvdwmpfl','Total volume of DWM (FWD, CWD and piles) in cubic feet, on forest land':'tvdwmall',\
                       'Dry weight of FWD (small) pieces, in short tons, on forest land':'dwfwdspfl','Dry weight of FWD (medium) pieces, in short tons, on forest land':'dwfwdmpfl','Dry weight of FWD (large) pieces, in short tons, on forest land':'dwfwdlpfl',\
                       'Dry weight of FWD (all sizes) pieces, in short tons, on forest land':'dwfwdaspfl','Dry weight of CWD, in short tons, on forest land':'dwcwdfl','Dry weight of DWM piles, in short tons, on forest land':'dwdwmpfl','Total dry weight of DWM (FWD, CWD and piles) in short tons, on forest land':'tdwdwmallfl',\
                       'Carbon in FWD (small) pieces, in short tons, on forest land':'cfwdspfl','Carbon in FWD (medium) pieces, in short tons, on forest land':'cfwdmpfl','Carbon in FWD (large) pieces, in short tons, on forest land':'cfwdlpfl','Carbon in FWD (all sizes) pieces, in short tons, on forest land':'cfwdaspfl',\
                       'Carbon in CWD, in short tons, on forest land':'ccwdfl','Carbon in DWM piles, in short tons, on forest land':'cdwmallfl','Total carbon in DWM (FWD, CWD and piles) in short tons, on forest land':'tcdwmall','Area change - sampled at both inventories by remeasured plots':'ac-sbirp',\
                       'Area change - area forest land both measurements from remeasured plots':'ac-aflbrp','Area change - area forest land either measurement from remeasured plots':'ac-aflemrp','Area change - area timberland both measurements from remeasured plots':'ac-atlbmrp',\
                       'Area change - area timberland either measurement from remeasured plots':'ac-atlemrp'
                      }
        self.dmDict = {'aslw':'1','afl':'2','atl':'3','nltfl':'4','ngsfl':'5',\
                       'nsdfl':'6','nlsfl':'7','nlttl':'8','ngstl':'9','nsdtl':'10',\
                       'nlstl':'11','nvltfl':'12','nvgsfl':'13','nvslpfl':'14','gvstfl':'15',\
                       'gvltfl':'16','svltfl':'17','nvsdfl':'18','nvlttl':'19','nvgstl':'20',\
                       'nvslptl':'21','nvsttl':'22','nvsdtl':'23','agdwfl':'24','dwmbfl':'25',\
                       'dwtlfl':'26','agdwlsfl':'27','dwsfl':'28','bgdwfl':'29','agdwfl':'30',\
                       'agdwbfl':'31','agdwsdfl':'32','aggwfl':'33','agdwfl':'34','agmdwfl':'35',\
                       'dwmbtl':'36','agdwtl':'37','dwtltl':'38','agdwlstl':'39','dwstl':'40',\
                       'bgdwtl':'41','agdwtl':'42','agdwtlrrm':'43','agmdwtlrrm':'44','agcfl':'45',\
                       'bgcfl':'46','agbgcsdfl':'47','agclssbfl':'48','bgclssbfl':'49','cscrcwdfl':'50',\
                       'clfl':'51','cosfl':'52','tcfl':'53','agbgcfl':'54','fcp1lagfl':'55',\
                       'fcp2lbgfl':'56','fcp3dwfl':'57','fcp4lfl':'58','fcp5sofl':'59','fctfl':'60',\
                       'agctl':'61','bgctl':'62','agbgcsdtl':'63','agclssbtl':'64','bgclssbtl':'65',\
                       'cscrcwdtl':'66','cltl':'67','costl':'68','agbgctl':'69','aangfl':'70',\
                       'aanggsfl':'71','aagstfl':'72','aangtl':'73','aanggstl':'74','aagsttl':'75',\
                       'aamfl':'76','aamcffl':'77','aamgsfl':'78','aamstfl':'79','aamtl':'80',\
                       'aamcftl':'81','aamgstl':'82','aamsttl':'83','aarfl':'84','aargsfl':'85',\
                       'aarstfl':'86','aahrfl':'87','aahrgsfl':'88','aahrswfl':'89','aaorfl':'90',\
                       'aaorgsfl':'91','aaorstfl':'92','aartl':'93','aargstl':'94','aarsttl':'95',\
                       'aahrtl':'96','aahrgstl':'97','aahrswtl':'98','aaortl':'99','aaorgstl':'100',\
                       'aaorsttl':'101','ncwdpfl':'102','tvfwdspfl':'103','tvfwdmpfl':'104',\
                       'tvfwdlpfl':'105','tvfwdaspfl':'106','tvcwdfl':'107','tvdwmpfl':'108',\
                       'tvdwmall':'109','dwfwdspfl':'110','dwfwdmpfl':'111','dwfwdlpfl':'112',\
                       'dwfwdaspfl':'113','dwcwdfl':'114','dwdwmpfl':'115','tdwdwmallfl':'116',\
                       'cfwdspfl':'117','cfwdmpfl':'118','cfwdlpfl':'119','cfwdaspfl':'120',\
                       'ccwdfl':'121','cdwmallfl':'122','tcdwmall':'123','ac-sbirp':'124',\
                       'ac-aflbrp':'125','ac-aflemrp':'126','ac-atlbmrp':'127','ac-atlemrp':'128'}
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
                          'WA':'53','WV':'54','WI':'55','WY':'56','PR':'72',
                          'VI':'78'}
