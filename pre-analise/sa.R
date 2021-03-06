library(ggplot2)

# DF generico ----
x<- 50000
df <- data.frame('x1'=-1+seq(0,x-1)*2/x,
                 'x2'=runif(x,-1,1),
                 'x3'=runif(x,-1,1),
                 'x4'=runif(x,-1,1),
                 'y' =as.numeric(seq(1,x)))

# funcoes ----

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
           
sensivity <- function(name, df, y, n_delta, second=FALSE, total=FALSE, plot = FALSE){
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
  ifelse(plot == TRUE, return(mean_values),return (var(mean_values)/var(df[[y]])))
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

# testes ----

sec_order(c('po','oi','ui','uioio','jkhjk','hjkhjkh','eeiii'))

sensivity('shading',df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)[[1]]

sensivity('area',df = df_sa2,y = 'EHF',n_delta = 100)

sensivity(c('x2','x3'),df = df,y = 'y',n_delta = 50, second = TRUE)

sensivity('x1',df = df,y = 'y',n_delta = 20, total = TRUE)

cargatermica <- sensivity('thermal_loads',df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)

cg <- sensivity('thermal_loads',df = df_sa2,y = 'EHF',n_delta = 100)

var(cargatermica)
cg

u_wall <- sensivity('u_wall',df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)

var_EHF <- var(df_sa2$EHF)

var(cargatermica)/var_EHF

# baixando o DF ----

setwd('D:/LabEEE_1-2/idf-creator/')
df_sa <- read.csv('df_sa.csv')

#df_sa$ori <- ifelse(df_sa$zone%%2 == 0, df_sa$ori <- (179.95 * (1 + df_sa$azimuth) - 90)%%360, df_sa$ori <- (179.95 * (1 + df_sa$azimuth) + 90)%%360)
df_sa$ori <- ifelse(df_sa$zone%%6 == 5,df_sa$ori <- df_sa$azimuth, ifelse(df_sa$zone%%2 == 0, df_sa$ori <- (df_sa$azimuth+.5)%%2-1, df_sa$ori <- (df_sa$azimuth+1.5)%%2-1))

df_sa2 <- df_sa
df_sa2$X <- df_sa2$X.1 <- df_sa2$file <- df_sa2$zone <- NULL
sa_x <- colnames(df_sa2)[! colnames(df_sa2) %in% 'EHF']

# df_sa2 <- data.frame('glass'=df_sa2$glass,'thermal_loads'= df_sa2$thermal_loads,
#                      'open_fac'=df_sa2$open_fac, 'wwr'=df_sa2$wwr,'EHF'=df_sa2$EHF)
# df_sa2$glass <- df_sa2$thermal_loads <- df_sa2$open_fac <- df_sa2$wwr <- NULL
# 
# sa_x <- colnames(df_sa2)[! colnames(df_sa2) %in% 'EHF']

# first order ----
df_frst <- data.frame('x' = sa_x)
df_frst$S1 <- NA
df_frst$Stot <- NA
for(name in sa_x){
  print(name)
  df_frst$S1[df_frst$x == name] <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)
  df_frst$Stot[df_frst$x == name] <- 1-sensivity(name,df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)
}

# 2nd Order ----

df_scnd <- sec_order(sa_x)
df_scnd$S <- NA
for(name in df_scnd$x1){
  #print(c(df_scnd$x1[i],df_scnd$x2[i]))
  df_scnd$S[df_scnd$x1 == name] <- sensivity(c(name,df_scnd$x2[df_scnd$x1 == name]),df = df_sa2,y = 'EHF',n_delta = 10, second = TRUE)
}

df_scnd$S2 <- NA
for(i in 1:nrow(df_scnd)){
  print(df_scnd$x1[i])
  print(df_scnd$x2[i])
  print(df_frst$x[df_frst$x == df_scnd$x1[i]])
  print(df_frst$x[df_frst$x == df_scnd$x2[i]])
  df_scnd$S2[i] <- df_scnd$S[i] - df_frst$S1[df_frst$x == df_scnd$x1[i]] - df_frst$S1[df_frst$x == df_scnd$x2[i]]
}

# ---- first ----

name = 'area'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'ratio'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'abs'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle('Absort�ncia') +
  ylab('EHF') +
  xlab('Absort�ncia') +
  ylim(0.6,1)

name = 'shading'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'ori'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'u_wall'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'corr_vent'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'stairs'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'open_fac'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle('Fator de abertura') +
  ylab('EHF') +
  xlab('Fator de abertura') +
  ylim(0.6,1)

name = 'thermal_loads'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle('Carga T�rmica') +
  ylab('EHF') +
  xlab('Carga T�rmica') +
  ylim(0.6,1)

name = 'glass'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'height'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle(name) +
  ylab('EHF') +
  xlab(name) +
  ylim(0.6,1)

name = 'wwr'
mean <- sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100, plot = TRUE)
df_plot <- data.frame('x' = rep(NA,length(mean)), 'EHF' = mean)
df_plot$x <- -1.01 + seq(1,length(mean))*(2/length(mean))
ggplot(df_plot,aes(df_plot$x,df_plot$EHF)) + geom_point() + ggtitle('PAF') +
  ylab('EHF') +
  xlab('PAF') +
  ylim(0.6,1)

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

# ---- histo ----
hist(df_sa$EHF)

df_plot <- df_sa
df_plot$EHF <- (df_plot$EHF) **(4)
ggplot(df_plot, aes(df_plot$EHF)) + geom_histogram(binwidth = .01) + ggtitle('EHF')


df_base <- df_sa
df_base$X.1 <- df_base$X <- df_base$file <- df_base$zone <- NULL

i <- 100
df_i <- df_base[sample(nrow(df_base), i), ]
#df_i <- apply(df_i,2,as.numeric)
preview_mean <- mean(apply(df_i,2,mean))
i <- i*1.1
df_i <- df_base[sample(nrow(df_base), round(i)), ]
#df_i <- apply(df_i,2,as.numeric)
current_mean <- mean(apply(df_i,2,mean))

while((current_mean - preview_mean)**2 > (.0001)**2){
  print(current_mean - preview_mean)
  
  preview_mean <- current_mean
  i <- i*1.1
  df_i <- df_base[sample(nrow(df_base), round(i)), ]
  #df_i <- apply(df_i,2,as.numeric)
  current_mean <- mean(apply(df_i,2,mean))
}

print(current_mean - preview_mean)

print(i)

apply(df_base[sample(nrow(df_base), 5000), ],2,mean)  #- apply(df_base[sample(nrow(df_base), 100), ],2,mean)
