pacman:: p_load("psych")

#reads data
time <- read.csv("~/Desktop/Time.csv", row.names = 1)

#gets stats I want
printing <- describe(time)[c(3:6,8:9)]

#output
print(printing)