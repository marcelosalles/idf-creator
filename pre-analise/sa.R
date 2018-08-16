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
    mean_values[i] = mean_value
  }

  #print(var(mean_values))
  #print(var(df[y]))
  return (var(mean_values)/var(df[y]))
}

df_sa2 <- df_sa
df_sa2$X <- df_sa2$file <- df_sa2$zone <- NULL
sa_x <- colnames(df_sa2)[! colnames(df_sa2) %in% 'EHF']



for(name in sa_x){
  print(name)
  print(sensivity(name,df = df_sa2,y = 'EHF',n_delta = 100)[[1]])
}

sensivity('shading',df = df_sa2,y = 'EHF',n_delta = 2, total = TRUE)[[1]]

sensivity('x1',df = df,y = 'y',n_delta = 1000)

sensivity(c('x2','x3'),df = df,y = 'y',n_delta = 50, second = TRUE)

sensivity('x1',df = df,y = 'y',n_delta = 20, total = TRUE)
