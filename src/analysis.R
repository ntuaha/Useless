setwd('/home/aha/Project/Useless')
data = read.table("./sentense3.log",header=T,sep=",")
by_age = by(data,data$age,function(d) table(d$word))
filter_age = sapply(by_age,function(d) unlist(d[d>1]))

getImportant = function(d){
  t = unlist(d)
  ranks = rank(-t)
  ans = c(rownames(t)[ranks==1],rownames(t)[ranks==2],rownames(t)[ranks==3],rownames(t)[ranks==4],rownames(t)[ranks==5])
  return(ans)
}

important_name = sapply(filter_age,getImportant)

writeout = function(n){
  cdata = important_name[[n]]
  cdata = t(c(n,cdata))
  write.table(cdata,file="./output.csv",sep=",",append = TRUE,col.names=F,row.names = FALSE)
}
#important_name$name = NULL
sapply(names(important_name),writeout)

