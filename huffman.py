# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    return {char: s.count(char) for char in s}


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    # sorted_freq = {c: freqs[c] for c in sorted(freqs, key=freqs.get)}
    encode.cipher = {char: '' for char in s}
    sorted_freq = sorted(freqs.items(), key=lambda x: x[1])
    find_cipher(sorted_freq)
    return ""


def find_cipher(freqs):
    if len(freqs) == 1:
        return
    new_node = freqs.pop(0)
    new_node2 = freqs.pop(0)
    encode.cipher[new_node[0]] += '0'
    encode.cipher[new_node2[0]] += '1'
    new_node3 = [new_node[0] + new_node2[0], new_node[1] + new_node2[1]]
    find_cipher(freqs)


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    return ""


str1 = "aaaabcc"
freq = frequencies(str1)
encoded = encode(freq, str1)
