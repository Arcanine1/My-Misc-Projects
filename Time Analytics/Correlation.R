#PURPOSE: Output the correlation between each variable and time

pacman::p_load(lars, caret)

#gets data
source("Time Analytics/importFUNCTION.R")
time<- importAndCleanData()

#adds a time column
time$progress <- c(1:nrow(time)) 

 # for-loop over columns 
for(i in 1:(ncol(time) - 1)) {   
    #computes regression between time and the current column  
    linreg.lm <- lm(as.matrix(time[,i]) ~ time$progress)

    #prints col name
    colName <-  names(time)[i]
    print(colName)

    #prints slope
    slope <- coef(linreg.lm)[2]
    slope <- as.numeric(slope)
    print(round(slope,3))

    #prints r^2
    r2 <- summary(linreg.lm)$r.squared
    print(100*round(r2,3))
    cat("\n")


}