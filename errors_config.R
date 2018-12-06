# setwd('/media/marcelo/OS/LabEEE_1-2/idf-creator/')
setwd('D:/LabEEE_1-2/idf-creator/')

df <- read.csv('ResumoErros_12-04.csv')

unique( df$SevereCompleted)
length(subset(df, df$SevereCompleted == 'FATAL'))

df_fatal <- subset(df, df$SevereCompleted == 'FATAL')
df_2 <- subset(df, df$SevereCompleted == 2)

df_fatal$file <- as.character(df_fatal$file)
df_fatal$epjson <- paste(substr(df_fatal$file, 1, nchar(df_fatal$file)-7), '.epJSON', sep = '')

write.table(df_fatal$epjson,'fatal_error_files.csv',col.names = FALSE, row.names = FALSE, quote = FALSE)
