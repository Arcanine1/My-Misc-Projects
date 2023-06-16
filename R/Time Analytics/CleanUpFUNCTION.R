# Function to combine two columns and remove the original columns
combiner <- function(time, colnew, col1, col2){
  time[colnew] <- time[col1] + time[col2]
  time <- time[, !(colnames(time) %in% c(col1, col2))]
  
    time
}

# Function to Clean up
CleanUp <- function(time) {

  # Combine "Internships..other." and "Palav" into "Internships"
  time <- combiner(time, "Internships", "Internships..other.", "Palav")

  # Combine "RW" and "hanging.out.with.friends" into "friends"
  time <- combiner(time, "friends", "RW", "hanging.out.with.friends")

  # Combine "FaceTime" and "Texting" into "OnlineSocial"
  time <- combiner(time, "OnlineSocial", "FaceTime", "Texting")

  # Combine "Family.Time..walking.etc." and "Golf.Dad.Sports" into "Family"
  time <- combiner(time, "Family", "Family.Time..walking.etc.", "Golf.Dad.Sports")

  # Combine "Technical.Projects" and "Other.Projects" into "projects"
  time <- combiner(time, "projects", "Technical.Projects", "Other.Projects")

   time
}