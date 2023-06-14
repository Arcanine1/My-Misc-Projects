time <- read.csv("~/Desktop/Time.csv", row.names = 1)

pc <- prcomp(time)

summary(pc)

biplot(pc)
