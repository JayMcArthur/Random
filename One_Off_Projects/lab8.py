import crc8

def main():
    sent = 'LABS'
    s_converted = ''.join(format(ord(x), 'b') for x in sent)
    # print('Sent data: ' + str(s_converted))
    hash = crc8.crc8()
    hash.update(b'PUNE')
    print('CRC8 IN: ' + hash.hexdigest())

    received = "JAYA"
    r_converted = ''.join(format(ord(x), 'b') for x in received)


    # Driver Code
    SentMessage = s_converted
    k = 8
    ReceivedMessage = r_converted
    # Calling the findChecksum() function
    Checksum = findChecksum(SentMessage, k)

    # Calling the checkReceiverChecksum() function
    ReceiverChecksum = checkReceiverChecksum(ReceivedMessage, k, Checksum)

    # Printing Checksum
    # print("SENDER SIDE CHECKSUM: ", Checksum)
    # print('Received Data: ' + str(r_converted) + " " + Checksum)
    hash.update(b'JAYB')
    print('CRC8 OUT: ' + hash.hexdigest())
    # print("RECEIVER SIDE CHECKSUM: ", ReceiverChecksum)
    finalsum = bin(int(Checksum, 2) + int(ReceiverChecksum, 2))[2:]

    # Finding the sum of checksum and received checksum
    finalcomp = ''
    for i in finalsum:
        if i == '1':
            finalcomp += '0'
        else:
            finalcomp += '1'

    # If sum = 0, No error is detected
    if int(finalcomp, 2) == 0:
        print("STATUS: ACCEPTED")

    # Otherwise, Error is detected
    else:
        print("STATUS: ERROR DETECTED")


# Function to find the Checksum of Sent Message
def findChecksum(SentMessage, k):
    # Dividing sent message in packets of k bits.
    c1 = SentMessage[0:k]
    c2 = SentMessage[k:2 * k]
    c3 = SentMessage[2 * k:3 * k]
    c4 = SentMessage[3 * k:4 * k]

    # Calculating the binary sum of packets
    Sum = bin(int(c1, 2) + int(c2, 2) + int(c3, 2) + int(c4, 2))[2:]

    # Adding the overflow bits
    if len(Sum) > k:
        x = len(Sum) - k
        Sum = bin(int(Sum[0:x], 2) + int(Sum[x:], 2))[2:]
    if len(Sum) < k:
        Sum = '0' * (k - len(Sum)) + Sum

    # Calculating the complement of sum
    Checksum = ''
    for i in Sum:
        if (i == '1'):
            Checksum += '0'
        else:
            Checksum += '1'
    return Checksum


# Function to find the Complement of binary addition of
# k bit packets of the Received Message + Checksum
def checkReceiverChecksum(ReceivedMessage, k, Checksum):
    # Dividing sent message in packets of k bits.
    c1 = ReceivedMessage[0:k]
    c2 = ReceivedMessage[k:2 * k]
    c3 = ReceivedMessage[2 * k:3 * k]
    c4 = ReceivedMessage[3 * k:4 * k]

    # Calculating the binary sum of packets + checksum
    ReceiverSum = bin(int(c1, 2) + int(c2, 2) + int(Checksum, 2) +
                      int(c3, 2) + int(c4, 2) + int(Checksum, 2))[2:]

    # Adding the overflow bits
    if len(ReceiverSum) > k:
        x = len(ReceiverSum) - k
        ReceiverSum = bin(int(ReceiverSum[0:x], 2) + int(ReceiverSum[x:], 2))[2:]

    # Calculating the complement of sum
    ReceiverChecksum = ''
    for i in ReceiverSum:
        if i == '1':
            ReceiverChecksum += '0'
        else:
            ReceiverChecksum += '1'
    return ReceiverChecksum
