pacman::p_load(dendextend)

#defines numbers of clusters
num <- 7

#reads in data
time <- read.csv("~/Desktop/Time.csv", row.names = 1)

#converts to dist
distance_time <- dist(time)

#creates cluster
hclust_time <- hclust(distance_time)

#converts to dendogran
dendo <- as.dendrogram(hclust_time)

#makes look good
hang.dendrogram(dendo)
dendo <- color_branches(dendo, k=num)
dendo <- color_labels(dendo,k=num)

#graphs
plot(dendo)
rect.dendrogram(dendo,k=num)