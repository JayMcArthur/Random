from Crypto.Cipher import AES


def encrypt(f_in, f_out):
    # Read file content
    with open(f_in, "rb") as file:
        file_content = file.read()
    backup_key = bytes([index * 2 for index in range(16)])
    encobj = AES.new(backup_key, AES.MODE_GCM)
    ciphertext, tag = encobj.encrypt_and_digest(file_content)
    cyphertext = bytes(encobj.nonce) + bytes(ciphertext) + bytes(tag)
    with open(f_out, "wb") as out_file:
        out_file.write(cyphertext)


def decrypt(f_in, f_out):
    backup_key = bytes([index * 2 for index in range(16)])
    # Read file content
    with open(f_in, "rb") as file:
        file_content = file.read()
    # Decrypt
    nonce_length = 12
    nonce = file_content[:nonce_length]
    ciphertext = file_content[nonce_length:-16]
    tag = file_content[-16:]
    encobj = AES.new(backup_key, AES.MODE_GCM, nonce)
    plaintext = encobj.decrypt_and_verify(ciphertext, tag)
    with open(f_out, "wb") as out_file:
        out_file.write(plaintext)


def main():
    dec_in = "D:/Coding/Python/Random/One_Off_Projects/test/Whipper_20230621_194907.zip"
    dec_out = "D:/Coding/Python/Random/One_Off_Projects/test/box2.hive"
    enc_in = "D:/Coding/Python/Random/One_Off_Projects/test/box.hive"
    enc_out = "D:/Coding/Python/Random/One_Off_Projects/test/Whipper_20230629_194907.zip"
    decrypt(dec_in, dec_out)
    #encrypt(enc_in, enc_out)


