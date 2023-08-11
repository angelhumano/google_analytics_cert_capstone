# ---
# title: "Google Data Analytics Certificate Capstone (Bellabeat Case Study)"
# author: "Gabriel Fernandez"
# output:
#   github_document: default
#   
# toc: yes
# urlcolor: blue
#
#
# ---

# %%
# Set default options for code chunks
knitr::opts_chunk$set(
  echo = TRUE,          # Display R code and its output
  comment=NA,           # Suppress code comments in output
  warning = FALSE,      # Suppress warning messages
  fig.align='center',   # Align figures in the center
  eval = TRUE           # Evaluate R code
)



# %% name="setup"
knitr::opts_chunk$set(
  echo = TRUE,
  comment=NA,
  warning = FALSE,
  fig.align='center',
  eval = TRUE
)




# %% warning=false message=false
# Import libraries 
library(tidyverse) # includes ggplot2
library(skimr) #  provides a compact and informative summary of your dataframe or dataset
library(lubridate)
library(janitor) # set of utility functions for data cleaning and data frame tidying tasks
library(RColorBrewer) # Color palettes for data visualization
library(ggcorrplot) # Visualize correlation matrices using ggplot2
library(scales) # formatting and transforming data for visualizations



# %% [markdown]
# Let us clean:
#
# - Change column names to lower case because R is case sensitive.
#
# - Change "Id" from double to a character because the number represents a category.
#
# - Change "ActivityDate" from char to date.
#
#

# %%
weight_logs <-
  read_csv("original_data/weightLogInfo_merged.csv",
    trim_ws = TRUE,
    show_col_types = FALSE
  )
# %% [markdown]
#
#

# %%
glimpse(weight_logs)
# %% [markdown]
#
#

# %%
glimpse(weight_logs)
# %% [markdown]
# Observations:
#
# - Many variables show a right-skewed distribution: a larger number of data values are located on the left side of the curve.
#
# - The variables total_steps, total_distance, tracker_distance have a similar distribution. We can explore their correlations later.
#
# - Since the distributions are not normal. The median is a better indicator of central tendency for the numerical variables in these dataset.
#
# - **The variable "logged_activities_distance" and "sedentary_active_distance" might not provide useful information since most of the data points are zero. It seems that the users are not logging the distance frequently.**
#
# - The following variables seem related. We will explore them further in the bivariate analysis section:
#
#     - sedentary_minutes; sedentary_active_distance 
#     
#     - lightly_active_minutes; light_active_distance
#     
#     - fairly_active_minutes; moderately_active_distance
#     
#     - very_active_minutes; very_active_distance   
#
# - The variables calories and sedentary_minutes exhibit a multimodal distribution, indicating the presence of subpopulations within the data. In this dataset, gender could be a potential variable that would result in a bimodal distribution when examining histograms of calories and sedentary minutes. Unfortunately, the gender of the users is not provided, limiting our ability to confirm this hypothesis.