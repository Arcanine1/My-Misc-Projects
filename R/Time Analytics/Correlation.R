pacman::p_load(lars, caret)

#gets data
time <- read.csv("~/Desktop/Time.csv", row.names = 1)

#adds a time column
time$progress <- c(1:nrow(time)) 

 # for-loop over columns 
for(i in 1:(ncol(time) - 1)) {   
    #computes regression between time and the current column  
    linreg.lm <- lm(as.matrix(time[,i]) ~ time$progress)

    #gets col name
    colName <-  names(time)[i]
    print(colName)

    #gets slope
    slope <- coef(linreg.lm)[2]
    slope <- as.numeric(slope)
    print(round(slope,3))

    #gets r^2
    r2 <- summary(linreg.lm)$r.squared
    print(100*round(r2,3))
    cat("\n")


}