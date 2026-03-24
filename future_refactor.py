'''REFACTOR ZONE 
When I want to look at other cities, I'm going to need to come up with a procedure where when I load in a dataframe 
It follows a procedure where the name that the census uses is converted to something that's useful for me so that when I have these sheets that don't match keys I can find Columbus Ohio vs Columbus Georgia a different way '''

'''
cleaned_historic_dataframes[0].loc[:,'Foreign Key'] = cleaned_historic_dataframes[0]['Name'].str.extract(r'^(\w+-\w+|^\w+\s\w+)',expand=False)
print(cleaned_historic_dataframes[0])

pop_2010_2020.loc[:,'Foreign Key'] = pop_2010_2020['Geographic Area'].str.extract(r'^(\w+-\w+|^\w+\s\w+)',expand=False)
'''