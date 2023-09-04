Google Data Analytics Certificate Capstone (Bellabeat Case Study)
================
Gabriel Fernandez

``` r
# Set default options for code chunks
knitr::opts_chunk$set(
  echo = TRUE,          # Display R code and its output
  comment=NA,           # Suppress code comments in output
  warning = FALSE,      # Suppress warning messages
  fig.align='center',   # Align figures in the center
  eval = TRUE           # Evaluate R code
)
```

``` r
knitr::opts_chunk$set(
  echo = TRUE,
  comment=NA,
  warning = FALSE,
  fig.align='center',
  eval = TRUE
)
```

``` r
# Import libraries 
library(tidyverse) # includes ggplot2
library(skimr) #  provides a compact and informative summary of your dataframe or dataset
library(lubridate)
library(janitor) # set of utility functions for data cleaning and data frame tidying tasks
library(RColorBrewer) # Color palettes for data visualization
library(ggcorrplot) # Visualize correlation matrices using ggplot2
library(scales) # formatting and transforming data for visualizations
```

Let us clean:

- Change column names to lower case because R is case sensitive.

- Change “Id” from double to a character because the number represents a
  category.

- Change “ActivityDate” from char to date.

# heading 1

``` r
weight_logs <-
  read_csv("original_data/weightLogInfo_merged.csv",
    trim_ws = TRUE,
    show_col_types = FALSE
  )
```

## Heading 2

``` r
glimpse(weight_logs)
```

    Rows: 67
    Columns: 8
    $ Id             <dbl> 1503960366, 1503960366, 1927972279, 2873212765, 2873212…
    $ Date           <chr> "5/2/2016 11:59:59 PM", "5/3/2016 11:59:59 PM", "4/13/2…
    $ WeightKg       <dbl> 52.6, 52.6, 133.5, 56.7, 57.3, 72.4, 72.3, 69.7, 70.3, …
    $ WeightPounds   <dbl> 115.9631, 115.9631, 294.3171, 125.0021, 126.3249, 159.6…
    $ Fat            <dbl> 22, NA, NA, NA, NA, 25, NA, NA, NA, NA, NA, NA, NA, NA,…
    $ BMI            <dbl> 22.65, 22.65, 47.54, 21.45, 21.69, 27.45, 27.38, 27.25,…
    $ IsManualReport <lgl> TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, …
    $ LogId          <dbl> 1.462234e+12, 1.462320e+12, 1.460510e+12, 1.461283e+12,…

``` r
glimpse(weight_logs)
```

    Rows: 67
    Columns: 8
    $ Id             <dbl> 1503960366, 1503960366, 1927972279, 2873212765, 2873212…
    $ Date           <chr> "5/2/2016 11:59:59 PM", "5/3/2016 11:59:59 PM", "4/13/2…
    $ WeightKg       <dbl> 52.6, 52.6, 133.5, 56.7, 57.3, 72.4, 72.3, 69.7, 70.3, …
    $ WeightPounds   <dbl> 115.9631, 115.9631, 294.3171, 125.0021, 126.3249, 159.6…
    $ Fat            <dbl> 22, NA, NA, NA, NA, 25, NA, NA, NA, NA, NA, NA, NA, NA,…
    $ BMI            <dbl> 22.65, 22.65, 47.54, 21.45, 21.69, 27.45, 27.38, 27.25,…
    $ IsManualReport <lgl> TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, …
    $ LogId          <dbl> 1.462234e+12, 1.462320e+12, 1.460510e+12, 1.461283e+12,…

# References

### Guidelines and research articles

- 1.  Handling sedentary time: [A Comparison of Sedentary Behavior as
      Measured by the Fitbit and ActivPAL in College
      Students](https://www.mdpi.com/1660-4601/18/8/3914)

- 2.  Danger of prolong sitting(sedentary time): [Association of daily
      sitting time and leisure-time physical activity with body fat
      among U.S. adults. Journal of Sport and Health
      Science](https://www.sciencedirect.com/science/article/pii/S2095254622001016)

- 3.  [Dietary Guidelines for Americans,
      2020-2025](https://www.dietaryguidelines.gov/)

- 4.  [Physical Activity Guidelines for Americans (2nd
      ed.)](https://health.gov/sites/default/files/2019-09/Physical_Activity_Guidelines_2nd_edition.pdf)

### Links

- [Projects Datasets:](https://www.kaggle.com/datasets/arashnic/fitbit)

- [EDA guide](https://rpubs.com/jovial/r)

- Metadata: [Fitbit data
  dictionary](https://www.fitabase.com/resources/knowledge-base/exporting-data/data-dictionaries/)

- [Plotting histograms with
  ggplot2](https://appsilon.com/ggplot2-histograms/)

- [Histograms article](https://statisticsbyjim.com/basics/histograms/)

- [Error bars vs
  CI](https://blogs.sas.com/content/iml/2019/10/09/statistic-error-bars-mean.html)

- [Add density line to histogram](https://r-coder.com/density-plot-r)

- [Categorical, ordinal, interval,
  variables](https://www.graphpad.com/guides/prism/latest/statistics/the_different_kinds_of_variabl.htm)

### Appendix: Interesting sites for further investigation

- [Adult Physical Inactivity Prevalence Maps by
  Race/Ethnicity](https://www.cdc.gov/physicalactivity/data/inactivity-prevalence-maps/index.html#Race-Ethnicity)

- [Physical activity among adults aged 18 and over : United States,
  2020](https://stacks.cdc.gov/view/cdc/120213)
