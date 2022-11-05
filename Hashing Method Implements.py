class HW_Hashing:
    def __init__(self, size):
        self.M = size
        self.h = [[None, None] for x in range(size)]
        self.d = [[None, None] for x in range(size)]

    def hash(self, key):
        return key % self.M

    def hash2(self, key):
        return (key*key % 17)*11%self.M

    def put(self, key, data):
        for k in range(self.M):
            if(self.h[k][0]==key):
                self.h[k][1] = data
                return
            if(self.d[k][0]==key):
                self.d[k][1] = data
                return
        #동일키에 다른 값 예외처리
        if(([None,None] not in self.h) and ([None,None] not in self.d)):
            raise Exception("Table 다 참")
        #배열이 꽉 차 있을경우 오류 메세지 발생
        
        while(([None,None] in self.h) or ([None,None] in self.d)):#배열이 찰때까지 반복
            if(self.h[self.hash(key)][0] == None):
                self.h[self.hash(key)][0] = key
                self.h[self.hash(key)][1] = data
                #비어있다면 키와 값 저장
            
            elif(self.h[self.hash(key)][0] != None):
                temp1key = self.h[self.hash(key)][0]
                temp1Value = self.h[self.hash(key)][1] # 과정 2-2-1 임시저장

                self.h[self.hash(key)][0] = key
                self.h[self.hash(key)][1] = data # 과정 2-2-1 htable[i]에 삽입
                
                j = self.hash2(temp1key) #과정 2-2-2 j=d(okey)계산
            
                if(self.d[j][0] == None):
                    self.d[j][0] = temp1key
                    self.d[j][1] = temp1Value
                    #self.d[j] = temp1 #과정 2-2-3 비어 있다면 dtable[j] 삽입 후 종료
                
                else:
                    temp2key = self.d[j][0] #임시저장
                    temp2Value = self.d[j][1]
                    self.d[j][0] = temp1key
                    self.d[j][1] = temp1Value
                    
                    #과정 2-2-6
                    self.put(temp2key,temp2Value)#재귀함수 실행
        

            return

    def get(self,key):
        for k in self.h:
            if(k[0] == key):
                return k[1]
        for k in self.d:
             if(k[0] == key):
                return k[1]
        #각각 self.h와 self.d의 리스트를 탐색해서 값 가져오기


    def delete(self,key):
        for k in self.h:
            if(k[0] == key):
                k[0] = None
                k[1] = None
                return
        for k in self.d:
            if(k[0] == key):
                k[0] = None
                k[1] = NOne
                return
        #각각 self.h와 self.d의 리스트를 탐색해서 값 삭제하기

    def print_table(self):
        print('********** Print Tables **********')
        print('h-table:')
        for i in range(self.M):
            if(i < 10):
                print(i,'    ',end='')
            else:
                print(i,'   ',end='')
        print('')
        for i in self.h:
            if(i[0] == None):
                print('None  ',end='')
            else:
                print(i[0],'   ',end='')
        print('')
            
        print('d-table:')
        
        for i in range(self.M):
            if(i < 10):
                print(i,'    ',end='')
            else:
                print(i,'   ',end='')

        print('')
        for i in self.d:
            if(i[0] == None):
                print('None  ',end='')
            else:
                print(i[0],'   ',end='')
        print('')

        
        

if __name__ =='__main__':
    t = HW_Hashing(13)
    t.put(25, 'grape')
    t.put(43, 'apple')
    t.put(13, 'banana')
    t.put(26, 'cherry')
    t.put(39, 'mango')
    t.put(71, 'lime')
    t.put(50, 'orange')
    t.put(64, 'watermelon')
    print()
    print('--- Get data using keys:')
    print('key 50 data =', t.get(50))
    print('key 64 data =', t.get(64))
    print()
    t.print_table()
    print()
    print('----- after deleting key 50, -----------')
    t.delete(50)
    t.print_table()
    print()
    print('key 64 data =', t.get(64))
    print('----- after adding key 91 with data berry:--------------')
    t.put(91,'berry')
    t.print_table()
    print()
    print('----- after changing data with key 91 from berry to kiwi:------------')
    t.put(91,'kiwi')
    print('key 91 data =', t.get(91))
    t.print_table()
