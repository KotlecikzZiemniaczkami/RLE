class Compress:
    def __init__(self, path):
        self.__path = path

    def compression(self):
        file = open(self.__path, 'r')
        text = file.read()
        file.close()
        CompressedText = ''
        i = 0
        counter = 1
        letter = text[0]
        for i in range(1,len(text)):
            if letter != text[i]:
                CompressedText = CompressedText + str(counter) + letter
                counter = 1
                letter = text[i]
            else:
                counter += 1
        file2 = open("compressed", 'w')
        file2.write(CompressedText)
        file2.close()

    def decompress(self):
        file = open(self.__path)
        text = file.read()
        file.close()
        decompressedText = ''
        counter = ''
        for i in range(len(text)):
            if text[i].isnumeric():
                counter += text[i]
            else:
                letter = text[i]
                decompressedText += int(counter) * letter
                counter=''
        file2 = open("dempressed", 'w')
        file2.write(decompressedText)
        file2.close()

