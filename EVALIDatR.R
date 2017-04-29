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
    RETYPE = "reptype=Circle"
    LAT = "&lat=45.0"
    LON = "&lon=-93.0"
    RAD = "&radius=50"
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


#example of working URL from Miles(2015):
# http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=Circle&lat=45.0&lon=-93.0&radius=50&snum=Area%20of%20timberland,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=272014,552014&pselected=None&rselected=Stand-size%20class&cselected=Ownership%20group%20-%20Major&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom=

example = "http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=Circle&lat=45.0&lon=-93.0&radius=50&snum=Area%20of%20timberland,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=272014,552014&pselected=None&rselected=Stand-size%20class&cselected=Ownership%20group%20-%20Major&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
        
out=read_html(example) #works 

#testing - replicating example from Miles(2015)
st = "272014,552014"
yr = ""
nm = "Area of timberland, in acres"
dn = "No denominator - just produce estimate."
pg = "None"
r = "Stand-size class"
c = "Ownership group - Major"


testing=fetchTable(st, yr, nm, dn, pg, r, c)

testing==example #should return TRUE

#rvest syntax example from online
webpage <- read_html(testing)

tbl=html_nodes(webpage,"table") #extract nodes
df=html_table(tbl)[[1]] #put data into dataframe


