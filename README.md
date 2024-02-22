# Spreadsheet Analysis
## Data set details
Released by Netflix, this dataset illustrates, for the first time in the streaming giant's history, what people watched on the platform over a six month period (Jan 2023 - June 2023). [Dataset Link: Netflix Engagement Report](https://about.netflix.com/en/news/what-we-watched-a-netflix-engagement-report)

This dataset was originally in a .XSLV file, so I downloaded the file and then exported it as a CSV. Here are the first 20 rows of my clean_data.csv:

The only problem I found in the original dataset was the missing data for a TV show's or film's release data. I solved this issue by simply replacing the empty slots with "NaN" indicators Additionally, I went ahead and divided the Hours Viewed column by 1,000,000 to get a better understanding of how big or small of an audience each Netflix TV series or film pulled. I also added a new column that illustrated if a title was a TV Show, however I could identify a group of Netflix's TV catalog because I used keywords like "Season" and "Temporada" which not all TV Shows had in their titles. There is without a doubt many more TV shows. Lastly, I changed the Release Date column to 'Premiere Year' to make comparing titles by date easier. To accomplish all of these tasks, I divided lines by those I could split with "," and those I could not due to a "," being in the title. Throughout this process, I had several errors where the added values would appear in between a title string or in between the hours viewed column. I largely fixed this by rewriting each line and going step by step to ensure that everything was being executed the way it was meant to.

Links to your data files (the original raw data, the munged data, and the spreadsheet file including the formulas and charts). These can be links to files in your own repository or links to the files stored in a cloud storage service if your files are too large to be included in your own repository.

URLS:

[Clean Data](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-dtuesta1/blob/main/data/clean_data.csv)

[Netflix CSV Data](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-dtuesta1/blob/main/data/netflix_data.csv)

[Excel Spreadsheet](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-dtuesta1/blob/main/data/netflix_spreadsheet.xlsx)


## Analysis:
###  Aggregate Statistics
- Average Hours Viewed (in 1M units) = 5.13 - This value represents the average number of hours all Netflix titles have amounted to over the six-month period. The result is 5.13 million and it provides a baseline understanding of the overall engagement on the platform throughout ALL titles.

- Max Hours Viewed (in 1M units) = 812.10 - On Netflix, the maximum number of hours a single title has been viewed is 812.10 million hours. This value demonstrates how popular Netflix title's can be. 

- Min Hours Viewed (in 1M units) = 0.10 - For a single title, the lowest amount of hours viewed is 0.1 million views, or 100,000 views which per Netflix was rounded up and there could be even smaller viewership for some titles on the platform. Indicates that not every title is popular or garners the same kind of attention as the rest.

- Min Premiere Year = 2010 - Identifies the oldest content being viewed on Netlfix. However, this is just the premiere year on Netflix, not the show's creation, and there were lots of missing data points for this category. 

###  Aggregate Statistics with Conditions
- Average Hours Viewed from 2021 Premiere Content: The average hours viewed for titles premiered in 2021 is 8.05 million hours. This reflects the popularity of content released in 2021.

- Average Hours Viewed from 2023 Premiere Content: The average hours viewed for titles premiered in 2023 is 52.14 million hours. The substantial increase in average hours viewed for 2023 released content demonstrates a possible trend towards higher viewership with more recent releases.

- Maximum Hours Viewed from 2010 Premiere Content: The maximum hours viewed for titles premiered in 2010 is 17.60 million hours. Despite being older, some 2010 content continue to attract high viewership, showcasing the longevity and demand for older titles. These titles hold a tremendous amount of value for Netflix, an example of this "Suits," the platforms most viewed show last year. 

- Average Hours Viewed if Available Globally: The average hours viewed for titles available globally is 10.66 million hours. Content available globally tend to have higher average viewership, indicating a broader appeal and accessibility.

- Average Hours Viewed if Not Available Globally: The average hours viewed for titles not available globally is 3.31 million hours. Titles with limited availability have lower average viewership, emphasizing the impact of global accessibility on content consumption.

### Chart
![Hours Viewed (in 1M units) by Global Availability and Premiere Run](/data/Chart.png)
- The chart above reveals that, typically and not always, titles that are not available globally pull sligtly higher viewership than those that are available globally. This is especially true in 2011, where the average viewership was much much higher in titles that were not available globally. This could signal that titles that aren't available globally  appeal and entertain local audiences much more than titles for global release. Another explanation could be the presence of a highly popular regional content during that year.

- From 2011 to 2019, titles not available globally have tredded downward while those available globally remained stagnant. 

- On the other hand, the immense difference average hours viewed for 2023 titles, with 57.44 million hours for globally available and 26.86 million hours for not globally available, emphasizes the impact of global reach on viewership.


