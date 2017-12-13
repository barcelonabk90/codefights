
'''
You are working on an AI that can recognize words. 
To begin with, you'd like to try the following approach: 
for the given pair of words the AI should find two strings of sorted letters that uniquely identify these words.

Given words word1 and word2, return an array of two strings sorted lexicographically, 
where the first string contains characters present only in word1,
and the second string contains characters present only in word2.

Example

For word1 = "program" and word2 = "develop",
the output should be
wordsRecognition(word1, word2) = ["agmr", "delv"].

Letters 'o' and 'p' are present in both words, and other letters identify them uniquely.
'''
def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(set(w1) - set(w2)))
        #return ''.join(sorted(set([i for i in w1 if i not in w2])))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]

'''
You're implementing a plugin for your favorite code editor. 
This plugin launches various scripts depending on the open file extension.
Each script is associated with exactly one extension, 
and the information about which script should be launched for each extension is stored in a dictionary scriptByExtension.

You are planning to add more supported extensions for some scripts,
so now you would also like to store information about the extensions which each script supports.
As a starting point, you'd like to obtain the (extension, script) pairs from the dictionary,
sorted lexicographically by the extensions.

Implement a function that will do the job.

Example

For

scriptByExtension = {
  "validate": "py",
  "getLimits": "md",
  "generateOutputs": "json"
}
the output should be

transposeDictionary(scriptByExtension) = [["json", "generateOutputs"], 
                                          ["md", "getLimits"], 
                                          ["py", "validate"]]
'''
def transposeDictionary(scriptByExtension):
    return sorted([[j,i] for i,j in scriptByExtension.items()])
    #return [[j, i] for i, j in sorted(scriptByExtension.items(), key=lambda x: x[1])]