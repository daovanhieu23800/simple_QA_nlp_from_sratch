from dictionary import Dictionary
from word_segment import word_segmenting

a = Dictionary()
dictionary = a.get_dict()
class DependencyParser():
    def __init__(self, word_segment) :
        self.stack = ["root"]
        self.buffer = word_segment
        self.grammar_relation = []

    def add_relation(self, relation, word_before, word_after):
        self.grammar_relation.append(f"{relation}({word_before}, {word_after})")

    def get_relation(self, word_before, word_after):
        relation=""
        #RA
        if dictionary[word_before]=='lúc' and dictionary[word_after]=="mốc thời gian":
            relation = "RAtime"

        elif dictionary[word_before]=='thành phố' and dictionary[word_after]=="tên thành phố":
            relation = "RAname"
        
        elif dictionary[word_before]=='máy bay' and dictionary[word_after]=="nào":
            relation = "RAWH_det"

        elif dictionary[word_before]=='thành phố' and dictionary[word_after]=="nào":
            relation = "RAWH_det_city"
        
        elif dictionary[word_before]=='máy bay' and dictionary[word_after]=="mã chuyến bay":
            relation = "RAnmod"

        elif dictionary[word_before]=='máy bay' and dictionary[word_after]=="tên hãng hàng không":
            relation = "RAnmod"


        elif dictionary[word_before]=='mã hiệu' and dictionary[word_after]=="máy bay":
            relation = "RAnmod"

        
        
        elif dictionary[word_before]=='root' and (dictionary[word_after] in ["đến","bay","xuất phát", "hạ cánh"]):
            relation = "RAroot"

        elif dictionary[word_before]=='đến' and dictionary[word_after] in ["tên thành phố","thành phố"] and ( '(RAroot(root, đến)' in self.grammar_relation):
            relation = "RAto_loc" 
        
        elif (dictionary[word_before]in ["bay","xuất phát", "hạ cánh"]) and dictionary[word_after] == "từ" :
            relation = "RAfrom_loc"
        
        elif (dictionary[word_before]in ["bay","xuất phát", "hạ cánh"]) and dictionary[word_after] == "đến" :
            relation = "RAto_loc"
        
        elif (dictionary[word_before]in ["bay","xuất phát", "hạ cánh"]) and dictionary[word_after] == "ở" :
            relation = "RAat_loc"
        
        elif (dictionary[word_before]in ["bay","xuất phát", "hạ cánh"]) and dictionary[word_after] == "tên thành phố" :
            relation = "RAname_loc"
        
        elif (dictionary[word_before]in ["đến","bay","xuất phát", "hạ cánh"]) and dictionary[word_after] == "lúc" :
            relation = "RAat_time"  

        elif (dictionary[word_before]in ["đến","bay","xuất phát", "hạ cánh"]) and dictionary[word_after] == "khoảng thời gian" :
            relation = "RArun_time"  

        elif (dictionary[word_before]== "lúc" ) and dictionary[word_after] == "mốc thời gian" :
            relation = "RAtime"  
        elif (dictionary[word_before]in ["đến", "bay","xuất phát", "hạ cánh"]) and dictionary[word_after] == "?" :
            relation = "RAquery"

        elif (dictionary[word_before]in ["đến", "bay","xuất phát", "hạ cánh"]) and dictionary[word_after] == "mất mấy giờ" :
            relation = "RAWHrun_time"
        #LA

        elif dictionary[word_before]=='hãng hàng không' and dictionary[word_after]=="tên hãng hàng không":
            relation = "LAnmod"

        elif dictionary[word_before]=='máy bay' and (dictionary[word_after] in ["đến","bay","xuất phát", "hạ cánh"]):
            relation = "LAnsubj"


        elif dictionary[word_before]=='hãy cho biết' and dictionary[word_after] == "mã hiệu":
            relation = "LAWH_det_id"

        elif dictionary[word_before]=='từ' and (dictionary[word_after] in ["tên thành phố","thành phố"]):
            relation = "LAfrom_loc"

        elif dictionary[word_before]=='đến' and (dictionary[word_after] in ["tên thành phố","thành phố"]):
            relation = "LAto_loc"

        elif dictionary[word_before]=='ở' and (dictionary[word_after]==["tên thành phố","thành phố"]):
            relation = "LAat_loc"

        else:
            relation = "not_determine"
        return relation

    def check_depend(self, word_stack, word_buffer):
        relation = self.get_relation(word_stack, word_buffer)
        if len(self.stack )>= 2:
            print(f'({self.stack[-2]}, {self.stack[-1]})',[string for string in self.grammar_relation if f"({self.stack[-2]},{self.stack[-1]})" in string],'********')
        if relation == "LAfrom_loc"\
        or relation == "LAto_loc"\
        or relation == "LAnsubj"\
        or relation == "LAnmod"\
        or relation == "LAWH_det_id"\
        or relation == "LAat_loc":
            print(relation)
            self.LA(relation, word_stack, word_buffer)


        elif relation == "RAtime"\
        or relation == "RAWH_det_city"\
        or relation == "RArun_time" \
        or relation == "RAto_loc"\
        or relation == "RAname_loc"\
        or relation == "RAat_loc"\
        or relation == "RAquery"\
        or relation == "RAat_time"\
        or relation == "RAto_loc"\
        or relation == "RAfrom_loc"\
        or relation == "RAWH_det"\
        or relation == "RAroot"\
        or relation == "RAnmod"\
        or relation == "RAWHrun_time"\
        or relation == "RAname":
        
            print(relation)
            self.RA(relation, word_stack, word_buffer)
        
        # elif dictionary[word_stack]=='remove_word':
        
        #     self.Reduce()
        #     self.Shift()
        #     print('remove_word')

      

        elif len(self.stack)>=2 and len([string for string in self.grammar_relation if f"({self.stack[-2]}, {self.stack[-1]})" in string])>0:
            print("Reduce")
            self.Reduce()

        else: 
            print('shift')
            self.Shift()

    def Shift(self):
        word = self.buffer.pop(0)
        self.stack.append(word)
        
    
    def Reduce(self):
        self.stack.pop()
        
    
    def RA(self, relation,word_stack, word_buffer):
        self.Shift()    
        self.add_relation(relation, word_stack, word_buffer)
         
    
    def LA(self, relation,word_stack, word_buffer):
        self.Reduce()
        self.add_relation(relation, word_buffer, word_stack)
        
    
    def get_result(self):
        print(self.stack, self.buffer)
        self.Shift()

        while(len(self.buffer)!=0):
        #for i in range(8):
            print('-----------------')

            word_stack = self.stack[-1]
            word_buffer = self.buffer[0]   
            print("before:          ",self.stack, '-----' ,self.buffer,'-----' , self.grammar_relation) 
            print(word_stack,": ",dictionary[word_stack]  , '-----' ,word_buffer, ": ",dictionary[word_buffer])
            self.check_depend(word_stack, word_buffer)
            print("After:          ",self.stack, '-----' ,self.buffer,'-----' , self.grammar_relation) 
        return self.grammar_relation
    
