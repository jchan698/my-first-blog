
# list of city names (in Afghanistan)
 cities <- structure(list(city = structure(c(1L, 3L, 4L, 5L, 2L), 
                                          .Label = c("Gereshk", "Lahkar Gah", "Lashkar Gah", "Marjah", "Nad-e Ali"), class = "factor")), 
                    .Names = "city", row.names = c(NA, -5L), class = "data.frame")

#your list of city names

setwd('C:/Users/Janice/Downloads')
csv.data <- read.csv("1%.csv")


 
 
library(geonames)
 
# conveninence function to look up and format results
GNsearchAF <- function(x) {
  res <- GNsearch(name=x, country="AF")
  return(res[1, ])
}

# loop over city names and reformat
GNresult <- sapply(cities, GNsearchAF)
GNresult <- do.call("rbind", GNresult)
GNresult <- cbind(city=row.names(GNresult), 
                  subset(GNresult, select=c("lng", "lat", "adminName1")))