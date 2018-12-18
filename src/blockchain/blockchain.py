import hashlib
#### Jeetendra Mandal - Created for developer community to understand the basics of BlockChain development
class Block:
    def __init__(self, no, nonce, data, hashcode, prev):
        self.no=no
        self.nonce=nonce
        self.data=data
        self.hashcode=hashcode
        self.prev=prev

    def getStringVal(self):
        return self.no, self.nonce, self.data, self.hashcode, self.prev

class Blockchain:
        def __init__(self):
            self.chain = []
            self.prefix = "0000"

        def addNewBlock(self, data):
            no = len (self.chain)
            nonce = 0

            if len(self.chain) == 0 :
                prev = "0"
            else:
                prev = self.chain[-1].hashcode

            hashcode = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
            block = Block(no, nonce, data, hashcode, prev)

            self.chain.append(block)

        def printBlockChain(self):
            chainDict={}
            for no in range(len(self.chain)):
                chainDict[no] = self.chain[no].getStringVal()
            print(chainDict)

        def mineChain(self):
            ### Check if chain is broken
            brokenLink =self.checkIfBroken()


            if (brokenLink == None) :
                pass
            else :
                for block in self.chain[brokenLink.no:]:
                    print("Mining Block :", block.getStringVal())
                    self.mineBlock(block)

        def mineBlock(self, block):
            nonce = 0
            myHash = hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
            while myHash[0:4] != self.prefix:
                myHash = hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
                nonce = nonce + 1
            else:
                self.chain[block.no].hashcode = myHash
                self.chain[block.no].nonce = nonce
                if (block.no < len(self.chain) -1):
                    self.chain[block.no+1].prev = myHash

        def checkIfBroken(self):
            for no in range(len(self.chain)):
                if self.chain[no].hashcode[0:4]==self.prefix:
                    pass
                else:
                    return self.chain[no]

        def changeData (self, no, data):
            self.chain[no].data = data
            self.chain[no].hashcode = hashlib.sha256(str(str(self.chain[no].nonce)+str(self.chain[no].data)).encode('utf-8')).hexdigest()
