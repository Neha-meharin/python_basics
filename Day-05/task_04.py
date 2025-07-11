
movies=[]
i=0
while i<2:
   y=input("enter movie")
   rate=int(input("rate each movie"))
   movies.append((y,rate))
   i=i+1;
print("Your movies and ratings:")
print(movies)
n = len(movies)
for i in range(n):
    for j in range(0, n - i - 1):
        if movies[j][1] < movies[j + 1][1]:
            movies[j], movies[j + 1] = movies[j + 1], movies[j]
print("sOrted movie on rating",movies)
greatest = movies[0]
for i in range(1, n):
    if movies[i][1] > greatest[1]:
        greatest = movies[i]
print("movie with gretest rating is",greatest)

lowest = movies[0]

for i in range(1, n):
    if movies[i][1] < lowest[1]:
        lowest = movies[i]
print("movie with lowestt rating is",lowest)
