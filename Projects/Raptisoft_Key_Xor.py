import shutil
from os import listdir, mkdir
from os.path import isfile, join


def doXOR():
    path = "C:/Users/JayMc/Downloads/SB_v1.2.2_unsplit/assets/data"
    shutil.rmtree("../decrypted")
    mkdir("../decrypted")
    for file in [f for f in listdir(path) if isfile(join(path, f))]:
        with open(path + "/" + file, "rb") as in_file, open("decrypted/" + file, "wb") as out_file:
            input = in_file.read()
            output = []
            # MakerMall Key - TheWorldsSecondGreatestLover
            if file == "item.txt":
                key = "F0rk1tA3ll"
            elif file == "wave.txt":
                key = "BEwareTheFisH"
            else:
                key = "FORASUMMERSDAY"

            for i in range(len(input)):
                output.append(input[i] ^ ord(key[i % len(key)]))

            out_file.write(bytearray(output))

def customXOR():
    with open("C:/Users/JayMc/Desktop/Coding/Javascript/SB_v1.2.2_unsplit/assets/images/boss.bundle", "rb") as in_file, open(
            "../decrypted/test_bundle.txt", "wb") as out_file:
        input = in_file.read()
        key = "FORASUMMERSDAY"
        output = []

        for i in range(len(input)):
            output.append(input[i] ^ ord(key[i % len(key)]))

        out_file.write(bytearray(output))