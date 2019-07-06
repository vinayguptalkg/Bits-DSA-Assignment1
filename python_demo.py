import sys
class HashTable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.hash_table =  [[] for _ in range(capacity)]
        self.size = 0
        self.avgsize = capacity * 5
        self.load_factor = 0.75
    def search(self, key):
        hash_key = self.hashing_func(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def hashing_func(self,key):
        return key % len(self.hash_table)

    def insert(self, key, value):
        hash_key = self.hashing_func(key) % len(self.hash_table)
        key_exists = False
        need_rehash = False
        self.size = self.size + 1
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                if (len(bucket)*1.0/self.capacity) > self.load_factor :
                    print("rehash")
                    need_rehash = True
                break
        if key_exists:
            bucket[i] = ((key, self.search( key)+1))
        else:
            bucket.insert(0,(key, 1))

        if need_rehash:
            print("rehash required")
            self.rehash()

    def delete(self, key):
        hash_key = self.hashing_func(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]
        self.size = self.size -1
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print ('Key {} deleted'.format(key))
        else:
            print ('Key {} not found'.format(key))

    def length(self):
        return len(self.hash_table)

    def rehash(self):
        element =[]
        for index in range(len(self.hash_table)):
            bucket = self.hash_table[index]
        #   for i, kv in enumerate(bucket):
        #       k,v = kv
        #       element.append(kv)
        #       self.delete(k)
        self.capacity = self.capacity *2
        self.hash_table = [[] for _ in range(self.capacity)]
        self.avgsize = self.capacity * 5
        for k,v in element:
            self.insert(k,v)

class DriverHash:
    load_factor = 0.75
    def initializeHash(self):
        self.HashTable = HashTable(10)
    
    def insertHash(self,lic):
        self.HashTable.insert(lic,1)
    
    def printViolators(self):
        for index in range(len(self.HashTable.hash_table)):
            bucket = self.HashTable.hash_table[index]
            for i, kv in enumerate(bucket):
                k, v = kv
                if(v > 3):
                    print(k,v)

    def destroyHash(self):
        for index in range(len(self.HashTable.hash_table)):
            bucket = self.HashTable.hash_table[index]
            bucket = []
        self.HashTable.hash_table = []
        self.hash_table = None

class PoliceNode:
    def __init__(self,policeId,fineAmt):
        self.policeId = policeId;
        self.fineAmt = fineAmt
        self.left = None
        self.right = None

class PoliceTree:
    
    def insertByPoliceId(self,policeRoot, policeId, amount):
        if policeRoot == None:
            return PoliceNode(policeId,amount)
        if policeRoot.policeId == policeId:
            policeRoot.fineAmt = policeRoot.fineAmt + amount
            return policeRoot
        if policeRoot.policeId > policeId:
            policeRoot.left = self.insertByPoliceId(policeRoot.left,policeId,amount)
        else:
            policeRoot.right = self.insertByPoliceId(policeRoot.right,policeId,amount)
        return policeRoot

    def insertByFineAmt(self,policeRoot,newNode):
        if policeRoot == None:
            return newNode
        if policeRoot.fineAmt > newNode.fineAmt:
            policeRoot.left = self.insertByFineAmt(policeRoot.left,newNode)
        else:
            policeRoot.right = self.insertByFineAmt(policeRoot.right,newNode)
        return policeRoot

    def reorderByFineAmount (self,policeRoot):
        head =[]
        self.inorder(policeRoot,head)
        root = None
        print(len(head))
        for i in range(len(head)):
            print(i)
            x = head[i]
            root = self.insertByFineAmt(root,PoliceNode(x.policeId,x.fineAmt))
            x.left = None
            x.right = None
            x = None
        return root

    def inorder(self, node, head):
        if(node == None):
            return;
        self.inorder(node.left,head)
        head.append(node)
        self.inorder(node.right,head)

    def printBonusPolicemen (self,policeRoot):
        if policeRoot == None:
            return
        max = self.FindMaxFine(policeRoot)
        print('Maximum is:', max)
        self.printBonusPolicemenUtil(policeRoot,max)


    def printBonusPolicemenUtil (self,policeRoot,max):
        if policeRoot == None:
            return
        self.printBonusPolicemenUtil(policeRoot.left,max)
        amount = policeRoot.fineAmt
        print('Police id:',policeRoot.policeId,policeRoot.fineAmt)
        if( amount >= .9*max):
            print(policeRoot.policeId)
        self.printBonusPolicemenUtil(policeRoot.right,max)

    def FindMaxFine(self,root):
        if root == None:
            return -sys.maxsize-1
        lmax = self.FindMaxFine(root.left)
        rmax = self.FindMaxFine(root.right)
        return max(lmax,rmax,root.fineAmt)

    def destroyPoliceTree (self,policeRoot):
        if policeRoot == None:
            return
        self.destroyPoliceTree(policeRoot.left)
        self.destroyPoliceTree(policeRoot.right)
        policeRoot = None

    def printPoliceTree (self,policeRoot):
        if(policeRoot == None):
            return
        self.printPoliceTree(policeRoot.left)
        print(policeRoot.policeId)
        print(policeRoot.fineAmt)
        self.printPoliceTree(policeRoot.right)

##read from file in read only mode
f=open("inputPS3.txt", "r")
f1 = f.readlines()
#Initialization
dh = DriverHash()
#initianlize hash table
dh.initializeHash()
pt = PoliceTree()
head = None
#Iterate all lines read from file
for line in f1:
    x,y,z = line.split("/") #read policID in x , license in y, fine amt in z
    #a = PoliceNode(int(x.strip(),10),int(z.strip(),10))
    #policeNodeList.append(a)
    head = pt.insertByPoliceId(head, int(x.strip(),10),int(z.strip(),10))
pt.printPoliceTree(head)
h = pt.reorderByFineAmount(head)
print("After reorder")
#pt.printPoliceTree(h)
pt.printBonusPolicemen(h)
pt.destroyPoliceTree(h)
#print(len(dh.HashTable.hash_table))
##HashTable start --
#dh.insertHash(int(y.strip(),10))#strip to trim space, cast string to decimal base 10s
#print(len(dh.HashTable.hash_table))
##print voilators
#dh.printViolators()
#dh.destroyHash()
#dh.initializeHash()
#print(len(dh.HashTable.hash_table))
##HashTable end







