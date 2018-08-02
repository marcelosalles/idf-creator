setwd('C:/Users/LabEEE_1-2/idf-creator/sa/')

df0 <- read.csv('sample0.csv')
df1 <- read.csv('sample1.csv')
df_lhs <- read.csv('lhs_sample.csv')

df_bldg <- cbind(df0, df_lhs)

df_room <- cbind(df1, 'wall' = c(rep('glass_1',nrow(df1)/3),rep('glass_2',nrow(df1)/3),rep('glass_3',nrow(df1)/3)))
#df_room <- cbind(df1, 'wall' = c(rep(0,nrow(df1)/3),rep(1,nrow(df1)/3),rep(2,nrow(df1)/3)))

# Pre-training data check ----

# Tratar df_bldg
df_bldg$wall_num[df_bldg$wall == 'wall_1'] <- 0
df_bldg$wall_num[df_bldg$wall == 'wall_2'] <- 1
df_bldg$wall_num[df_bldg$wall == 'wall_3'] <- 2

df_bldg$corr_vent_num[df_bldg$corr_vent == 'False'] <- 0
df_bldg$corr_vent_num[df_bldg$corr_vent == 'True'] <- 1

df_bldg$stairs_num[df_bldg$stairs == 'False'] <- 0
df_bldg$stairs_num[df_bldg$stairs == 'True'] <- 1

df_bldg$X.corr_vent. <- df_bldg$X.stairs. <- df_bldg$X.wall. <- NULL

# inicio

df <- df_room

# supply names of columns that have 0 variance

names(df[,apply(df, 2, var, na.rm=TRUE) == 0])

# exclude columns with zero variance

df <- df[,apply(df, 2, var, na.rm=TRUE) != 0]

library(Hmisc)
hist.data.frame(df)

library(summarytools)

descr(df, style = "rmarkdown")

dfSummary(df)

#correlation matrix

df.backup <- df

cor_matrix <- cor(df)

round(cor_matrix, 2)

#correlograms

library(corrplot)

corrplot(cor_matrix, type = "upper", order = "original", tl.col = "black", tl.srt = 45)



corrplot.mixed(cor_matrix, lower = "number", upper = "ellipse", tl.pos = "lt", 
               
               number.cex = 0.8, bg = "black")

#chart of correlation matrix

library("PerformanceAnalytics")

chart.Correlation(df, histogram=TRUE, pch=19)

