import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby("race").size().sort_values(ascending = False)

    # What is the average age of men?
    average_age_men = df.groupby('sex')['age'].mean().loc['Male']
    average_age_men=round(average_age_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.groupby('education')['education'].size().loc['Bachelors']/len(df.index)*100

    percentage_bachelors=round(percentage_bachelors,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    
    higher_education = df[df['education'].isin(["Bachelors","Masters","Doctorate"])]
    lower_education = df[df['education'].isin(["Bachelors","Masters","Doctorate"]) == False]

    # percentage with salary >50K
    higher_education_rich = len( higher_education[higher_education['salary']=='>50K'].index)/len(higher_education.index)*100
    higher_education_rich=round(higher_education_rich,1)
    lower_education_rich = len(lower_education[lower_education['salary']=='>50K'].index)/len(lower_education.index)*100
    lower_education_rich=round(lower_education_rich,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week']==min_work_hours]

    rich_percentage = len(num_min_workers[num_min_workers['salary']==">50K"].index)/len(num_min_workers.index)*100

    rich_percentage=round(rich_percentage,0)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_countries = df[df['salary']==">50K"].groupby("native-country").size()
    highest_earning_countries=list(zip(highest_earning_countries,highest_earning_countries.index))
    all_countries=df.groupby("native-country").size()
    all_countries=list(zip(all_countries,all_countries.index))

    c_p={"a":0}
    for h_earn,c_name in highest_earning_countries:
      all_earn=1
      for a_earn,cnameall in all_countries:
        if c_name==cnameall:
          all_earn=a_earn
          break
      c_p[c_name]=round(100*h_earn/all_earn,1)
        
        
    highest_earning_country=max(c_p, key=c_p.get)
    print(c_p)
      
    highest_earning_country_percentage=max(c_p.values())
      
    highest_earning_country_percentage=round(highest_earning_country_percentage,1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_top_earning_occupations = df.loc[(df['salary']==">50K") & (df['native-country']=="India")].groupby("occupation")["occupation"].size()
    top_IN_occupation=india_top_earning_occupations.index.values[india_top_earning_occupations.argmax(axis=0)]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
