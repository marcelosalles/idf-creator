setwd('C:/Users/LabEEE_1-2/idf-creator/')

# ----
month_means <- read.csv('month_means.csv')
month_means$mont_num <- c(1,2,3,4,5,6,7,8,9,10,11,12)

setwd('C:/Users/LabEEE_1-2/idf-creator/pre-analise/')

files <- list.files(pattern = '*.idf')
files <- files[1900:2009]
df_EHF <- data.frame('file'= rep(NA,length(files)*15), 'zone'= rep(NA,length(files)*15), 'EHF' = rep(NA,length(files)*15))
line <- 0

#zones_seq <- c(6,12,18,24) 
for (file in files){
  print(file)
  
  csv_file <- paste(substr(file,1,nchar(file)-3),'csv',sep = '')
  
  size <- file.info(csv_file)['size']
  if(size >0){
    n_zones <- 0
    df <- read.csv(csv_file)
    df$sup_lim <- -1
    df$zn_0 <- df$zn_1 <- df$zn_2 <- df$zn_3 <- df$zn_4 <- df$zn_5 <- df$zn_6 <- df$zn_7 <- df$zn_8 <- df$zn_9 <- df$zn_10 <- df$zn_11 <- df$zn_12 <- df$zn_13 <- 
      df$zn_14 <- df$zn_15 <- df$zn_16 <- df$zn_17 <- df$zn_18 <- df$zn_19 <- df$zn_20 <- df$zn_21 <- df$zn_22 <- df$zn_23 <- -1
    
    for(i in 1:12){
      df$sup_lim[as.integer(substr(df$Date.Time,1,3)) == i] <- month_means$mean_temp[i] + 3.5
    }
    if('ZONE_0.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_0 <- ifelse(as.numeric(df$ZONE_0.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 0
      df_EHF$EHF[line] <- mean(df$zn_0[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_1.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_1 <- ifelse(as.numeric(df$ZONE_1.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 1
      df_EHF$EHF[line] <- mean(df$zn_1[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_2.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_2 <- ifelse(as.numeric(df$ZONE_2.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 2
      df_EHF$EHF[line] <- mean(df$zn_2[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_3.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_3 <- ifelse(as.numeric(df$ZONE_3.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 3
      df_EHF$EHF[line] <- mean(df$zn_3[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_4.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_4 <- ifelse(as.numeric(df$ZONE_4.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 4
      df_EHF$EHF[line] <- mean(df$zn_4[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_5.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_5 <- ifelse(as.numeric(df$ZONE_5.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 5
      df_EHF$EHF[line] <- mean(df$zn_5[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_6.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_6 <- ifelse(as.numeric(df$ZONE_6.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 6
      df_EHF$EHF[line] <- mean(df$zn_6[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_7.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_7 <- ifelse(as.numeric(df$ZONE_7.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 7
      df_EHF$EHF[line] <- mean(df$zn_7[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_8.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_8 <- ifelse(as.numeric(df$ZONE_8.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 8
      df_EHF$EHF[line] <- mean(df$zn_8[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_9.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_9 <- ifelse(as.numeric(df$ZONE_9.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 9
      df_EHF$EHF[line] <- mean(df$zn_9[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_10.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_10 <- ifelse(as.numeric(df$ZONE_10.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 10
      df_EHF$EHF[line] <- mean(df$zn_10[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_11.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_11 <- ifelse(as.numeric(df$ZONE_11.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 11
      df_EHF$EHF[line] <- mean(df$zn_11[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_12.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_12 <- ifelse(as.numeric(df$ZONE_12.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 12
      df_EHF$EHF[line] <- mean(df$zn_12[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_13.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_13 <- ifelse(as.numeric(df$ZONE_13.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 13
      df_EHF$EHF[line] <- mean(df$zn_13[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_14.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_14 <- ifelse(as.numeric(df$ZONE_14.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 14
      df_EHF$EHF[line] <- mean(df$zn_14[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_15.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_15 <- ifelse(as.numeric(df$ZONE_15.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 15
      df_EHF$EHF[line] <- mean(df$zn_15[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_16.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_16 <- ifelse(as.numeric(df$ZONE_16.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 16
      df_EHF$EHF[line] <- mean(df$zn_16[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_17.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_17 <- ifelse(as.numeric(df$ZONE_17.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 17
      df_EHF$EHF[line] <- mean(df$zn_17[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_18.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_18 <- ifelse(as.numeric(df$ZONE_18.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 18
      df_EHF$EHF[line] <- mean(df$zn_18[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_19.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_19 <- ifelse(as.numeric(df$ZONE_19.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 19
      df_EHF$EHF[line] <- mean(df$zn_19[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_20.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_20 <- ifelse(as.numeric(df$ZONE_20.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 20
      df_EHF$EHF[line] <- mean(df$zn_20[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_21.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_21 <- ifelse(as.numeric(df$ZONE_21.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 21
      df_EHF$EHF[line] <- mean(df$zn_21[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_22.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_22 <- ifelse(as.numeric(df$ZONE_22.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 22
      df_EHF$EHF[line] <- mean(df$zn_22[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
    if('ZONE_23.Zone.Operative.Temperature..C..Hourly.' %in% colnames(df)){
      line <- line + 1
      n_zones <- n_zones + 1
      df$zn_23 <- ifelse(as.numeric(df$ZONE_23.Zone.Operative.Temperature..C..Hourly.) > df$sup_lim, 1, 0)
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- 23
      df_EHF$EHF[line] <- mean(df$zn_23[as.numeric(df$SCH_OCUPACAO.Schedule.Value....Hourly.) > 0])
    }
  }else{
    if(n_zones >= 24){
      n_zones <- 6
    }else{
      n_zones <- n_zones + 6
    }
    for(zone in 1:n_zones){
      line <- line + 1
      df_EHF$file[line] <- substr(file,1,nchar(file)-4)
      df_EHF$zone[line] <- zone
    }
  }
}
write.csv(df_EHF,'EHF3.csv')

# ----

df_ehf1 <- read.csv('EHF1.csv')
df_ehf1$file <- as.character(df_ehf1$file)
nacount <- is.na(df_ehf1$file) # elimina os NA e coloca o nome do arquivo correto
df_ehf1$X[nacount]
df_ehf1$file[1059] <- 'pre-analise_1950'
df_ehf1$file[2398] <- 'pre-analise_3155'
df_ehf1$file[3161] <- 'pre-analise_873'

df_ehf2 <- read.csv('EHF2.csv')
df_ehf2$file <- as.character(df_ehf2$file)
nacount <- is.na(df_ehf2$file)
df_ehf2$X[nacount]
df_ehf2$file[1262] <- 'pre-analise_4561'
df_ehf2$file[1474] <- 'pre-analise_4773'

df_ehf3 <- read.csv('EHF.csv')
df_ehf3$file <- as.character(df_ehf3$file)
nacount <- is.na(df_ehf3$file)
df_ehf3$X[nacount]
df_ehf3$file[226] <- 'pre-analise_6825'
df_ehf3$file[1994] <- 'pre-analise_8593'

df_ehf <- rbind(df_ehf1,df_ehf2,df_ehf3)

nacount <- is.na(df_ehf$file)
length(nacount[nacount == TRUE])
length(unique(df_ehf$file))

cond0 <- substr(df_ehf$file, nchar(df_ehf$file)-4,nchar(df_ehf$file)-4) == "_"
df_ehf$file_fix[cond0] <- df_ehf$file[cond0]

cond1 <- substr(df_ehf$file, nchar(df_ehf$file)-1,nchar(df_ehf$file)-1) == "_"
df_ehf$file_fix[cond1] <- paste(substr(df_ehf$file[cond1], 1,12),"000",substr(df_ehf$file[cond1], nchar(df_ehf$file[cond1]),nchar(df_ehf$file[cond1])), sep = '')

cond2 <- substr(df_ehf$file, nchar(df_ehf$file)-2,nchar(df_ehf$file)-2) == "_"
df_ehf$file_fix[cond2] <- paste(substr(df_ehf$file[cond2], 1,12),"00",substr(df_ehf$file[cond2], nchar(df_ehf$file[cond2])-1,nchar(df_ehf$file[cond2])), sep = '')

cond3 <- substr(df_ehf$file, nchar(df_ehf$file)-3,nchar(df_ehf$file)-3) == "_"
df_ehf$file_fix[cond3] <- paste(substr(df_ehf$file[cond3], 1,12),"0",substr(df_ehf$file[cond3], nchar(df_ehf$file[cond3])-2,nchar(df_ehf$file[cond3])), sep = '')

df_ehf$file <- df_ehf$filefix
df_ehf$file_fix <- df_ehf$file
colnames(df_ehf)[colnames(df_ehf) == 'file_fix'] <- 'file'

# ----

df_bldg <- read.csv('sa/sample0.csv')
df_office <- read.csv('sa/sample1.csv')

df_sa <- data.frame('area' = rep(df_bldg$area,times=rep(c(6,12,18,24),2475)),
                    'ratio' = rep(df_bldg$ratio,times=rep(c(6,12,18,24),2475)),
                    'height' = rep(df_bldg$height,times=rep(c(6,12,18,24),2475)),
                    'abs' = rep(df_bldg$abs,times=rep(c(6,12,18,24),2475)),
                    'shading' = rep(df_bldg$shading,times=rep(c(6,12,18,24),2475)),
                    'azimuth' = rep(df_bldg$azimuth,times=rep(c(6,12,18,24),2475)),
                    'u_wall' = rep(df_bldg$u_wall,times=rep(c(6,12,18,24),2475)),
                    'corr_vent' = rep(df_bldg$corr_vent,times=rep(c(6,12,18,24),2475)),
                    'stairs' = rep(df_bldg$stairs,times=rep(c(6,12,18,24),2475)))
df_sa <- data.frame(rep(df_bldg,times=rep(c(6,12,18,24),2475)))

df_sa <- cbind(df_sa, df_office)
                    
# falied ----
ehf_NA <- is.na(df_ehf$EHF)
failed <- df_ehf$file[ehf_NA]
failed
df_ehf_sa <- df_ehf[ is.na(df_ehf$EHF) == FALSE, ]
