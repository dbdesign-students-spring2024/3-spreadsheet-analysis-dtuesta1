# Spreadsheet Analysis
## Data set details
Released by Netflix, this dataset illustrates, for the first time in the streaming giant's history, what people watched on the platform over a six month period (Jan 2023 - June 2023). [https://about.netflix.com/en/news/what-we-watched-a-netflix-engagement-report](Dataset Link: Netflix Engagement Report).

This dataset was originally in a .XSLV file, so I downloaded the file and then exported it as a CSV. Here are the first 20 rows of my clean_data.csv:

The only problem I found in the original dataset was the missing data for a TV show's or film's release data. I solved this issue by simply replacing the empty slots with "NaN" indicators Additionally, I went ahead and divided the Hours Viewed column by 1,000,000 to get a better understanding of how big or small of an audience each Netflix TV series or film pulled. I also added a new column that illustrated if a title was a TV Show, however I could identify a group of Netflix's TV catalog because I used keywords like "Season" and "Temporada" which not all TV Shows had in their titles. There is without a doubt many more TV shows. Lastly, I changed the Release Date column to 'Premiere Year' to make comparing titles by date easier. To accomplish all of these tasks, I divided lines by those I could split with "," and those I could not due to a "," being in the title. Throughout this process, I had several errors where the added values would appear in between a title string or in between the hours viewed column. I largely fixed this by rewriting each line and going step by step to ensure that everything was being executed the way it was meant to.

Links to your data files (the original raw data, the munged data, and the spreadsheet file including the formulas and charts). These can be links to files in your own repository or links to the files stored in a cloud storage service if your files are too large to be included in your own repository.



Analysis: