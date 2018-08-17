library(ggplot2)
x<- 50000
df <- data.frame('x1'=-1+seq(0,x-1)*2/x,
                 'x2'=runif(x,-1,1),
                 'x3'=runif(x,-1,1),
                 'x4'=runif(x,-1,1),
                 'y' =as.numeric(seq(1,x)))

filter <- function(x, df, lower_delta, upper_delta, type){
  if(type == 'total'){
    sub_df <- df
    for(xi in x){
      sub_df <- sub_df[sub_df[xi] >= lower_delta & sub_df[xi] < upper_delta, ]
    }
  }
  if(type == 'second'){
    x1 <- x[1]
    x2 <- x[2]
    sub_df <- df[df[x1] >= lower_delta & df[x1] < upper_delta &
      df[x2] >= lower_delta & df[x2] < upper_delta, ]
  }
  if(type == 'first'){
    sub_df <- df[df[x] >= lower_delta & df[x] < upper_delta, ]
  }
  return(sub_df)
}
           
sensivity <- function(name, df, y, n_delta, second=FALSE, total=FALSE){
  lower_bound <- -1
  upper_bound <- 1
  delta <- (upper_bound-lower_bound)/n_delta
  
  if(total == TRUE){
    type = 'total'
    col_x <- colnames(df)[! colnames(df) %in% y] # delete Y
    x <- col_x[! col_x %in% name] # delete name
  }else{
    if(second == TRUE){
      type = 'second'
      x <- name
    }else{
        type = 'first'
        x <- name
    }
  }
  
  mean_values = c(rep(NA,n_delta))
  
  for(i in 1:n_delta){
    lower_delta <- lower_bound+(i-1)*delta
    upper_delta = lower_delta+delta
    sub_df <- filter(x, df, lower_delta, upper_delta, type)
    mean_value <- mean(sub_df[[y]])
    mean_values[i] <- mean_value
  }
  return(mean_values)

  #print(var(mean_values))
  #print(var(df[y]))
  #return (var(mean_values)/var(df[y]))
}

sec_order <- function(vec){
  names_list <- data.frame('x1'=rep(NA,(length(vec)-1)),'x2'=rep(NA,(length(vec)-1)))
  if(length(vec) > 2){
    for(i in 1:(length(vec)-1)){
      names_list$x1[i] <- vec[1]
      names_list$x2[i] <- vec[i+1]
    }
    next_names <- sec_order(vec[!vec %in% vec[1]])
    names_list <- rbind(names_list,next_names)
  }else{
    names_list$x1[1] <- vec[1]
    names_list$x2[1] <- vec[2]
  }
  return(names_list)
}

sec_order(c('po','oi','ui','uioio','jkhjk','hjkhjkh','eeiii'))

setwd('C:/Users/LabEEE_1-2/idf-creator/')
df_sa <- read.csv('df_sa.csv')
df_sa2 <- df_sa
df_sa2$X <- df_sa2$X.1 <- df_sa2$file <- df_sa2$zone <- NULL
sa_x <- colnames(df_sa2)[! colnames(df_sa2) %in% 'EHF']

# df_sa2 <- data.frame('glass'=df_sa2$glass,'thermal_loads'= df_sa2$thermal_loads,
#                      'open_fac'=df_sa2$open_fac, 'wwr'=df_sa2$wwr,'EHF'=df_sa2$EHF)
# df_sa2$glass <- df_sa2$thermal_loads <- df_sa2$open_fac <- df_sa2$wwr <- NULL
# 
# sa_x <- colnames(df_sa2)[! colnames(df_sa2) %in% 'EHF']

df_frst <- data.frame('x' = sa_x)
df_frst$S1 <- NA
df_frst$Stot <- NA
for(i in 1:nrow(df_frst)){
  #print(name)
  #df_frst$S1[i] <- sensivity(df_frst$x[i],df = df_sa2,y = 'EHF',n_delta = 100)[[1]]
  mean <- sensivity(df_frst$x[i],df = df_sa2,y = 'EHF',n_delta = 100)
  print(mean)
  df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
  df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))

  ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(df_frst$x[i])
  #df_frst$Stot[i] <- 1-sensivity(df_frst$x[i],df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)[[1]]
}

df_scnd <- sec_order(sa_x)
df_scnd$S <- NA
for(i in 1:nrow(df_scnd)){
  #print(c(df_scnd$x1[i],df_scnd$x2[i]))
  df_scnd$S[i] <- sensivity(c(df_scnd$x1[i],df_scnd$x2[i]),df = df_sa2,y = 'EHF',n_delta = 10, second = TRUE)[[1]]
}

df_scnd$S2 <- NA
for(i in 1:nrow(df_scnd)){
  df_scnd$S2[i] <- df_scnd$S[i] - df_frst$S1[df_frst$x == df_scnd$x1[i]] - df_frst$S1[df_frst$x == df_scnd$x2[i]]
}
sensivity('shading',df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)[[1]]

sensivity('area',df = df_sa2,y = 'EHF',n_delta = 100)

sensivity(c('x2','x3'),df = df,y = 'y',n_delta = 50, second = TRUE)

sensivity('x1',df = df,y = 'y',n_delta = 20, total = TRUE)
# ---- first ----

name = 'area'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'ratio'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'abs'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle('Absortância') +
  ylab('EHF') +
  xlab('Absortância')

name = 'shading'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'azimuth'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'u_wall'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'corr_vent'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'stairs'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'open_fac'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle('Fator de abertura') +
  ylab('EHF') +
  xlab('Fator de abertura')

name = 'thermal_loads'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle('Carga Térmica') +
  ylab('EHF') +
  xlab('Carga Térmica')

name = 'glass'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'height'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name)

name = 'wwr'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle('PAF') +
  ylab('EHF') +
  xlab('PAF')
# ---- total ----

name = 'area'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'ratio'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'abs'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'shading'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'azimuth'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'u_wall'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'corr_vent'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'stairs'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'open_fac'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'thermal_loads'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'glass'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'height'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)

name = 'wwr'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name)
