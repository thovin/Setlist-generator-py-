#This program imports lists of various ballroom dances
#and creates a .txt file containing a randomly generated setlist
import random

#Takes an input file and places its contents into a list of songs
def makeSongList(inputFileName):
	inputFile=open("%s"%inputFileName,"r")
	list=[]
	lines=inputFile.readlines()
	for i in range(len(lines)):
		lines[i]=lines[i].split(";")
		list.append(lines[i][0].strip())
	inputFile.close()
	return list

##Takes an input file and places its contents into a list of artists
def makeArtistList(inputFileName):
	inputFile=open("%s"%inputFileName,"r")
	list=[]
	lines=inputFile.readlines()
	for i in range(len(lines)):
		lines[i]=lines[i].split(";")
		list.append(lines[i][1].strip())
	inputFile.close()
	return list

#Randomly selects a song
def pickSongInList(lengthOfList):
	return random.randint(0,lengthOfList-1)

#Create lists of songs
waltz=makeSongList("waltzList.txt")
waltzArtists=makeArtistList("waltzList.txt")
chacha=makeSongList("chachaList.txt")
chachaArtists=makeArtistList("chachaList.txt")
tango=makeSongList("tangoList.txt")
tangoArtists=makeArtistList("tangoList.txt")
foxtrot=makeSongList("foxtrotList.txt")
foxtrotArtists=makeArtistList("foxtrotList.txt")
eastCoastSwing=makeSongList("ecsList.txt")
eastCoastSwingArtists=makeArtistList("ecsList.txt")
singleStepSwing=makeSongList("singleswingList.txt")
singleStepSwingArtists=makeArtistList("singleswingList.txt")
westCoastSwing=makeSongList("wcsList.txt")
westCoastSwingArtists=makeArtistList("wcsList.txt")
barnDance=makeSongList("barndanceList.txt")
barnDanceArtists=makeArtistList("barndanceList.txt")
lineDances=makeSongList("linedanceList.txt")
lineDancesArtists=makeArtistList("linedanceList.txt")

#Gets the length of the setlist from the user
numOfSongs=int(input("How many songs would you like in your setlist?\n"))
while numOfSongs>(len(waltz)+len(chacha)+len(tango)+len(foxtrot)+len(eastCoastSwing)+len(singleStepSwing)+len(westCoastSwing)+len(barnDance)+len(lineDances)):
	numOfSongs=int(input("Error: too few songs in library. Please select smaller number\n"))

#Generate lists for while loop. Used to eliminate song duplication,
#unless there are too few songs provided
count=0
setListSongs=[]
setListArtists=[]
oldWaltzNumbers=[]
oldChachaNumbers=[]
oldTangoNumbers=[]
oldFoxtrotNumbers=[]
oldECSNumbers=[]
oldSingleSwingNumbers=[]
oldWCSNumbers=[]
oldBarnDanceNumbers=[]
oldLineDanceNumbers=[]
oldRanNumbers=[]

#Main function
while count<numOfSongs:
	ranNum=random.randint(1,9)
	#Used to ensure a balanced variety of dances
	if len(oldRanNumbers)==9:
		oldRanNumbers=[]
	while ranNum in oldRanNumbers:
		ranNum=random.randint(1,9)
	oldRanNumbers.append(ranNum)
		
	
	if ranNum==1:
	#waltz
		oldNumbers=oldWaltzNumbers
		dance=waltz
		danceArtists=waltzArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldWaltzNumbers=oldNumbers
	elif ranNum==2:
	#chacha
		oldNumbers=oldChachaNumbers
		dance=chacha
		danceArtists=chachaArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldChachaNumbers=oldNumbers
	elif ranNum==3:
	#tango
		oldNumbers=oldTangoNumbers
		dance=tango
		danceArtists=tangoArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldTangoNumbers=oldNumbers
	elif ranNum==4:
	#foxtrot
		oldNumbers=oldFoxtrotNumbers
		dance=foxtrot
		danceArtists=foxtrotArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldFoxtrotNumbers=oldNumbers
	elif ranNum==5:
	#eastCoastSwing/ECS
		oldNumbers=oldECSNumbers
		dance=eastCoastSwing
		danceArtists=eastCoastSwingArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldECSNumbers=oldNumbers
	elif ranNum==6:
	#singleStepSwing/singleSwing
		oldNumbers=oldSingleSwingNumbers
		dance=singleStepSwing
		danceArtists=singleStepSwingArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldSingleSwingNumbers=oldNumbers
	elif ranNum==7:
	#westCoastSwing/WCS
		oldNumbers=oldWCSNumbers
		dance=westCoastSwing
		danceArtists=westCoastSwingArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldWCSNumbers=oldNumbers
	elif ranNum==8:
	#barnDance
		oldNumbers=oldBarnDanceNumbers
		dance=barnDance
		danceArtists=barnDanceArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldBarnDanceNumbers=oldNumbers
	else:
	#lineDance
		oldNumbers=oldLineDanceNumbers
		dance=lineDances
		danceArtists=lineDancesArtists
		if len(oldNumbers)==len(dance):
			oldNumbers=[]
		ranSongNum=pickSongInList(len(dance))
		if ranSongNum in oldNumbers:
			while ranSongNum in oldNumbers:
				ranSongNum=pickSongInList(len(dance))
		oldNumbers.append(ranSongNum)
		setListSongs.append(dance[ranSongNum])
		setListArtists.append(danceArtists[ranSongNum])
		oldLineDanceNumbers=oldNumbers
	count+=1

	
#Outputs generated setlist to a .txt file
outputFile=open("Setlist.txt","w")
for i in range(len(setListSongs)):
	outputFile.write(setListSongs[i]+";"+setListArtists[i]+"\n")
outputFile.close()
	