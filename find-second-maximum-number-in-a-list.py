if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scoreSheet = list(arr)
    highestScore = max(scoreSheet)
    secondHighestScore = -100
    
    for score in scoreSheet:
        if score != highestScore:
            secondHighestScore = max(secondHighestScore, score)
            
    print(secondHighestScore)
