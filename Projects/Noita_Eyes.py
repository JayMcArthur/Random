from enum import IntEnum
from collections import defaultdict

# NOTES
# https://docs.google.com/document/d/1s6gxrc1iLJ78iFfqC2d4qpB9_r_c5U5KwoHVYFFrjy0/edit#heading=h.tf3tc7h8he20
# https://docs.google.com/document/d/1HRgOw1Lkhqds-hS51HEMnYJPnTWXiXYn2EdyBA0CDVY/edit#heading=h.kube2smqfujy
# https://docs.google.com/document/d/1QeagH8TklJsd8iribMtT5LIRL91laOUU_tFcVl7OOqA/edit
# https://docs.google.com/document/d/1XMNXktCoSabnFWZf9rJFoaKMzsA1bbv7x1Xh9tXkKYk/edit#heading=h.gq20wfhs4tmi
# https://colab.research.google.com/drive/1JMJeTRx4rHNQP0q4LGqIPafQ8v40xekR?usp=sharing#scrollTo=fRtqmR9BdMWU

class L(IntEnum):
    East_1 = 0
    West_1 = 1
    East_2 = 2
    West_2 = 3
    East_3 = 4
    West_3 = 5
    East_4 = 6
    West_4 = 7
    East_5 = 8


eye_raw = [
    [0x5634505c, 0xacf68674, 0x2c9ac076, 0x981e2346, 0x2e474a1f, 0x29848a73, 0xc220213a, 0x75a31019, 0x01fecf4e, 0x2c7aa564, 0x2bf7569a, 0xf9b307f9, 0x3e145ee9, 0xeb76f050, 0xb54a6af2, 0x993474bb, 0x5eea05e8, 0x43ea988d, 0xadde7d91, 0x4136e1da, 0x0101ef86, 0x472533a7, 0x3fe75e9e, 0x90a4b336, 0xc9b9c908, 0x863f83a7, 0x52329ab4, 0x20c91280],
    [0xb1c95194, 0xeaf95a7c, 0x2ca1eeba, 0x981e2346, 0x2e474a1f, 0x29848a73, 0xac567db9, 0x75a31019, 0x56f0b2ae, 0x2c7a8998, 0x9dfd44ec, 0xf9b30744, 0x7b7555aa, 0x48353272, 0xcc6a521c, 0x993f346f, 0xe9153d2e, 0x53c3db0d, 0x7293312c, 0x628375f9, 0xe49c1fef, 0xb40dac02, 0xccc378b2, 0x537dbb53, 0x4d4eaf5f, 0xf319978d, 0x40e1fc47, 0xbca3f152, 0xbf905626, 0x00000000],
    [0x1cf72f99, 0x8634c1ef, 0x2ca1f81b, 0x981e2346, 0x2e474a1f, 0x29848a73, 0xe1637be9, 0x75a31019, 0xb914ade3, 0xe2cfe1d3, 0xb723d349, 0x786f45ab, 0x48c7c97b, 0xbee5b2a5, 0xef63311a, 0x2cbc058b, 0x655c358a, 0xae1bc859, 0x797cd4b3, 0x805b0e68, 0x64bf17b9, 0x87eb66f8, 0xc737f7dd, 0x40a4cabc, 0x4f299b43, 0x8dfe0c08, 0xe0b4b2f4, 0x2aabf66d, 0xfae456c4, 0x5a0d593c, 0x072a8e6a, 0x2b885f6a, 0x616cf703, 0x00002d28],
    [0xba591cfd, 0xe339e9b5, 0x9f5fdb97, 0x40aa767c, 0x6a205b2d, 0x292a2b08, 0xe906ad86, 0x2819fcb0, 0x2d7097c7, 0xb3ad535d, 0x5f701c14, 0xe25103af, 0x3d510e03, 0x7941b070, 0x0e4ab73f, 0x7d50d317, 0x71e3af41, 0x2a497ecf, 0xc25d5cb0, 0x87dfd311, 0x00ae0a79, 0xed860703, 0x07cb6914, 0x31468f6d, 0x856d0002, 0xfac360d1, 0x9449c363, 0x47499296, 0x4b209af6, 0x00000000],
    [0x3f7f2d6f, 0xbc7824f9, 0xd99610d2, 0xec6ae62e, 0x9c10ea2f, 0x2929e6c7, 0xaf3a9d6b, 0x3f77f101, 0x72274d9d, 0x867e7502, 0x89efd32a, 0x888f5ab2, 0x80a77a7b, 0xae3ea520, 0x1bcfa31f, 0x7d640202, 0xc2abe496, 0x40c36cc3, 0x8a590904, 0x2584e684, 0xeb45f210, 0xe9d5b567, 0x1f571e0d, 0x40d17965, 0x7628b91f, 0xec75a14d, 0x70e3ed4a, 0x7ee7240c, 0xd76e5ea0, 0xb536c25e, 0xd4da8afe, 0x2a9c303c, 0xec314373, 0xedaf6daf, 0x96eca434, 0x61f5113b, 0x9fb1a087, 0x281000c2, 0x08a797d1, 0x00000000],
    [0x9445728a, 0x7e7550ff, 0x0d0f6513, 0xf30328d5, 0x9d27ce70, 0x292a0d5c, 0x52a05d69, 0xbfca758c, 0xe8109a74, 0x251a1f3f, 0x5dedc516, 0x24d30587, 0x44e5f584, 0xb3d39014, 0x5790c997, 0x82380e0a, 0xb411f01b, 0xe2449c62, 0x7ebe9feb, 0xb5e7969a, 0x4471d7ec, 0x4a9c0282, 0x866a064b, 0x313a62bf, 0xa8f7fe37, 0x29b312b3, 0xeccf2773, 0x79186c2a, 0x3f22c3ac, 0xb85b08f3, 0xf689a796, 0x286b232d, 0x0577b0f1, 0x4eeb3967, 0x42200715, 0x0000020c],
    [0xd85141c4, 0x76b4f66f, 0x910a0cde, 0x8f93f5f0, 0x84925ae2, 0x2929e6c7, 0x29a68a25, 0x40933e6d, 0xc75f5618, 0xc57372ac, 0x794787b0, 0xbb64926d, 0xb2dbe0fe, 0xf1fe39ca, 0x936186e5, 0x474efd70, 0x6cad7fcf, 0xc342342e, 0x81bafa5d, 0xe7a638fd, 0x40004d4a, 0x29a2c904, 0x5cdb6750, 0xb62839cb, 0xfd8931dd, 0x8dfa2566, 0x030d69c9, 0xee71ed89, 0x22f7029a, 0xce69520b, 0x4f349ac3, 0x4748bf1d, 0x9690947d, 0x00013c03],
    [0x789603e6, 0xe339e97e, 0xb2c91190, 0x8f93f5e9, 0x84925ae2, 0x2929e6c7, 0x4feb4015, 0x409374a5, 0xf7e604ea, 0x94979e7e, 0x01bcc357, 0x4a96793f, 0x36f40675, 0xc355c0a8, 0xb0f85513, 0x2a752013, 0x1b30e279, 0xbc7decdd, 0x8a93175e, 0xc62c6bc0, 0x63dafb6f, 0x9781e76a, 0xf3ba1e66, 0xb0a58e3b, 0x641fde95, 0x297c940b, 0x7874c807, 0x95120e03, 0x1017d733, 0xf6a5f2ff, 0xdf851acf, 0x9540156f, 0x2fdb567c, 0x2167abfb],
    [0xe3c3e1eb, 0x7e7550f0, 0x67eb65a7, 0x8f93f5f3, 0x84925ae2, 0x2929e6c7, 0x5d0b8d5d, 0x40935218, 0xa3e4e814, 0xc671e036, 0xdc181d46, 0x5047870a, 0x3dbac96b, 0x85653473, 0xaa9846f1, 0x24ee71d2, 0xc9269dc8, 0x76ba6749, 0xa9c340c6, 0x8da82039, 0x32d0143b, 0x802c4c1b, 0xb02e0347, 0x77df0666, 0x5cb83226, 0x8fbb8712, 0x99246bfc, 0x569c4f81, 0xa564670b, 0xb4e02af6, 0xeb81e037, 0x5159ba32, 0x0000008c, 0x00000000]
]
eye_base_7 = [[], [], [], [], [], [], [], [], []]
eye_as_string = [[], [], [], [], [], [], [], [], []]
eye_as_int = [[], [], [], [], [], [], [], [], []]
tri_as_int = []
tri_as_string = []
tri_base_10 = [[], [], [], [], [], [], [], [], []]
tri_freq_count = defaultdict(int)
tri_into_chars = [[], [], [], [], [], [], [], [], []]
converted_strings = []


