class BinarySearch():
    def search(self, key, sorted_list):
        if len(sorted_list)==1:
            if key==sorted_list[0]:
                return

        i=0
        j=len(sorted_list)-1
        mid = (j-i)//2
        while i <= j:
            if sorted_list[mid] == key:
                return mid
            if sorted_list[mid] < key:
                i = mid+1

            else:
                j = mid-1
            mid = (i + j) // 2


        return -1


if __name__ == "__main__":
    # sorted_list = list(np.sort(np.random.randint(1, 64, 15)))
    key = 42
    sorted_list = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
    bs = BinarySearch()
    print(sorted_list, key)
    print(bs.search(key, sorted_list))