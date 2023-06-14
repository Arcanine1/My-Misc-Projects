#gets data
time <- read.csv("~/Desktop/Time.csv", row.names = 1)

#converts to principal components
pc <- prcomp(time)

#shows principal components
summary(pc)

#shows biplot
biplot(pc)
