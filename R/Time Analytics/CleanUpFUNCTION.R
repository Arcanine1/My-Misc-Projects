# Function to combine two columns and remove the original columns
combiner <- function(data, colnew, col1, col2){
  data[colnew] <- data[col1] + data[col2]
  data <- data[, !(colnames(data) %in% c(col1, col2))]
  
    data
}

# Function to Clean up
#inputs and outputs data
CleanUp <- function(data) {

  data <- combiner(data, "Internships", "Internships..other.", "Palav")

  data <- combiner(data, "friends", "RW", "hanging.out.with.friends")

  data <- combiner(data, "OnlineSocial", "FaceTime", "Texting")

  data <- combiner(data, "Family", "Family.Time..walking.etc.", "Golf.Dad.Sports")

  data <- combiner(data, "projects", "Technical.Projects", "Other.Projects")

   data
}
