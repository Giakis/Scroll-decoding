import random

#Συνάρτηση που υλοποιούνται οι ολισθήσεις
def swap(lst , n):
    return lst[n : ] + lst[ : n]


#Δημιουργεία 16-bit τυχαίου αριθμού
message = []
for i in range(0, 16):
    message.append(random.randint(0, 1))
print(message)

#Αριστερές ολισθήσεις όπως ορίζεται από την άσκηση
message_6  = swap(message, 6)
message_10 = swap(message, 10)

#Κωδικοποίηση όπως ζητείται από την εκφώνηση της άσκησης
coded = []
for i in range(0, 16):
    coded.append(message[i]^message_6[i]^message_10[i])

#Αριστερές ολισθήσεις, οι οποίες βρέθηκαν έπειτα από τον τύπο που αναπτύξαμε για την άσκηση
coded_2  = swap(coded, 2)
coded_4  = swap(coded, 4)
coded_12 = swap(coded, 12)
coded_14 = swap(coded, 14)

#Αποκωδικοποίηση με την βοήθεια του τύπου που αναπτύξαμε για να πάρουμε το αρχικό μήνυμα
decoded = []
for i in range(0, 16):
    decoded.append(coded[i]^coded_2[i]^coded_4[i]^coded_12[i]^coded_14[i])
print(decoded)