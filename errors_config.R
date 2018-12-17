setwd('/media/marcelo/OS/LabEEE_1-2/idf-creator/')
# setwd('D:/LabEEE_1-2/idf-creator/')

df_error <- read.csv('ResumoErros_compare_12-10.csv')
#df_error <- df_error[order(df_error$file),]

unique( df_error$SevereCompleted)
length(subset(df_error, df_error$SevereCompleted == 'FATAL'))

df_fatal <- subset(df_error, df_error$SevereCompleted == 'FATAL')
df_2 <- subset(df_error, df_error$SevereCompleted == 2)

df_fatal$file <- as.character(df_fatal$file)
df_fatal$epjson <- paste(substr(df_fatal$file, 1, nchar(df_fatal$file)-7), '.epJSON', sep = '')

write.table(df_fatal$epjson,'fatal_error_files.csv',col.names = FALSE, row.names = FALSE, quote = FALSE)

df_sobol <- read.csv('sample_sobol_12-05.csv')
df_sobol <- cbind(df_ordered, df_sobol)  # from ehf.R
write.csv(df_sobol, 'dataset_12-17.csv', row.names = FALSE)

  df_sobol$compare <- NA

df_error$file <- as.character(df_error$file)
df_sobol$file <- as.character(df_sobol$file)

for(line in 1:nrow(df_sobol)){
  print(line)
  df_sobol$compare[line] <- ifelse(any(grepl(substr(df_sobol$file[line], nchar(df_sobol$file[line])-4,nchar(df_sobol$file[line])),df_error$file)), df_sobol$file[line], NA)
}

df_compare <- subset(df_sobol, !is.na(df_sobol$compare ))

df_final <- df_compare

df_final$real_zone_height <- 2.8+.4*df_final$zone_height
df_final$real_floor_height <- 15+15*df_final$floor_height
# df_final <- subset(df_final, df_final$real_floor_height/df_final$real_zone_height > 1)

df_final$zn_number <- (as.integer(df_final$real_floor_height/df_final$real_zone_height))*6+2

df_final$zn_number[df_final$room_type < .6] <- (as.integer(df_final$real_floor_height[df_final$room_type < .6]/df_final$real_zone_height[df_final$room_type < .6]))*6
df_final$zn_number[df_final$room_type < .2] <- (as.integer(df_final$real_floor_height[df_final$room_type < .2]/df_final$real_zone_height[df_final$room_type < .2]))*6+5
df_final$zn_number[df_final$room_type < -.2] <- (as.integer(df_final$real_floor_height[df_final$room_type < -.2]/df_final$real_zone_height[df_final$room_type < -.2]))*6+1
# df_final$zn_number[df_final$room_type < -.6] <- as.integer(real_floor_height/df_final$real_zone_height)*6+1

df_final <- df_final[!(df_final$ground > 0 & df_final$zn_number >= 6) & !(df_final$ground < 0 & df_final$zn_number < 6),]

write.csv(df_final, 'compare_ok.csv')
