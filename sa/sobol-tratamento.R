setwd('C:/Users/LabEEE_1-2/idf-creator/sa/')

df <- read.csv('sample.csv')

uni_fun <- function(x){
  return(print(lapply(x,unique)))
}

for (typ in unique(df$type)){
  print(typ)
  sub.df <- subset(df, df$type == typ)
  uni_fun(sub.df)
}

df_top <- subset(df, df$type == 'TOP')
