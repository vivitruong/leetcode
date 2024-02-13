# A shopkeeper sells n items where the price of the ith item in price[i]. To maintain balance,
#the shopkeeper wishes to adjust the price of items such that the median of prices is exactly k.
#In one move, the shopkeeper can increase the price of any itemm by 1, and the shopkeeper can perform this move any number of times.
# Find the minimum number of moves in which the median of prices becomes exactly k. The index of the median of an array of m sorted elements,
# where m is odd, is (m+1)/2. For example [2,5,4,1,1,1,6] sorted is [1,1,1,2,4,5,6]. Its length is 7 so the median is at index (7+1)/2 = 4 using 1-based indexing,
# The median is 2... Function description : Complete the function getMinimumMoves (price, k) , return long_int : the minimum number of moves to make the
# median of the array exactly k


def getMinimumMoves(price, k):
    price.sort()  # Step 1
    n = len(price)
    median_index = (n + 1) // 2 - 1  # Correcting the median index calculation
    current_median = price[median_index]  # Adjusted to get the correct current median

    moves = 0
    if current_median < k:
        # Need to increase prices to make the median equal to k
        for i in range(median_index, n):
            if price[i] < k:
                moves += k - price[i]
    elif current_median > k:
        # Need to decrease prices to make the median equal to k
        for i in range(median_index, -1, -1):
            if price[i] > k:
                moves += price[i] - k

    return moves

# Example usage:
price = [5, 3, 3, 6, 3, 9, 2]
k = 3
result = getMinimumMoves(price, k)
print(result)
