### Summery 
###### This project is simple project to test pandas library. 

### Used IDE 
###### Pycharm from jetbrains 

---

### Project description 
###### This project consumes two Covid-19 data files : time_series_covid_19_confirmed_US.csv and time_series_covid_19_deaths_US.csv and calculate the death % each day. 

### Project Data source 
###### I used public data set from Kaggle. The data is a daily confirmed case and death case of Covid-19. ﻿﻿﻿﻿﻿There are columns of each day. I used these two data sets and calculated the death %  by dividing the death case by a confirmed case. To handle the NaN case ( divide by 0), 
###### I mapped the confirmed case to 1 for 0. It's done since it doesn't affect the % value. 

----
### Source 
##### raw data is located under data/raw folder 

### Output 
###### The output of the project is .csv file will be written in data/processed 

### Execution 
###### Code can be executed either using notebook or python file. 