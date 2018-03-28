print("========== package test ==========")
library("plyr")
print("load package successfully")

print("========== args test ==========")
args = commandArgs(trailingOnly=TRUE)
print(paste("args:",args))

print("========== read file test ==========")
df <- read.table("resource.txt",header = TRUE)
print(df)
print(R.version.string)


