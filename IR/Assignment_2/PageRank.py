class TwoPageRank:
    def __init__(self):
        self.path = [[0] * 10 for _ in range(10)]
        self.pagerank = [0] * 10

    def calc(self, total_nodes):
        InitialPageRank = 1 / total_nodes
        OutgoingLinks = 0
        DampingFactor = 0.85
        TempPageRank = [0] * 10

        for k in range(1, total_nodes + 1):
            self.pagerank[k] = InitialPageRank

        print(
            f"Total Number of Nodes: {total_nodes}\nInitial PageRank of All Nodes: {InitialPageRank}\n")

        for k in range(1, total_nodes + 1):
            print(f"Page Rank of {k} is: {self.pagerank[k]}")

        ITERATION_STEP = 1
        while ITERATION_STEP <= 2:
            for k in range(1, total_nodes + 1):
                TempPageRank[k] = self.pagerank[k]
                self.pagerank[k] = 0

            for InternalNodeNumber in range(1, total_nodes + 1):
                for ExternalNodeNumber in range(1, total_nodes + 1):
                    if self.path[ExternalNodeNumber][InternalNodeNumber] == 1:
                        k = 1
                        OutgoingLinks = 0
                        while k <= total_nodes:
                            if self.path[ExternalNodeNumber][k] == 1:
                                OutgoingLinks = OutgoingLinks + 1
                            k = k + 1
                        self.pagerank[InternalNodeNumber] += TempPageRank[ExternalNodeNumber] * (
                            1 / OutgoingLinks)

            print(f"\nAfter {ITERATION_STEP}th Step")
            for k in range(1, total_nodes + 1):
                print(f"Page Rank of {k} is: {self.pagerank[k]}")
            ITERATION_STEP = ITERATION_STEP + 1

        for k in range(1, total_nodes + 1):
            self.pagerank[k] = (1 - DampingFactor) + \
                DampingFactor * self.pagerank[k]

        print("\nFinal Page Rank:")
        for k in range(1, total_nodes + 1):
            print(f"Page Rank of {k} is: {self.pagerank[k]}")


def main():
    nodes = int(input("Enter the Number of WebPages:\n"))
    p = TwoPageRank()
    print("Enter the Adjacency Matrix with 1->PATH & 0->NO PATH Between two WebPages:")

    for i in range(1, nodes + 1):
        for j in range(1, nodes + 1):
            p.path[i][j] = int(input())
            if j == i:
                p.path[i][j] = 0

    p.calc(nodes)


if __name__ == "__main__":
    main()


# OUTPUT ->
# Enter the Number of WebPages:
# 4
# Enter the Adjacency Matrix with 1->PATH & 0->NO PATH Between two WebPages:
# 0
# 1 
# 1
# 0
# 0
# 0
# 0
# 1
# 1
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# Total Number of Nodes: 4
# Initial PageRank of All Nodes: 0.25

# Page Rank of 1 is: 0.25
# Page Rank of 2 is: 0.25
# Page Rank of 3 is: 0.25
# Page Rank of 4 is: 0.25

# After 1th Step
# Page Rank of 1 is: 0.08333333333333333
# Page Rank of 2 is: 0.20833333333333331
# Page Rank of 3 is: 0.375
# Page Rank of 4 is: 0.3333333333333333

# After 2th Step
# Page Rank of 1 is: 0.125
# Page Rank of 2 is: 0.16666666666666666
# Page Rank of 3 is: 0.375
# Page Rank of 4 is: 0.3333333333333333

# Final Page Rank:
# Page Rank of 1 is: 0.25625000000000003
# Page Rank of 2 is: 0.2916666666666667
# Page Rank of 3 is: 0.46875
# Page Rank of 4 is: 0.43333333333333335


#OUTPUT ->
#Enter the Number of WebPages
#4
#Enter the Adjacency Matrix with 1->PATH & 0->NO PATH Between two WebPages:

#0 1 0 1
#1 2 3 0
#2 1 0 1
#0 2 1 1
#Total Number of Nodes :4.0 Initial PageRank of All Nodes :0.25

#Initial PageRank Values , 0th Step
#Page Rank of 1 is : 0.25
#Page Rank of 2 is : 0.25
#Page Rank of 3 is : 0.25
#Page Rank of 4 is : 0.25

#After 1th Step
#Page Rank of 1 is : 0.25
#Page Rank of 2 is : 0.25
#Page Rank of 3 is : 0.25
#Page Rank of 4 is : 0.25

#After 2th Step
#Page Rank of 1 is : 0.25
#Page Rank of 2 is : 0.25
#Page Rank of 3 is : 0.25
#Page Rank of 4 is : 0.25

#Final Page Rank :
#Page Rank of 1 is : 0.36250000000000004
#Page Rank of 2 is : 0.36250000000000004
#Page Rank of 3 is : 0.36250000000000004
#Page Rank of 4 is : 0.36250000000000004