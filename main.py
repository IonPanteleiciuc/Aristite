from fonctions import *
import time
start_time = time.time()

# Create the object

mape ={
    "h11": 1,
    "h12": 2,
    "h13": 3,

    "h21": 4,
    "h22": 5,
    "h23": 6,
    "h24": 7,

    "h31": 8,
    "h32": 9,
    "h33": 10,
    "h34": 11,
    "h35": 12,

    "h41": 13,
    "h42": 14,
    "h43": 15,
    "h44": 16,

    "h51": 17,
    "h52": 18,
    "h53": 19
}

while not(somme_1(mape) and somme_2(mape) and somme_3(mape)):
    #somme_1(mape)
    remplir1(mape)
    print("Jeu : ", mape)

print("YES ! : ", mape.values())
print("--- %s seconds ---" % (time.time() - start_time))
