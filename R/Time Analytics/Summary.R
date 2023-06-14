pacman:: p_load("psych")

time <- read.csv("~/Desktop/Time.csv", row.names = 1)

printing <- describe(time)[c(3:6,8:9)]

print(printing)