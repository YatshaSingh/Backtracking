class Solution:
    """
    @param words: a set of words without duplicates
    @return: all word squares
             we will sort your return value in output
    """
    def word_squares(self, words: List[str]) -> List[List[str]]:
        di={}
        n=len(words[0])
        def backtrack(index,ans,n):
            if index==n:
                res.append(ans.copy())
                return
            prefix =""
            for word in ans:
                prefix+=word[index]
            if prefix not in di:
                return
            for i in di[prefix]:
                ans.append(i)
                backtrack(a+1,ans,nn)
                ans.pop()

                
        for word in words:
            for i in range(len(word)):
                if word[:i+1] not in di:
                    di[word[:i+1]]=[word]
                else:
                    di[word[:i+1]].append(word)
        ans=[]
        res=[]
        for word in words:
            ans.append(word)
            backtrack(1,ans,len(word))
