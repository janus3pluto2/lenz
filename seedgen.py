# Python 3.9.13

# modals that come with python v3.9
import random
import hashlib


# random number generator
#seedlocktest = int(3301)
#random.seed(seedlocktest)
x = []  # list
# seed genarator loop creates six numbers
for ii in range(6):
    A = random.randint(11, 99)
    x.append(A)

a = x[0]
b = x[1]
c = x[2]
d = x[3]
e = x[4]
f = x[5]

# my table for
ranZero = (a, b, c, d, e, f)
ranOne = a + b + c + d + e + f
ranTwo = a + 1 + b + 2 + c + 3 + d + 4 + e + 5 + f + 6
ranThree = a + 1 + 3 + b + 2 + 5 + c + 3 + 7 + d + 4 + 11 + e + 5 + 13 + f + 6 + 17


# seedOne is 16 in length
seedOne = ranOne * 16 * 2 ** 256
# seedTwo is 32 in length
seedTwo = ranTwo * 32 * 2 ** 256
# seedThr is 64 in length
seedThr = ranThree * 64 * 2 ** 256
# length of between 1000 1500
seed_gen = str(ranOne + seedOne + ranTwo + seedTwo + ranThree + seedThr * 16 ** 256)
seed_gen_int = int(ranOne + seedOne + ranTwo + seedTwo + ranThree + seedThr * 16 ** 256)
# values and keys for the blk_1, blk_2, blk_3
blk_1_seed_1 = ranOne + seedOne + a + b       # 16 in length
blk_2_seed_2 = ranTwo + seedTwo + c + d       # 32 in length
blk_3_seed_3 = ranThree + seedThr + e + f     # 64 in length
##
# dictionary nested
##
blk_1 = {
    "ranOne": ranOne,
    "seedOne": seedOne,
    "blk_seed_1": blk_1_seed_1
}

blk_2 = {
    "ranTwo": ranTwo,
    "seedTwo": seedTwo,
    "blk_seed_2": blk_2_seed_2
}

blk_3 = {
    "ranThree": ranThree,
    "seedThr": seedThr,
    "blk_seed_3": blk_3_seed_3
}


#sha512 hash for randOne
#whitch is exported to blockchain

origin_seed = hashlib.sha512()
origin_seed.update(str(ranZero).encode('utf-8'))
origin_seed.hexdigest()
hsh = origin_seed.hexdigest()

f = open("E:/mmm/lenz-main/medusa/lenz-v0-0-1/seedgenTX.txt", 'w')
f.writelines("seed : ")
f.writelines(seed_gen)
f.writelines("\n")
f.writelines("data for Merkle root : ")
f.writelines(origin_seed.hexdigest())

f.close()
print("****"*40)
#print("seedlocktest:",seedlocktest)
print("ranZero:",ranZero)
print("randOne:",ranOne)
print("ranTwo:",ranTwo)
print("ranThree:",ranThree)
print("****"*40)
print("seedOne:",seedOne)
print("seedTwo:",seedTwo)
print("seedThr:",seedThr)
print("****"*40)
print("blk_1:",blk_1)
print("blk_2:",blk_2)
print("blk_3:",blk_3)
print("****"*40)
print("seed_gerated:", seed_gen)
print("origin key",origin_seed.hexdigest())
