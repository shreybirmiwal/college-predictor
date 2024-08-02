
# CollegePredictor

Data analysis and modeling performed on a large dataset of students applying to college. Interesting correlations and predictive models created.



## Methodology

#### 1. Finding a Dataset

The popular subreddit, r/collegeresults includes many posts of highschool students with the stats and college acceptances/rejections. Here is a screenshot of a post:

![image](https://github.com/user-attachments/assets/a88de724-cb49-41bc-a1b6-ea6d232d4aad)

You can see how it is very useful data that we can extract.


#### 2. Gathering Dataset
I first tried webscraping the data using selenium webdriver. This took a long time and was unsuccesful. I next tried the reddit API, however this only had reccord of the 1000 most recent posts. Next, I tried the pushshift API, however this was currently broken. Lastly, I used the reddit dump files and artic shift, which you can find here:

https://www.reddit.com/r/pushshift/comments/1akrhg3/separate_dump_files_for_the_top_40k_subreddits/

The code used to process this is here: 1-DataPrep\1-data-collect-artic-shift

#### 3. Extracting Features

The data from reddit was not clean and organized. It came in paragraph form.
I opted to use Regex in order to extract data, such as ````r"(?:Hooks \(Recruited Athlete, URM, First-Gen, Geographic, Legacy, etc.\)|Hooks):\s*(.*)"````.

At the end of this processing, we had a CSV file that looks like this:

![image](https://github.com/user-attachments/assets/96154dfa-667b-48d0-bda5-86654d360d74)

The code for this can be found here: 1-DataPrep/3-extract-values


#### 4. Standarizing Features

After step 3, we had a dataset, however each value was different. For example, in the 'Gender' column, there was: "Guy" "dude" "Dude" "male" "Male" "man" "BOY" just for Male alone. In addition, the RANK, GPA, SAT, had to be processed

At the end of processing (code found here: 1-DataPrep\5-encode-data), a ready to use csv file was created, as shown below:
![image](https://github.com/user-attachments/assets/5e95cc06-310b-4d11-b5fa-98c6a0d73442)

