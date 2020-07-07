def threeNumberSum(arr, target): # Space: O(1) Time: O(n^2) n = length of arr
    # Write your code here
    triplets = []

    # sort the array so we can say with certainty we've checked all
    # values, when using a 'meeting in the middle strategy'.
    arr.sort() # O(nlogn)

    # iterate through the array.
    # for each item in the array, we're going to be checking the other items in the array
    # for a match
    # in order to avoid n^2 or n^3 runtime, we're going to use a "meet in the middle" strategy
    for i in range(len(arr) - 2): # O((n^2) / 2) -> O(n^2)
        # second number index
        # we don't need to check the current number against numbers before it,
        # because the array is sorted and we've already checked those numbers against
        # the current

        #set the low pointer to the indext after the current index
        low = i + 1

        # third number index
        #Set the high pointer to the last index in the array
        high = len(arr) - 1

        # check for matches
        while low < high:

            # using "is" caused an error on 4th test case (large numbers?)
            if arr[i] + arr[low] + arr[high] == target:
                # triplet found
                triplet = [arr[i], arr[low], arr[high]]
                triplet.sort() # I don't think this would be necessary with the sorted output - I would remove
                triplets.append(triplet)
                # increment and decrement low and high values and look for other matches.
                low += 1
                high -= 1

            elif arr[i] + arr[low] + arr[high] < target:
                # no match was found and we're not reaching the target
                low += 1
            else:
                # no match was found and we're adding up to higher than the target
                high -= 1

    return triplets