class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainVisitCount = defaultdict(int)
        domainVisitPair = []

        for pair in cpdomains:
            count, domain = pair.split()
            subDomains = domain.split(".")

            for i in range(len(subDomains)):
                subDomain = '.'.join(subDomains[i:])
                domainVisitCount[subDomain] += int(count)

        for subDomain in domainVisitCount:
            pair = " ".join([str(domainVisitCount[subDomain]), subDomain])
            domainVisitPair.append(pair)

        return domainVisitPair
