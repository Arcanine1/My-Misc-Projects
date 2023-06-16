pacman:: p_load("psych")

source("CleanUpFUNCTION.R")

#gets data
time <- read.csv("~/Desktop/Time.csv", row.names = 1)

#merges data
time <- CleanUp(time)

#gets stats I want
printing <- describe(time)[c(3:6,8:9)]

#output
print(printing)