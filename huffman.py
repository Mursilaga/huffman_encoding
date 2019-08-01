# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    return {char: s.count(char) for char in s}


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    # sorted_freq = {c: freqs[c] for c in sorted(freqs, key=freqs.get)}
    encode.cipher = {char: '' for char in s}
    sorted_freq = sorted(freqs.items(), key=lambda x: x[1])
    find_cipher(sorted_freq)
    result = ""
    for c in s:
        result += encode.cipher[c]
    return result


def find_cipher(freqs):
    if len(freqs) == 1:
        return
    new_node = freqs.pop(0)
    new_node2 = freqs.pop(0)
    for c in new_node[0]:
        encode.cipher[c] = '1' + encode.cipher[c]
    for c in new_node2[0]:
        encode.cipher[c] = '0' + encode.cipher[c]

    insert_node = [new_node[0] + new_node2[0], new_node[1] + new_node2[1]]
    insert_point = 0
    for i in range(len(freqs)):
        if insert_node[1] > freqs[i][1]:
            insert_point = i
    freqs.insert(insert_point, insert_node)
    find_cipher(freqs)


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    return ""


str1 = "aaaabcc"
freq = frequencies(str1)
encoded = encode(freq, str1)
decoded = decode(freq, encoded)
print(decoded)