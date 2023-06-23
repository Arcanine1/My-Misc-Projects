#PURPOSE: Creates Summary Statistics

pacman:: p_load("psych")

#gets data
source("Time Analytics/importFUNCTION.R")
time<- importAndCleanData()

#gets stats I want
printing <- describe(time)[c(3:6,8:9)]

print(printing)

head(printing)

#prints a pie chart

pie(printing$mean, labels = row.names(printing), col = rainbow(nrow(printing)), cex = .7)
