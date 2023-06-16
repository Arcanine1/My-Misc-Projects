source("CleanUpFUNCTION.R")

#gets data
time <- read.csv("~/Desktop/Time.csv", row.names = 1)

#merges data
time <- CleanUp(time)

#converts to principal components
pc <- prcomp(time)

#shows principal components
summary(pc)

#shows biplot
biplot(pc)
