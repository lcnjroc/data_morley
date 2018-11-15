import CSV
import numpy as np
import matplotlib.pylot as plt

# figure out what we wanna use
categories = [] # these are the column headers in the csv file
installs = [] # this is the installs row
ratings = [] # this is the ratings row

with open('data/googeplaystore.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		# move the page column headers out of the actual data to get a clean dataset
		if line_count is 0: #this will be text not data
			print('pushing categories into a seperate array')
			categories.append(row) #  push the text into this array
			line_count += 1 # increment the line count for the next loop
		else;
			# grab the ratings and push it into the ratings array
			ratingData = row[2]
			ratingData = ratingData.replace("NaN", "0")
			ratings.append(float(ratingData)) # int will turn a string (peice of text) into a number
		    # print('pushing ratings data into the ratings array')
			installData = row[5]
			installData = installData.replace(",", "") # get arid of the commas

			# get arid of the trailing +
			installs.append(np.char.strip(installData, "+"))
			line_count += 1

# get some values we can work with
# how many ratings are 4+?
# how many are below 2?
# how many are in the middle?
np_reviews = np.array(ratings) # turn a plain Python List into a Numpy array
popular_apps = no_ratings > 4
print('popular_apps:', len(popular_apps))

percent_popular = len(np_ratings[popular_apps]) / len(np_ratings) * 100
print("percent_popular")

unpopular_apps = np_ratings < 4
print("percent_unpopular", len(np_ratings[unpopular_apps]))

percent_unpopular = 100 - (np_ratings[unpopular_apps]) / len(np_ratings) * 100
print("percent_unpopular")

somewhat_popular = 100 - (percent_popular + percent_unpopular)
print("somewhat_popular")

# do a visualization with out new data
labels = "Sucks", "Meh", "Love it!"
sizes = [unpopular_apps, somewhat_popular, popular_apps]
colors = ['yellowgreen', 'lightgreen', 'lightskyblue']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=color, autopct='%1.1%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Do we love our apps?")
plt.xlabel("User Ratings - App Installs (10,000+ apps)")
plt.show()

# print ('processed', line_count, 'lines of data')
print(categories)
print('first row of data', installs [0])
print('last row of data', installs [-1])
