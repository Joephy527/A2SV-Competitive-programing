if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record = [name, score]
        records.append(record)
        
    records.sort(key=lambda rec: (rec[1], rec[0]))
    minScore = records[0][1]
    secondMinScore = records[-1][1]
    
    for name, score in records:
        if score != minScore:
            secondMinScore = score
            break
            
    for name, score in records:
        if score == secondMinScore:
            print(name)
