from kappacrypt import FileCryptor
from kappacrypt.keys import RSAKeys
# encryption
fc = FileCryptor("file")
rsa = RSAKeys()
rsa.load(
    {"public_key": "id_rsa.pub"}
)
# rsa.gen_keys()
# rsa.dump() # keys will be dumped to current directory
fc.encrypt(rsa.public_key)

# # decryption
fc = FileCryptor("file.encrypted")
rsa = RSAKeys()
rsa.load(
    {"private_key": "id_rsa"}
)
fc.decrypt(rsa.private_key)

# #You can also dump keys to specifed directory by using
# rsa.dump({"private_key": "path to rsa private key",
#           "public_key": "path to rsa public key"})