class SuperList(list):
    def __len__(self):
        return 1000


superList = SuperList()

print(len(superList))

superList.append(5)
print(superList[0])
