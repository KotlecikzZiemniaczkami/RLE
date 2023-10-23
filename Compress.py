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

