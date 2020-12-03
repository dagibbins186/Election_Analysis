file_to_load='Resources/12032020-election_results_DS.csv'
#Open the election results and read the file
with open(file_to_load) as election_data:
    #Perform analysis
    print(election_data)
#Close the file
election_data.close()