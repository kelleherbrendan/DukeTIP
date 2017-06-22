from numpy import *

########################################################
# These functions will be used in Phase 3 (skip for now)
########################################################

def findSimilar(iLike, userLikes):
    # Create an And similarity
    similarityAnd = 0 # replace 0 with the correct code
    # Create a per user sum
    similaritySum = 0 # replace 0 with the correct code
    # Create an Or similarity
    userSimilarityOr = 0 # replace 0 with the correct code

    # Calculate the similarity
    userSimilarity = 0 # replace 0 with the correct code to calculate the Jaccard Index for each user

    # Make the most similar user has a new like that the previous user did not have
    # I used a while loop.
    # You can "get rid" of a user that is most similar, but doesn't have any new likes
    # by setting the userSimilarity for them to 0
    # When you get the index, save it in the variable maxIndex

    # Print the max similarity number (most times this is something like 0.17

    # Return the index of the user which is the best match
    return maxIndex
    
def printMovie(id):
    # Print the id of the movie and the name.  This should look something like
    # "    - 430: Duck Soup (1933)" if the id is 430 and the name is Duck Soup (1933)
    print(0) # replace 0 with the correct code

def processLikes(iLike):
    print("\n\nSince you like:")
    
    # Print the name of each movie the user reported liking
    # Hint: Use a for loop and the printMovie function.

    # Convert iLike into an array of 0's and 1's which matches the array for other users
    # It should have one column for each movie (just like the userLikes array)
    # Start with all zeros, then fill in a 1 for each movie the user likes
    iLikeNp = 0 # replace 0 with the code to make the array of zeros
    # You'll need a few more lines of code to fill in the 1's as needed

    # Find the most similar user
    user = 0 # replace 0 with the correct code (hint: use one of your functions)
    print("\nYou might like: ")
    # Find the indexes of the values that are ones
    # https://stackoverflow.com/a/17568803/3854385 (Note: You don't want it to be a list, but you do want to flatten it.)
    recLikes = 0 # replace 0 with the needed code

    # For each item the similar user likes that the person didn't already say they liked
    # print the movie name using printMovie (you'll also need a for loop and an if statement)

########################################################
# Begin Phase 1
########################################################

# Load Data
movieNames = loadtxt("./movieData/u.item", dtype={
    'names': ('id', 'name'),
    'formats': ('int', 'S128')}, delimiter="|", usecols=(0, 1))
movieDict = dict(zip(movieNames['id'], movieNames['name']))
movieData = loadtxt("./movieData/u.data", dtype={
    'names': ('user', 'movie', 'rating'),
    'formats': ('int', 'int', 'int')}, usecols=(0, 1, 2))

########################################################
# Begin Phase 2
########################################################

# Gather ratings for each movie
movieRatingTemp = {}
for i in range(len(movieData)):
    if movieData[i]['movie'] not in movieRatingTemp:
        movieRatingTemp[movieData[i]['movie']] = []
        movieRatingTemp[movieData[i]['movie']].append(movieData[i]['rating'])
    else:
        movieRatingTemp[movieData[i]['movie']].append(movieData[i]['rating'])

# Get average movie ratings and number of ratings per movie
movieRating = {}
movieRatingCount = {}
for movieID in movieRatingTemp:
    movieRatingCount[movieID] = len(movieRatingTemp[movieID])
    movieRating[movieID] = mean(movieRatingTemp[movieID])

# Get sorted ratings
movieRatingS = [(k, movieRating[k]) for k in sorted(movieRating, key=movieRating.get, reverse=True)]

# Top 10 Movies
print("Top Ten Movies:")
for a in range(10):
    print(str(a+1) + '. ' +
          str(movieDict[movieRatingS[a][0]]) +
          ' (ID: ' + str(movieRatingS[a][0]) +
          ') Rating: ' + str(movieRatingS[a][1]) +
          ' Count: ' + str(movieRatingCount[movieRatingS[a][0]]))

# Top 10 Movies with at least 100 ratings    
print("\n\nTop Ten movies with at least 100 ratings:")
a = 0
b = 0
while a < 10:
    if movieRatingCount[movieRatingS[b][0]] >= 100:
        print(str(b + 1) + '. ' +
              str(movieDict[movieRatingS[b][0]]) +
              ' (ID: ' + str(movieRatingS[b][0]) +
              ') Rating: ' + str(movieRatingS[b][1]) +
              ' Count: ' + str(movieRatingCount[movieRatingS[b][0]]))
        a += 1
    b += 1

########################################################
# Begin Phase 3
########################################################

# Create a user likes numpy ndarray so we can use Jaccard Similarity
# A user "likes" a movie if they rated it a 4 or 5
# Create a numpy ndarray of zeros with demensions of max user id + 1 and max movie + 1 (because we'll use them as 1 indexed not zero indexed)

maxMovie = movieData['movie'].max() + 1
maxUser = movieData['user'].max() + 1
userLikes = zeros((maxUser, maxMovie))

# Go through all the rows of the movie data.
# If the user rated a movie as 4 or 5 set userLikes to 1 for that user and movie
# Note: You'll need a for loop and an if statement
# user = rows/arrays, movie = column

print(movieData)

exit(0)

for a in range(maxUser):
    if movieData[a]['rating'] >= 4:
        userLikes[a][] = 1
# if rating >= 4:
    # array[user][movie] = 1

########################################################
# At this point, go back up to the top and fill in the
# functions up there
########################################################

# First sample user
# User Similiarity: 0.133333333333
iLike = [655, 315, 66, 96, 194, 172]
processLikes(iLike)

# What if it's an exact match? We should return the next closest match
# Second sample case
# User Similiarity: 0.172413793103
iLike = [79,  96,  98, 168, 173, 176, 194, 318, 357, 427, 603]
processLikes(iLike)

# What if we've seen all the movies they liked?
# Third sample case
# User Similiarity: 0.170731707317
iLike = [79,  96,  98, 168, 173, 176, 194, 318, 357, 427, 603, 1]
processLikes(iLike)

# If your code completes the above recommendations properly, you're ready for the last part,
# allow the user to select any number of movies that they like and then give them recommendations.
# Note: I recommend having them select movies by ID since the titles are really long.
# You can just assume they have a list of movies somewhere so they already know what numbers to type in.
# If you'd like to give them options though, that would be a cool bonus project if you finish early.
