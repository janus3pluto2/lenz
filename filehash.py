####################################################################################################
#  janeZero        part of the seedgen file that makes sure no on edits the file without specified #
#                  software.                                                                       #
#                                                             #
####################################################################################################
import hashlib
from seedgen import seed_gen
## file hash pulls a table from seedgen.py
## input the file name including the path to that file
## size of the file


def hash_file(filename: object) -> object:
    # This function returns the SHA-256 hash
    # of the file passed into it
    # make a hash object
    h = hashlib.sha256(b'3301')
    # open file for reading in binary mode
    with open(filename, 'rb') as file:
        ## loop till the end of the file
        chunk = 0
        while chunk != b'':
            ## read only 1024 bytes at a time
            chunk = file.read(10000)
            h.update(chunk)
    ## return the hex representation of digest
    return h.hexdigest()
# filehash
message1 = hash_file("seedgen.py")
message2 = hash_file("seedgenTX.txt")
message3 = hash_file("filehash.py")
message4 = seed_gen
# previous_seed = last_int
filehash = [message1, message2, message3, message4]

print("seedgen:\t\t",message1)
print("seedgenTX:\t\t",message2)
print("filehash:\t\t",message3)
print("seed_gen\t\t:",message4)   

