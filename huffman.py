# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    return {char: s.count(char) for char in s}


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    sorted_freq = {c: freqs[c] for c in sorted(freqs, key=freqs.get, reverse=True)}
    return ""


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    return ""


str1 = "aaaabcc"
freq = frequencies(str1)
encoded = encode(freq, str1)
