class BucketSort:
    def __init__(self,a):
        self.a = a

    def result(self,bucketCount = 10):
        buckets = [[] for i in range(bucketCount+1)]
        maxElement = max(self.a)
        minElement = min(self.a)
        bucketRange = (maxElement-minElement+1)/bucketCount
        for i in range(len(self.a)):
            bucketIndex = int((self.a[i]-minElement)/bucketRange)
            buckets[bucketIndex].append(self.a[i])
        for i in range(len(buckets)):
            buckets[i] = sorted(buckets[i])
        self.a = []
        for bucket in buckets:
            self.a.extend(bucket)
        return self.a
