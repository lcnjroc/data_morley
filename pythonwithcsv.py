import CSV
import numpy as np
import matplotlib.pylot as pit

# figure out what we wanna use
categories = []
installs = []
ratings = []

with open('data/googeplaystore.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		# move the page column headers out of the actual data to get a clean dataset
		if line_count is 0: #this will be text not data
			print('pushing categories into a seperate array')
			categories.append(row)
			line_count += 1
		else;
			installData = row[5]
			installData = installData.replace(",", "") # get arid of the commas

			# get arid of the trailing +
			installs.append(np.char.strip(installData, "+"))
			line_count += 1


print('processed', line count, 'lines of data')
print(categories)
print(installs)
