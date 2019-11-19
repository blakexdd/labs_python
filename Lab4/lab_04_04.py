'''
 * FILE NAME: lab_04_04.py
 * PROGRAMMER: VG6
 * DATE: 29.10.2019
'''
from collections import Counter, namedtuple
import heapq
import sys

class Encoder:
    def encode(self, s):
        pass

    def decode(self, s):
        pass

class HuffmanEncoder(Encoder):
    compressionCoef = 0
    def __init__(self):
        self.compressionCoef = HuffmanEncoder.compressionCoef

    class Node(namedtuple("Node", ["left", "right"])):
        def walk(self, code, acc):
            self.left.walk(code, acc + "0")
            self.right.walk(code, acc + "1")

    class Leaf(namedtuple("Leaf", ["char"])):
        def walk(self, code, acc):
            code[self.char] = acc or "0"

    def __setCompressionCoef(self, s, code):
        k1, k2 = 0, 0
        for ch, freq in Counter(s).items():
            k1 += freq * len(code[ch]) / 8
        k2 = sys.getsizeof(s)
        return k2 / k1

    def getCompressionCoef(self, s, code):
        return HuffmanEncoder.__setCompressionCoef(self, s, code)

    def encode(self, s):
        h = []
        for ch, freq in Counter(s).items():
            h.append((freq, len(h), HuffmanEncoder.Leaf(ch)))

        heapq.heapify(h)

        count = len(h)
        while len(h) > 1:
            freq1, _count1, left = heapq.heappop(h)
            freq2, _count2, right = heapq.heappop(h)
            heapq.heappush(h, (freq1 + freq2, count, HuffmanEncoder.Node(left, right)))
            count += 1

        code = {}
        if h:
            [(_freq, _count, root)] = h
            root.walk(code, "")

        print('Compression coeff is: ', HuffmanEncoder.__setCompressionCoef(self, s, code))
        return code

    def decode(self, s, code):
        res = ""
        while s:
            for key, value in code.items():
                if s.startswith(value):
                    res += key
                    s = s[len(value):]
        return res


class LZEEncoder(Encoder):
    compressionCoef = 0
    def __init__(self):
        self.compressionCoef = LZEEncoder.compressionCoef

    def encode(self, s):
        d_size = 256
        d = dict((chr(i), i) for i in range(d_size))

        w = ''
        result = []
        for c in s:
            wc = w + c
            if wc in d:
                w = wc
            else:
                result.append(d[w])
                d[wc] = d_size
                d_size += 1
                w = c

        if w:
            result.append(d[w])
        return result

    def decode(self, s):
        from io import StringIO
        d_size = 256
        d = dict((i, chr(i)) for i in range(d_size))

        result = StringIO()
        w = chr(list(s).pop(0))
        result.write(w)
        for k in s:
            if k in d:
                entry = d[k]
            elif k == d_size:
                entry = w + w[0]
            else:
                raise ValueError('Bad compressed k: %s' % k)
            result.write(entry)

            d[d_size] = w + entry[0]
            d_size += 1
            w = entry

        return result.getvalue()

    def __setCompressionCoef(self):
        pass

    def getCompressionCoef(self):
        pass

def main():
    s = 'Python is a widely used high-level programming language for general-purpose' \
    'programming, created by Guido van Rossum and first released in 1991.'

    code1 = HuffmanEncoder()
    code2 = LZEEncoder()
    coded = code2.encode(s)
    code = code1.encode(s)
    coded1 = ''.join(str(i) for i in coded)
    encoded = "".join(code[ch] for ch in s)
    print('code is: ', code)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))
    print(encoded)
    decoded = code1.decode(encoded, code)
    print('Decoded text is: ', decoded)
    print('Compressed with ZLE: ', coded1)
    print('Decoded with LZE: ', code2.decode(coded)[1:])

if __name__ == "__main__":
    main()