library(tidyverse)

path <- '/home/grzegorz/Pulpit/Projects/RaspberryPi/MoistureMeasurments/'

files = list.files(path)
files <- files[str_detect(files, 'txt')]
files <-str_c(path, files)

data <- map(files, read_csv) %>% map_dfr(.f = rbind)

data %>% 
  ggplot(aes(x=Timestamp, y = Moisture)) + 
  geom_point() + 
  theme_bw()
