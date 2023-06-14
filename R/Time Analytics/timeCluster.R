time <- read.csv("~/Desktop/Time.csv", row.names = 1)

distance_time <- dist(time)

hclust_time <- hclust(distance_time)

plot(hclust_time)
