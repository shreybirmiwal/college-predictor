
# CollegePredictor

Data analysis and modeling were performed on a large dataset of students applying to college. Interesting correlations and predictive models created.



## Methodology

#### 1. Finding a Dataset

The popular subreddit, r/collegeresults includes many posts of high school students with the stats and college acceptances/rejections. Here is a screenshot of a post:

![image](https://github.com/user-attachments/assets/a88de724-cb49-41bc-a1b6-ea6d232d4aad)

You can see how it is very useful data that we can extract.


#### 2. Gathering Dataset
I first tried web scraping the data using the selenium web driver. This took a long time and was unsuccessful. I next tried the Reddit API, however, this only had record of the 1000 most recent posts. Next, I tried the pushshift API, however this was currently broken. Lastly, I used the Reddit dump files and artic shift, which you can find here:

https://www.reddit.com/r/pushshift/comments/1akrhg3/separate_dump_files_for_the_top_40k_subreddits/

The code used to process this is here: 1-DataPrep\1-data-collect-artic-shift

#### 3. Extracting Features

The data from Reddit was not clean and organized. It came in paragraph form.
I opted to use Regex in order to extract data, such as ````r"(?:Hooks \(Recruited Athlete, URM, First-Gen, Geographic, Legacy, etc.\)|Hooks):\s*(.*)"````.

At the end of this processing, we had a CSV file that looked like this:

![image](https://github.com/user-attachments/assets/96154dfa-667b-48d0-bda5-86654d360d74)

The code for this can be found here: 1-DataPrep/3-extract-values


#### 4. Standardizing Features

After step 3, we had a dataset, however each value was different. For example, in the 'Gender' column, there was: "Guy" "dude" "Dude" "male" "Male" "man" and "BOY" just for Males alone. In addition, the RANK, GPA, and SAT, had to be processed

At the end of processing (code found here: 1-DataPrep\5-encode-data), a ready to use CSV file was created, as shown below:
![image](https://github.com/user-attachments/assets/5e95cc06-310b-4d11-b5fa-98c6a0d73442)


#### 5. Data Analysis

1. First, I performed basic data analysis on each university by extracting the following features:
* Total Applications
* Acceptances, Waitlists, Rejections
* Average [Accepted, Waitlist, Reject] [SAT, Extra Curricular, Essays]

![image](https://github.com/user-attachments/assets/6b590142-456a-49ff-b2cc-15f69d373c8f)
Above are the columns generated

2. Second, I extracted correlations between numerical features using a correlation matrix. You can view the matrix plot in the 2-visualize/res folder

![HARVARD Correlation Matrix](https://github.com/user-attachments/assets/b9f43844-1af8-4061-8923-32de7b1dc4ca)
Above is a correlation matrix from Harvard

3. Third, I extracted the correlations between categorical features by using a statistical chi^2 test. I only compared each feature against the target (desicion)

![image](https://github.com/user-attachments/assets/a48ff98c-1844-4684-8dad-fe14fd7e8495)
Above are the columns generated of the p-values for each categorical feature

4. Fourth, I used partial dependency plots in order to see how each feature affects the decision. 

![image](https://github.com/user-attachments/assets/05bc95da-ab99-4ff4-bac8-644d7ef79390)
Above is an example PDP from USCS. You can see how higher essays, SAT, and extracurriculars are dependent (correlated) with a positive decision outcome.


5. Fifth, I performed PCA and created an ML model trained on the data
Since many of the features are not linear (for example State), I opted for Random Forest Classifier. For each school, the accuracy differed between 21% and 94%. Many of the schools where above 65%, proving that it is indeed possible to train a machine learning model and predict admissions outcomes. It leaves us with a question, do colleges make admission decisions using AI?

![image](https://github.com/user-attachments/assets/8f182d6c-613a-46c0-8e1e-8464033d1d48)

Above is an interesting image after conducting PCA on a dataset of MIT applications. It is clear a difference between accepted and denied students, furthering my claim that students can be differianted by a computer just solely by self reported grades, demographics, and essays.


## Interesting Findings

I posted these on my Twitter, which you can find here: https://x.com/shreybirmiwal/status/1819460900346384763

### #1 The SAT score doesn't "really" matter
According to the feature importance table (generated after creating a random forest model), most schools only value the SAT by about 16%. On the high end, UT-Dallas values SAT at about 39%.

![image](https://github.com/user-attachments/assets/9cac1898-6262-4875-afb5-112bd2b7d7cd)

Furthermore, after a certain point (SAT above ~1500), it does not matter. A 1520 vs a 1540 is negligible in the eyes of a college admission. The partial dependency plots for USCS show a decrease in SAT-acceptance dependence/correlation when SAT is above ~1550.

### #2 The ivies care about hooks

The graph below shows the log inverse of the p-value of a chi-squared test between hooks (legacy, minorities, etc) and decision

![image](https://github.com/user-attachments/assets/ec24a0ed-0cf8-4704-b038-5390d06cdd69)

It is clear of a statistically significant correlation between Hooks and decision

### #3 Top schools have top SAT. Is it correlation?
No surprise that the top schools have an average SAT very high:
![image](https://github.com/user-attachments/assets/3bafba1b-4018-44ac-9d99-0b4a4babc318)

Is this correlation and not causation? I think not correlation:
![image](https://github.com/user-attachments/assets/3007dbe2-04a8-4bfe-a06a-8ab7483f364d)

Notice in the image above Caltech correlation matrix shows a 30% correlation between SAT and extracurriculars. A high SAT likely means you try very hard and have good essays, extracurriculars, recommendations, etc.

### #4 Higher income means better college outcomes

Take another look at the correlation matrix from #3. 
Income was:
* correlated 29% with better essays,
* correlated 15% with better extracurriculars
* correlated 12% with higher SAT

I suspect, higher income means better tutors, more internships and research, and more essay reviews.

### #5 It does matter what major you apply for
![image](https://github.com/user-attachments/assets/fb3862c1-8dce-4b23-be65-044dcf252033)
UT-Austin has some majors guaranteed acceptance if you are top 6% of the class, but not all majors such as engineering. This is why we see UT heavily considers major, and Yale, GTech, etc hardly does so. It is evident by the high log inverse p-value of major against decision.

### #6 You can get into a state school even if you don't live in that state
![image](https://github.com/user-attachments/assets/c53bc958-841d-4c90-9c69-ffdae58ebe8c)
The avg. log inverse p-value for residence is:
* 3.25 for public schools 
* 1.48 for private schools:

Only a 2.19X difference - not as crazy as people make it seem. Some schools actually have equal preferences.





## Acknowledgements

Thanks for reading! I learned a lot about statistics, data processing, regex, feature engineering, correlations and data analysis, and machine learning modeling with random forests!