#query = "Máy bay nào đến thành phố Huế lúc 13:30HR ?"
# query = "Máy bay nào đến thành phố Huế lúc 13:30HR ?. "
# query = "Máy bay nào bay từ Đà Nẵng đến TP. Hồ Chí Minh mất 1 giờ ?. "
# query = "Hãy cho biết mã hiệu các máy bay hạ cánh ở Huế ?. "
# query = "máy bay nào xuất phát từ Tp.Hồ Chí Minh, lúc mấy giờ ?. "
# query = "Máy bay nào bay từ TP.Hồ Chí Minh đến Hà Nôi ?. "
# query = "Máy bay VN4 có xuất phát từ Đà Nẵng không ?. "
# query = "Thời gian máy bay VJ5 bay từ TP. Hà Nội đến Khánh Hòa mất mấy giờ ?."
# # query = "Có máy bay nào xuất phát từ Hải Phòng không ?. "
# # query = "Máy bay của hãng hàng không VietJet Air bay đến những thành phố nào ?"
# # query = "Có máy bay nào bay từ Hải Phòng đến Khánh Hòa không?"
# dictionary = Dictionary().get_dict()    
# word_segment = word_segmenting(query)
# print(word_segment)
# dparser = DependencyParser(word_segment)
# print('-----------------')
# #print(dparser.get_relation("đến", "?"))
# (dparser.get_result())

for i in range(10):
    file_path = f'/Users/hieudao/Desktop/nlo_assigmenp/Input/input_{i}.txt'
    file = open(file_path, 'r')
    
    query = file.readline()
    word_segment=word_segmenting(query)
    dparser = DependencyParser(word_segment)
    result=dparser.get_result()
    new_f = open(f"/Users/hieudao/Desktop/nlo_assigmenp/dependency_output/dependency_output_{i}.txt", "w")
    new_f.write(str(result))
    new_f.close()
    file.close()