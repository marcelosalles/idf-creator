x<- 5000
df <- data.frame('x1'=-1+seq(0,x-1)*2/x,
                 'x2'=runif(x,-1,1),
                 'x3'=runif(x,-1,1),
                 'x4'=runif(x,-1,1),
                 'y' =seq(1,x))
           
sensivity <- function(name,df, y, n_delta, second=FALSE, total=FALSE){
  if(total == TRUE){
    col_x <- colnames(df)[! colnames(df) %in% y]
    x <- col_x[! col_x %in% name]
    sub_df <- df[ , which(names(df) %in% x)]
    lower_bound <- min(apply(sub_df,2,min))
    upper_bound <- max(apply(sub_df,2,max))
  }else{
    if(second == TRUE){
      x1 <- name[1]
      x2 <- name[2]
      sub_df <- df[ , which(names(df) %in% name)]
      lower_bound <- min(apply(sub_df,2,min))
      upper_bound <- max(apply(sub_df,2,max))
      
      delta <- (upper_bound-lower_bound)/n_delta
      
      mean_values = c(rep(NA,n_delta))
      for (i in 1:n_delta){
        lower_delta <- lower_bound+(i-1)*delta
        upper_delta = lower_delta+delta
        mean_value <- mean(df[y][df[x1] >= lower_delta & df[x1] < upper_bound &
                            df[x2] >= lower_delta & df[x2] < upper_bound])
        mean_values[i] = mean_value
      }
    }else{
      lower_bound <- min(df[name])
      upper_bound <- max(df[name])
      
      delta <- (upper_bound-lower_bound)/n_delta
      
      mean_values = c(rep(NA,n_delta))
      for (i in 1:n_delta){
        lower_delta <- lower_bound+(i-1)*delta
        upper_delta = lower_delta+delta
        mean_value <- mean(df[y][df[name] >= lower_delta & df[name] < upper_bound])
        mean_values[i] = mean_value
      }
    }
  }
  print(mean(mean_values))
  print(var(df[y]))
  return (var(mean_values)/var(df[y]))
}

sensivity(c('x1','x2'),df = df,y = 'y',n_delta = 50, second = TRUE)

sensivity('x4',df = df,y = 'y',n_delta = 50)#, second = TRUE)

ei <- df[ , which(names(df) %in% oi)]
