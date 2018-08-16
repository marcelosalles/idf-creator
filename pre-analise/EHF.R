setwd('C:/Users/LabEEE_1-2/idf-creator/')

month_means <- read.csv('month_means.csv')
month_means$mont_num <- c(1,2,3,4,5,6,7,8,9,10,11,12)

setwd('C:/Users/LabEEE_1-2/idf-creator/pre-analise/')

files <- list.files(pattern = '*.idf')
#files <- files[200:300]
df_EHF <- data.frame('file'= rep(NA,length(files)), 'EHF' = rep(NA,length(files)))
line <- 0

for (file in files){
  print(file)
  line = line + 1
  
  csv_file <- paste(substr(file,1,nchar(file)-3),'csv',sep = '')
  
  size <- file.info(csv_file)['size']
  if(size >0){
    df <- read.csv(csv_file)
    df$sup_lim <- -1
    df$EHF <- -1
    
    for(i in 1:12){
      df$sup_lim[as.integer(substr(df$Date.Time,1,3)) == i] <- month_means$mean_temp[i] + 3.5
    }
    df$EHF <- ifelse(as.numeric(df$ZONE_0.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
    df_EHF$file[line] <- substr(file,1,nchar(file)-4)
    df_EHF$EHF[line] <- mean(df$EHF[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
  }
}
write.csv(df_EHF,'EHF.csv')
