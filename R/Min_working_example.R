source("EVALIDatR.R") #load functions 


#example query for the state of NJ for a single year(2015)
#declare variables
type="state"
st = "34"
yr = "2015"
nm = "Area of timberland, in acres"
dn = "No denominator - just produce estimate."
pg = "None"
r='Stand age 10 yr classes'
c='Reserved status class'


#scrape table
testing_state=fetchTable(type=type,st=st,yr=yr,nm=nm, dn=dn, pg=pg, r=r, c=c)

#rvest syntax example from online
webpage1 <- read_html(testing_state)

#extract nodes
tbl=html_nodes(webpage1,"table")

#put data into dataframe
#estimate
df=html_table(tbl,trim=TRUE,fill=TRUE,header=TRUE)[[1]] 

#sampling error
df2=html_table(tbl,trim=TRUE,fill=TRUE,header=TRUE)[[2]] 


#number of non-zero plots
df3=html_table(tbl,trim=TRUE,fill=TRUE,header=TRUE)[[3]] 

#Column classification variable description - towards bottom of webpage
df4=html_table(tbl,trim=TRUE,fill=TRUE,header=TRUE)[[4]]


##example radius query, replicating example from Miles(2015)
type = "radius"
st = "272014,552014"
yr = ""
lat= "45.0"
lon= "-93.0"
rad="50"
nm = "Area of timberland, in acres"
dn = "No denominator - just produce estimate."
pg = "None"
r = "Stand-size class"
c = "Ownership group - Major"


testing_radius=fetchTable(type=type,st=st,lat=lat,lon=lon,rad=rad,yr=yr,nm=nm, dn=dn, pg=pg, r=r, c=c)

#rvest syntax example from online
webpage2 <- read_html(testing_radius)

#extract nodes
tbl=html_nodes(webpage2,"table")


#put data into dataframe
#estimate
df=html_table(tbl,trim=TRUE,fill=TRUE,header=TRUE)[[1]] 

#sampling error
df2=html_table(tbl,trim=TRUE,fill=TRUE,header=TRUE)[[2]] 


#number of non-zero plots
df3=html_table(tbl,trim=TRUE,fill=TRUE,header=TRUE)[[3]] 

#Column classification variable description - towards bottom of webpage
df4=html_table(tbl,trim=TRUE,fill=TRUE,header=TRUE)[[4]]



# TO DO:
#figure out how to reshape and graph

#library(ggplot2)
#library(reshape2)
#library(dplyr)
#ggplot(df,aes(x=))



