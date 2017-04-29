#install.packages("rvest") #if install needed
library(rvest)

# VARIABLE NAMES
# st = FIA state code,
# yr = year, 
# nm = numerator,
# dn = denominator,
# pg = page variable,
# r = row variable,
# c = column variable,
# of = output file name (currently html file)
# all arguments are strings

fetchTable = function(st, yr, nm, dn, pg, r, c){
    BASEADDR = "http://apps.fs.fed.us/Evalidator/batcheval.jsp?"
    RETYPE = "reptype=State"
    LAT = "&lat=0"
    LON = "&lon=-0"
    RAD = "&radius=0"
    num = paste("&snum=",nm)
    den = paste("&sdenom=",dn)
    stcode = paste("&wc=",st)
    #yr = yr
    page = paste("&pselected=",pg)
    row = paste("&rselected=",r)
    col = paste("&cselected=",c)
    OTHER = "&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
    url = paste(BASEADDR,RETYPE,LAT,LON,RAD,num,den,stcode,yr,page,row,col,OTHER)
    url=gsub(" ","%20",url) #replace spaces with "%20"
    return(url)
}


#testing
st = "9"
yr = "2015"
nm = ""
dn = ""
pg = "None"
r = "Forest type group"
c = "Ownership group"
ofprfix = "TPA"
of = paste("out",ofprfix,st,".html")

testing=fetchTable(st, yr, nm, dn, pg, r, c)

testing

#returns "http://apps.fs.fed.us/Evalidator/batcheval.jsp?%20reptype=State%20&lat=0%20&lon=-0%20&radius=0%20&snum=%20%20&sdenom=%20%20&wc=%209%202015%20&pselected=%20None%20&rselected=%20Forest%20type%20group%20&cselected=%20Ownership%20group%20&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="

#rvest syntax example from online
webpage <- read_html(testing) #not working


