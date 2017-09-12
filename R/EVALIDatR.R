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

#define function to take parameters and build connection string with default behavior to state queries

fetchTable = function(type,lat="0",lon="-0",rad="0",st, yr, nm, dn, pg, r, c){
    BASEADDR = "http://apps.fs.fed.us/Evalidator/batcheval.jsp?"
    RETYPE=ifelse(test=(type=="radius"),
      yes="reptype=Circle",
      no="reptype=State")
    LAT = paste("&lat=",lat,sep="")
    LON = paste("&lon=",lon,sep="")
    RAD = paste("&radius=",rad,sep="")
    num = paste("&snum=",nm,sep="")
    den = paste("&sdenom=",dn,sep="")
    stcode = paste("&wc=",st,sep="")
    yr = yr
    page = paste("&pselected=",pg,sep="")
    row = paste("&rselected=",r,sep="")
    col = paste("&cselected=",c,sep="")
    OTHER = "&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
    url = paste(BASEADDR,RETYPE,LAT,LON,RAD,num,den,stcode,yr,page,row,col,OTHER,sep="")
    url=gsub(" ","%20",url) #replace spaces with "%20"
    return(stringr::str_trim(url))
}
