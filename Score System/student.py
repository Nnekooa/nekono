class student:
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores
        self.sum_score=0
        self.ave=0
        self.level=' '
        self.rank=0

        for i in range(len(self.scores)):
            self.sum_score += self.scores[i]

        self.ave=self.sum_score*1.0/len(self.scores)

        if self.ave>=90: self.level='A'
        elif self.ave>=80: self.level='B'
        elif self.ave>=70: self.level='C'
        elif self.ave>=60: self.level='D'
        else: self.level='F'