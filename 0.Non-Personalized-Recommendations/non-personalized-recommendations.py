import numpy as np

global ratings
global ratings_4
global movies
global n_users
global users

def get_number_of_users():
    file = open('./ml-1m/ratings.dat', 'r')
    users = {}
    for line in file:
        arr = line.split("::")
        users[arr[0]] = arr[1]
    file.close()
    return len(users), users

def process_ratings_4(filename):
    file = open(filename, 'r')
    ratings_4 = {}
    for line in file:
        arr = line.split("::")
        if int(arr[2]) >= 4:
            if arr[1] in ratings_4:
                ratings_4[arr[1]].append(arr[0])
            else:
                ratings_4[arr[1]] = [arr[0]]
    file.close()
    return ratings_4

def process_ratings(filename):
    file = open(filename, 'r')
    ratings = {}
    for line in file:
        arr = line.split("::")
        if arr[1] in ratings:
            ratings[arr[1]].append(arr[2])
        else:
            ratings[arr[1]] = [arr[2]]
    file.close()
    return ratings

def process_movies(filename):
    file = open(filename, 'r', encoding="latin-1")
    movies = {}
    for line in file:
        arr = line.split("::")
        movies[arr[0]] = arr[1]
    file.close()
    return movies

#Function that makes a list with all the ratings of all the movies
def get_all_ratings():
    all_ratings = []
    for movie in ratings:
        for r in ratings[movie]:
            all_ratings.append(r)
    return all_ratings

def calculate_simple_association(movieX, movieY):
    ratX = ratings[movieX]
    ratY = ratings[movieY]

    union = list(filter(lambda x: x in ratX, ratY))
    return len(union) / len(ratX)

def calculate_advanced_association(movieX, movieY):
    ratX = ratings[movieX]
    ratY = ratings[movieY]

    all_ratings = get_all_ratings()
    diff = list(filter(lambda x: x in ratX, all_ratings))
    union = list(filter(lambda x: x in ratY, diff))
    not_ratX = n_users - len(ratX)

    return calculate_simple_association(movieX, movieY)/(len(union)/not_ratX)

def get_top_n_simple_association(movieX, n):
    top_n = []
    for movie in ratings:
        if movie != movieX:
            top_n.append((movie, calculate_simple_association(movieX, movie)))
    top_n.sort(key=lambda tup: tup[1], reverse=True)
    return [x[0] for x in top_n[:n]], top_n[:n]

def get_top_n_advanced_association(movieX, n):
    top_n = []
    for movie in ratings:
        if movie != movieX:
            top_n.append((movie, calculate_advanced_association(movieX, movie)))
    top_n.sort(key=lambda tup: tup[1], reverse=True)
    return [x[0] for x in top_n[:n]] , top_n[:n]


def get_top_n_movies(n):
    top_n = []
    for movie in ratings:
        top_n.append((movie, len(ratings[movie])))
    top_n.sort(key=lambda tup: tup[1], reverse=True)
    return [x[0] for x in top_n[:n]], top_n[:n]

def get_top_n_movies_4(n):
    top_n = []
    for movie in ratings_4:
        top_n.append((movie, len(ratings_4[movie])))
    top_n.sort(key=lambda tup: tup[1], reverse=True)
    return [x[0] for x in top_n[:n]], top_n[:n]

ratings_4 = process_ratings_4('./ml-1m/ratings.dat')
ratings = process_ratings('./ml-1m/ratings.dat')
movies = process_movies('./ml-1m/movies.dat')
n_users, users = get_number_of_users()

print("Question 1, simple association of MovieID's 1 and 1064 = {}".format(calculate_simple_association('1', '1064')))
print("\n")
print("Question 2, advanced association of MovieID's 1 and 1064 = {}".format(calculate_advanced_association('1', '1064')))
print("\n")
print("Question 4, simple association of MovieID's 1 and 2858 = {}".format(calculate_simple_association('1', '2858')))
print("\n")
print("Question 7, advanced association of MovieID's 1 and 2858 = {}".format(calculate_advanced_association('1', '2858')))
print("\n")
q9,_ = get_top_n_movies(10)
titles = list(map(lambda x: movies[x], q9))
n_users = sum(list(map(lambda x: len(ratings[x]), q9)))
print("Question 9, top 10 movies = MovieID's:{}, Nº Reviews: {}, Titles:{}".format(q9,n_users,titles)) 
print("\n")
id,q10 = get_top_n_simple_association('3941', 5)
titles = list(map(lambda x: movies[x], id))
print("Question 10, top 5 associations of MovieID 3941 = {} , with titles: {}".format(q10, titles))  
print("\n")
id,q11 = get_top_n_advanced_association('3941', 5)
titles = list(map(lambda x: movies[x], id))
print("Question 11, top 5 advanced associations of MovieID 3941 = {} , with titles: {}".format(q11, titles))
print("\n")
q14,_ = get_top_n_movies_4(10)
titles = list(map(lambda x: movies[x], q14))
n_users = sum(list(map(lambda x: len(ratings_4[x]), q14)))
print("Question 14, top 10 movies = MovieID's:{}, Nº Reviews: {}, Titles:{}".format(q14,n_users,titles)) 