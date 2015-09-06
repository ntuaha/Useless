setwd('/home/aha/Project/Useless')
data = read.table("./sentense3.log",header=T,sep=",")
by_age = by(data,data$age,function(d) table(d$word))
filter_age = sapply(by_age,function(d) unlist(d[d>1]))

getImportant = function(d){
  return (rownames(sort(-unlist(d)))[1:10])
}
important_name = lapply(filter_age,getImportant)

writeout = function(n){
  cdata = important_name[[n]]
  cdata = t(c(n,cdata,rep("",len=10))[1:11])
  write.table(cdata,file="./output.csv",sep=",",append = TRUE,col.names=F,row.names = FALSE)
}
sapply(names(important_name),writeout)