use_code_encoding = not True
tri_ordering_1 = [[0, 0], [0, 1], [1, 0]]
tri_ordering_2 = [[1, 2], [1, 1], [0, 2]]


def create_eyes(e_r, e_b_7, e_s, e_i) -> None:
    write_string = ""
    write_array = []
    for e_input, e_write_b7, e_write_s, e_write_i in zip(e_r, e_b_7, e_s, e_i):
        message_part = 0
        for i in range(0, len(e_input), 2):
            combined_read = e_input[i + 1] << 32 | e_input[i]
            decoded = []
            while combined_read:
                decoded.append(int(combined_read % 7))
                combined_read //= 7
            e_write_b7.append(''.join(str(x) for x in decoded[::-1]))
            for char in decoded[::-1]:
                if char == 0:  # Extra Padding
                    continue
                if char == 6:  # Line Break
                    e_write_s.append(write_string)
                    e_write_i.append(write_array)
                    write_string = ""
                    write_array = []
                    message_part += 1
                    continue
                if use_code_encoding:  # Code Encoding
                    write_string += str(char)
                    write_array.append(char)
                else:  # Default Doc Encoding
                    write_string += str(char - 1)
                    write_array.append(char - 1)


def create_tri(e_i, t_i, t_s) -> None:
    tris_part_int = []
    tris_part_string = []
    [y1_1, x1_1], [y1_2, x1_2], [y1_3, x1_3], = tri_ordering_1
    [y2_1, x2_1], [y2_2, x2_2], [y2_3, x2_3], = tri_ordering_2

    for message_read in e_i:
        for i in range(0, len(message_read), 2):
            x = 0
            while x < len(message_read[i]) - 1:
                t1 = [message_read[i + y1_1][x + x1_1], message_read[i + y1_2][x + x1_2], message_read[i + y1_3][x + x1_3]]
                tris_part_int.append(t1)
                t1 = ''.join(str(x) for x in t1)
                tris_part_string.append(t1)
                tri_freq_count[int(t1)] += 1

                if x + 2 == len(message_read[i]):
                    break

                t2 = [message_read[i + y2_1][x + x2_1], message_read[i + y2_2][x + x2_2], message_read[i + y2_3][x + x2_3]]
                tris_part_int.append(t2)
                t2 = ''.join(str(x) for x in t2)
                tris_part_string.append(t2)
                tri_freq_count[int(t2)] += 1
                x += 3
        t_i.append(tris_part_int)
        t_s.append(tris_part_string)
        tris_part_int = []
        tris_part_string = []


