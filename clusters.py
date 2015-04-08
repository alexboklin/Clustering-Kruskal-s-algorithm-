import heapq
import time
import argparse

import sys

def main():

    start = time.process_time()

    parser = argparse.ArgumentParser(description="Implements Prim's minimum spanning tree algorithm.")
    parser.add_argument("-s", help="the maximum spacing of a k-clustering", action="store_true")
    parser.add_argument("-c", help="clusters", action="store_true")
    parser.add_argument("-t", help="execution time", action="store_true")
    parser.add_argument("filename", help=".txt file to parse")
    args = parser.parse_args()
    
    try:
        with open(args.filename, 'r') as file:
            raw = [ list(map(float, i.split())) for i in file.readlines() ]
    except IOError:
        print("No such file.")
        sys.exit()

    minKey = int(min([v[0] for v in raw[1:]] + [v[1] for v in raw[1:]]))
    maxKey = int(max([v[0] for v in raw[1:]] + [v[1] for v in raw[1:]]))

    clusters = { k: {k} for k in range(minKey, maxKey + 1) }
    where = { k: k for k in range(minKey, maxKey + 1) }

    check = [ (v[2], v[0], v[1]) for v in raw[1:] ]
    heapq.heapify(check)

    while True:
        k = int(input("Number of clusters: "))
        if k <= 1 or k > int(raw[0][0]):
            print("Invalid number of clusters.")
            continue
        else:
            break
    
    while True: 

        while True:
            extract = heapq.heappop(check)
            toFill = min(where[extract[1]], where[extract[2]])
            toDel = max(where[extract[1]], where[extract[2]])
            if extract[1] in clusters[toFill] and extract[2] in clusters[toFill]:    
                continue
            break

        if len(clusters) == k:
            break
        
        for i in clusters[toDel]:
            where[i] = toFill

        clusters[toFill] =  clusters[toFill].union(clusters[toDel])
        del clusters[toDel]



    if args.s:
        print("The maximum spacing of a {}-clustering is: {} (between vertices {} and {})".format(k, extract[0], int(extract[1]), int(extract[2]))) 

    if args.c:
        print(clusters)

    if args.t:
        print("--- {} seconds ---".format(time.process_time() - start))

if __name__ == "__main__":
    main()   

