
def knapSack(W, wt, val, n, memo):
    
    if (W, n) in memo:
        return memo[(W, n)]

    if n == 0 or W == 0:
        return 0
  
    if wt[n-1] > W:
        result = knapSack(W, wt, val, n-1, memo)
    else:
  
        result = max(
            val[n-1] + knapSack(W - wt[n-1], wt, val, n-1, memo),
            knapSack(W, wt, val, n-1, memo)
        )

    memo[(W, n)] = result
    return result

if __name__ == '__main__':
    
    profit = [int(x) for x in input("Enter the profit values (space-separated): ").split()]
    weight = [int(x) for x in input("Enter the weight values (space-separated): ").split()]
    W = int(input("Enter the maximum weight capacity: "))
   
    if len(profit) != len(weight):
        print("The lengths of the profit and weight arrays must match!")
    else:
        n = len(profit)
        memo = {} 
        max_profit = knapSack(W, weight, profit, n, memo)
        print("Maximum profit achievable:", max_profit)
