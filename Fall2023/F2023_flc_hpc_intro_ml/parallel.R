# https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/parallel.html
# Load libraries
library(parallel)
library(lme4)

# Get the number of available cores
detectCores()

# Define the function
f <- function(i) {
  lmer(Petal.Width ~ . - Species + (1 | Species), data = iris)
}

# Use a subset of the iris dataset for demonstration purposes
dataset <- iris

# Serial computation
system.time(save1 <- lapply(1:100, f))

# Perform parallel computation
system.time(save2 <- mclapply(1:1500, f, mc.cores = 8))