def tris_to_digits(t_s, t_d, t_c, c_s) -> None:
    base = 6 if use_code_encoding else 5
    for message_read, message_write1, message_write2 in zip(t_s, t_d, t_c):
        for tri in message_read:
            message_write1.append(int(tri, base))
            message_write2.append(chr(int(tri, base)+32))
        c_s.append(''.join(message_write2))


def main() -> None:
    create_eyes(eye_raw, eye_base_7, eye_as_string, eye_as_int)
    create_tri(eye_as_int, tri_as_int, tri_as_string)
    tris_to_digits(tri_as_string, tri_base_10, tri_into_chars, converted_strings)

    for num, c_s in enumerate(converted_strings):
        print(f'Message {num}: {c_s}')

    # print(f'Message 1: {tri_as_int[L.East_1]}')
    # print(f'Message 2: {tri_as_int[L.West_1]}')
    # print(f'Message 3: {tri_as_int[L.East_2]}')
    # print(f'Message 4: {tri_as_int[L.West_2]}')
    # print(f'Message 5: {tri_as_int[L.East_3]}')
    # print(f'Message 6: {tri_as_int[L.West_3]}')
    # print(f'Message 7: {tri_as_int[L.East_4]}')
    # print(f'Message 8: {tri_as_int[L.West_4]}')
    # print(f'Message 9: {tri_as_int[L.East_5]}')
