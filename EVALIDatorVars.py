#EVALIDatorVars.py


class EVALIDatorVars:
    #default constructor
    def __init__(self):
        #tuple of variable names used in this class
        v = ('varDict', 'stateDict')
        #dictionary of numerator/denominator variables
        self.NmDict = {'aslw':'1','afl':'2','atl':'3','nltfl':'4','ngsfl':'5',\
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
        self.DmDict = {'aslw':'1','afl':'2','atl':'3','nltfl':'4','ngsfl':'5',\
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
