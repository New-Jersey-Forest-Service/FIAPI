#EVALIDatorVars.py


class EVALIDatorVars:
    #default constructor
    def __init__(self):
        #tuple of variable names used in this class
        v = ('varDict', 'stateDict')
        #dictionary of numerator/denominator variables
        self.varDict = {''}#this needs values added to it!!!
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
