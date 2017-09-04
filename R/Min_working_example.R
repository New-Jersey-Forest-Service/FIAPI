source("EVALIDatR.R") #load functions 

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
testing=fetchTable(type=type,st=st,yr=yr,nm=nm, dn=dn, pg=pg, r=r, c=c)

#rvest syntax example from online
webpage <- read_html(testing)

#extract nodes
tbl=html_nodes(webpage,"table")

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

library(ggplot2)
library(reshape2)
library(dplyr)
ggplot(df,aes(x=))




