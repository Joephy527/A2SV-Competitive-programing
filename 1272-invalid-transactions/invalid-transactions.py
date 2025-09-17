class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        idx = set()

        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            time, amount = int(time), int(amount)

            if amount > 1000:
                idx.add(i)

                continue

            for j, tr in enumerate(transactions):
                if i == j: continue

                n, t, a, c = tr.split(",")
                t, a = int(t), int(a)

                if name == n and c != city and abs(time - t) < 61:
                    idx.add(i)
                    idx.add(j)

        return [transactions[i] for i in idx]