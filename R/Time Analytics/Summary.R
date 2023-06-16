#PURPOSE: Creates Summary Statistics

pacman:: p_load("psych")

#gets data
source("importFUNCTION.R")
time<- importAndCleanData()

#gets stats I want
printing <- describe(time)[c(3:6,8:9)]

print(printing)